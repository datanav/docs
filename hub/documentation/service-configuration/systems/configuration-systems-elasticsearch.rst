.. _elasticsearch_system:

Elasticsearch system
--------------------

The Elasticsearch system represents the information needed to connect
to an `Elasticsearch <https://en.wikipedia.org/wiki/Elasticsearch>`_ server/cluster for indexing JSON documents. It is
used in conjunction with the :ref:`Elasticsearch sink <elasticsearch_sink>`.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:elasticsearch",
        "hosts": ["localhost:9200"]
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

   * - ``hosts``
     - List<String>
     - Contains a list of host+port pairs, or full URL to the Elasticsearch server(s)
     - ``["localhost:9200"]``
     -

   * - ``username``
     - String
     - The username to use when authenticating with the HTTP server. Note that you also have to specify
       authentication protocol in ``authentication`` and ``password`` for this property to have any effect.
     -
     -

   * - ``password``
     - String
     - The password to use if ``username`` and ``authentication`` is set. It is mandatory if ``username`` is provided.
     -
     -

   * - ``authentication``
     - String
     - What kind of authentication protocol to use. Note that authentication is opt-in only and the default is no
       authentication. Allowed values is "basic" (other authentication methods may be added in the future).
       Note that ``username`` and ``password`` are also required if ``authentication`` is set.
     -
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-elasticsearch-server",
        "name": "Our Elasticsearch Server",
        "type": "system:elasticsearch",
        "hosts": ["localhost:9200"]
    }


Example configuration with authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-elasticsearch-server",
        "name": "Our Elasticsearch Server",
        "type": "system:elasticsearch",
        "hosts": ["localhost:9200"],
        "username": "myusername",
        "password": "$SECRET(password)",
        "authentication": "basic"
    }
