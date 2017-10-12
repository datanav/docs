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

   * - since
     - A token that tells the endpoint
       after what location in the stream to start streaming entities.

       This token references the ``_updated`` property in entities.

       ``since`` is typically used to continue from the point where
       the previous request ended. In order to do this the value of
       the ``_updated`` property in the last entity in the previous
       request can used.

   * - limit
     - An integer. Tells the server to cap the response to this many
       entities. By using limit one can split the entities stream
       across multiple requests.

       The default is to have no limit, which means that all entities
       will be returned. Note that an endpoint may implement a
       different default.

The HTTP body is JSON data which will always be in the form of a
JSON array even if it is a single entity. The
serialisation of entities as JSON is described in more detail
:doc:`here <entitymodel>`.

.. _json_pull_examples:

Examples
========

In the examples we'll use two pipes. The first loads letters into the
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

