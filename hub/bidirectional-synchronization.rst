.. _bidirectional-synchronization:

Bidirectional synchronization
==============================

Introduction
------------

A masterdata management tool's primary objective is to gather data from multiple sources and determine the "best version" of the data, and preferably store or propagate the final product. In Sesam this final product is stored in our :ref:`global datasets <global_datasets>` as :ref:`golden records <best-practice-golden-record>`. 

If setup correctly, there might be multiple systems contributing to the golden records. This means we have potentially multiple systems with varying data quality. The golden records however contain the best version of the data from all of these systems. 

We want to do more than just import data to create golden records; we also want to use these records to enhance data quality in our source systems. To achieve this, we need to both import and export data between systems whenever we can. This will help maintain high data quality across the whole enterprise.

Now, our global datasets serve not only as the source for golden records but also as master data for all systems that need two-way communication. While this *bidirectional synchronization* has clear advantages, it also brings additional complexity that we need to handle.

Benefits
--------

- Ensure optimal data quality throughout the organization

- Keep data synchronized in real-time

- Minimize the need to manually update several systems with the same information 

Main patterns to be managed
---------------------------

- **Duplicate management**

  * Internal duplicate management (*)
      - Ensure that system A does not inject duplicates into system A
      - Ensure that pre-existing duplicates in A are merged and kept in sync    

  * External duplicate management (*)
      - Make sure that System A does not inject duplicates into system B

  .. admonition:: Commentary (*)

    Not necessarily restricted to bidirectional synchronization. The effects however, if not properly managed, are greater than in a situation without bidirectional synchronization.* 

- **Preservation of source system data integrity**
  
  * Before updating entities in a system, we need to ensure that we don't overwrite any data that Sesam is not aware of yet

- **Race condition management**

  * Ensure that the golden records are complete before propagating the data downstream

  * Ensure that the output of ``-transform`` pipes is complete before propagating the data downstream
 

Duplicate management
--------------------

The risk of duplicates is greater in a bidirectional synchronization scenario because the global models are now sources for all systems. This means that entities that already have versions in all systems could potentially lead to unwanted inserts if not managed correctly. An entity existing in system A could even lead to an insert back to system A if we do not have the required mechanism in place to block it.

Internal duplicate management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The concept of internal duplicates covers two different scenarios. First, a system should not be able to insert its own entities back to itself (*management of new duplicates*). Second, preexisting duplicates, e.g. the sales team creating two versions of a company in their CRM system, should be treated as the same entity whenever possible (*management of preexisting duplicates*).  

Management of new duplicates
****************************

We can ensure that entities are not inserted into their own source by applying a combination of the :ref:`namespace split pattern <namespace_split>` and the :ref:`duplicate hops block pattern <duplicate-hops-block>`. 

The first will ensure that all entities attempting to communicate with the source system are doing it in the correct semantic context, i.e. they are using the correct namespace in their ``_id`` value. This allows you to block inserts if entities already have the target system's namespace.

The second will ensure that no entities that already have a successful insert in the sink dataset of the ``-share`` pipe will be inserted again.

Management of preexisting duplicates
************************************

The only way to ensure that preexisting duplicates do not propagate as duplicates downstream is to identify them and :ref:`merge <merging>` them in their global pipe. This can be done by locating an appropriate merge criterion that the two entities have in common. 

External duplicate management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

External duplicate management covers two different scenarios:

1. Ensuring that preexisting duplicates are not propagated as duplicates into other systems
2. Ensuring that entities inserted by Sesam are kept track of and merged with their origin entity 

Point 1, e.g. a company represented in system *A* has a corresponding company represented in system *B*, can be managed by letting the entities merge in their global pipe. This also requires the identification of a (preferably) unique merge criterion that ensures that these two entities are treated as the same entity. By applying the :ref:`namespace split pattern <namespace_split>` we can ensure that the correct version of the data is sent to the correct ``-share`` pipe. 

Points 2 is solved by a combination of :ref:`capture response with transform pattern <capture_response_with_transform>` and the :ref:`establish origin pattern <establish_origin_pattern>` as seen in the :ref:`insert pattern <insert_pattern>` section.

Preservation of source system data integrity
--------------------------------------------

When updating entities in a system we might encounter situations where we potentially overwrite new data in the source system with "old" data. This could occur if we

1. Import data from system *A*
2. System *A* is updated by an other process than Sesam
3. Sesam updates system *A* without knowing about the changes done in step 2

These situations can be managed by performing :ref:`optimistic locking <optimistic_locking>` in the ``-share`` pipe. This will ensure that the space in time where an entity *could* be updated without Sesam's knowledge is minimized. 

Race condition management
-------------------------

Whenever you do bidirectional synchronization you should be aware of potential `race conditions <https://en.wikipedia.org/wiki/Race_condition>`__  when managing the data. 

In Sesam we manage these race condition by ensuring the :ref:`completeness <completeness_feature>` of the data before letting it propagate downstream. 

There are generally two different completeness checks we do to minimize race conditions:

- Initial completeness
    * Ensures that all required datasets are populated when doing the initial synchronization
-  Transform completeness
    * By using the :ref:`completeness DTL function <completeness_dtl_function>` we can ensure that all required pipes have successfully run before processing data through ``-transform`` pipes 

Example of the initial completeness:

.. code-block:: json

  "source": {
    "type": "dataset",
    "dataset": "global-organisation",
    "initial_completeness": ["A-company-organisation-enrich",
      "global-classification-enhance"]
  }


Example of the completeness DTL function:

.. code-block:: json

  "source": {
    "type": "dataset",
    "completeness": {
      "expression": ["if",
        ["and",
          ["gt",
            ["integer",
              ["completeness", "global-location", "A-company-collect"]
            ], 0],
          ["gt",
            ["integer",
              ["completeness", "A-company-transform-split", "A-company-collect"]
            ], 0],
          ["gte",
            ["completeness", "global-location", "A-company-collect"],
            ["completeness", "A-company-transform-split", "A-company-collect"]
          ]
        ],
        ["now"],
        ["if-null",
          ["min",
            ["list",
              ["completeness", "global-location", "A-company-collect"],
              ["completeness", "A-company-transform-split", "A-company-collect"]
            ]
          ],
          ["coalesce",
            ["list",
              ["completeness", "global-location", "A-company-collect"],
              ["completeness", "A-company-transform-split", "A-company-collect"],
              ["datetime", 0]
            ]
          ]
        ]
      ]
    },
    "dataset": "A-company-transform-split"
  }

