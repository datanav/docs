
.. _projects-infrastructure-advanced-4-3:

Advanced
--------

.. _dev-ci-test-prod-nodes-4-3:

Multiple Sesam node environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

dev = personlig node der utvikling foregår

test = node som kjører samme config som prod med testdata for å finne
bugs

CI = do tests for pull requests /deployments before deploying.

prod = live node som kjører live integrasjoner

Tagging av brancher for deployment

.. seealso::

  TODO

.. _optimistic-locking-4-3:

Optimistic Locking
~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Optimistic locking...

  - is a method used to minimize the risk of a change to an entity being written to a target system whilst said entity has **already** been updated in its source
  - is solved in Sesam by using multiple transforms
  - compares hash values in Sesam to verify that a source entity has not changed since it was read from its source, when syncronizing data in systems

`Optimistic locking <https://en.wikipedia.org/wiki/Optimistic_concurrency_control>`_ is a method used to minimize the risk of a change to an entity being written to a target system whilst said entity has **already** been updated in its source. This challenge is solved in Sesam by using multiple transforms. In the following example, a chained transform is used to solve for optimistic locking, where you query your source for the entity you are working on. As such, you verify that no change has happened in the source compared to the entity you are about to expose out of Sesam.

In terms of undertaking this comparison, Sesam compares hash values to verify that a source entity has not changed since it was read from its source, when syncronizing data in systems. What is essential here, is that the property used for comparison **always** changes when your source entity changes. Therefore, Sesam **always** use hash values to implement optimistic locking in a Sesam dataflow . The dataflow you will be looking at now goes from ``hubspot-person-raw`` > ``hubspot-person`` > ``global-person`` > ``person-hubspot`` > ``person-hubspot-opt-locking`` > ``person-hubspot-update-endpoint``. For brevity, you will not be presented with the configuration or output from either the ``hubspot-person-raw`` or ``hubspot-person`` pipes. 

Output entity example from the pipe ``global-person``:

.. code-block:: json

  {
    "_id": "sesam-person:10",
    "sesam-person:email": "trdskjold_dk_007@gmail.com",
    "sesam-person:employee_id": 10,
    "sesam-person:first_name": "Tordenskjold",
    "sesam-person:last_name": "Danmarkson",
    "sesam-person:position": "Sesam Architect",
    "sesam-person:engagement": "full time",
    "hubspot-person:email": "trdskjold007@hotmail.com",
    "hubspot-person:id": 10,
    "hubspot-person:process": [
      {
        "type": "lead",
        "company_name": "University of Aalborg",
        "contact": "Clever Cleverson",
        "position": "CTO"
      },
      {
        "type": "completed",
        "company_name": "University of Aarhus",
        "contact": "Dr. Clever Cleverson",
        "position": "CTO"
      },
      {
        "type": "lead",
        "company_name": "University of Copenhagen",
        "contact": "Extreme Dr. Clever Cleverson",
        "position": "CTO"
      }
    ],
    "global-person:email": "trdskjold_dk_007@gmail.com",
    "global-person:id": 10,
    "global-person:name": "Tordenskjold Danmarkson",
    "global-person:leads": [
      {
        "type": "lead",
        "company_name": "University of Aalborg",
        "contact": "Clever Cleverson",
        "position": "CTO"
      },
      {
        "type": "lead",
        "company_name": "University of Copenhagen",
        "contact": "Extreme Dr. Clever Cleverson",
        "position": "CTO"
      }
    ],
    "rdf:type": [
      "~:sesam:Person",
      "~:hubspot:Person"
    ]   
  }

Config in the preparation pipe ``person-hubspot``:

.. code-block:: json

  {
    "_id": "person-hubspot",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["comment", "*** Filter data ***"],
          ["filter",
            ["and",
              ["is-not-empty",
                ["intersection",
                  ["list", "~:hubspot:Person", "~:sesam:Person"], "_S.rdf:type"]
              ]
            ]
          ],      
          ["comment", "*** Adding Hubspot properties ***"],
          ["add", "properties",
            ["apply", "properties", "_S."]
          ],
          ["comment", "*** Apply-hops to raw pipe to get hash value for comparison ***"],
          ["add", "::hash_for_opt_locking",
            ["hash128", "murmur3",
              ["json-transit",
                ["first",
                  ["apply-hops", "raw-entity-for-hash", {
                    "datasets": ["hubspot-person-raw hpr"],
                    "where": [
                      ["eq", "_S.hubspot-person:id", "hpr.id"]
                    ]
                  }]
                ]
              ]
            ]
          ]
        ],
        "properties": [
          ["add", "::NAME", "_S.global-person:name"],
          ["add", "::EMAIL_ADDRESS", "_S.global-person:email"],
          ["add", "::ID", "_S.global-person:id"],
          ["add", "::LEADS", "_S.global-person:leads"]
        ],
        "raw-entity-for-hash": [
          ["copy", "*", "_*"]
        ]
      }
    }
  }

With respect to the above pipe configuration, you should focus on the ``hash_for_opt_locking`` property and the transform rules that ensure the creation of said hash value. The ``hash128`` transform function, in addition to the ``json-transit`` function ensure that the returned object from the ``apply-hops`` rule ``raw-entity-for-hash`` evaluates as a valid hash value. The ``json-transit`` `function <https://docs.sesam.io/DTLReferenceGuide.html#json>`_ serializes its provided arguments whilst the ``hash128`` `function <https://docs.sesam.io/DTLReferenceGuide.html#hashing>`_ creates a valid "murmur3" hash value. Finally, the ``raw-entity-for-hash`` rule, ensures that only source properties are copied from the ``hubspot-person-raw`` dataset, and not its :ref:`reserved fields <reserved-fields>`.

To finish off this step in the datafow, look at the below output entity from the pipe ``person-hubspot``:

.. code-block:: json

  {
    "_id": "sesam-person:10",
    "NAME": "Tordenskjold Danmarkson",
    "EMAIL_ADDRESS": "trdskjold_dk_007@gmail.com",
    "ID": 10,
    "LEADS": [
      {
        "type": "lead",
        "company_name": "University of Aalborg",
        "contact": "Clever Cleverson",
        "position": "CTO"
      },
      {
        "type": "lead",
        "company_name": "University of Copenhagen",
        "contact": "Extreme Dr. Clever Cleverson",
        "position": "CTO"
      }
    ],
    "hash_for_opt_locking": 8.617848865595105e+37
  }

Config in the preparation pipe ``person-hubspot-opt-locking``:

.. code-block:: json

  {
    "_id": "person-hubspot-opt-locking",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "person-hubspot"
    },
    "transform": {
      "type": "chained",
      "transforms": [{
        "type": "dtl",
        "rules": {
          "default": [
            ["filter",
              ["eq", "_S._deleted", false]
            ],
            ["copy", "*"]
          ]
        }
      }, {
        "type": "http",
        "system": "hubspot",
        "batch_size": 1,
        "url": "/get/record?properties=*&id={{ID}}"
      }, {
        "type": "dtl",
        "rules": {
          "default": [
            ["copy", "*"],
            ["add", "hash_from_http_source",
              ["hash128", "murmur3",
                ["json-transit", "_T."]
              ]
            ],
            ["discard",
              ["eq", "_T.hash_from_http_source",
                ["integer", "_S.hash_for_opt_locking"]
              ]
            ],
            ["remove",
              ["list", "hash_from_http_source", "hash_for_opt_locking"]
            ]
          ]
        }
      }]
    }
  }

So, walking you through what happens in the above pipe configuration, you should note the property ``"type": "chained"``. A ``chained`` transform allows you to chain multiple transforms. This is essential when solving for optimistic locking in Sesam. In the first transform of the above three you see a filter on ``_deleted`` entities. This is just to ensure that no ``_deleted`` entities are passed on from this point. In the second transform you see that we are querying the system ``hubspot`` for an identical entity to the one currently being transformed. Following this, the last transform takes effect. In this transform you can see that a ``copy`` function has been defined and that a ``discard`` function follows. This ``discard`` ensures optimistic locking. The comparison of the hash values in the ``discard`` function, makes sure entities are discarded if both hash values are not equal. After this comparison, you can see the ``remove`` function, which ensures exposure of properties that align with the schema requirements in Hubspot. 

To finish off this section, lets expose data out of Sesam in the pipe ``person-hubspot-update-endpoint``:

.. code-block:: json

  {
    "_id": "person-hubspot-update-endpoint",
    "type": "pipe",
    "source": {
      "supports_signalling": true,
      "type": "dataset",
      "dataset": "person-hubspot-opt-locking"
    },
    "sink": {
      "type": "rest",
      "system": "hubspot-rest",
      "operation": "update"
    },
    "transform": [{
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"]
        ]
      }
    }]
  }

Output:

.. code-block:: json

  [
    {
      "_id": "sesam-person:10",
      "NAME": "Tordenskjold Danmarkson",
      "EMAIL_ADDRESS": "trdskjold_dk_007@gmail.com",
      "ID": 10,
      "LEADS": [
        {
          "type": "lead",
          "company_name": "University of Aalborg",
          "contact": "Clever Cleverson",
          "position": "CTO"
        },
        {
          "type": "lead",
          "company_name": "University of Copenhagen",
          "contact": "Extreme Dr. Clever Cleverson",
          "position": "CTO"
        }
      ]
    }
  ]

Note in the pipe config of ``person-hubspot-update-endpoint`` the property ``supports_signalling`` within the ``source`` dictionary. ``supports_signalling`` tells Sesam that this pipe must run as soon as an entity changes in its source dataset. In this example that is the dataset from ``person-hubspot-opt-locking``. In practice, this makes sure that the time window from checking for optimistic locking to exposure of data out of Sesam is at a minimum.

.. seealso::

  :ref:`developer-guide` > :ref:`configuration` > :ref:`source_section` > :ref:`dataset_source`

.. _workflow-in-projects-4-3:

Workflow in Projects
~~~~~~~~~~~~~~~~~~~~

Get task

[Document task]

Pull repo

Create branch

Do changes

Test changes

[Create more test cases]

Update expected data

Push changes

Document solution

Deploy to test

Test changes in test – go back to create branch if necessary.

Deploy to prod

.. seealso::

  TODO

.. _tasks-for-projects-and-infrastructure-intermediate-4-3:

Tasks for Projects & Infrastructure: Intermediate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
