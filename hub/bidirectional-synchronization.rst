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

|start-h4| **Management of new duplicates** |end-h4|

foobar




.. |start-h4| raw:: html

     <h4>

.. |end-h4| raw:: html
    
     <h4>
