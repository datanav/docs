############
Key benefits
############

The unique combination of Sesam's key features leads to simplified management 
of master data in data driven environments. The service includes most of
the core features needed to build a data-fabric based platform.

|

Delta stream processing
=======================

Delta processing means that only data that has changed is ever processed
by Sesam. 


**How it works:**

The delta stream processing pipes collect raw data, connect data objects across sources, and store data into a combined semantic data storage. 

The same delta stream processing pipes transform and share the data with any target system, using each systems’ native schema. Thus, all data processing in Sesam is unified in a low-code, high-throughput,
low-latency service.

**Benefits of delta stream processing:**

- Reduced processing cost.
- Reduced processing time by at least 95% compared to bulk ETL jobs.
- Completely removes unnecessary data updates.

|

Graph-based dependency tracking
===============================

Graph-based dependency tracking ensures that every composite object is
always updated as a delta stream throughout the Sesam service, no matter
the number of complex transformations, including merging from any number
of source objects. 


**How it works:**

Dependency tracking is made possible by the fact that there is no code in Sesam, only metadata configuration describing
the transformations in pipes.


**Benefits of graph-based dependency tracking:**

- Heavily reduced operating costs by processing complex objects from multiple sources as delta streams. 
- Reduces processing time by ensuring that complete reprocessing is never required, no matter the number of sources, the complexity of the transformations, or the number of target systems and data schemas involved.
- Sesam uses metadata configuration, so that all data flows uniformly, without the need for custom code.
- Improves data governance through complete transparency.

|

Semantic data storage with dynamic multi-schema
===============================================

In Sesam the output of any delta stream processing pipe is stored in
semantic datasets. 

A semantic dataset is an immutable object store,
capable of containing the complete version of any object. Every dataset
has a completely dynamic schema, continuously updated to fit the data
stored in it. 

Semantic technology ensures that each property´s origin is
preserved and allows a single object to contain multiple schemas,
assembled into one global object. Adding golden properties, and
continuously evolving them, can be done whenever needed, as these
properties are added to the existing global object without affecting the
original properties.

**How it works:**

Sesam supports continuously evolving global properties in the multi-schema data store, so that canonical models can emerge over time, and any standardized data model can be implemented independently and be stored in a single object.

When all source properties and global properties are available as a single composite object, the cost and time of acquiring data and transforming the data into a target system in its native schema is heavily reduced.


**Benefits of semantic data storage with dynamic multi-schema:**

Improved data quality and governance:

#. Data never loses its origin and context.
#. Data never gets corrupted or lost in translation.
#. Every representation of an object, regardless of source, is stored as a single entity, without conflict or consistency corruption.
	

Improved operational efficiency:

#. Reduces cost and processing time as a source system only needs to share its data once, and in its native schema. 
#. Reduces the number of integrations by up to 90%
#. Simplifies each integration by never having to modify any source systems or do any data modeling before adding source data.
#. Supports continuously evolving global properties in the multi-schema datastore, so that canonical models can emerge over time, and any standardized data model can be implemented independently and be stored in a single object

Increased flexibility and cost savings related to changes and sunsetting of LOB systems:

#. Easily implement your new business systems without setting up integrations to other systems in your environement. Sesam Master Data Hub handles the integration of data.
#. Run multiple business systems supporting the same processes in parallel with full data consistency across every system.
#. Reduce cost by retiring legacy systems who’s primary purpose is to feed your processes with historical data. Sesam Master Data Hub will store your legacy systems data and make them available for new systems and analytics.