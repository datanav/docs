.. _tutorial_getting_started_transform:

Transform data
==============

In this tutorial we will look closer into the transformation phase of a Sesam synchronization. 

The transformation phase is where we prepare the data to be sent out to a target. We will now use the data you worked with in the previous tutorial to improve the data quality in the HubSpot company data as well as build a payload structure.

.. admonition::  Objectives:
   
    After you complete this tutorial you will have learned the following:

    #. How to use :ref:`Data Transformation Language <DTLReferenceGuide>` to create system specific payloads 
    #. How to use global properties to increase payload data quality


.. admonition:: Prerequisites

    Before starting on this tutorial we suggest you complete the :doc:`Connect tutorial <tutorial-getting-started-connect>` as we will use that data in this tutorial.


Populate a payload with high quality data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to create the transform pipe, please follow the steps below.

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the configuration below
#. Click **Start** to ensure your pipe runs
#. Click the **Output** tab to see the result

.. code-block:: json

    {
      "_id": "company-hubspot-transform",
      "type": "pipe",
      "source": {
        "type": "dataset",
        "dataset": "global-organization"
      },
      "transform": {
        "type": "dtl",
        "rules": {
          "default": [
            ["add", "id", "_S.hubspot-company:id"],
            ["add", "payload",
              ["dict", "properties",
                ["apply", "create-properties", "_S."]
              ]
            ]
          ],
          "create-properties": [
            ["add", "address", "_S.global-organization:address"],
            ["add", "city", "_S.global-organization:city"],
            ["add", "name", "_S.global-organization:name"],
            ["add", "about_us", "_S.global-organization:organization-number"],
            ["add", "zip", "_S.global-organization:zipcode"]
          ]
        }
      }
    }

Notice that in this case we only use the properties we created in the connect phase. We could however have used any properties available to us in Sesam, as long as they are accepted by the HubSpot API.

HubSpot has specific requirements for the incoming data structure to their API, which is why we have added the ``payload`` and ``properties`` structures to the data.