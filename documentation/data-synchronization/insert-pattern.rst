.. _insert_pattern:

Insert Pattern
--------------

When using Sesam to perform inserts in a system, we need to both make sure that Sesam does not create duplicates as well as make sure that neccessary mapping data is connected to the appropriate global pipe.

Avoid duplicates
^^^^^^^^^^^^^^^^

There are several scenarios where Sesam could potentially send insert messages multiple times:

Due to Change tracking or dependency tracking
"""""""""""""""""""""""""""""""""""""""""""""

Sesam will per default only process data that requires processing, as explained in the :ref:`change tracking <change-tracking>` and :ref:`dependency tracking <dependency-tracking>` features. In the case of inserting data from Sesam however, these functionalities may cause entities to be reprocessed, which could generate multiple insert messages. 
In order to avoid these situations we need check if the data has already been sent. This information may be accessed in the pipe's sink dataset through a :ref:`hops <hops>`. If a source entity can be mapped to a sink entity, we can safely discard the source entity and avoid ducplicate entrys in the target system. In order for the hops to work, we need to make sure that the dataset is populated, even is there's no data in it. We do this by adding the sink property ``"set_initial_offset": "onload"``.

Due to Batching
"""""""""""""""

A pipe will by default process 100 entities before writing to the sink, although this number may vary due to different pipe settings. Should one entity in a batch fail, then the whole batch fails before anything is written to the sink. Sesam will therefore attempt to process these entities again, since the last batch failed, which could lead to multiple successful insert messages for the same entity. This situation is easily avoided by setting the :ref:`pipe batch size <pipe_properties>` to 1. 

Due to Data loss
""""""""""""""""

Should inserts be performed in the gap between backups, data could be lost. Sesam will in that case have no knowledge of which entities is has processed since the last backup, leading to potential duplicate entries to the target system. The solution is to activate :ref:`durable data <durable-data>` on the pipe's sink.

Due to Preview
""""""""""""""

When using the preview function in the :ref:`Sesam management studio <sesam-management-studio>`, the preview entity is actually passed through the transform. Normally this is not an issue since the preview function does not pass the data to the sink. However, when performing non-idempotent actions inside a transform this will have side effects. In the case of an insert messages inside a transform the preview will actually attempt to send an insert every time it's used, which could lead to duplicate entries in the target system which are untraceable in Sesam. To avoid this, use the :ref:`transform property side_effects <transform_properties>`. If set to ``true`` the pipe will end the transform, avoiding potential duplicate entries.  

Due to Deleted entities
"""""""""""""""""""""""

Per default Sesam will pass entities with ``"_deleted": true`` through all transforms, therefore these entities will need to be discarded in the pipe in order to avoid unwanted insert messages.

Connect mapping data
^^^^^^^^^^^^^^^^^^^^

Once an insert if performed, we need to store both the insert ```_id`` and the original source entity's ``_id`` to the sink dataset. This, together with the :ref:`capture response with transform pattern<capture_response_with_transform>`, will allow us to connect these two entities in the corresponding global pipe, which ensures a fully connected data flow. In the case where no other metadata can act as merge critera, this mapping is the only way to connect inserted entites with other corresponding entrys from other source systems.

Insert pipe configuration example 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following example illustrates duplicate entry precautions:

.. code-block:: json

	{
	  "_id": "<system>-<datatype>-share-insert",
	  "type": "pipe",
	  "source": {
	    "type": "dataset",
	    "dataset": "<system>-<datatype>-transform"
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
	                "datasets": ["<system>-<datatype>-share-insert si"],
	                "where": [
	                  ["eq", "_S._id", "si.$original_id"]
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
	    "system": "<system>",
	    "operation": "insert",
	    "properties": {
	      "url": "<url>"
	    },
	    "side_effects": true
	  }, {
	    "type": "dtl",
	    "rules": {
	      "default": [
	        ["comment", "store the id from the insert as new _id"],
	        ["add", "_id", "_S.response.<id>"],
	        ["comment", "kepp original _id for mapping purposes"],
	        ["add", "$original_id", "_S._id"],
	        ["merge-union", "_S.response"],
	        ["add", "rdf:type",
	          ["ni", "<rdf:type>"]
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
