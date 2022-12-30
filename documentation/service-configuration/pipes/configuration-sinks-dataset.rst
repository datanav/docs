
.. _dataset_sink:

Dataset sink
------------

The dataset sink writes the entities it is given to an identified dataset. The configuration looks like:

Prototype
^^^^^^^^^

::

    {
        "type": "dataset",
        "dataset": "id-of-dataset"
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

   * - ``dataset``
     - String
     - The id of the dataset to write entities into. Note: if it doesn't exist before
       entities are written to the sink, it will be created on the fly.

       .. NOTE::

          The dataset id cannot contain forward slash characters (``/``) nor can it
          reference a ``system:`` dataset.
     -
     - Yes

   * - ``set_initial_offset``
     - Enum<String>
     - This property specifies when the sink should set the initial offset on its dataset.

       When the initial offset is set then the dataset is considered to be *populated*.

       - ``if-source-populated`` (the default) means that the pipe will set the initial offset
         when the source is populated and the pipe has consumed all the source entities. This
         is a very useful default as the populated flag will propagate automatically downstream once
         datasets get populated upstream.
       - ``never`` means that the pipe will never set the initial offset.
       - ``always`` means that the pipe will always set the initial offset when the pipe completed
         successfully.
       - ``initially`` means that the pipe will set the initial offset at the start of the pump run.
       - ``onload`` means that the initial offset will be set when the pipe is loaded / configured.

     - ``if-source-populated``
     -

   * - ``indexes``
     - String or Array
     - If set to ``"$ids"`` then an index on the ``$ids`` property will be automatically
       maintained. This index will then be used by the dataset browser to look up
       entities both by ``_id`` and ``$ids``. The property ``global_defaults.always_index_ids`` can be enabled in
       the :ref:`service metadata <service_metadata_section>` if all dataset sinks should by default maintain an index
       on ``$ids``.

       If the value is an array then it can contain index expressions that should be
       maintained on the sink dataset. This is typically used for declaring subset indexes.
     - ``[]``
     -

   * - ``track_children``
     - Boolean
     - If ``true`` then the ``$children`` property will be compared against the previous
       version of the entity and a delta produced. This will cause the ``$children``
       property to be updated on entities just before they are written to the dataset.

       This is a special feature that can be used in combination with the
       ``["create-child", ...]`` DTL function and the ``emit_children`` pipe transform.
       The purpose is to be able to detect deleted children entities when doing
       incremental syncs.

       The effective value of this property is inferred to be ``true``
       if any of the pipe's transforms use the ``create-child`` DTL
       function. It is possible to override this by setting the
       property's value to ``false``.
     - Inferred
     -

   * - ``enable_optimistic_locking``
     - Boolean
     - If ``true`` then the ``_updated`` property in each entity will be compared against the previous
       version of the entity. If the ``_updated`` property of at least one entity doesn't match, an error
       will raised and no entities will be written to the target dataset.

       The purpose is to be guard against two agents trying to update the same entity at the same time; in some
       cases one doesn't want the last edit to "win" automatically. The typical usecase is a pipe with a
       ``http_endpoint`` source where the http endpoint can be accessed by several independant processes
       that use the sesam instance as a storage service. In this case the pipe should *not* have any transforms,
       since the http_endpoint will send the resulting entity back to the calling process; if the entity has been
       transformed by DTL or some other transform, the result might make little sense to the calling process.

     - ``false``
     -

   * - ``circuit_breaker_threshold_factor``
     - Decimal
     - Specifying this property will enable a :ref:`circuit breaker <circuit-breakers>` on
       the pipe. It specifies a factor that is used to calculate the circuit breaker limit. Note
       that this is a factor and not a percentage, e.g. ``0.32`` means 32% and ``1.5`` means 150%.
       If the factor is ``0.5`` and the dataset already contains 100 entities, then the circuit
       breaker will trip if it sees more than 50 new entities.
     - ``null``
     - No

   * - ``circuit_breaker_threshold_count``
     - Integer
     - Specifying this property will enable a :ref:`circuit breaker <circuit-breakers>` on
       the pipe. The count specifies the circuit breaker limit directly. The limit defines how many
       new entities can be written to the dataset before the circuit breaker trips. If this property
       is set to ``100``, then 100 entities can be written before it trips.

       .. NOTE::

          If both ``circuit_breaker_threshold_factor`` and ``circuit_breaker_threshold_count`` are
          specified then the maximum value of those two are used as the circuit breaker limit. The
          count is in this case typically used to specify the lower limit.
     - ``null``
     - No

   * - ``deletion_tracking``
     - Boolean
     - If ``true`` (the default), then after a full run any entities that existed in the dataset before
       the run but that weren't seen during the run will be deleted.

       If ``false``, then any existing entities in the dataset will not be touched. This is only
       useful in very special circumstances.
     - ``true``
     - No

   * - ``mark_deletion_tracked``
     - Boolean
     - If ``true`` (the default is ``false``), a ``"$deletion_tracked":true`` property will be added to entities deleted
       by deletion tracking after full runs or rescans. See also the ``deletion_tracking`` property.
     - ``false``
     - No

   * - ``bitset_commit_interval``
     - Integer
     - Specifies how often dataset bitsets and dataset compaction changes are written to disk. The higher the number the fewer writes, but at the cost of having to redo the work if the pipe fails before completion. The changes are always written to disk once the pipe completes.
     - ``1000000``
     - No

   * - ``prevent_multiple_versions``
     - Boolean
     - If ``true`` then the pipe will fail if a new version of an existing entity is attempted written to the sink dataset. This is useful if one wants to prevent multiple versions of the same entity to be written to the sink dataset.
     - ``false``
     - No

   * - ``suppress_filtered``
     - Boolean
     - The default value is ``false`` unless it is a full sync and the source is of type ``dataset`` and ``include_previous_versions`` is ``false`` [*]. The purpose of this property is to make it possible to opt-in or opt-out of a specific optimization in the pipe. The optimization is to suppress entities that are filtered out in a transform early so that they are not passed to the sink. This optimization should only be used when the pipe produces exactly one version per ``_id`` in the output. The optimization is useful when the pipe filters out a lot of entities.
     - ``false`` [*]
     - No

   * - ``max_entity_bytes_size``
     - Enum<String>
     - Defines the maximum size in bytes of an individual entity as it is stored in a dataset.
     - ``104857600`` (100MB)
     -


Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "dataset",
            "dataset": "Northwind:Customer",
        }
    }
