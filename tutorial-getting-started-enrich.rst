.. _tutorial_getting_started_enrich:

Enrich data
===========

In this tutorial we will look closer into how to semantically enrich your data. We add semantic value to our data in Sesam by identifying reference objects in the data and link them to their associated target, such as the link between a Primary Key (PK) and a Foreign Key (FK). In Sesam we use namespaced identifiers (NI's) and rdf:types to create these links. In this tutorial we will only add some enrichment in order for you to understand the concept. To semantically enrich data you need to know what the data means, which is why semantic enrichment should always be done with someone with more intimate knowledge about the data, such as a system owner. 

.. admonition::  Objectives:

    After you complete this tutorial you will have learned the following:

    #. How add NI's to your entity metadata
    #. How add rdf:types to your entities

.. admonition:: Prerequisites

  Before starting on this tutorial we suggest you:
    - Complete the `Collect data tutorial <tutorial-getting-started-collect>`_ as we will now use that data.

  In order to simplify matters, we would like you to assign a contact to one of the companies you now have populated your HubSpot account with. To do this, go to your "Companies" overwiew in HubSpot. Select ``THEMOON AS``. On the right hand side you should see the option to add a contact. Press ``+ Add`` and select "Brian Halligan" (a pre-existing test contact) and finish the contact selection. Brian Halligan should now be vivible as a contact for ``THEMOON AS``. 


|
|


Add semantic value
^^^^^^^^^^^^^^^^^^
When adding semantic value to our data we create a more scalable solution. We also create a more efficient solution as the enrich data both allows us to visualize the relationships in the source data as well as increases functionality throughout the whole data flow. 

The Hubspot Data
****************
In order to add the link between associated contacts for a company and contacts, as well as adding the rdf:type tag to the entities, please follow the steps below:

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the DTL configuration below
#. Press **Start** to ensure your pipe runs 

.. code-block:: json
  :linenos:
  
    {
      "_id": "hubspot-company-enrich",
      "type": "pipe",
      "source": {
        "type": "dataset",
        "dataset": "hubspot-company-collect"
      },
      "transform": {
        "type": "dtl",
        "rules": {
          "default": [
            ["copy", "*"],
            ["merge",
              ["apply", "contacts-ni", "_S.associations.contacts.results"]
            ]
          ],
          "contacts-ni": [
            ["filter",
              ["eq", "_S.type", "company_to_contact"]
            ],
            ["add", "contact-ni",
              ["ni", "hubspot-contact", "_S.id"]
            ]
          ]
        }
      },
      "add_namespaces": true,
      "namespaces": {
        "identity": "hubspot-contact",
        "property": "hubspot-contact"
      }
    }









    - 
    - 
    - 
    
  You should also acquire:
    - 
    - 
    - 
    - 

