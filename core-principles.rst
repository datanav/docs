===============
Core principles
===============

Sesam is a master data hub that simplifies the process of making
up-to-date master data available in a data platform architecture. Sesam
enables rapid development of solutions that can be effectively
managed on top of a data platform. Sesam is a data platform component
that collects data from source systems and connects all representations of
an object across a variety of source systems in a continuously updated
and dynamic `data model <https://en.wikipedia.org/wiki/Data_model>`_,
and makes the data easily accessible inside the data platform.

Sesam has a set of fundamental principles to ensure that the capture,
exploitation, and management of master data in data platform solutions
will be as fast and efficient as possible. Together, these principles 
ensure continuously updated master data, with high data quality, that 
can be effectively managed over time.

.. rubric:: Master data is any structured data that changes, not just the most central data

The definition of `master
data <https://en.wikipedia.org/wiki/Master_data>`_ is "Data that
provides context to transactional data", but in a data platform
architecture, the definition of transactional data is somewhat unclear.
We therefore redefine this to be "Data that provides context to time series
data". With `time series, <https://en.wikipedia.org/wiki/Time_series>`_
we mean captured data that evolves over time,
such as sensor data and log data. It gives us the following definition
of master data in a data platform:

   *Structured data that changes over time and that is needed for use
   outside the system where it was created.*

This means that master data is not limited to customer, product, asset,
and employee data, but contains both `reference
data <https://en.wikipedia.org/wiki/Reference_data>`_ and all possible
forms of structured data stored in a system, where the data also is
required to be made available outside of that system. Master data is all
data in a data platform that is neither unstructured nor in time
series. Examples of master data slightly outside the usual definition
are: order and invoice information, work orders, timesheet, document
metadata, as well as any type of category.

.. rubric:: Parallel and continuously function-adapted data models, not static and canonical

The biggest challenge for data quality is that each system in a
composite architecture has different representations of the same object.
The challenge is amplified in a data-driven architecture, where the data
itself should be meaningful and not wrapped in functional shells as in a
traditional `SOA
architecture. <https://en.wikipedia.org/wiki/Service-oriented_architecture>`_

The "simple" solution is to agree on one a single data model for each
object type, a so-called `canonical
model <https://en.wikipedia.org/wiki/Canonical_model>`_, that ideally
represents a standardized superset everything you will need at the time, from 
all systems. 
While this may be a requirement in a message-based integration
architecture, and is truly valuable in an industry-wide data 
`interoperability <https://en.wikipedia.org/wiki/Interoperability>`_ 
scenario, in a data platform however, the canonical model becomes a constant burden 
demanding continual enhancement and expansion over time. The result becomes a 
datamodel that lags behind 
the continously evolving needs of the platform.

Many businesses have allocated enormous resources on efforts to stabilize their canonical model. Any given data model will always be a
perspective of the object one wants to describe at a given time, not an objective and lasting truth.

In Sesam, we solve this fundamental problem in the diametrically
opposite way: We collect all the different representations of an object,
without changing the data model for any of the different
representations. Instead of a false idea of "`Single source of
Truth," <https://en.wikipedia.org/wiki/Single_source_of_truth>`_ Sesam
will gather and connect all perspectives, i.e. data models, which exists
about an object in a composite dynamic representation. Any single master
data object becomes available, in all its different perspectives, as a
single resource. This makes it easy to continuously develop the platform-wide,
domain-wide, or functionality-wide data models needed in the data
platform. The composite object representation linking all the different
representations across systems is stored as a single object in :ref:`global 
datasets <concepts-global-datasets>`. 

The representation is stored in a standard
`JSON <https://en.wikipedia.org/wiki/JSON>`_ based format, and
continuously updated with data from all source systems. The complete
object is stored in one global dataset only, and in a single data
format. However, the data models describing the object can be
continuously enhanced, based on the development of the source systems,
and driven by the functional needs at any time.

.. rubric:: Adapt your data platform to the business systems, not the other way around

A data platform exists to collect data from different systems and share
this data in a consistent manner, to make it easier to retrieve the
value that lies in the data. This is an ongoing process that must
facilitate continually expanding value outtake, and quick delivery of
the right data with the right quality for new purposes.

The master data
will need to be compiled from a set of business systems that are
constantly changing, both in the case of new versions of a system,
and in the case or replacing them with new systems. To effectively
manage a data platform, and make it fast and easy 
to use best-of-breed business systems  `out-of-the-box 
<https://en.wikipedia.org/wiki/Out_of_the_box_(feature)>`_, 
it is essential that the business systems
and data platform are as loosely coupled as possible. 

Sesam does not require any modifications in the business systems, but 
instead each system talk in their own language, meaning they can collect and 
share data in the form that the system supports, through mechanisms for 
which the systems were built. Whether the business system communicates via 
REST API, SOAP, XML, CSV, SQL or any other communication form or format 
is irrelevant. If there is structured data, Sesam will be able to talk to
every system in their own language. 

Internally in Sesam all data is transformed into a 
:ref:`extended <concepts-transit-encoding>` JSON based
data format, but retains its original data model. This is essential to
not degrade the quality of the data. Any conversion from one data model
to another will mean a reduction in data quality.

In Sesam, the original
data model will be retained in addition to the origin of the data by 
using :ref:`namespaces <best-practice-namespace>`, and
thus the context in which they were created is retained as part of the
data format. It ensures that data is not lost in the transmission from
business system to data platform.

.. rubric:: Synchronize the data, don't let it flow only in one direction

Any system that is the source of master data needs to continuously keep
their data up to date. These data updates do not have to come through
the system's own UI, but should be able to originate from anywhere in
the data platform architecture. The aim of a data platform is to make
data available to ensure that a wide set of value-added services, such
as automation, machine learning, mobile applications, web etc. can be deployed.

All services built on data will be able to create new valuable data that is
sent back and will further enrich the data platform. This data should
not only remain inside the data platform, but continuously update the
subject systems in question. 

Sesam synchronizes data from its global
dataset back into the business system, so that in practice one achieves
a functional `multi-master
replication <https://en.wikipedia.org/wiki/Multi-master_replication>`_
across both business systems and the entire data platform solution. In
all systems where semantically equal properties about the same object
exist, the data will be coordinated to achieve consistency on all
levels.

.. rubric:: Build autonomous services, avoid dependencies, and tight coupling

Just as a common data model can't meet all needs, one data access point
isn't effective to cover a wide range of data-driven services. The most
stable architecture is to allow each service to have an optimized data
source with a subset of data that is tailored to the service's needs.
This forms the core of a `loosely
connected <https://en.wikipedia.org/wiki/Loose_coupling>`_
architecture, and means that each service can choose to use the data
store and the data model that is most efficient, while ensuring that the
services do not stop working at the same time due to a common
dependency.

Sesam is optimized for synchronizing master data between the
master data hub and each service's data store in the same way as against
business systems. Regardless of the optimal store for a service, whether
it's SQL-based, search-index-based, NoSQL-based, graph-based, or using
special tools such as Firebase, Qlik, Tableau, etc.

.. rubric:: Stream changes to master data, don't use slow and resource intensive ETL

Traditional data platform architecture is often based on `ETL
<https://en.wikipedia.org/wiki/Extract,_transform,_load>`_ to retrieve
master data as opposed to time series data, which in most cases is
streamed into the platform. A reason for this is that the amount of
master data is usually limited, and that the source systems often cannot
deliver a stream of changes. 

The biggest problem in this approach is
that master data is always composed from multiple systems, so all data
from all systems must be reloaded each time data is updated. This causes
a low refresh rate, and undesired dependencies between source systems to
make ETL jobs able to complete. This causes all downstream systems that
need master data to also be forced to batch process their data using
ETL.

Sesam is an at-design-time `dataflow  <https://en.wikipedia.org/wiki/Dataflow>`_ 
tool optimized to always just
collect changes and stream them into the global datasets, and from there
out to all systems that need the change. Regardless of whether a
source supports change tracking, Sesam will immediately convert any
batch load to a stream of the real changes contained in that batch using
delta comparison. 

Sesam will automatically interpret the dataflow
configuration so that it knows every single object affected by any
change. Even the construction of complex composite data objects across a 
multitude of source systems with advanced dependencies, is automaticaly
change tracked by the Sesam engine.
This non trivial requirement is a prerequisite for being able to stream 
compound objects without having to ETL the entire dataset each time updated 
data is needed.

.. rubric:: Standardize master data management, don’t hide it in code

The complexity of a data platform is increasing for every system and
data type you add to it, and the chance of losing control becomes
eminent over time. It’s imperative to standardize the way master data is
managed and gain a transparent unified methodology throughout the
platform, which is flexible and can be maintained over time.

Coding is extremly effective in an isolated environment, 
and it gives every developer free
rein to solve their individual tasks to their own liking. The problem is
effective management over time in a complex environment. 
Every code snippet becomes a `black
box <https://en.wikipedia.org/wiki/Black_box>`__, and while this may be
the best way to solve some functional needs, it is destructive when it
comes to managing master data.

A core challenge in a heterogeneous environment, as data platforms are,
is the lack of transparency. Utilization of composite data from a wide
range of source systems is the core principle to gain value from a data
platform, and if the process for generation of that data is not
transparent, you can never trust its quality.

In Sesam every part of the dataflow, storage and management is highly
standardized and defined declaratively. There is no code, only
structured :ref:`configuration <concepts-config>`, stored as data, 
which instructs the platform
how to collect data, how to connect and enrich them, and how to share
them. This makes the master data management completely transparent, and
even the most complicated dataflow self-documented. All data can be
traced back to its origin, inspected at any point in a flow, and the
data quality completely trustworthy.

