.. _deletion_tracking:

:badge:`Free feature,badge-success badge-pill`

Deletion Tracking
=================

The :ref:`dataset sink <dataset_sink>` is capable of detecting that entities have disappeared from the source. It can do this when the pipe does a full rescan. At the end of a pipe's run the sink will write a deleted version of those entities (where the ``"_deleted"`` property is set to ``true``). This feature is helpful when the source system doesn't send deleted entities, instead of using a flag to indicate deletion. It is also useful in the case where filters or other configuration changes causes previously sent entities to no longer be produced by the pipe.