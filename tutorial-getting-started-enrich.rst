.. _tutorial_getting_started_enrich:

Enrich data
===========

In this phase we will add value to the data we have `previously collected <tutorial-getting-started-collect>`_ by semantically enriching it.

.. admonition::  Objectives:

    After you complete this tutorial you will have learned the following:

    #. How to add NI's to your entity metadata
    #. How to add rdf:types to your entities
    #. How to add namespaces to your entities

.. admonition:: Prerequisites

  Before starting on this tutorial we suggest you complete the `Collect data tutorial <tutorial-getting-started-collect>`_ as we will use that data in this tutorial.

|
|


Add semantic value
^^^^^^^^^^^^^^^^^^
In this step we will add semantic value to our data.

The Hubspot Data
****************
In order to semantically enrich your HubSpot company data, follow the steps below. 

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the DTL configuration below
#. Press **Start** to ensure your pipe runs 
#. Press refresh to see number of entities processed (should be 10). You can also see them in the pipe's output page. 

.. code-block:: json
  
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


The company in the pipe´s output with ``about_us`` value "991721355" should now have the new ``contact-ni`` property, like shown bellow.

.. code-block:: json
  :emphasize-lines: 2
  
    {
    "hubspot-company:contact-ni": "~:hubspot-contact:<some ID>"
    }


The Enhetsregisteret Data
*************************
For the Enhetsregisteret data we will only add namespaces and the ``rdf:type`` property. 

Follow the steps below to create the Enrich pipe for the Enhetsregisteret data.

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the DTL configuration below
#. Press **Start** to ensure your pipe runs 
#. Press refresh to see number of entities processed (should be 10). You can also see them in the pipe's output page. 

.. code-block:: json
  
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

..
    To learn more about semantic enrichment in Sesam, see the Learn section Enrich