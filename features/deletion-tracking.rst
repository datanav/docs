.. _deletion-tracking:

Deletion Tracking
=================

The :ref:`dataset sink <dataset_sink>` is capable of detecting that entities have disappeared from the source. It can do this when the pipe does a full rescan. At the end of a pipe run the sink will write a deleted version of those entities (where the ``"_deleted"`` property is set to ``true``). This is a useful feature particularly when the source itself is not able to emit deletes. It is also useful in the cases where filters or other configuration changes causes previously emitted entities to no longer be produced by the pipe.