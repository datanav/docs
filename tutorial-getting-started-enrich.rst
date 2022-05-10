.. _tutorial_getting_started_enrich:

Enrich data
===========

In this phase we will add value to the data we have `previously collected <tutorial-getting-started-collect>`_ by semantically enriching it.

.. admonition::  Objectives:

    After you complete this tutorial you will have learned the following:

    #. How to add NI's to your entity metadata
    #. How to add rdf:types to your entities

.. admonition:: Prerequisites

  Before starting on this tutorial we suggest you complete the `Collect data tutorial <tutorial-getting-started-collect>`_ as we will use that data in this tutorial.

|
|

Assign an association on HubSpot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In HubSpot you can assign a contact to a specific company. 

We would like you now to assign **Brian Halligan** (a pre-existing test contact) to one of the companies you now have populated your HubSpot account with. 

#. Log in to your HubSpot account
#. Navigate to "Companies"
#. Select ``THEMOON AS``
#. Press ``+ Add`` on Contacts (on the right hand side)
#. Select **Brian Halligan** and finish the contact selection. **Brian Halligan** should now be visible as a contact for ``THEMOON AS``


Add semantic value
^^^^^^^^^^^^^^^^^^
We will now add semantic value to our data.

The Hubspot Data
****************
In order to add the link between company and contacts, as well as adding the rdf:type tag and namespaces to the entities, please follow the steps below:

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