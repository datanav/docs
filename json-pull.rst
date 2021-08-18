.. _json_pull_protocol:

==================
JSON Pull Protocol
==================


.. contents:: Table of Contents
   :depth: 2
   :local:

The JSON Pull protocol is an HTTP-based protocol that uses GET
requests to retrieve streams of :doc:`entities <entitymodel>`. It
supports splitting up the data across multiple requests.

The protocol is supported by the :ref:`http_endpoint
<http_endpoint_sink>` sink and the :ref:`json <json_source>`
source. This protocol can be used by microservices and other clients
to retrieve entities.

Requests
========

The following HTTP request parameters are supported:

.. list-table::
   :header-rows: 1
   :widths: 20, 80

   * - Parameter
     - Description

   * - ``since``
     - A token that tells the endpoint
       after what offset in the stream to start streaming entities.

       This token references the ``_updated`` property in entities.

       ``since`` is typically used to continue from the point where
       the previous request ended. In order to do this the value of
       the ``_updated`` property in the last entity in the previous
       request can used.

       If the ``since`` request parameter is not given it means that
       entities from the beginning should be returned.

   * - ``limit``
     - An integer. Tells the server to cap the response to this many
       entities. By using limit one can split the entities stream
       across multiple requests.

       The default is to have no limit, which means that all entities
       will be returned. Note that an endpoint may implement a
       different default.

   * - ``subset``
     - If specified then the specified JSON encoded subset expression
       will be used to retrieve a subset of entities. If the
       subset does not exist, then 404 is returned. This is an optional
       feature and the endpoint may not support subsets at all. In that
       case it may ignore the request parameter entirely.

The HTTP body is JSON data which will always be in the form of a
JSON array even if it is a single entity. The
serialisation of entities as JSON is described in more detail
:doc:`here <entitymodel>`.


Response headers
================

.. list-table::
   :header-rows: 1
   :widths: 20, 80

   * - Header
     - Description

   * - ``X-Dataset-Populated``
     - This header contains the dataset's populated flag. It is ``true`` if the dataset is populated and ``false`` if it is not. If the header is missing then the populated flag should be considered to be unknown.

   * - ``X-Dataset-Max-Updated``
     - This is the highest committed offset in the dataset. If you ask for all the entities then the last entity you receive should have this offset in its ``_updated`` property. The value is JSON encoded.

   * - ``X-Dataset-Filtered``
     - This will be set to ``true`` if the source entity stream is filtered. In general you aren't guaranteed to see the entity at the ``X-Dataset-Max-Updated`` offset in this case. One example of where you'll see this is if you have a :ref:`publisher pipe <http_endpoint_sink>` that has a transform.

   * - ``X-Dataset-Generation``
     - When a dataset is created it is assigned a UUID. If the dataset is deleted and then recreated it will get a new generation UUID.

   * - ``X-Dataset-Restore-Uuid``
     - When a dataset is restored [from a backup] then it is assigned a UUID.

   * - ``X-Dataset-Restore-Offset``
     - This the highest committed offset in the dataset at the point when it was last restored. The value is JSON encoded.

The :ref:`automatic reprocessing <automatic_reprocessing>` feature makes use of several of these headers to know when to rewind or reset a pipe.


.. _json_pull_examples:

Example: published endpoint
===========================

In this example we'll use two pipes. The first loads letters into the
``letters`` dataset:

::

   {
       "_id": "letters",
       "type": "pipe",
       "source": {
           "type": "embedded",
           "entities": [
               {"_id": "A"},
               {"_id": "B"},
               {"_id": "C"},
               {"_id": "D"},
               {"_id": "E"},
               {"_id": "F"},
               {"_id": "G"},
               {"_id": "H"},
               {"_id": "I"},
               {"_id": "J"},
               {"_id": "K"},
               {"_id": "L"},
               {"_id": "M"},
               {"_id": "N"},
               {"_id": "O"},
               {"_id": "P"},
               {"_id": "Q"},
               {"_id": "R"},
               {"_id": "S"},
               {"_id": "T"},
               {"_id": "U"},
               {"_id": "V"},
               {"_id": "W"},
               {"_id": "X"},
               {"_id": "Y"},
               {"_id": "Z"}
           ]
       }
   }

The second one publishes the dataset as an :ref:`HTTP endpoint
<http_endpoint_sink>`:

::

    {
        "_id": "published-letters",
        "type": "pipe",
        "source": {
            "type": "dataset",
            "dataset": "letters"
        },
        "sink": {
            "type": "http_endpoint"
        }
    }

Once the ``letters`` pipes has been run then the ``letters`` dataset
has been populated. It should contain 26 entities - one for each
letter.

To use the ``curl`` command to communicate with Sesam we need a JWT
token for authorization. We'll add the JWT authorization header to an
environment variable to make this easier:

::

   export AUTH_HEADER="Authorization: bearer YOUR-JWT-TOKEN"

Now we can use the `published endpoint <./api.html#get--publishers-pipe_id-entities>`_,
``/api/publishers/published-letters/entities``, which supports the
JSON Pull protocol, to retrieve the entities.

::

    $ curl -s -H "$AUTH_HEADER" 'http://localhost:9042/api/publishers/published-letters/entities' | jq .
    [
      {
        "_id": "A",
        "_deleted": false,
        "_updated": 0,
        "_previous": null,
        "_ts": 1507790035417034,
        "_hash": "16347804dece906038080f1ce18fc581"
      },
      {
        "_id": "B",
        "_deleted": false,
        "_updated": 1,
        "_previous": null,
        "_ts": 1507790035417078,
        "_hash": "49316b0ce64d07e4cf58ff8caede27c3"
      },
      {
        "_id": "C",
        "_deleted": false,
        "_updated": 2,
        "_previous": null,
        "_ts": 1507790035417108,
        "_hash": "964675e8251bbc72f66e6b97fe91482f"
      },
      ...snip...
      {
        "_id": "X",
        "_deleted": false,
        "_updated": 23,
        "_previous": null,
        "_ts": 1507790035417768,
        "_hash": "268c63c34e22c7a63053e8aad251b3aa"
      },
      {
        "_id": "Y",
        "_deleted": false,
        "_updated": 24,
        "_previous": null,
        "_ts": 1507790035417793,
        "_hash": "986e0f38daace41b0bd4a122ed540967"
      },
      {
        "_id": "Z",
        "_deleted": false,
        "_updated": 25,
        "_previous": null,
        "_ts": 1507790035417817,
        "_hash": "05118526797098ea97f0b63ae562e174"
      }
    ]

Because we did not specify any request parameters, all entities in the
dataset was returned.

We can also ask for entities that arrived after as specific point by
using the ``since`` request parameter. This will return only entities
that have a value in their ``"_updated"`` property that are ordered after
the one given in the ``since`` request parameter.

::

    $ curl -s -H "$AUTH_HEADER" 'http://localhost:9042/api/publishers/published-letters/entities?since=21' | jq .
    [
      {
        "_id": "W",
        "_deleted": false,
        "_updated": 22,
        "_previous": null,
        "_ts": 1507790035417743,
        "_hash": "fb732242a8014e1409cb20a9888ca91e"
      },
      {
        "_id": "X",
        "_deleted": false,
        "_updated": 23,
        "_previous": null,
        "_ts": 1507790035417768,
        "_hash": "268c63c34e22c7a63053e8aad251b3aa"
      },
      {
        "_id": "Y",
        "_deleted": false,
        "_updated": 24,
        "_previous": null,
        "_ts": 1507790035417793,
        "_hash": "986e0f38daace41b0bd4a122ed540967"
      },
      {
        "_id": "Z",
        "_deleted": false,
        "_updated": 25,
        "_previous": null,
        "_ts": 1507790035417817,
        "_hash": "05118526797098ea97f0b63ae562e174"
      }
    ]

Asking for ``since=21`` returned the last four letters which had
sequence values 22, 23, 24 and 25.

Now, if we only want a certain number of letters in each request we
can use the ``limit`` request parameter to specify how many entities
we want.


Let's ask for 3 entities since 20.

::

  $ curl -s -H "$AUTH_HEADER" 'http://localhost:9042/api/publishers/published-letters/entities?since=20&limit=3' | jq .
  [
    {
      "_id": "V",
      "_deleted": false,
      "_updated": 21,
      "_previous": null,
      "_ts": 1507790035417716,
      "_hash": "3e51777d62023b889d1c0f5e31b5fdba"
    },
    {
      "_id": "W",
      "_deleted": false,
      "_updated": 22,
      "_previous": null,
      "_ts": 1507790035417743,
      "_hash": "fb732242a8014e1409cb20a9888ca91e"
    },
    {
      "_id": "X",
      "_deleted": false,
      "_updated": 23,
      "_previous": null,
      "_ts": 1507790035417768,
      "_hash": "268c63c34e22c7a63053e8aad251b3aa"
    }
  ]

And then 3 entities since 23.

::

  $ curl -s -H "$AUTH_HEADER" 'http://localhost:9042/api/publishers/published-letters/entities?since=23&limit=3' | jq .
  [
    {
      "_id": "Y",
      "_deleted": false,
      "_updated": 24,
      "_previous": null,
      "_ts": 1507790035417793,
      "_hash": "986e0f38daace41b0bd4a122ed540967"
    },
    {
      "_id": "Z",
      "_deleted": false,
      "_updated": 25,
      "_previous": null,
      "_ts": 1507790035417817,
      "_hash": "05118526797098ea97f0b63ae562e174"
    }
  ]

Example: dataset subset
=======================

In this example we'll use one pipe. It is almost the same as the one in the previous section, but this time we've identified the vowels and also declared an index on the :ref:`dataset sink <dataset_sink>`. This index can be used to retrieve a subset from the ``letters`` dataset:

::

   {
       "_id": "letters",
       "type": "pipe",
       "source": {
           "type": "embedded",
           "entities": [
               {"_id": "A", "vowel": true},
               {"_id": "B"},
               {"_id": "C"},
               {"_id": "D"},
               {"_id": "E", "vowel": true},
               {"_id": "F"},
               {"_id": "G"},
               {"_id": "H"},
               {"_id": "I", "vowel": true},
               {"_id": "J"},
               {"_id": "K"},
               {"_id": "L"},
               {"_id": "M"},
               {"_id": "N"},
               {"_id": "O", "vowel": true},
               {"_id": "P"},
               {"_id": "Q"},
               {"_id": "R"},
               {"_id": "S"},
               {"_id": "T"},
               {"_id": "U", "vowel": true},
               {"_id": "V"},
               {"_id": "W"},
               {"_id": "X"},
               {"_id": "Y", "vowel": true},
               {"_id": "Z"}
           ]
       },
       "sink": {
           "indexes": ["_S.vowel"]
       }
   }


Now we can use the `dataset endpoint <./api.html#get--datasets-dataset_id-entities>`_,
``/api/datasets/letters/entities``, which supports the
JSON Pull protocol, to retrieve the subset. The subset is expressed as an equality expression, ``["eq", "_S.vowel", true]``, with the index expression in the left side and the subset value on the right side. Note that all request parameters must be URL encoded, and in the case of the subset expression this makes it look garbled.

::

    $ curl -s -H "$AUTH_HEADER" 'http://localhost:9042/api/datasets/letters/entities?subset=%5B%22eq%22%2C+%22_S.vowel%22%2C+true%5D' | jq .
    [
      {
        "vowel": true,
        "_id": "A",
        "_deleted": false,
        "_updated": 0,
        "_previous": null,
        "_ts": 1566889765658992,
        "_hash": "bd43d289d45c8dccffda0aa05d9e39cf"
      },
      {
        "vowel": true,
        "_id": "E",
        "_deleted": false,
        "_updated": 4,
        "_previous": null,
        "_ts": 1566889765659581,
        "_hash": "36d1cfe98ee07d463c82d356cac55c35"
      },
      {
        "vowel": true,
        "_id": "I",
        "_deleted": false,
        "_updated": 8,
        "_previous": null,
        "_ts": 1566889765660099,
        "_hash": "0f46df8330b95f661d1165eba5a141ac"
      },
      {
        "vowel": true,
        "_id": "O",
        "_deleted": false,
        "_updated": 14,
        "_previous": null,
        "_ts": 1566889765660912,
        "_hash": "0a02eda8f99d6bf81f49e63a059f95fa"
      },
      {
        "vowel": true,
        "_id": "U",
        "_deleted": false,
        "_updated": 20,
        "_previous": null,
        "_ts": 1566889765661476,
        "_hash": "c50c560caac61b289a605a8f23e044ce"
      },
      {
        "vowel": true,
        "_id": "Y",
        "_deleted": false,
        "_updated": 24,
        "_previous": null,
        "_ts": 1566889765661751,
        "_hash": "82bb94970ffea2b08cc15de9d26dd4f6"
      }
    ]

Note that subsets can also be exposed via a published endpoint, but then the ``subset`` property must be specified on the :ref:`dataset source <dataset_source>`. In that case the ``subset`` request parameter is not neccessary as only this one specific subset is published.
