Key features and benefits
=========================

The combination of Sesame's key features simplifies data management for
master data in data driven environments. The service includes most of
the core features needed to build a data-fabric based platform.

Delta stream processing
-----------------------

Delta processing means that only data that has changed is ever processed
by Sesam. The delta stream processing pipes collect raw data, connect
data objects across sources, and store data into a combined semantic
data storage. The same delta stream process pipes transform and share
the data to any target system, using each systems’ native schema. Thus,
all data processing in Sesam is unified in a low-code, high-throughput,
low-latency service.

Benefits of delta stream processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sesam processes only deltas, so that no systems connected by Sesam needs
to reprocess existing data. This reduces system processing time and
update delays by at least 95% compared to bulk ETL jobs, and completely
removes unnecessary data updates.

Graph-based dependency tracking
-------------------------------

Graph-based dependency tracking ensures that every composite object is
always updated as a delta stream throughout the Sesam service, no matter
the number of complex transformations, including merging from any number
of source objects. The dependency tracking is made possible by the fact
that there is no code in Sesam, only metadata configuration describing
the transformations in pipes.

Benefits of graph-based dependency tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sesam supports graph-based dependency tracking, so that even complex
objects from multiple sources can be processed as delta streams. This
ensures that complete reprocessing never is required, no matter the
number of sources, the complexity of the transformations, or the number
of target systems and data schemas involved.

Sesam uses metadata configuration, so that all data flows uniformly,
without the need for custom code, giving complete transparency and
heavily reduced operating cost.

Semantic data storage with dynamic multi schema
-----------------------------------------------

In Sesam the output of any delta stream processing pipe is stored in
semantic datasets. A semantic dataset is an immutable object store,
capable of containing the complete version of any object. Every dataset
has a completely dynamic schema, continuously updated to fit the data
stored in it. Semantic technology ensures that each property´s origin is
preserved and allows a single object to contain multiple schemas,
assembled into one global object. Adding golden properties, and
continuously evolve them, can be done whenever needed, as these
properties are added to the existing global object without affecting the
original properties.

Benefits of semantic data storage with dynamic multi schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sesam stores all data in semantic data storage, so that data never loses
its origin and context, and never gets corrupted or lost in translation.
Every representation of an object, regardless of source, is stored as a
single entity, without conflict or consistency corruption.

Sesam connects every representation of any single object, and stores it
as a multi schema global object, so that any source system only needs to
share its data once, and in its native schema. On average this reduces
the number of integrations by 90%, in addition to simplifying each
integration by never having to modify any source systems or do any data
modeling before adding source data.

Sesam supports continuously evolving global properties in the multi
schema datastore, so that canonical models can emerge over time, and any
standardized data model can be implemented independently and be stored
in a single object. When all source properties and global properties are
available as a single composite object, the cost and time of acquiring
data and transforming the data into a target system in its native
schema, is heavily reduced.
