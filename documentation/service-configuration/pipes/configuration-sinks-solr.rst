
.. _solr_sink:

Solr sink
---------

The Solr sink writes the entities it is given to a Solr index.

The ``_id`` property is used as the document id. All other properties,
except the ones at the root level matching ``_*`` or ``$*`` are added
to the document. Notice the limitations described in the next section.

This sink supports :ref:`batching <pipe_batching>`.

Limitations
^^^^^^^^^^^

Due to the limited document structure allowed by Solr, there are some
restrictions on the form of the entities accepted by the sink:

* Only "flat" entities are allowed - any child entities must be removed or merged into the root entity before being sent to the sink.
* Lists properties are supported, but they can only contain a single type of property.
* Lists cannot contain other lists or entities.

If the document does not adhere to these rules, then an error is raised.

Prototype
^^^^^^^^^

::

    {
        "type": "solr",
        "system": "solr-system-id",
        "commit_within": null,
        "commit_at_end": true
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

