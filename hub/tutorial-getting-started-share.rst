.. _tutorial_getting_started_share:

Share data
==========

In this phase we will demonstrate how to share your data to a target system.
More specifically, we will apply the necessary logic to send the data from the :doc:`transform phase <tutorial-getting-started-transform>` back to HubSpot. 

.. admonition::  Objectives:

    After you complete this tutorial you will have learned the following:

    #. How to perform optimistic locking in Sesam
    #. How to send data from Sesam to a target system

.. admonition:: Prerequisites

  Before starting on this tutorial we suggest you complete the :doc:`Transform data tutorial <tutorial-getting-started-transform>` as we will use that data in this tutorial.

In this last phase, we will create two pipes:

#. The first pipe performs *optimistic locking* 
#. The second pipe sends the data to HubSpot


Perform optimistic locking in Sesam
***********************************

The main purpose of this pipe is to perform *optimistic locking*, i.e. to make sure that there have not been any updates to an entity in HubSpot since our last import of HubSpot data to Sesam. 

This is a great feature that will ensure that we do not overwrite any HubSpot data we are not supposed to.

Follow the steps bellow to create the pipe with optimistic locking:

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the configuration below
#. Click **Start** to ensure your pipe runs 
#. Click the **Output** tab to see the results

.. code-block:: json
  
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



Send data to HubSpot
*********************

In this pipe we will connect to the HubSpot system in Sesam in order to send our updated and enriched data back to HubSpot.

But before we start, please navigate to your HubSpot company contacts and click on the company **SOFTARCH TECHNOLOGIES AS**. 

On the left hand top corner, click on **Actions** and select **View all properties**.

If you scroll down you will notice that this company has no street address associated with it. This is one of the fields we will update with our last pipe.    

Now, let´s get to it! Follow the steps below to create the last pipe:

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the configuration below
#. Click **Start** to ensure your pipe runs 

.. code-block:: json
  
    {
      "_id": "company-hubspot-share-update-endpoint",
      "type": "pipe",
      "source": {
        "type": "dataset",
        "dataset": "company-hubspot-share-update"
      },
      "sink": {
        "type": "rest",
        "system": "hubspot",
        "operation": "update",
        "properties": {
          "url": "companies"
        }
      }
    }


Note that this pipe uses the operation ``update``. In *getting started* we do not cover inserting new entities into HubSpot, only updating already existing ones. 

Now, go back to **SOFTARCH TECHNOLOGIES AS** in your HubSpot account and look at the street address again. It should now be updated with the address from Enhetsregisteret: *H0507 c/o Reidar Andersen Dronningens gate 50B*.

Congratulations! You have now created your first Sesam synchronization!

.. admonition:: Want to learn more?

  Sign up on any of our Sesam courses or workshops, or have a look at the more in-depth tutorials with detailed descriptions of all five phases of a Sesam data-flow.
