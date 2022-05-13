.. _tutorial_getting_started_connect:

Connect data
============

.. In this phase we will find sameness from our two sources and merge them into one.

In this phase we will see how the same companies from different sources can be merged for a more complete perspective of the prespective companies.
We will also get a small taste of master data management (MDM) mechanisms in Sesam.

.. admonition::  Objectives:

    After you complete this tutorial you will have learned the following:

    #. How to merge entities from different sources
    #. How to define global properties

.. admonition:: Prerequisites

  Before starting on this tutorial we suggest you complete the `Enrich data tutorial <tutorial-getting-started-enrich>`_ as we will use that data in this tutorial.

Create global pipe
******************
To create a global pipe, follow the steps below. 

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the configuration below
#. Click **Start** to ensure your pipe runs 
#. Click the **Output** tab to see the result

.. code-block:: json
  :linenos:
  
  {
    "_id": "global-company",
    "type": "pipe",
    "source": {
      "type": "merge",
      "datasets": ["enhetsregisteret-company-enrich ec", "hubspot-company-enrich hc"],
      "equality_sets": [
        ["ec.orgnr", "hc.properties.about_us"]
      ],
      "identity": "first",
      "version": 2
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["add", "name",
            ["coalesce",
              ["list", "_S.enhetsregisteret-company:navn", "_S.hubspot-company:properties.hubspot-company:name"]
            ]
          ],
          ["add", "zipcode",
            ["coalesce",
              ["list", "_S.enhetsregisteret-company:forradrpostnr", "_S.hubspot-company:properties.hubspot-company:zip"]
            ]
          ]
        ]
      }
    },
    "metadata": {
      "global": true
    }
  }

``"identity": "first"`` tells Sesam to pick the ``_id`` from the first dataset source as ``_id`` for the merged entity.

We use ``orgnr`` from Enhetsregisteret and ``about_us`` from HubSpot to find matching companies from the two systems.

Notice how the matching companies from the two sources have been merged together.

Also notice how ``$ids`` and ``rdf:type`` have data from both sources.

The properties we added in the global pipe are listed in the ``global-company`` namespace.
We use ``coalesce`` to determine the trust we have in each source, the first source begin the one we trust the most.

These global properties will be used later in the transform phase.

..
    To learn more about connecting data in Sesam, see the Learn section Connect
