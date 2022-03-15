
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
``$type`` can be specified on the :ref:`Elasticsearch system
<elasticsearch_system>`.

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
