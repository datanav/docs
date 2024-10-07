.. _bidirectional-synchronization:

Bidirectional synchronization
==============================

Introduction
------------

From a masterdata management perspective, a masterdata management tool's primary objective is to gather data from multiple sources and determine the "best version" of the data, and preferably store or propagate the final product. In Sesam this final product is stored in our :ref:`global datasets <global_datasets>` as :ref:`golden records <best-practice-golden-record>`. 

If setup correctly there might be multiple system sources contributing to the source of our golden records. This means we have potentially multiple system's with non-optimal data quality. The golden records however contain the best version of the data from all of these systems. 

Ideally we would like to not only import data from systems in order to create the golden records, but also use the golden records to improve the data quality in the source systems. To do this we need to both import and export data to and from systems whenever possible to ensure the best data quality throughout the enterprise. The global datasets are now not only the source of the golden record, but also the source of masterdata for all bidirectional systems. This **bidirectional synchronization** has obvious benefits but also add more complexity that needs to be managed.

Benefits
--------

- Ensuring optimal data quality throughout the organization

- Keeping data synchronized in real-time

- Minimizing the requirement for manual updating several system with the same information 

Main patterns to be managed
---------------------------

- **Duplicate management**

    * Internal duplicate management (*)
        * Ensure that system A do not inject duplicates into system A
        * Ensure that pre-existing duplicates in A are merged and kept in sync    

    * External duplicate management (*)
        * Make sure that System A do not inject duplicates in system B

- **Preservation of source system data integrity**
    * Before we update entities to a system we need to make sure that we do not overwrite entity data in the system that Sesam has yet not been aware of

- **Race condition management**
    * Ensure that the golden records are complete before propagating the data downstream
    * Ensure that the output of ``-transform`` pipes is complete before propagating the data downstream

*Points marked with \(\*\ )\  are not necessarily restricted to bidirectional synchronization. The effects however, if not properly managed, are greater than in a situation without bidirectional synchronization.*  

Duplicate management
--------------------

The risk of duplicates is greater in a bidirectional synchronization scenario because the global models are now sources for all systems. This means that entities that already have versions in all systems could potentially lead to inserts in the other systems if not managed correctly. An entity existing in system A could even lead to an insert back to system A if we do not have the required mechanism in place to block it.

Internal duplicate management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The concept of internal duplicates covers two different scenarios. Firstly, a system should not be able to insert its own entities back to itself (*management of new duplicates*). Secondly, preexisting duplicates (the sales team might have created two versions of a company in their CRM system) should be treated as the same entity whenever possible (*management of preexisting duplicates*).  

|start-h5| **Management of new duplicates** |end-h5|

We can ensure that entities are not inserted into their own source by applying a combination of the :ref:`namespace split pattern <namespace_split>` and the :ref:`duplicate hops block pattern <duplicate-hops-block>`. 

The first will ensure that all entities attempting to communicate with the source system are doing it in the correct semantic context, i.e. they are using the correct namespace in their ``_id`` value. This allows you to block inserts if entities already have the target system's namespace.

The second will ensure that no entities that already have a successful insert in the sink dataset of the ``-share`` pipe will be inserted again.

|start-h5| **Management of preexisting duplicates** |end-h5|

The only way to ensure that preexisting duplicates do not propagate as duplicates downstream is to identify them and :ref:`merge <merging>` them in their global pipe. This can be done by locating an  appropriate merge criterion that the two entities have in common. 

External duplicate management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

External duplicate management covers two different scenarios:

1. Ensuring that preexisting duplicates are not propagated as duplicates into other systems
2. Ensuring that entities inserted by Sesam are kept track of and merged with their origin entity 

Point 1, e.g. a company represented in system *A* has a corresponding company represented in system *B* can be managed by by letting the entities merge in their global pipe. This also requires the identification of (preferably) uniquely identifying merge criterion that ensure these two entities are treated as the same entity. By applying the :ref:`namespace split pattern <namespace_split>` we can ensure that the correct version of the data is sent to the correct ``-share`` pipe. 

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

Whenever you do bidirectional synchronization you have to be aware of potential  `race conditions <https://en.wikipedia.org/wiki/Race_condition>`__  when managing the data. 

In Sesam we manage these race condition by ensuring the :ref:`completeness <completeness_feature>` of the data before letting it propagate downstream. 

There are generally two different completeness checks we do in order to minimize race conditions:

- Initial completeness
    * Ensures that all required datasets are populated when doing the initial synchronization
-  Transform completeness
    * By using the :ref:`completeness DTL function <completeness_dtl_function>` we can ensures that all required pipes have successfully run before processing data through ``-transform`` pipes 

|start-h5| **Example of the initial completeness** |end-h5|

::

  "source": {
    "type": "dataset",
    "dataset": "global-organisation",
    "initial_completeness": ["A-company-organisation-enrich",
      "global-classification-enhance"]
  },

|start-h5| **Example of the completeness DTL function** |end-h5|

::

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

.. |start-h5| raw:: html

     <h5>

.. |end-h5| raw:: html
    
     <h5>
