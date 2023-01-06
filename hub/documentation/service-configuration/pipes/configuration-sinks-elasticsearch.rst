
.. _elasticsearch_sink:

Elasticsearch sink
------------------

The Elasticsearch sink writes the entities it is given to an
Elasticsearch server/cluster.

The ``_id`` property is used as the document id. All other properties,
except the ones at the root level matching ``_*`` or ``$*`` are added
to the document.

If the input entity has the property ``$index`` then this is the index
into which the document is written. The ``$type`` property is used as
the document type. Note that default values for ``$index`` and
``$type`` can be specified with the ``default_index`` and ``default_type``
properties.

This sink supports :ref:`batching <pipe_batching>`.

Prototype
^^^^^^^^^

::

    {
        "type": "elasticsearch",
        "system": "elasticsearch-system-id",
        "default_index": null,
        "default_type": null
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

   * - ``system``
     - String
     - The id of the :ref:`Elasticsearch system <elasticsearch_system>` component to use.
     -
     - Yes

   * - ``default_index``
     - String
     - The index to insert the documents into. This the default value for
       the ``$index`` property on the indexable entities. Note that this is
       overridable on each entity.
     - null
     -

   * - ``default_type``
     - String
     - The document type to use for the entities. This the default value for
       the ``$type`` property on the indexable entities. Note that this is
       overridable on each entity.
     - null
     -

   * - ``index_mapping_properties``
     - Object
     - If this is set the specified property mappings are added to the elasticsearch index.
       See `<https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html>`_
       for more information. Note that if this property is changed the pipe will be reset
       if :ref:`automatic reprocessing <automatic_reprocessing>` is enabled.

       | example:
       |     {
       |         "dataset": {"type": "keyword"},
       |         "namespaces": {"type": "keyword"},
       |         "ids": {"type": "keyword"},
       |         "refs": {"type": "keyword"}
       |     }
     - null
     -

   * - ``index_check_document``
     - String
     - If this is set, the specified elasticsearch document will be used as a marker
       to check if the elasticsearch index contains data from this pipe. The usecase
       is to automatically reset the pipe if the elasticsearch index has been emptied
       by some external process.

       If the '_source' field is enabled in the elasticsearch index (this is the
       default), the pipe will check if the document in the index is identical with the
       ``index_check_document`` value. If '_source' is disabled, the pipe will only check
       that the document exists in the index.
     - null
     -

   * - ``first_run_delete_query``
     - Object
     - If this is set, the value will be used in a 'delete_by_query' call each time
       this pipe is doing a full run.
       See `<https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-delete-by-query.html>`_
       for the details on how the 'delete_by_query' operation works. The value in
       the ``first_run_delete_query`` sink-property is used as the 'query'.'match' value
       in the 'delete_by_query' call.

       | example:
       |     {
       |         "dataset": "my-source-dataset"
       |     }
     - null
     -
