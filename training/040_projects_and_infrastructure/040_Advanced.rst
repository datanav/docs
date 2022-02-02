
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

  - is a method used to ensure that a change to an entity is not written to a target system whilst the same entity has been updated in its source
  - is solved in Sesam by using multiple transforms
  - compares properties such as dates, timestamps or hash values to verify whether a source entity has changed compared to the entity that is about to be exposed out of Sesam

Optimistic locking is a method used to ensure that a change to an entity is not written to a target system whilst the same entity has been updated in its source. This challenge is solved in Sesam by using multiple transforms. In the following example, a chained transform is used to solve for optimistic locking, where you query your source for the entity you are working on. As such you verify that no change has happened in the source compared to the entity you are about to expose out of Sesam.

In terms of undertaking this comparison, properties such as dates, timestamps or hash values can be used to check whether a source entity has changed compared to the entity that is about to be exposed out of Sesam. To exemplify, you will now see this done whilst updating an entity and comparing for optimistic locking based on timestamp values. The dataflow you will be looking at now goes from ``global-person`` > ``person-hubspot`` > ``person-hubspot-opt-locking`` > ``person-hubspot-update-endpoint``. 

Output entity example from pipe ``global-person``:

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
    "hubspot-person:timestamp": 1998865,
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

Config in preparation pipe ``person-hubspot``:

.. code-block:: json

  {
    "_id": "person-hubspot",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-person",
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
          ["comment", "*** Adding Hubspot properties ***"]
          ["add", "properties",
            ["apply", "properties", "_S."]
          ]
        ],
        "properties": [
          ["add", "::NAME", "_S.global-person:name"],
          ["add", "::EMAIL_ADDRESS", "_S.global-person:email"],
          ["add", "::ID", "_S.global-person:id"],
          ["add", "::LEADS", "_S.global-person:leads"],
          ["add", "::timestamp_for_opt_locking": "_S.hubspot-company:timestamp"]
        ]
      }
    }
  }

Output entity from pipe ``person-hubspot``:

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
    "timestamp_for_opt_locking": 1998865
  }

Config in preparation pipe ``person-hubspot-opt-locking``:

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
        "url": "/get/record?properties=timestamp"
      }, {
        "type": "dtl",
        "rules": {
          "default": [
            ["copy", "*"],
            ["comment", "*** Checking for change in timestamp value ***"]
            ["discard",
              ["eq", ["integer", "_T.timestamp_for_opt_locking"], "_T.timestamp"]
            ],
            ["remove",
              ["list", "timestamp", "timestamp_for_opt_locking"]
            ]
          ]
        }
      }]
    }
  }

So, walking you through what happens in the above pipe configuration, you should note the property ``"type": "chained"``. a ``chained`` transform allows you to chain multiple transforms. This is essential when solving for optimistic locking in Sesam. In the first transform of the above three you see a filter on ``_deleted`` entities. This is just to ensure that no ``_deleted`` entities are passed on from this point. In the second transform you see that we are querying the system ``hubspot`` for what, conveniently enough, looks like a timestamp value for a record. Following this, the last transform takes effect. In this transform you can see that a ``copy`` function has been defined and that a ``discard`` function follows. This ``discard`` ensures optimistic locking. The comparison of the timestamp values in the ``discard`` function, makes sure entities are discarded if both timestamp values are not equal. After this comparison, you can see the ``remove`` function, which ensures exposure of properties that align with the schema requirements in Hubspot. 

To finish off this section, lets expose data out of Sesam in ``person-hubspot-update-endpoint``.

Config in outbound pipe ``person-hubspot-update-endpoint``:

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
