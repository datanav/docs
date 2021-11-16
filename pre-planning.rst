Planning a Sesam project
============================

The main planning task before starting a Sesam project is to document
an overview of what master data types are needed, their source, and how
they should be organized inside Sesam.

The :ref:`dataflow <best-practice-workflow>` can be documented by filling this
:download:`template <files/Sesam data flow planning.xlsx>` by following these 4 steps:

1. Identify what master data you need and where this data must be
   available

2. Identify where the master data exists today

3. Identify the system independent globals (common data grouping) needed
   to store the master data in Sesam

4. Connect the systems and master data types to the globals

Identify master data
--------------------

Based on the functional needs of the project, identify the data types at
a high level, and where this data must be available.

For the master data giving context to the data platform, driving
analytics, AI, web and Apps, select the appropriate data platform
components from your preferred vendors. Eg. Azure, Google etc.

For master data needed to fill and synchronize with new or existing
business systems, identify their API, or other data protocol, the
endpoint URI, and what connector can be used to communicate with them.

Identify master data sources
----------------------------

Identify the source systems that contain the necessary data to fill the
master data requirements of the project.

Identify their API, or other data protocol, and what connector can be
used to communicate with them, including if the system has test and prod
environments and their endpoint URIs.

To be able to effectively implement the project, a system owner and
preferably a data owner for each system should be identified.

Once all sources have been identified, an initial priority of the
different sources can be set. Central objects will always be stored in
multiple systems, and prioritizing what system will override others is
important to support multi master data synchronization.

Identify globals
----------------

Once det necessary master data sources and targets have been found, the
source master data must be grouped into globals in Sesam.

Group data by type, not role. One object should never fit in more than
one group. Start generically in this phase. Re grouping to more detailed
groups can be done with time.

Samples of a good way of grouping into globals:

-  Person - Not use employee, contact person, or user

-  Business – Not use supplier, customer, or partner

-  Product – Not use screw, nut or bolt

Connect data types to the globals
---------------------------------

Finally connect all identified data types to their respective globals to
complete the data flow architecture.

Incoming data may be split into
different globals, and outgoing data may need to combine several
globals.
