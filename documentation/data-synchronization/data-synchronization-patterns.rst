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


Insert
------

When using Sesam to perform inserts in a system, we need to both make sure that Sesam does not create duplicates as well as make sure that neccessary mapping data is connected to the appropriate global pipe.

Avoid duplicates
^^^^^^^^^^^^^^^^

There are several scenarios where Sesam could potentially send insert messages multiple times:

**Change tracking or dependency tracking**
""""""""""""""""""""""""""""""""""""""""""

Sesam will per default only process data that requires processing, as explained in the :ref:`change tracking <change-tracking>` and :ref:`dependency tracking <dependency-tracking>` features. In the case of inserting data from Sesam however, these functionalities may cause entities to be reprocessed, which could generate multiple insert messages. 
In order to avoid these situations we need check if the data has already been sent. This information may be accessed in the pipe's sink dataset through a :ref:`hops <hops>`. If a source entity can be mapped to a sink entity, we can safely discard the source entity and avoid ducplicate entrys in the target system. In order for the hops to work, we need to make sure that the dataset is populated, even is there's no data in it. We do this by adding the sink property ``"set_initial_offset": "onload"``.


**Batching**
""""""""""""

A pipe will by default process 100 entities before writing to the sink, although this number may vary due to different pipe settings. Should one entity in a batch fail, then the whole batch fails before anything is written to the sink. Sesam will therefore attempt to process these entities again, since the last batch failed, which could lead to multiple successful insert messages for the same entity. This situation is easily avoided by setting the :ref:`pipe batch size <pipe_properties>` to 1. 

**Data loss**
"""""""""""""

As explained in the :ref:`durable data <durable-data>` feature, Sesam does a backup of all the data inside the subscription every 24 hours. However, should inserts be performed in the gap between backups, this data could be lost. Sesam will in that case have no knowledge of which entities is has processed since the last backup, leading to potential duplicate entries to the target system. The solution is to activate durable data on the pipe's sink. This will store all sink dataset data in a third durable version, which in turn ensures that no data is lost.

**Preview**
"""""""""""

When using the preview function in the :ref:`Sesam management studio <sesam-management-studio>`, the preview entity is actually passed through the transform. Normally this is not an issue since the preview function does not pass the data to the sink. However, when performing non-idempotent actions inside a transform this will have side effects. In the case of an insert messages inside a transform the preview will actually attempt to send an insert every time it's used, which could lead to duplicate entries in the target system which are untraceable in Sesam. To avoid this, use the :ref:`transform property side_effects <transform_properties>`. If set to ``true`` the pipe will end the transform, avoiding potential duplicate entries.  

**Deleted entities**
""""""""""""""""""""

Per default Sesam will pass entities with ``"_deleted": true`` through all transforms

Connect mapping data
^^^^^^^^^^^^^^^^^^^^

Once an insert if performed, we need to store both the insert ```_id`` and the original source entity's ``_id`` to the sink dataset. This will allow us to connect these two entities in the corresponding global pipe, which ensures a fully connected data flow. In the case where no other metadata can act as merge critera, this mapping is the only way to connect inserted entites with other corresponding entrys from other source systems.

Insert pipe configuration example 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following example illustrates duplicate entry precautions:

.. code-block:: json

	{
	  "_id": "share-insert",
	  "type": "pipe",
	  "source": {
	    "type": "dataset",
	    "dataset": "insert-source"
	  },
	  "sink": {
	    "set_initial_offset": "onload"
	  },
	  "transform": [{
	    "type": "dtl",
	    "rules": {
	      "default": [
	        ["comment", "removing deleted entities and entities which have already been processed and stored in the sink dataset"],
	        ["discard",
	          ["or",
	            ["eq", "_S._deleted", true],
	            ["is-empty",
	              ["hops", {
	                "datasets": ["share-insert si"],
	                "where": [
	                  ["eq", "_S._id", "si.ref-id"]
	                ]
	              }]
	            ]
	          ]
	        ],
	        ["comment", "create your payload in this transform"],
	        ["copy", "*"]
	      ]
	    }
	  }, {
	    "type": "rest",
	    "system": "my-system",
	    "operation": "insert",
	    "properties": {
	      "url": "my-url"
	    },
	    "side_effects": false
	  }, {
	    "type": "dtl",
	    "rules": {
	      "default": [
	        ["comment", "store the id from the insert as new _id"],
	        ["add", "_id", "_S.response.id"],
	        ["comment", "kepp original _id for mapping purposes"],
	        ["add", "ref-id", "_S._id"],
	        ["merge-union", "_S.response"],
	        ["add", "rdf:type",
	          ["ni", "<my-rdf:type>"]
	        ]
	      ]
	    }
	  }],
	  "metadata": {
	  	"comment": "activating durable data to avoid data loss",
	    "durable": true
	  },
	  "batch_size": 1,
	  "namespaces": {
	    "identity": "<my-namespace>",
	    "property": "<my-namespace>"
	  }
	}
