.. _merge_datasets_source:

Merge datasets source
---------------------

The merge datasets source is similar to the ``dataset source``, except
it can process several datasets at once and keep track of each one in
its ``since`` marker handler.

The merge datasets source reads its all of its datasets and returns
entities ordered by their ``_ts`` field. It knows how to deal with
identities, so that only the *latest* version of entities are returned.

Entity ids are not modified in any way.

Prototype
^^^^^^^^^

::

   {
       "type": "merge_datasets",
       "datasets": ["id-of-dataset1", "id-of-dataset2"],
       "strategy": "latest",
       "supports_signalling": false
    }

Properties
^^^^^^^^^^

The configuration has two primary properties, ``datasets`` which must
be a list of datasets ids and ``strategy`` for choosing the merge
strategy.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``datasets``
     - List<String>
     - A list of datasets ids.
     -
     - Yes

   * - ``initial_datasets``
     - List<String{>=0}>
     - By default the source will be considered populated if all the datasets in the ``datasets``  property have been populated. If some of these datasets will never be populated then this property can be used to list the datasets that must be populated before the source is considered populated. You should normally not have to use this property.

       See also the :ref:`dataset sink <dataset_sink>` property ``set_initial_offset``.
     -
     -

   * - ``ignore_non_existent_datasets``
     - Boolean
     - If set to ``false``, datasets listed in ``initial_datasets`` that do not exist will prevent the source from
       being populated. With the default value (``true``) the source will be populated even if one or more datasets
       in ``initial_datasets`` do not exist.
     - true
     -

   * - ``require_populated_input``
     - Boolean
     - If set to ``true``, the pipe will not run unless the datasets in ``datasets`` (or in ``initial_datasets``, if it has been specified) have been populated.
       The global default ``global_defaults.require_populated_input`` can be set for all pipes in the
       :ref:`service metadata <service_metadata_section>`.
     - ``false``
     -

   * - ``strategy``
     - String
     - The name of the strategy to use to merge entities. Valid
       options are "``latest``" (the default) and "``all``".

       The "``latest``" strategy returns the version of the entity with
       the newest timestamp (as given in the ``_ts`` field). It will
       return the entity from the dataset that contains the latest
       version. This strategy is useful when only the latest version
       of an entity among the given datasets are of interest.

       The "``all``" strategy returns a merged version of the entity that
       contains all latest versions from all datasets. The individual
       dataset entities are keyed under the dataset id that they came
       from. The entities are ordered by the timestamp of the latest
       version of that entity. The returned entity contains all latest
       versions from all datasets where is appears. This strategy is
       useful when all datasets provide data for the resulting
       entity. In a lot of cases one may want to use it with a
       transform, so that only the entity can be shaped in a way that
       is more useful downstream.
     - "latest"
     -

       .. _merge_datasets_source_property_supports_signalling:

   * - ``supports_signalling``
     - Boolean
     - Flag used to enable or disable signalling support between internal pipes (dataset to dataset pipes). If enabled, a pipe
       run is scheduled as soon as the input dataset(s) changes. It does not interrupt any already running pipes.

       See ``global_defaults.use_signalling_internally`` in the :ref:`service metadata <service_metadata_global_defaults_use_signalling_internally>` section for more details.

       If signalling is enabled globally, you will have to explicitly set ``supports_signalling`` to ``false`` to
       disable it on individual pipes where you don't want to automatically schedule runs on changes. Note that it is
       automatically disabled (if not explicitly enabled on the source) if the schedule interval is less than 2 minutes or a cron
       expression has been used.
     - false
     -

   * - ``if_source_empty``
     - Enum<String>
     - Determines the behaviour of the pipe when the merge datasets source does not return any entities. Normally, any previously synced
       entities will be deleted even if the pipe does not receive any entities from its source.
       If set to ``"fail"``, the pipe will automatically fail if the source returns no entities. This means that any
       previous entities in the pipe's dataset are not deleted.
       If set to ``"accept"``, the pipe will *not* fail and any previously synced entities will be deleted.

       The global default ``global_defaults.if_source_empty`` can be set for all pipes in the
       :ref:`service metadata <service_metadata_section>`.
     - ``"accept"``
     -


Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``true`` (Fixed)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``true`` (Fixed)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "merge_datasets",
            "datasets": ["products", "products-metadata"]
        }
    }
