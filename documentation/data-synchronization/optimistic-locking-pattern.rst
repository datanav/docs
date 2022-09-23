.. _optimistic_locking:

Optimistic locking pattern
--------------------------

Optimistic locking in Sesam minimizes the risk of data loss in external systems in situations where Sesam both reads and writes data to that system. 

We perform optimistic locking by comparing each entity we wish to update in the target system to the last imported version of that entity in Sesam. If the entities are identical, no updates have been performed on that entity in the target system since Sesam's last import, and we can "safely" perform our update. If the entities are not identical we risk overwriting the new data in the external system and should therefore discard that entity update and wait for a new Sesam import to take place and try again. 

We retain the current entity in the target system by doing a lookup action through an external transformation. The comparison itself is done by comparing the hashed versions of the two entites. 

Optimistic locking configuration example
""""""""""""""""""""""""""""""""""""""""

.. code-block:: json

	{
	  "_id": "<system>-<datatype>-share-update",
	  "type": "pipe",
	  "source": {
	    "type": "dataset",
	    "dataset": "<system>-<datatype>-transform"
	  },
	  "sink": {
	    "type": "rest",
	    "system": "<system>",
	    "operation": "update"
	  },
	  "transform": [{
	    "type": "dtl",
	    "rules": {
	      "default": [
	        ["copy", "*"]
	      ]
	    }
	  }, {
	    "type": "rest",
	    "system": "<system>",
	    "operation": "lookup"
	  }, {
	    "type": "dtl",
	    "rules": {
	      "default": [
	        ["comment", "**** OPTIMISTIC LOCKING ****"],
	        ["comment", "Collecting last imported version of entity"],
	        ["add", "_old",
	          ["first",
	            ["hops", {
	              "datasets": ["<company>-<datatype>-collect a"],
	              "where": [
	                ["eq", "_S.id", "a.id"]
	              ]
	            }]
	          ]
	        ],
	        ["add", "_json_old",
	          ["json-transit",
	            ["apply", "remove-under", "_T._old"]
	          ]
	        ],
	        ["add", "_json_new",
	          ["first",
	            ["json-transit",
	              ["apply", "remove-under", "_S.response"]
	            ]
	          ]
	        ],
	        ["comment", "Creating hash of last imported version"],
	        ["add", "_hash_old",
	          ["hash128", "murmur3", "_T._json_old"]
	        ],
	        ["comment", "Creating hash of lookup entity"],
	        ["add", "_hash_new",
	          ["hash128", "murmur3", "_T._json_new"]
	        ],
	        ["comment", "Comparing hashed entities"],
	        ["if",
	          ["eq", "_T._hash_old", "_T._hash_new"],
	          [
	            ["comment", "**** SAME DATA IN SYSTEM AS IN SESAM ****"],
	            ["comment", "Save the the required to target"]
	            ["add", "<payload>", "_S.<payload>"]
	          ],
	          [
	            ["comment", "**** DIFFERENT DATA IN SYSTEM THAN IN SESAM ****"],
	            ["discard"]
	          ]
	        ]
	      ],
	      "remove-under": [
	        ["copy", "*", "_*"]
	      ]
	    }
	  }]
	}
