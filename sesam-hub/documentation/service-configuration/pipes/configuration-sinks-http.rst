
.. _http_endpoint_sink:

HTTP endpoint sink
------------------

This is a special data sink that registers an HTTP publisher endpoint
that one can get entities from.

A pipe that references the ``HTTP endpoint`` sink will not pump any
entities, in practice this means that a pump is not configured for the
pipe; the only way for entities to flow through the pipe is by
retrieving them from the HTTP endpoint.

It exposes these URLs:

.. list-table::
   :header-rows: 1
   :widths: 50, 60

   * - URL
     - Description

   * - ``http://localhost:9042/api/publishers/mypipe/entities``
     - JSON entities endpoint

   * - ``http://localhost:9042/api/publishers/mypipe/entities/some_filename.json``
     - JSON entities endpoint - filename in URL variant

   * - ``http://localhost:9042/api/publishers/mypipe/sdshare-collection``
     - SDShare collections feed

   * - ``http://localhost:9042/api/publishers/mypipe/sdshare-fragments``
     - SDShare fragments feed

The serialisation of entities as JSON is described in more detail
:ref:`here <entity-data-model>`. This endpoint is compatible with :ref:`The
JSON source <json_source>`.

Note that any URL parameters given to these endpoints are bound to a DTL variable named ``_B``
and is available to any DTL transform on the pipe in which the endpoint sink is a part, see
:ref:`DTL Variables <variables>` for more details.

The SDShare protocol is described `here
<http://www.sdshare.org/spec/sdshare-v1.0.html>`__.

The exposed URLs may support additional parameters such as ``since`` and ``limit`` - see
the `API reference <./api.html#get--publishers-pipe_id-sdshare-collection>`__ for the full details.

Prototype
^^^^^^^^^

::

    {
        "type": "http_endpoint"
    }


Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``filename``
     - String
     - This property provides a hint to HTTP clients on what filename to use when downloading data (via the
       ``Content-Disposition`` header property). Note that this property is not entirely standardized yet, so to be
       compatible with most HTTP clients, the filename should be ASCII characters only. For the same reason, quotes or
       backward or forward slashes should be avoided. If this property is not set, the contents will be served inline.
     -
     -

   * - ``content_disposition``
     - String
     - This property provides a hint to HTTP clients how to render the file data. The valid values are ``attachment``
       and ``inline``. It is used in the ``Content-Disposition`` header and the behaviour is client specific.
     - ``attachment``
     -


Example configuration
^^^^^^^^^^^^^^^^^^^^^

The pipe configuration given below will expose the ``my-entities``
publisher endpoint and read the entities from the ``my-entities``
dataset

::

    {
        "_id": "my-entities",
        "name": "My published entities endpoint",
        "type": "pipe",
        "sink": {
            "type": "http_endpoint"
        }
    }


