.. _durable-data:

Durable Data
============

For cloud subscriptions, data is backed up to an external service once every 24 hours. During a disaster recovery data written the last 24 hours can be lost. This might not a huge problem when Sesam is pulling data from sources, as the data that was lost can be pulled again. For pipes with http_endpoint sources and non-idempotent sinks, this will most likely be a problem. In our cloud subscriptions you now have the possibility to request that a pipes data is stored in three replicas. This reduces the likelihood of data loss. Note that this incurs a 3x increase in data size for the pipes that has this feature enabled.

This feature can be enabled on a pipe by setting the pipe's :ref:`metadata.durable <pipe_metadata_durable>` property to ``true``.