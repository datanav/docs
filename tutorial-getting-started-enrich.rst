.. _tutorial_getting_started_enrich:

Enrich data
===========

In this tutorial we will look closer into the Enrich phase of a Sesam synchronization, where we add value to our data through semantically enrichment. We will not go through the full extent of semantic enrichment, only enough for you to understand the concept. To semantically enrich data you need to know what the data means, which is why this phase should always be done with someone with more intimate knowledge about the data, such as a system owner. 

.. admonition::  Objectives:

    After you complete this tutorial you will have learned the following:

    #. How to add NI's to your entity metadata
    #. How to add rdf:types to your entities

.. admonition:: Prerequisites

  Before starting on this tutorial we suggest you complete the `Collect data tutorial <tutorial-getting-started-collect>`_ as we will use that data in this tutorial.

  In order to simplify matters, we would like you to assign a contact to one of the companies you now have populated your HubSpot account with. To do this, go to your "Companies" overwiew in HubSpot. Select ``THEMOON AS``. On the right hand side you should see the option to add a contact. Press ``+ Add`` and select **Brian Halligan** (a pre-existing test contact) and finish the contact selection. **Brian Halligan** should now be visible as a contact for ``THEMOON AS``. 


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
#. Press refresh to see number of entities processed (should be 10). You can also see them in the pipe's output page. 

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
            ],
            ["add", "rdf:type",
              ["ni", "hubspot:company"]
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
        "identity": "hubspot-company",
        "property": "hubspot-company"
      }
    }


On the output entity ``hubspot-company:5584839113`` you should now see a new property called ``contact-ni`` which contains the link to contacts, as well as namespaces on every property and the new ``rdf:type`` property.

The Enhetsregisteret Data
*************************
For the Enhetsregisteret data we will only add namespaces and the ``rdf:type`` property. Follow the steps below to create the Enrich pipe for the Enhetsregisteret data.

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the DTL configuration below
#. Press **Start** to ensure your pipe runs 
#. Press refresh to see number of entities processed (should be 10). You can also see them in the pipe's output page. 

.. code-block:: json
  :linenos:
  
    {
      "_id": "enhetsregisteret-company-enrich",
      "type": "pipe",
      "source": {
        "type": "dataset",
        "dataset": "enhetsregisteret-company-collect"
      },
      "transform": {
        "type": "dtl",
        "rules": {
          "default": [
            ["copy", "*"],
            ["add", "rdf:type",
              ["ni", "enhetsregisteret:company"]
            ]
          ]
        }
      },
      "add_namespaces": true,
      "namespaces": {
        "identity": "enhetsregisteret-company",
        "property": "enhetsregisteret-company"
      }
    }


On the output entities you should now see namespaces on every property and the new ``rdf:type`` property.