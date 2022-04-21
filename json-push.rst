.. _json_push :

==================
JSON Push Protocol
==================


The JSON Push protocol is an HTTP-based protocol that uses POST
requests to perfom incremental or full data syncs across to an HTTP
endpoint. It supports splitting up the data into smaller batches, so
that not all the data have to be sent in a single request.

The protocol is supported by the :ref:`http_endpoint
<http_endpoint_source>` source and the :ref:`json <json_sink>`
sink. This protocol can be used by microservices and other clients to
send entities.

Requests
========


The following HTTP request parameters are supported:

.. list-table::
   :header-rows: 1
   :widths: 20, 80

   * - Parameter
     - Description

   * - sequence_id
     - A string token that is generated every time the data sync is
       started. Included in all requests.
     
   * - is_full
     - A boolean. Has the value ``true`` if this is a full data sync,
       and ``false`` if not. Included in all requests. The default
       value is ``false``.

   * - request_id
     - A string token that is generated for every request. Included
       in all requests.

   * - previous_request_id
     - A string token referencing the request_id of the
       previous request. Included in all but the first request.
     
   * - is_first
     - A boolean. Included in the first request with the value ``true``. Note that this flag
       is only set during a full data sync (i.e. ``is_full`` is ``true``).
     
   * - is_last
     - A boolean. Included in the last request with the value ``true``. Note that this flag
       is only set during a full data sync (i.e. ``is_full`` is ``true``).

The HTTP body is JSON data which will always be in the form of a
JSON array even if it is a single entity. The
serialisation of entities as JSON is described in more detail
:doc:`here <entitymodel>`.

If the sequence_id is not the same as the one that is currently
active, then it will replace the active one (full sync only). Only a
single sequence_id should be active at any time. A sequence id goes
out of scope when the 'is_last=true' request parameter is given. Note
that an incremental request does not affect the active sequence.


Conflicts
=========

When doing an incremental sync the request parameters can silently be
ignored and the entities should be accepted.

The HTTP server should recognize these cases as conflicting when doing
a full data sync:

- The ``previous_request_id`` does not match with the request_id of the
  previous request. Return '409 Conflict'.

- The value of ``is_full`` is not the same as in the previous request of
  the same sequence. Return '409 Conflict'.

- The ``is_first`` request parameter is true when we know that it is not
  the first request in the active sequence. Return '409 Conflict'.

If the JSON Push Sink receives a ``409 Conflict`` response code, then it
must stop the active sync, and try again later. It should start from
the beginning with a new sequence if it was a full data sync.

.. _json_push_examples:

Examples
========

This section contains three examples that illustrates how you can use
the JSON push protocol to push data to Sesam using incremental and
full syncs. The examples use the ``curl`` command line utility.

Our examples all use the following pipe which sets up a receiver
endpoint that we can use to push our JSON entities to:

::
   
   $ cat pipe.json
   {
       "_id": "myendpoint",
       "type": "pipe",
       "source": {
           "type": "http_endpoint"
       },
       "sink": {
           "type": "dataset",
           "dataset": "mydataset"
       }
   }

To use the ``curl`` command to communicate with Sesam we need a JWT
token for authorization. We'll add the JWT authorization header to an
environment variable to make this easier:

::
   
   export AUTH_HEADER="Authorization: bearer YOUR-JWT-TOKEN"


Example 0: incremental sync
---------------------------

This example has one JSON request body, which looks like this:

::

  $ cat sequence0.json
  [
      {
          "_id": "a",
          "name": "A"
      },
      {
          "_id": "b",
          "name": "B"
      }
  ]

We can now ``POST`` the contents of the ``sequence0.json`` file to the
``/api/receivers/myendpoint/entities`` endpoint. This request is
treated as an incremental sync, which in practice will just add the
entities to the ``mydataset`` dataset.

::
   
   $ curl -X POST -H "$AUTH_HEADER" -H "Content-Type: application/json" --data @sequence0.json http://localhost:9042/api/receivers/myendpoint/entities
   {}

If we now look at the ``mydataset`` dataset using the API, it now looks like this:

::
   
   $ curl -s -H "$AUTH_HEADER" http://localhost:9042/api/datasets/mydataset/entities | jq .
   [
     {
       "name": "A",
       "_id": "a",
       "_deleted": false,
       "_updated": 0,
       "_previous": null,
       "_ts": 1489654249474509,
       "_hash": "8b48c6574f7e8474194090eb9123666e"
     },
     {
       "name": "B",
       "_id": "b",
       "_deleted": false,
       "_updated": 1,
       "_previous": null,
       "_ts": 1489654249474537,
       "_hash": "d3b66df7c0e6513556378c2ec5b91d5c"
     }
   ]

Example 1: full sync
--------------------

This example has three JSON request bodies, which look like this:

::
   
  $ cat sequence1.0.json
  [
      {
          "_id": "b",
          "name": "B"
      }
  ]
  
  $ cat sequence1.1.json
  [
      {
          "_id": "a",
          "name": "A (updated)"
      },
      {
          "_id": "c",
          "name": "C"
      }
  ]
  
  $ cat sequence1.2.json
  [
      {
          "_id": "d",
          "name": "D"
      }
  ]

We can now ``POST`` the contents of the three files to the
``/api/receivers/myendpoint/entities`` endpoint. We'll want to do this
in one sequence, but across three HTTP requests.

All our request set the request parameter ``is_full`` to ``true`` in
order to indicate that we're doing a full sync, i.e. we're sending the
complete set of data in this sequence. This will enable deletion
detection, which we'll see an example of later.

We also set the ``sequence_id`` request parameter to a unique token
that represents our sequence. In this case we use the value ``1`` to
indicate that this is our first sequence.

Since this is our first request in the sequence we set ``request_id``
to ``1``.

.. NOTE::

   In general it is a good idea to use `UUIDs <https://en.wikipedia.org/wiki/Universally_unique_identifier>`_ for
   ``sequence_id``, so that we can guarantee that they are unique. For
   ``request_id`` it is OK to use numbers as the request id is local
   to the sequence.

The first request starts the sequence and posts the contents of the
first file. Note that the ``is_first`` request parameter is set to
``true``.

::

   $ curl -X POST -H "$AUTH_HEADER" -H "Content-Type: application/json" --data @sequence1.0.json 'http://localhost:9042/api/receivers/myendpoint/entities?is_full=true&sequence_id=1&request_id=1&is_first=true'
   {}

Our dataset now contains the same two entities as before as the first
file did not contain any changes to the ``b`` entity. This is normal
as a dataset will only update when entities actually are different.

::
   
  $ curl -s -H "$AUTH_HEADER" http://localhost:9042/api/datasets/mydataset/entities | jq .
  [
    {
      "name": "A",
      "_id": "a",
      "_deleted": false,
      "_updated": 0,
      "_previous": null,
      "_ts": 1489654249474509,
      "_hash": "8b48c6574f7e8474194090eb9123666e"
    },
    {
      "name": "B",
      "_id": "b",
      "_deleted": false,
      "_updated": 1,
      "_previous": null,
      "_ts": 1489654249474537,
      "_hash": "d3b66df7c0e6513556378c2ec5b91d5c"
    }
  ]

The second request posts the contents of the second file. Note that
the ``previous_request_id`` references the ``request_id`` of our
previous request. This is just a safety measure so that we make sure
that we don't miss any requests.

::

   $ curl -X POST -H "$AUTH_HEADER" -H "Content-Type: application/json" --data @sequence1.1.json 'http://localhost:9042/api/receivers/myendpoint/entities?is_full=true&sequence_id=1&request_id=2&previous_request_id=1'

Our dataset now contains an updated ``a`` entity and a new ``c`` entity.

::

   $ curl -s -H "$AUTH_HEADER" http://localhost:9042/api/datasets/mydataset/entities | jq .
   [
     {
       "name": "A",
       "_id": "a",
       "_deleted": false,
       "_updated": 0,
       "_previous": null,
       "_ts": 1489654249474509,
       "_hash": "8b48c6574f7e8474194090eb9123666e"
     },
     {
       "name": "B",
       "_id": "b",
       "_deleted": false,
       "_updated": 1,
       "_previous": null,
       "_ts": 1489654249474537,
       "_hash": "d3b66df7c0e6513556378c2ec5b91d5c"
     },
     {
       "name": "A (updated)",
       "_id": "a",
       "_deleted": false,
       "_updated": 2,
       "_previous": 0,
       "_ts": 1489654329529744,
       "_hash": "73873bcb381ebef10644a0bda6798e6a"
     },
     {
       "name": "C",
       "_id": "c",
       "_deleted": false,
       "_updated": 3,
       "_previous": null,
       "_ts": 1489654329529773,
       "_hash": "3b6c7ae2d4d66d9f1cf185f0c3004cce"
     }
   ]

The third request is our last request. It posts the contents of the
third file. Here the ``is_last`` request parameter is set to ``true``
to tell the server that this is the last request in the sequence.

::
   
   $ curl -X POST -H "$AUTH_HEADER" -H "Content-Type: application/json" --data @sequence1.2.json 'http://localhost:9042/api/receivers/myendpoint/entities?is_full=true&sequence_id=1&request_id=3&previous_request_id=2&is_last=true'
   {}

Our dataset now contains a new ``d`` entity.

::
 
   $ curls -H "$AUTH_HEADER" http://localhost:9042/api/datasets/mydataset/entities | jq .
   [
     {
       "name": "A",
       "_id": "a",
       "_deleted": false,
       "_updated": 0,
       "_previous": null,
       "_ts": 1489654249474509,
       "_hash": "8b48c6574f7e8474194090eb9123666e"
     },
     {
       "name": "B",
       "_id": "b",
       "_deleted": false,
       "_updated": 1,
       "_previous": null,
       "_ts": 1489654249474537,
       "_hash": "d3b66df7c0e6513556378c2ec5b91d5c"
     },
     {
       "name": "A (updated)",
       "_id": "a",
       "_deleted": false,
       "_updated": 2,
       "_previous": 0,
       "_ts": 1489654329529744,
       "_hash": "73873bcb381ebef10644a0bda6798e6a"
     },
     {
       "name": "C",
       "_id": "c",
       "_deleted": false,
       "_updated": 3,
       "_previous": null,
       "_ts": 1489654329529773,
       "_hash": "3b6c7ae2d4d66d9f1cf185f0c3004cce"
     },
     {
       "name": "D",
       "_id": "d",
       "_deleted": false,
       "_updated": 4,
       "_previous": null,
       "_ts": 1489654349898053,
       "_hash": "9d8255209c3e1d318e8cf2cab7a3a73e"
     }
   ]

Example 2: full sync (deletion detection)
-----------------------------------------

This example has two JSON request bodies, which look like this:

::
   
   $ cat sequence2.0.json
   [
       {
           "_id": "a",
           "name": "A"
       },
       {
           "_id": "b",
           "name": "B"
       }
   ]
   
   $ cat sequence2.1.json
   [
       {
           "_id": "d",
           "name": "D"
       }
   ]

This example is similar to the previous one, but this time there's
only two requests and we'll show off the deletion detection
feature. Entities that exists in the dataset, but are not part of the
entities sent in a sequence will be marked as deleted.

The first request starts the sequence and posts the contents of the
first file. Note that the ``is_first`` request parameter is set to
``true``.

::
   
   $ curl -X POST -H "$AUTH_HEADER" -H "Content-Type: application/json" --data @sequence2.0.json 'http://localhost:9042/api/receivers/myendpoint/entities?is_full=true&sequence_id=2&request_id=1&is_first=true'

Our dataset now contains an updated ``a`` entity. ``b`` did not
change, so it was not added to the dataset.

::
   
   $ curl -s -H "$AUTH_HEADER" http://localhost:9042/api/datasets/mydataset/entities | jq .
   [
     {
       "name": "A",
       "_id": "a",
       "_deleted": false,
       "_updated": 0,
       "_previous": null,
       "_ts": 1489654249474509,
       "_hash": "8b48c6574f7e8474194090eb9123666e"
     },
     {
       "name": "B",
       "_id": "b",
       "_deleted": false,
       "_updated": 1,
       "_previous": null,
       "_ts": 1489654249474537,
       "_hash": "d3b66df7c0e6513556378c2ec5b91d5c"
     },
     {
       "name": "A (updated)",
       "_id": "a",
       "_deleted": false,
       "_updated": 2,
       "_previous": 0,
       "_ts": 1489654329529744,
       "_hash": "73873bcb381ebef10644a0bda6798e6a"
     },
     {
       "name": "C",
       "_id": "c",
       "_deleted": false,
       "_updated": 3,
       "_previous": null,
       "_ts": 1489654329529773,
       "_hash": "3b6c7ae2d4d66d9f1cf185f0c3004cce"
     },
     {
       "name": "D",
       "_id": "d",
       "_deleted": false,
       "_updated": 4,
       "_previous": null,
       "_ts": 1489654349898053,
       "_hash": "9d8255209c3e1d318e8cf2cab7a3a73e"
     },
     {
       "name": "A",
       "_id": "a",
       "_deleted": false,
       "_updated": 5,
       "_previous": 2,
       "_ts": 1489654388968749,
       "_hash": "8b48c6574f7e8474194090eb9123666e"
     }
   ]

The second request is our last request. It posts the contents of the
second file. Here the ``is_last`` request parameter is set to ``true``
to tell the server that this is the last request in the sequence. Note
that in this example there was no middle request that was neither
``is_first`` nor ``is_last``.

::
   
    $ curl -X POST -H "$AUTH_HEADER" -H "Content-Type: application/json" --data @sequence2.1.json 'http://localhost:9042/api/receivers/myendpoint/entities?is_full=true&sequence_id=2&request_id=2&previous_request_id=1&is_last=true'

Our dataset now contains a deleted ``c`` entity. The entity was
deleted because it did exist in the dataset, but was not part of the
entities that we sent. It is thus marked as deleted. ``d`` did not
change.

::
   
    $ curl -s -H "$AUTH_HEADER" http://localhost:9042/api/datasets/mydataset/entities | jq .
    [
      {
        "name": "A",
        "_id": "a",
        "_deleted": false,
        "_updated": 0,
        "_previous": null,
        "_ts": 1489654249474509,
        "_hash": "8b48c6574f7e8474194090eb9123666e"
      },
      {
        "name": "B",
        "_id": "b",
        "_deleted": false,
        "_updated": 1,
        "_previous": null,
        "_ts": 1489654249474537,
        "_hash": "d3b66df7c0e6513556378c2ec5b91d5c"
      },
      {
        "name": "A (updated)",
        "_id": "a",
        "_deleted": false,
        "_updated": 2,
        "_previous": 0,
        "_ts": 1489654329529744,
        "_hash": "73873bcb381ebef10644a0bda6798e6a"
      },
      {
        "name": "C",
        "_id": "c",
        "_deleted": false,
        "_updated": 3,
        "_previous": null,
        "_ts": 1489654329529773,
        "_hash": "3b6c7ae2d4d66d9f1cf185f0c3004cce"
      },
      {
        "name": "D",
        "_id": "d",
        "_deleted": false,
        "_updated": 4,
        "_previous": null,
        "_ts": 1489654349898053,
        "_hash": "9d8255209c3e1d318e8cf2cab7a3a73e"
      },
      {
        "name": "A",
        "_id": "a",
        "_deleted": false,
        "_updated": 5,
        "_previous": 2,
        "_ts": 1489654388968749,
        "_hash": "8b48c6574f7e8474194090eb9123666e"
      },
      {
        "name": "C",
        "_id": "c",
        "_deleted": true,
        "_updated": 6,
        "_previous": 3,
        "_ts": 1489654451658805,
        "_hash": "ec83ea023462b80f19a23e39639f7307"
      }
    ]
