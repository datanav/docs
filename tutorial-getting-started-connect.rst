.. _tutorial_getting_started_connect:

Connect data
============

In this phase we will demonstrate how to connect data across different sources.
More specifically how the same companies from different sources can be merged to give us a more complete perspective of the respective companies.

We will also get a small taste of master data management (MDM) mechanisms in Sesam by adding global properties.

.. admonition::  Objectives:

    After you complete this tutorial you will have learned the following:

    #. How to merge entities from different sources
    #. How to define global properties

.. admonition:: Prerequisites

  Before starting on this tutorial we suggest you complete the `Enrich data tutorial <tutorial-getting-started-enrich>`_ as we will use that data in this tutorial.

Create a global pipe
********************
To create a global pipe, follow the steps below. 

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the configuration below
#. Click **Start** to ensure your pipe runs 
#. Click the **Output** tab to see the result

.. code-block:: json
  :linenos:
  
  {
    "_id": "global-organization",
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
          ["add", "organization-number",
            ["coalesce",
              ["list", "_S.enhetsregisteret-company:orgnr", "_S.hubspot-company:properties.hubspot-company:about_us"]
            ]
          ],
          ["add", "name",
            ["coalesce",
              ["list", "_S.enhetsregisteret-company:navn", "_S.hubspot-company:properties.hubspot-company:name"]
            ]
          ],
          ["add", "address",
            ["coalesce",
              ["list", "_S.enhetsregisteret-company:forretningsadr", "_S.hubspot-company:properties.hubspot-company:address"]
            ]
          ],
          ["add", "zipcode",
            ["coalesce",
              ["list", "_S.enhetsregisteret-company:forradrpostnr", "_S.hubspot-company:properties.hubspot-company:zip"]
            ]
          ],
          ["add", "city",
            ["coalesce",
              ["list", "_S.enhetsregisteret-company:forradrpoststed", "_S.hubspot-company:properties.hubspot-company:city"]
            ]
          ]
        ]
      }
    },
    "metadata": {
      "global": true
    }
  }

Important to note here is that we fetch companies from *different sources* (Enhentsregisteret and HubSpot),
and merge the company entities when ``orgnr`` from Enhetsregisteret matches ``about_us`` from HubSpot.

Also notice how ``$ids`` and ``rdf:type`` have data from both sources, meaning we don't lose data.
We aggregate and preserve from all sources.

The properties we added are listed in the ``global-organization`` namespace.
Properties in a global namespace are what we call *global properties*.

We use ``coalesce`` to determine the trust we have in each source, the first source being the one we trust most.
This is one of the mechanisms Sesam provides for MDM.

By adding the global properties we no longer need to worry about which source system has the most accurate data.
From here on we can simply use the global properties instead when needed.

These global properties will be used later in the transform phase.

..
    To learn more about connecting data in Sesam, see the Learn section Connect
