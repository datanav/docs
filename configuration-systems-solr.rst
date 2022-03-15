.. _solr_system:

Solr system
-----------

The Solr system represents the information needed to connect to a `Apache Solr <https://en.wikipedia.org/wiki/Apache_Solr>`_
server for indexing JSON documents. It is used in conjunction with the :ref:`Solr sink <solr_sink>` or the :ref:`Sesam Databrowser sink
<databrowser_sink>` sinks.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:solr",
        "url": "http://localhost:8983/solr/",
        "timeout": 30,
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

   * - ``url``
     - String
     - Contains a full URL to the Solr dataset to read/write documents from
     - ``http://localhost:8983/solr/``
     -

   * - ``timeout``
     - Integer
     - The number of seconds to wait for a response from the Solr server.
     - 30
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-solr-server",
        "name": "Our Solr Server",
        "type": "system:solr",
        "url": "http://localhost:8983/solr/"
    }

