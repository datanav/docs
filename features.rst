Key features and benefits
=========================

The combination of Sesame's key features simplifies data management for
master data in data driven environments. The service consists most of
the core features needed to build a data-fabric based platform.

Delta stream processing
-----------------------

Delta processing means that only data that has changed is ever processed
by Sesam. The delta stream processing pipes collects raw data, connects
data objects across sources, and stores data into a combined semantic
data storage. The same delta stream process pipes transform and shares
the data to any target system using those systems native schema, making
all data processing in Sesam unified in a low-code, high-throughput,
low-latency service.

Benefits of delta stream processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sesam processes only deltas, so that no systems connected by Sesam needs
to reprocess existing data. This reduces system processing time and
update delays by at least 95% compared to bulk ETL jobs, and completely
removes unnecessary data updates.

Graph-based dependency tracking
-------------------------------

Graph based dependency tracking ensures that every composite object,
composed by any number of complex transformations, involving merging
from any number of source objects, always is updated as a delta stream
throughout the Sesam service. The dependency tracking is made possible
by the fact that there is no code in Sesam, only metadata configuration
describing the transformations in pipes.

Benefits of graph-based dependency tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sesam supports graph-based dependency tracking, so that even complex
objects from multiple sources can be processed as delta streams. This
ensures that it is never necessary with complete reprocessing, no matter
the number of sources, the complexity of the transformations, or the
number of target systems and data schemas involved.

Sesam uses metadata configuration, so that all data flows uniformly,
without the need for custom code, giving complete transparency and
heavily reduced operating cost.

Semantic data storage with dynamic multi schema
-----------------------------------------------

In Sesam the result of any delta stream processing pipe is stored in
semantic datasets. A semantic dataset is an immutable object store,
capable of containing the complete version of any object. Every dataset
has a completely dynamic schema, continuously updated by the data that
is stored in it. Semantic technology ensures that the data source is
preserved for all properties of the object and allows a single object to
contain multiple schemas, assembled into one global object. The
compilation of any golden properties can be done on demand, and
continuously evolve as the different needs arise, as these properties
are added to the existing global object whiteout affecting the original
properties.

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
available as single composite object, the cost and time of acquiring
data and transforming the data into a target system it its native
schema, is heavily reduced.
