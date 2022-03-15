
.. _sparql_sink:


SPARQL sink
-----------

The SPARQL sink converts entities to RDF statements and writes them to a graph in a triplestore via a SPARQL compatible
endpoint.

Prototype
^^^^^^^^^

::

    {
        "type": "sparql",
        "system": "id-of-url-system"
        "url": "sparql",
        "update_url": "sparql-update",
        "graph": "http://uri.of/graph",
        "do_diff": false,
        "write_sdshare_updated": true
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
     - The URL part of the SPARQL endpoint to use, see the ``url_pattern`` property of the :ref:`URL system <url_system>`
       for how this is substituted into the System URL.
     -
     - Yes

   * - ``update_url``
     - String
     - The URL part of the SPARQL endpoint to use for updates if it is different from ``url``. See the ``url_pattern``
       property of the :ref:`URL system <url_system>` for how this is substituted into the System URL.
     -
     -

   * - ``system``
     - String
     - The id of a :ref:`URL system <url_system>` component to use. Note that only ``basic`` and ``digest``
       ``authentication`` schemes are supported by the SPARQL sink.
     -
     - Yes

   * - ``graph``
     - String
     - A full URI for the graph to write the entities into.
     -
     - Yes

   * - ``do_diff``
     - Boolean
     - Tell the sink to compute the difference between the target graph RDF statements and the RDF statements generated
       by converting the input entity to RDF. This ensures the minimum number of write operations to the endpoint.
       This does however come with the cost of (many) more read operations. Use this option if your entities are large
       and/or there is large amounts of changes flowing through the sink on average.
     - false
     -

   * - ``write_sdshare_updated``
     - Boolean
     - Tell the sink to automatically insert SDShare updated predicates with the generated RDF statements written to
       the endpoint. Note that the local UTC time is currently used for this timestamp.
     - true
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "sparql",
            "url": "http://virtuoso.example.com:8890/sparql",
            "graph": "http://example.com/fylketest",
            "do_diff": true,
            "write_sdshare_updated": true
    }
