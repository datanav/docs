Recreate best effort history from a source pattern
--------------------------------------------------

We become master, pipe should be durable (coming feature). Add a last modified timestamp to the entities. If you do not make a unique ``_id`` (e.g. append the last modified timestamp to it) you need to turn off compaction to keep all data.