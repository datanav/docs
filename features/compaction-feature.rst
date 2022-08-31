.. _compaction-feature:

Compaction
==========

A dataset is an append-only immutable log of data that would, left unchecked, grow forever. This problem is partly mitigated as entities are only written to the log if they are new or different (based on a content hash comparison) from the most recent version of that entity. To supplement this and ensure that a dataset does not consume all available disk space a retention policy can be defined. A retention policy describes the general way in which the log should be compacted. The compaction feature in Sesam controls such policies. 

The default policy is to keep two versions of every entity. This is the minimal number of versions to keep in order to make dependency tracking work. A time-based policy is also available allowing you to say how old and entity can be before it becomes a candidate for compaction. If compaction is disabled the dataset is automatically compacted once every 24 hours (compaction type "background" in the global settings or


.. NOTE::

   Compaction will only be performed up to the lowest offset for which there exists a pipe doing dependency tracking on the dataset. Each pipe doing dependency tracking keeps a tracking offset on the dataset so that it knows which entities to perform dependency tracking for. It is this tracking offset that compaction cannot go beyond. This is done so that those pipes should not fall out of sync. If the compaction did not hold off then we could not guarantee that the output of those pipes are correct.

   Be aware that disabled pipes also hold off compaction. If the pipes are to be disabled for a long time then it is better to remove the pipe, or alternatively comment out the hops.

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

   * - ``compaction.automatic``
     - Boolean
     - If ``true`` then the dataset is a candidate for automatic compaction.
     - ``true``
     - No

   * - ``compaction.sink``
     - Boolean
     - If ``true`` then the dataset sink will perform dataset compaction. This will make compaction happen incrementally as new entities are written to the dataset. If this is enabled, then automatic compaction won't run for the dataset itself, but dataset index compaction will be scheduled. Note that dataset index compaction does not require a lock on the dataset.
     - ``true``
     - No

   * - ``compaction.keep_versions``
     - Integer
     - The number of unique versions of an entity to keep around. The default is ``2``.
       The value must be greater than or equal to ``0``. If set to ``0`` then a time
       threshold must be set explicitly.

       .. WARNING::

          A value less than ``2`` means that dependency tracking is best effort only,
          and it will not be able to find all reprocessable entities. Do full or partial
          rescans as a counter measure.

     - ``2``
     - No

   * - ``compaction.time_threshold_hours``
     - Integer
     - Specifies the threshold for how old entities must be before they are considered
       for compaction. This property is usually used when you want to keep entities
       around for a certain time.
     - ``null``
     - No

   * - ``compaction.time_threshold_hours_pump``
     - Integer
     - Same as ``compaction.time_threshold_hours``, but applies to the pipe's pump
       execution dataset. Pump execution datasets are always trimmed by time.  The
       default is 30 days, which is the minimum value allowed.
     - ``720``
     - No

   * - ``compaction.growth_threshold``
     - Float
     - The growth factor required for the automatically scheduled compaction to kick
       in. Uses the minimum value of ``1.0`` by default, meaning that compaction will always
       run when new entities are written to the dataset.
     - ``1.0``
     - No

   * - ``compaction.compaction_interval``
     - Float
     - Specifies the sink compaction interval. If this value is zero, sink compaction will run every time
       the pipe runs. If it is larger than zero, sink compaction will only run if at least
       ``compaction_interval`` seconds has passed since the last sink compaction. The use-case for this setting is
       to prevent a pipe that run often from constantly trying to compact the sink-dataset.
     - ``0``
     - No

