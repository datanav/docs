===============
Design patterns
===============

We've identified a set of patterns when working with problems related to dataflows in Sesam. We find it very useful
to name these patterns as it makes it easier to refer to them when discussing problems.

Here we present a list of them, grouped by the step in the dataflow that the problem manifests itself at.

.. note::
  This document is work in progress, but we publish it as it might contain useful tips.
  
Generic patterns
================

Rewriting identity
------------------
When rewriting ``_id`` you should always add a ``["add", "$original_id", "_S._id"]`` in order to be able to trace and debug. Multiple upstream entities could map to the same identity, and this can be very hard to figure out without this information. Also make sure you rewrite the identifier before you do any filtering.

Collect patterns
================

Source with since support but no deletions
------------------------------------------
Provides data with changes but no information about deletions. Requires periodic rescans. Called *update-in-place
systems*.

.. _pattern_source_only_deltas:

Source that only provides delta streams
---------------------------------------
If you restart the pipe you lose a lot of data. Make two pipes, disable, reset and use durable pipe,
disable deletion tracking.

Source with parameterized input
-------------------------------
Fetch more data based on some input source, requires rescan all the time.

Recreate best effort history from a source
------------------------------------------
We become master, pipe should be durable (coming feature). Add a last modified timestamp to the entities. If you do not make a unique ``_id`` (e.g. append the last modified timestamp to it) you need to turn off compaction to keep all data.

Make periodic entities from a versioned history
-----------------------------------------------
If a source provides a list of older versions of an entity, one way to materialize this is to convert them into periodic entities instead. This might make it easier to work with if your domain uses fixed periods for other purposes. One way to do this is to use the fixed periods as source and then for each period hop to the versioned dataset and join in the relevant version for this period.

Sporadic empty response
-----------------------
Source sometimes produces an empty array for some reason (during restarts, authentication problems, etc). Use :ref:`circuit breakers <concepts-circuit-breakers>`.

Avoid unnecessary load on source systems
----------------------------------------
For sources that support incremental sync and where pulling all the data might incur additional cost, system instability or other problems, your first pipe in Sesam should just make a clean copy of the data. You should add namespaces and do any other transformations in a secondary pipe, so that you are able to modify these transformations later without causing unnecessary load on the source system.

Enrich patterns
===============

Extract foreign references as separate datatypes
------------------------------------------------
Don't make NIs to stuff that is outside your control, keep the namespace local to the system. Extract the
properties to new separate datatypes. If you don't have them as objects you can't merge them with the same concept from
other sources. Time is not a good candidate for NI. Postal codes are a good example. If you make a NI make it reference your
own namespace. Use :ref:`create <dtl_transform-create>`.

Adding type information
-----------------------
Useful to pick out relevant subsets from the globals later. Add data type property (``rdf:type`` or ``$type``).

Splitting out lists of sub-objects
----------------------------------
Aggregate objects --- are the sub-objects part of the parent or can they live on their own? Use :ref:`create-child <dtl_transform-create-child>` and :ref:`emit_children <emit_children_transform>`.

Keep the data in its original structure
---------------------------------------
Data modeller expects data in the same structure as the system that produced it, and often need to send back the original structure.

Normalising data
----------------
Convert data to Sesam types and add them as new properties. Try to use different namespaces for the original data vs the normalised data.

Extract reference properties as reference/classification entities
-----------------------------------------------------------------
Having references as separate entities makes it possible to merge them with other reference entities from other systems and make it possible to map data from one system to another in the connect phase.

To extract entities you will have to use the :ref:`create <dtl-transforms>` transform function. To pick a subset of your extracted entities, you should use :ref:`filtering <dtl-transforms>`. 

.. warning::

  If you do a full scan for deletion tracking, then subset in the source will still create entities that are not in the latest versions of that subset, therefore :ref:`subset <dataset_source>` **should** not be used in conjunction with create.


Connect patterns
================

Cleaning data
-------------
Should be added as new properties, you might need the dirty data.

External merge
--------------
Hardcoded dataset with manually connected IDs, could also be an external source with manual input. Linking table. AI connected objects. `Duke <https://github.com/larsga/Duke>`_ is an example. Produces link objects.

Golden property based on priority
---------------------------------
Use :ref:`coalesce <coalesce_dtl_function>`.

Golden property based on last updated
-------------------------------------
Make sure you have a reliable timestamp from the source that you propagate. Think about feedback loops if data is
synced back. Can be good to standardise on e.g. ``$last_updated``.

Golden property based on quality
--------------------------------
Make a normalised quality score across the sources you want to pick from, and pick the property from the source that has the most relevant score.

..
  _This: (perhaps move below pattern to new "Enhanced patterns" phase)

Feedback loop
-------------------------------------------------------------
Expensive hops or external transforms is best to do in a separate dataflow. This allows you to optimise what you process using subsets, the primary dataflow does not have to wait for this data, it will be processed later if it applied to the entity. Entities might be processed twice if the feedback affected the entity. Use the ``_id`` of the merge source as the identifier. Make sure the feedback is marked as deleted when the data that produced it no longer exists (otherwise entities will never be deleted due to the feedback entity itself).

Hungarian notation references
-----------------------------
When referencing from one global to another global, one can  encode which global the reference points to in order to make it easier to understand what the reference is. E.g. a parent reference from global-person to global-person could be `parent-person-ni`. The reference name in this case is `parent` and the reference points to `global-person` and is of type `namespaced identifier`.

Transform patterns
==================

Late schema binding
-------------------
Ensure transformations are done in accordance to target schema. Only map using the datatypes namespace (bidirectional sync might not support patching, and you need the entire original object when sharing), and the global namespace. If you reference other namespaces you can no longer do all refactoring in the connect phase. 


Defining hierarchies for recursion
----------------------------------
:ref:`Recursive hops <hops>` should be used when your data exhibits inverse relationships. Typically used when filtering on reference/classification properties.

An inverse relationship allows for you to `broaden or narrow <https://www.w3.org/TR/2005/WD-swbp-skos-core-guide-20051102/#sechierarchy>`_ the scope of your data. 

When doing recursive hops you should define the property ``max_depth`` to safeguard against never ending recursions.

Re-mapping references to target identifiers
-------------------------------------------
You use the "Extract reference properties as reference/classification entities" pattern so that you can remap references to target identifiers by hopping to the classification/reference dataset and use the property from the correct target namespace.

Share patterns
==============

.. _optimistic_locking:

Optimistic locking
------------------
Should be added via an external transform and then two hash values should be compared. In case of difference, discard entity.

Exposing data
-------------
Focus should be on exposing data.

Capture response with transform
-------------------------------
Use transform instead of a sink to capture results back into a dataset. This transform will have side effects and this pipe needs to be durable to avoid reprocessing in case of data loss. Batch size needs to be set to 1 to avoid duplicates as this is not transactional. Do not mix dependency tracking in this pipe as it can also cause duplicates. Avoid the preview API as this will trigger the transform.

External reference
------------------
If datatype has a property where you can store external references, you can merge on this when collecting the shared data back.

Update or insert
----------------
Split into two separate pipelines. Update typically uses the "optimistic locking" pattern, inserts use the "capture response with transform" pattern.