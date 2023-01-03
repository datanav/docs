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

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-elasticsearch-server",
        "name": "Our Elasticsearch Server",
        "type": "system:elasticsearch",
        "hosts": ["localhost:9200"]
    }

