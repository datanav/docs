.. _compaction-feature:

Compaction
==========

A dataset is an append-only immutable log of data that would, left unchecked, grow forever. This problem is partly mitigated as entities are only written to the log if they are new or different (based on a content hash comparison) from the most recent version of that entity. To supplement this and ensure that a dataset does not consume all available disk space a retention policy can be defined. A retention policy describes the general way in which the log should be compacted. The default policy is to keep two versions of every entity. This is the minimal number of versions to keep in order to make dependency tracking work. A time-based policy is also available allowing you to say how old and entity can be before it becomes a candidate for :ref:`compaction <pipe_compaction>`.