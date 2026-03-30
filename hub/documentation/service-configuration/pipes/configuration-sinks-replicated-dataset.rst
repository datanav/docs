.. _replicated_dataset_sink:

Replicated dataset sink
-----------------------

The replicated dataset sink writes entities to a **replicated** dataset. Unlike the normal
:ref:`dataset sink <dataset_sink>`, it preserves the original entity sequence order and offsets from
the upstream source, making the resulting dataset a faithful copy.

A typical use case is renaming a pipe: create a new pipe that sources from the existing dataset and
uses a ``replicated_dataset`` sink writing to the new dataset name. Downstream pipes can then be
switched to the new dataset, and the original pipe retired.

.. NOTE::

   Deletion tracking, entity re-posting, and circuit breakers are **not** supported by this sink type.

Prototype
^^^^^^^^^

::

    {
        "type": "replicated_dataset",
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
     - The id of the dataset to write entities into. If the dataset does not exist it will be created
       as a replicated dataset.

       Note: the dataset id cannot contain forward slash characters (``/``) nor can it reference a
       ``system:`` dataset.
     - The pipe id.
     - Yes

   * - ``set_initial_offset``
     - Enum<String>
     - Controls when the sink marks its dataset as *populated*. Accepts the same values as the
       :ref:`dataset sink <dataset_sink>`: ``if-source-populated`` (default), ``never``, ``always``,
       ``initially``, and ``onload``.
     - ``if-source-populated``
     -

   * - ``indexes``
     - String or Array
     - If set to ``"$ids"`` then an index on the ``$ids`` property will be automatically
       maintained. If the value is an array then it can contain index expressions that should be
       maintained on the sink dataset. This is typically used for declaring subset indexes.
     - ``[]``
     -

   * - ``change_tracking``
     - Boolean
     - If ``true`` (the default), the sink will deduplicate identical entity versions and avoid writing
       an entity if it is identical to the previous version already stored in the dataset.
     - ``true``
     - No

   * - ``bitset_commit_interval``
     - Integer(>=1)
     - Specifies how many entities are processed before bitset updates are persisted to disk. The higher
       the number the fewer writes, but at the cost of having to redo the work if the pipe fails before
       completion. The changes are always written to disk once the pipe completes.
     - ``1000000``
     - No

   * - ``allow_normal_dataset``
     - Boolean
     - If ``true``, the sink will fall back to the normal dataset writer if the sink dataset already
       exists as a ``NORMAL`` type dataset, instead of raising an error. This is useful during a
       migration from a normal dataset to a replicated dataset.
     - ``false``
     - No

   * - ``auto_migrate_to_replicated_dataset``
     - Boolean
     - If ``true``, the sink will automatically convert an existing ``NORMAL`` dataset to a
       ``REPLICATED`` type in an atomic, re-entrant operation. All downstream pipes are quiesced,
       the old dataset is replaced, and downstream offsets are updated before the pipe re-runs.
     - ``false``
     - No



Example configuration
^^^^^^^^^^^^^^^^^^^^^


Renaming a pipe (copying ``old-pipe`` dataset to ``new-pipe``):

::

    {
        "_id": "new-pipe",
        "type": "pipe",
        "source": {
            "type": "dataset",
            "dataset": "old-pipe",
            "include_previous_versions": true
        },
        "sink": {
            "type": "replicated_dataset",
            "dataset": "new-pipe"
        }
    }

Once ``new-pipe`` is fully populated, downstream pipes can be switched from ``old-pipe`` to
``new-pipe`` and ``old-pipe`` can be retired.
