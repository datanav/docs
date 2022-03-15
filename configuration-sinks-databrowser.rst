
.. _databrowser_sink:

Sesam Databrowser sink
----------------------

The databrowser sink writes the entities it is given to a Solr index
to be displayed by the Sesam Databrowser application. The input
entities are transformed to special Databrowser JSON documents before
being sent off for indexing.

This sink supports :ref:`batching <pipe_batching>`.

The configuration looks like:

Prototype
^^^^^^^^^

::

    {
        "type": "databrowser",
        "system": "solr-system-id",
        "batch_size": 100,
        "commit_within": null,
        "commit_at_end": true,
        "keep_existing_solr_ids": false,
        "maintain_id_links": false
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
     - The id of the :ref:`Solr system <solr_system>` component to use.
     -
     - Yes

   * - ``batch_size``
     - Integer
     - The maximum number of documents to post to solr in one http request
     - 100
     -
   * - ``commit_within``
     - Integer
     - The number of seconds to wait until committing, i.e. invalidating the Solr
       caches. This is used to set up commit batching. The default is null
       (i.e. not set) which means that a commit will be issued at the end of the
       sync if ``commit_at_end`` is true. Do not set this too low as it will cause
       a lot of overhead on the Solr server.
     - null
     -

   * - ``commit_at_end``
     - Boolean
     - If true, then the sink will issue a commit at the end of the sync. In general
       it is best to rely on ``commit_within`` instead or just let the Solr server
       itself decide the commit interval.
     - true
     -

   * - ``keep_existing_solr_ids``
     - Boolean
     - This can be set to ``true`` in order to try to reuse the existing solr-id of an entity, even if
       the solr-ids of the entity no longer contains the solr-id that exists on the solr server.
       The cons of doing this is that it requires a http-request to solr for *each and every*
       entity, so it is *very* expensive. This option should therefore be set to false in
       cases where the id-problem is not likely to occur.
     - false
     -

   * - ``maintain_id_links``
     - Boolean
     - This can be set to ``true`` in order to maintain links to documents in the Solr index. If the current
       document doesn't exist in the solr index (via its ``id`` property), but there is a match in the ``ids`` property
       of some other document(s), this setting will force the new document to use ab existing id from the index.
       This makes sure any links to an existing document in the Solr index is kept (for example bookmarked documents).
       The option only has an effect if the ``keep_existing_solr_ids`` option is set to ``true``.
     - true
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "databrowser",
            "url": "http://localhost:8893/solr/my_index"
        }
    }
