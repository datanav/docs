.. _tutorial_getting_started_share:

Share data
==========

In this phase we will demonstrate how to share your data to a target system.
More specifically, we will apply the necessary logic to send the data from the :doc:`transform tutorial <tutorial-getting-started-trabsform>` back to HubSpot. 

This tutorial contains the configuration to two pipes: the first pipe performs *optimistic locking* and the second sends the dat to HubSpot.

.. admonition::  Objectives:

    After you complete this tutorial you will have learned the following:

    #. How to perform optimistic locking in Sesam
    #. How to send data from Sesam to a target system

.. admonition:: Prerequisites

  Before starting on this tutorial we suggest you complete the :doc:`Transform data tutorial <tutorial-getting-started-transform>` as we will use that data in this tutorial.

Perform optimistic locking in Sesam
***********************************

To create the first pipe in this tutorial, follow the steps below.

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the configuration below
#. Click **Start** to ensure your pipe runs 
#. Click the **Output** tab to see the result

.. code-block:: json
  :linenos:
  
  {
  "_id": "company-hubspot-share-update",
  "type": "pipe",
  "source": {
    "type": "dataset",
    "dataset": "company-hubspot-transform",
    "subset": ["eq",
      ["is-not-null", "_S.id"], true]
  },
  "transform": [{
    "type": "dtl",
    "rules": {
      "default": [
        ["discard",
          ["eq", "_S._deleted", false]
        ],
        ["copy", "*", "id"],
        ["add", "::id", "_S.id"]
      ]
    }
  }, {
    "type": "rest",
    "system": "hubspot",
    "operation": "get_company",
    "replace_entity": false
  }, {
    "type": "dtl",
    "rules": {
      "default": [
        ["comment", "**** OPTIMISTIC LOCKING ****"],
        ["add", "_old",
          ["first",
            ["hops", {
              "datasets": ["hubspot-company-collect a"],
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
        ["add", "_hash_old",
          ["hash128", "murmur3", "_T._json_old"]
        ],
        ["add", "_hash_new",
          ["hash128", "murmur3", "_T._json_new"]
        ],
        ["if",
          ["eq", "_T._hash_old", "_T._hash_new"],
          [
            ["comment", "**** SAME DATA IN SYSTEM AS IN SESAM ****"],
            ["add", "::payload", "_S.payload"],
            ["add", "::properties",
              ["dict", "id", "_S.id"]
            ]
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
