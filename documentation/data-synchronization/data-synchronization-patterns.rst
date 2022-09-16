.. _data-synchronization-patterns:

=============================
Data Synchronization Patterns
=============================

We've identified a set of patterns when working with problems related to data synchronizaion in Sesam. We find it very useful to name these patterns as it makes it easier to refer to them when discussing problems.

.. note::
  This document is subject to improvements as we continuesly are identifying new patters to enforce effective data synchronization in Sesam.

Collect patterns
================

Source with since support but no deletions
------------------------------------------
Provides data with changes but no information about deletions. Requires periodic rescans. Called *update-in-place systems*.

.. _pattern_source_only_deltas:

Source that only provides delta streams
---------------------------------------

If you restart the pipe you lose a lot of data. Make two pipes, disable, reset and use durable pipe, disable :ref:`deletion tracking <deletion-tracking>`.

Source with parameterized input
-------------------------------

Fetch more data based on some input source, requires rescan all the time. Quick summary is to have one pipe fetch the ids, then have another pipe that reads those ids and typically does a rest-transform for each id.

Recreate best effort history from a source
------------------------------------------

We become master, pipe should be durable (coming feature). Add a last modified timestamp to the entities. If you do not make a unique ``_id`` (e.g. append the last modified timestamp to it) you need to turn off compaction to keep all data.

Make periodic entities from a versioned history
-----------------------------------------------

If a source provides a list of older versions of an entity, one way to materialize this is to convert them into periodic entities instead. This might make it easier to work with if your domain uses fixed periods for other purposes. One way to do this is to use the fixed periods as source and then for each period hop to the versioned dataset and join in the relevant version for this period.

Sporadic empty response
-----------------------

Source sometimes produces an empty array for some reason (during restarts, authentication problems, etc). Use :ref:`circuit breakers <circuit-breakers>`.

Keep the data in its original structure
---------------------------------------
Data modeller expects data in the same structure as the system that produced it, and often need to send back the original structure.

Avoid unnecessary load on source systems
----------------------------------------

For sources that support incremental sync and where pulling all the data might incur additional cost, system instability or other problems, your first pipe in Sesam should just make a clean copy of the data. You should add namespaces and do any other transformations in a secondary pipe, so that you are able to modify these transformations later without causing unnecessary load on the source system.

Share patterns
==============

.. _optimistic_locking:

Optimistic locking
------------------

Should be added via an external transform and then two hash values should be compared. In case of difference, discard entity.

Exposing data
-------------

Focus for the share phase is exposing the data. Data should be transformed into the format of the target schema before it reaches the share phase.

Capture response with transform
-------------------------------

Use transform instead of a sink to capture results back into a dataset. This transform will have side effects and this pipe needs to be durable to avoid reprocessing in case of data loss. Batch size needs to be set to 1 to avoid duplicates as this is not transactional. Do not mix dependency tracking in this pipe as it can also cause duplicates. Avoid the preview API as this will trigger the transform.

External reference
------------------

If datatype has a property where you can store external references, you can merge on this when collecting the shared data back.

Update or insert
----------------
Split into two separate pipelines. Update typically uses the "optimistic locking" pattern, inserts use the "capture response with transform" pattern.
