
.. _tc_sesam_intro:

=====================
Introduction to Sesam
=====================

Beginner Topics
---------------

Different types of Architectures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###.. _tc_data-driven-architecture-1-1:###


.. _tc_enterprise-service-bus-1-1:

Enterprise Service Bus (ESB)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. sidebar:: Summary

  - Asyncronuous message queue
  - Centralized management
  - System decoupling
  - Scaleable
  - No centralized data storage

The ESB is a more robust IA and plays a critical role in connecting
diverse systems and services in a Service Oriented Architecture (SOA).
The ESB takes on the responsibility of ensuring that data sent from one
system conforms to the requirements in another system. This core
functionality is an important feature as to why the ESB is such an
established architectural principle. In addition, the ESB aids in
simplifying integration efforts when connecting differing applications
that need to communicate with each other. See figure :ref:`figure-esb-1-1`.

.. _tc_figure-esb-1-1:
.. figure:: ../../../training/010_architecture_and_concepts/media/Enterprise_Service_Bus.png
   :align: center

   Enterprise Service Bus

Taking into account the positives from using an ESB for your IA - some
challenges still remain unresolved. Recent years transition towards more
cloud-based solutions, hybrid solutions and the remaining tendency to
focus on the systems in the ESB rather than the data itself has
propelled what is called “Data Driven Architecture”.

.. _tc_datahub-1-1:

Datahub
~~~~~~~

.. sidebar:: Summary

  - Data centric
  - Very scaleable
  - Centralized data storage

Continuing along the path of building data-centric solutions, the term
“Datahub” comes into play. A datahub is recognized by its frictionless
data flow and builds upon the architectural principles presented
in DDA. A datahub can be described as a solution that consists of
multiple different technologies, i.e., a data warehouse, microservices,
databases etc.

A Datahub shares data by connecting providers of data with consumers of
data. As such, a datahub mediates and manages how data flows between systems and makes states of data visible to consumers outside the datahub.

In a sense, you could say that a datahub is a digital representation of
an enterprise and also what SESAM often becomes when it is used
properly. As with any other technologies there are pros and cons.
Some of these are listed below, so you might be able to recognize them
“down the road”.

Pros:

- Enterprise scope, i.e., runs on cloud, hybrid.

- Creates visibility into all data.

- Centralised data control & management.

- Moves data asynchronously.

- Connects data from different systems.

- Possibility of defining the best truth of an object across systems.

- Forces the break-down of walled silos.

Cons:

- Only cares about the latest version of data.

- Demands advanced capabilities.

- Does not operate well with silos.

.. seealso::

  TODO

.. _tc_the_parts_of_sesam-1-1:

The parts of sesam @Erik
~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Sesam's core components:

  - **Systems** to interaface with external systems
  - **Pipes** to move and transform data
  - **Datasets** to store data
  - **Entities** that are the actual data stored in datasets

In order to understand how Sesam works, it is important to understand
the parts Sesam is made up of. There are three central re-occurring
concepts in Sesam which you will encounter in your everyday life working
with the integration platform: systems, pipes and datasets.

.. figure:: ../../../training/010_architecture_and_concepts/media/Architecture_Beginner_Systems_pipes_datasets_A.png
   :align: center
   :alt: A general pipeline flow in Sesam depicting the three central parts of a Sesam integration, systems, pipes and datasets. The arrows symbolize the direction of data flow.
   :width: 100%

   A general pipeline flow in Sesam depicting the three central parts of a Sesam integration,
   systems, pipes and datasets. The arrows symbolize the direction of data flow.

These are the fundamental parts which make up a Sesam integration pipeline:

Systems:
   A system’s main feature is to act as the interface to import and export data
   into and out of Sesam nodes. The actual import and export is carried out by the pipes connected to the systems. The systems are  therefore found in the
   beginning and end of the pipeline flows and are often referred to as
   “source systems” or “target systems” respectively. A system could
   connect to a REST API, directly to a database or simply send data to
   a waiting http server. Sesam has several of these system types built
   into the product to simplify the workings inside the portal. In
   situations where the built-in system types are not enough for your
   requirements Sesam also supports connecting systems to a microservice
   which in turn can manipulate and delegate data according to your own
   specifications, making Sesam a very robust and comprehensive tool.

Pipes:
   A pipe's main functions are to actualize the import and export of data, to handle transformation of the data when needed as well as to specify
   where the data is supposed to be sent. Manipulation of the data is
   done through Sesam’s own Data Transformation Language (DTL) which
   allows you to add, remove, transform or combine data according to
   you own needs. A pipe generally acquires data from a system or from a
   dataset depending on where the pipe is located inside the integration
   pipeline.

Datasets:
   Datasets are Sesam’s storage units and can be compared
   to i.e., a table in an SQL database. Datasets are where the pipes store the
   data they produce, unless a sink specifies otherwise. Sesam stores data in order to be able
   to perform tracking and indexing, but you will learn more about these
   functionalities later in this book (maybe a link?).

Entities:
   A dataset consists of a list of entities. Entities in
   Sesam can be compared to individual rows in an SQL table and can
   represent anything from a person, a mechanical part to a contract. An
   entity is defined by its primary key, which is represented in Sesam
   as the value belonging to the key ``_id``.

.. seealso::

  Learn Sesam - Architecture & Concepts: Beginner: :ref:`systems-1-1`

  Learn Sesam - Architecture & Concepts: Beginner: :ref:`pipes-1-1`

  Learn Sesam - Architecture & Concepts: Beginner: :ref:`datasets-1-1`

  Learn Sesam - Architecture & Concepts: Beginner: :ref:`entities-json-keyvalpairs-1-1`

.. _tc_the_sesam_portal-1-1:

The Sesam portal
~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  The **Dashboard** is where you see all your Sesam subscriptions (nodes)
  and where you can order new ones.

Integrations, connections and configurations can all be accessed inside
the Sesam portal; the user interface of the Sesam product. The Sesam
portal can be accessed at portal.sesam.io and in this section you will
learn the most commonly used parts of the portal such that you can
orient yourself, as well as manage existing integrations. For a full
explanation if the workings and functionality of the Sesam portal,
please visit the :ref:`sesam-management-studio` section.

When logging in to the portal you will be met with a page like the figure below:

.. _tc_figure-sesam-portal-1-1:
.. figure:: ../../../training/010_architecture_and_concepts/media/Architecture_Beginner_The_Sesam_Portal_A.png
   :align: center
   :alt: The Sesam Portal
   :width: 100%

   The Sesam Portal


The cards on the Dashboard are often referred to as “subscriptions” or
“nodes” and they represent separate instances of Sesam installations.
Each node comes in different sizes (memory available) depending on the
requirements of the customer/project/user. In this example you will be
shown the portal inside the node called “Training Node”, but all nodes
will have the same setup, only different set of systems, pipes and
datasets.

When entering the “Training Node” you will be met with the page seen in
the figure below.

.. _tc_figure-training-node-landing-page-1-1:
.. figure:: ../../../training/010_architecture_and_concepts/media/Architecture_Beginner_The_Sesam_Portal_B.png
   :align: center
   :alt: Training Node Landing Page
   :width: 100%

   Training Node Landing Page

In this section we will only focus on the specific parts of the portal
needed to start working with Sesam, namely the “Pipes” page and the
“Systems” page.

.. seealso::

  Tools: :ref:`sesam-management-studio`

Pipes
^^^^^

Upon entering the “Pipes” page via the menu on the left hand side you will
be met by a list of pipes as seen below.
Unless filters are applied the list diplays all the available pipes in your
subscription as well as some of their corresponding meta-data.
The search and filter options available are specially handy when trying to
locate one, or a subset of pipes, in a subscription with many pipes.

.. _tc_pipe_overview_figure:

.. figure:: ../../../training/010_architecture_and_concepts/media/Architecture_Beginner_The_Sesam_Portal_C.png
   :align: center
   :alt: Sesam Node Pipe overview
   :width: 100%

   Pipe overview

We will now enter the pipe called “person-cmm” where we can look more into the
details regarding how you may use the portal to navigate, troubleshoot
and configure your pipes.

Upon entering a pipe you will by default be sent to the pipe’s “Graph”
view, as seen below.

.. _tc_figure-pipe-graph-view-1-1:
.. figure:: ../../../training/010_architecture_and_concepts/media/Architecture_Beginner_The_Sesam_Portal_D.png
   :align: center
   :alt: Pipe Graph view
   :width: 100%

   Pipe graph view

The graph view shows you which pipes are upstream and downstream to the
specific pipe you have selected, and it also displays connections to
related pipes (you will learn more about connected pipes later [link
maybe?]). For now, we will focus on four of the pipe’s tabs: Config,
Input, Output and the Execution log.

Config:
   The config tab is where the actual coding takes
   place. This is where you define what this specific pipe is supposed
   to do. A pipe config is written in DTL which you will learn more
   about in :ref:`dtl-beginner-3-1`.

Input:
   Whenever a pipe uses one or several datasets as a source,
   the source entities will be displayed here. These are the entities
   the pipe will perform some sort of transformation on.

Output:
   The output tab shows the entities after the DTL
   transformation. The way you see the output depends on whether the
   data is stored in a dataset or sent to a target system.
   The pipe you are looking at needs to have run at least once for there to be any output.

Execution log:
   The execution log supplies us with information on
   the state of the pipe. If a pipe runs as it should the execution log
   will display information on how many entities it has processed, how
   much time the processing took and much more. If a pipe is not able
   to process all the data, the execution log will display a failed pipe
   run as well as error messages which may assist you to locate the
   error. The execution log is a vital tool for troubleshooting.

.. seealso::

  Tools - Sesam Management Studio: :ref:`management-studio-pipes`

Systems
^^^^^^^

The systems page looks very much like the pipe tab in the Pipe overview above.

.. figure:: ../../../training/010_architecture_and_concepts/media/systems-overview.png
   :align: center
   :alt: Sesam Node System overview
   :height: 200px
   :width: 800px

   Systems overview

When entering a system you will se a set of tabs, just as we saw in a specific pipe.

.. figure:: ../../../training/010_architecture_and_concepts/media/system-graph.png
   :align: center
   :alt: System graph
   :height: 400px
   :width: 800px

   System graph view

For systems we will focus the three most commonly used tabs: Config, Secrets
and Status.

Config:
   Like with pipes, the config tab is where you specify what
   the system is supposed to do. There are many different types of
   systems which have a variety of configuration options. There are
   however some common traits that apply to most system. These traits
   include authorization parameters, location parameters such as
   IP-addresses, URLs and database names and system types.
   If your system is a microservice you may set environment variables
   whose values can be accessed inside the microservice.

Secrets:
   In the Secrets tab you may store sensitive information
   you do not wish everyone on the node to have access to. These secrets
   are often passwords or token used to authorization and
   authentication. Secrets stored in the system tabs are local secrets
   and may only be used by the specific system in which they are
   defined.

Status:
   In the Status tab you can monitor the health of your
   system. When connected to built-in systems this tab shows you whether
   you are connected correctly. When connected to Microservices this tab
   displays connection status and logging provided by the Microservice.

.. seealso::

  Tools - Sesam Management Studio: :ref:`management-studio-systems`


.. _tc_naming-conventions-1-1:

Naming conventions
~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  - Lower case
  - Hyphen (-) as separator
  - Singular form (`user`, not `users`)
  - Systems: Name of system (not type) (`hr`, not `mssql`)
  - Inbound pipes: *<source system>*\ `-`\ *<data type>* (`hr-user`)
  - Global pipes: `global-`\ *<category>* (`global-person`)
  - Preparation pipes: *<data-type>*\ `-`\ *<target-system>* (`user-hr`)
  - Endpoint pipes: *<data-type>*\ `-`\ *<target-system>*\ `-endpoint` (`user-hr-endpoint`)

When constructing an integration flow in Sesam the use of a standardized
naming convention becomes essential as the project grows to more than a few pipes.
A standardized naming convention helps you to easily structure your Sesam architecture such that:

-  Localizing specific flows becomes easier.

-  Troubleshooting becomes more efficient.

- Determining pipe type (inbound, outbound, preparation or global) becomes easier.

- Filtering relevant pipes become easier.

-  Switching between integration projects, or joining a new project,
   becomes more intuitive.

-  Support will be more efficient.

In Sesam we focus on naming pipes, datasets and systems in way that
explains the function of that specific structure. The following points
are the naming rules Sesam suggests you follow when constructing your
integration flows.

**Systems**

A system name should describe the source/target system from the
customers perspective, not from Sesam’s perspective. If a customer has
employee data inside a HR system named “HR”, but the data from “HR” is
supplied by an API provider called “API provider”, the Sesam system
should be named “hr”. The same rule applies if the HR data was populated
in a database which Sesam connects to. Naming the system after the
database might seem intuitive at first glance but naming from the
customers perspective makes communication and troubleshooting much
easier in the long run.

**Pipes**

*Inbound pipes:*

Inbound pipes should be named according to endpoint/table they connect to
in the source system and prefixed with the source system name such that
there is a clear and intuitive way of tracking their content. Let us use
the same example as for naming system. I this case the HR system in the
previous example populate its data in two tables: employee and
department. Our two inbound pipes connecting to the two tables containing
HR data will therefore be named “hr-employee” and “hr-department”. The
system name prefixed highlights that the HR system is upstream from the
pipes.

*Global pipes:*

Global pipes should be named according to the semantic relation
connecting the datasets used as the global pipes source and prefixed
with “global”. These semantic relations may vary between projects and
customers, but some are generally always occurring such as
global-person, global-company, global-customer or global-project.

*Preparation pipes:*

Preparation pipe naming can be more diverse but should explain the type
of data it transforms as well as the target system. If the inbound pipe
importing a table “person” from a system “HR” is named “hr-person", the
corresponding preparation pipe preparing data to be pushed to the table
“person” should be named “person-hr". We use the system name as a
postfix in this case to highlight the fact that this data has the HR
system down-stream. In many cases you might require several preparations
pipes between the global pipe and the endpoint pipe. In these cases, in
addition to the type of data transformed as the downstream target
system, the pipe name should reflect the functionality of that specific
preparation pipe. As an example, if a preparation pipe splits entities
into child entities, the children functionality should be part of the
pipe name i.e., “person-child-hr".

*Outbound pipes:*

An outbound pipe should have the same name as the name of the pipe
generating the outbound pipe’s source dataset, only postfixed with
“endpoint” i.e., “person-child-hr-endpoint”.

The following flow shows a typical Sesam flow with each pipe’s preferred
name with an example:

|

.. figure:: ../../../training/010_architecture_and_concepts/media/Architecture_Beginner_Pipes_A.png
   :align: center
   :width: 835px
   :height: 105px
   :alt: Full pipe flow with generic names.

   Full pipe flow with generic names.

|

.. figure:: ../../../training/010_architecture_and_concepts/media/Architecture_Beginner_Pipes_B.png
   :width: 800px
   :height: 100px
   :align: center
   :alt: Example of Full pipe flow with globals.

   Full pipe flow with example names.

.. seealso::

  Best Practices - Data modelling in Sesam: :ref:`best-practice-naming-conventions`

.. _tc_systems-1-1:

Systems
~~~~~~~

.. sidebar:: Summary

  Systems are interfaces to external systems.

Systems are one of Sesam's core components.
Systems can connect to external providers such as SQL databases, REST APIs,
Microservices and more, to either import data into Sesam or export data out from Sesam.
Systems are therefore the start and end points of every dataflow.

Systems may cover other functionalities as well, but we will cover those special cases
later.

In this section we will show you an example of the most commom system in a Sesam installation,
the mssql system. We will also show how this system can connect to pipes to
either import or export data, depending on your need.

The MSSQL system
^^^^^^^^^^^^^^^^

.. figure:: ../../../training/010_architecture_and_concepts/media/mssql-system-config.png
   :align: right
   :alt: MSSQL system config.

   MSSQL system config

Since they are a relatively common way to store data, Sesam has a ready built-in connector for MSSQL databases. The MSSQL system inside Sesam connects to an MSSQL database by sending the host, database and port information, as well as authentication parameters, through a built in connector inside Sesam. Note that in the system config we also have to specify the system type ``system:mssql``.

.. figure:: ../../../training/010_architecture_and_concepts/media/mssql-system-status.png
   :align: right
   :alt: MSSQL system status.

   MSSQL system status.

Once the connection is open the node can extract data from the tables in the database through inbound pipes connected to the system. You can see if the connection to the MSSQL database is open by going to the "Status" tab on the system page. Should the system health state "failure" in your connectivity, this could be because you have some parameter values in your config wrong, or there might be a firewall blocking your access.

.. seealso::

  Learn Sesam: :ref:`systems-beginner-2-1`

  Developer Guide - Service Configuration: :ref:`system_section`

.. _tc_pipes-1-1:

Pipes
~~~~~

Something more general about pipes maybe in context of systems and
datasets

Inbound(Input?)/Preparation/Outbound(Output?)

Very low level but enough to connect to system?

and refer to pipes chapter

Pump

Input & output(sink)

Namegivingconventions ref. 1.1.8

Where to make new ref 1.1.6

.. seealso::

  Learn Sesam: :ref:`dtl-beginner-3-1`

  Developer Guide - Service Configuration: :ref:`pipe_section`

.. _tc_datasets-1-1:

Datasets
~~~~~~~~

.. sidebar:: Summary

  - Sesam datasets are immutable logs of entities
  - Sesam datasets are schemaless
  - Entities in Sesam datasets *must* have ``_id``

Datasets are where data is stored inside Sesam, regardless of whether the
data comes from external systems or from internal pipes.

Data in a dataset is represented as a JSON list where each list item is a
data record, called *entity*, consisting of key-value pairs.

A dataset with two entities concerning people could look like this:

.. code-block:: json

   [
     {
       "id": "1",
       "name": "Jane Doe"
     },
     {
       "id": "2",
       "name": "John Doe"
     }
   ]

Dataset is the default sink type for internal pipes in Sesam, so if no sink
config is specified for a pipe it's output will be a dataset.

Datasets are also often the source for internal pipes.

.. seealso::

  Learn Sesam - Architecture & Concepts: Beginner: :ref:`entities-json-keyvalpairs-1-1`

  Learn Sesam - Architecture & Concepts: Beginner: :ref:`naming-conventions-1-1`

  Learn Sesam - Architecture & Concepts: Beginner: :ref:`pipes-1-1`

  Learn Sesam - DTL: Beginner: :ref:`dataset-id-3-1`

.. _tc_entities-json-keyvalpairs-1-1:

Entities / JSON (Key-value pairs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As stated earlier in this section, a dataset consists of a list of entities. An entity is a JSON type dictionary containing a set of key-value pairs identified by its unique identifier. A key-value pair is two related data elements. A key is a constant and defines what that data element is concerned with, i.e., postCode, email, phoneNumber, etc. Meanwhile, the value provides contextual information for a specific key. This could look like the following:

.. code-block:: json

   {
     "<key>": "<value>"
   }

   {
     "postCode": "6400"
   }


.. seealso::

  TODO

.. _tc_special-sesam-attributes-1-1:

Special sesam attributes
~~~~~~~~~~~~~~~~~~~~~~~~

Namespaces
^^^^^^^^^^
Namespaces in Sesam are primarily used on properties, and its main functions are to ensure uniqueness across sources and to maintain the origin of the properties. "global-person:fullname" is an example of a namespaced property, where "global-person" is the namespace and "fullname" is the property name.

Namespaced identifiers (NIs) are identifiers (i.e. property values) given a namespace.
"source:reference": "~:foo:bar" is an example of a NI, where "source" is the property namespace, "reference" is the property name, "foo" is the namespace of the referenced data and "bar" is the identifier usually matching an identifier in the referenced data. The "~" is the Sesam syntax for defining a datatype as a NI.

As such, NIs in Sesam are similar to foreign keys in databases in that NIs are a visual indication of how data is connected, and enables easier and more precise joins. However, Sesam does not enforce any relationship between NIs and the referenced properties. You use the functions ["make-ni"] or ["ni"] to create NIs when modelling data in Sesam.

.. seealso::

  TODO

Rdf:type
^^^^^^^^
The RDF type is metadata used to relate data and give some semantic context. When used with a namespace, it keeps track of the origin of the data, as well as the business type. It is composed upon input and will be used to relate and filter like you would use a foreign key.

Using the above NI "~:foo:bar", an RDF type defined property in Sesam could look like the following: ``{"rdf:type": "~:foo:bar"}.``

.. seealso::

  TODO

.. _tc_id-1-1:

\_id
^^^^
The identity (_id) of systems, pipes and datasets must be unique and consistent as data moves via systems, through pipes and into datasets.

The _id of a system is usually defined by the name of your source system i.e., salesforce. In case you need two systems in Sesam that both originate from salesforce, you'll need to make two unique names for each of these i.e., salesforce and salesforce-rest.

For pipes, the _id is typically defined by establishing which properties in the pipe´s dataset are unique across its entities. This could typically be primary key(s) when data is imported from a database or potentially a unique property or even concatenated properties when data is imported from an API.

When data reaches a pipe's dataset, the _id will be identical to what you defined the _id to be, in that pipe's config.

.. seealso::

  TODO

.. _tc_pipes-where-dtl-executes-3-1:

Pipes, where DTL executes
~~~~~~~~~~~~~~~~~~~~~~~~~

(Repeting 1.1.5?)

Sesam consumes and produces streams of data in the form of lists of
entities.

Streams of entities flow through **pipes**. A pipe has an associated
**pump** that pull data entities from the **source**, push them through
any **transforms**, and send the results to the **sink**. All of this is
configured in the pipes configuration. As with water pipes, there is a
flow inside the single pipe (segment), and pipes connect to other pipes
and systems.

DTL (Data transformation Language) as the name implies is a
transformation. It is part of the internal flow of the pipe and an
entity enters and is transformed before the resulting entity is passed
to the next step in the flow. Usually the sink.

A pipe do not strictly have to have a DTL-transform, but most pipes have
one. DTL is not used outside pipes in Sesam.

**Source** and **Target** are two central concepts in DTL. Source is
data entering the flow and target is data exiting the flow. In some DTL
functions this is implicit, like copy and rename. For other DTL
functions you use built-in Variables "_S." (**S**\ ource) and "_T."
(**T**\ arget).

The simplest DTL transforms only copy or rename a subset of the fields
from the source (single) entity that flows from pipe-source into
DTL-transform. The source-concept is context based in pipes and DTL. You
will see examples of this.

Example: (need to line up with other examples and have a nice layout)

(*Link to short video*?)

(pipe with only embeded data?? Make the dataset)

(pipe with this datasett as source??)

This is the config for a pipe that gets data entities from the dataset
salesforce-lead and make new enteties from each entity and put them in

.. code-block:: json

   {

      "_id": "dtl-test",

      "type": "pipe",

      "source": {

         "type": "dataset",

         "dataset": "salesforce-lead"

      },

      "transform": {

         "type": "dtl",

         "rules": {

            "default": [

               ["copy", ["list", "_id", "Username"]],

               ["rename","EmailAddress",":Contact-point"]

            ]

         }

      }

   }

DTL is often more complex. E.g. it can pull and use data from other data
sets in your Sesam node or deal with nested structures in the source
entity.

DTL has many functions that you can use to transform data. You find an
overview in the DTL Reference Guide. You will use this much.

**What happens when a pipe runs?**

**What is the relationship of pipes and DTL?**

.. seealso::

  TODO

.. _tc_entities-pipes-and-id-3-1:

Entities, pipes and _id @Geir Atle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The reserved property _id
^^^^^^^^^^^^^^^^^^^^^^^^^

Everything in Sesam must have a unique identity, whether it is a system
configuration, a pipe configuration, a dataset, an entity within a
dataset, etc.

The reserved property named ``_id`` is used as unique identity for
components in Sesam.

This unique identity allows for precise references between
configurations and precise connections between data entities.

See <ref to ``_id`` restrictions> for more information on how to create
valid identifiers.

.. seealso::

  TODO

System _id
^^^^^^^^^^

The identity (``_id``) of a system must be unique within a Sesam node
instance.

Once a system configuration is saved, its identity cannot be changed. If
you need to change a system’s identity, you can Duplicate the system
configuration, save the duplicated configuration with the desired
identity, and then delete the original configuration.

Remember to also update any other configurations that were referencing
the original system to reference the new identity.

In the Sesam Management Studio, when you view the list of all systems in
the Systems menu, the System column will by default show you the
identity of all the defined systems in that Sesam node.

If the name property is also defined for a system configuration, then
the System column will show that value instead of the identity.

Regardless, if you need to reference a system configuration from another
configuration in Sesam, you reference the system’s identity.

.. seealso::

  :ref:`naming-conventions-1-1`,
  :ref:`systems`

Pipe _id
^^^^^^^^

The identity (``_id``) of a pipe must be unique within a Sesam node
instance.

Once a pipe configuration is saved, its identity cannot be changed. If
you need to change a pipe’s identity, you can Duplicate the pipe
configuration, save the duplicated configuration with the desired
identity, and then delete the original configuration.

In the Sesam Management Studio, when you view the list of all pipes in
the Pipes menu, the Pipe column will by default show you the identity of
all the defined pipes in that Sesam node.

If the name property is also defined for a pipe configuration, then the
Pipe column will show that value instead of the identity.

Regardless, if you need to reference a pipe configuration from another
configuration in Sesam, you reference the pipe’s identity.

.. seealso::

  :ref:`dtl-in-practice-3-1`,
  :ref:`naming-conventions-1-1`

.. _tc_dataset-id-3-1:

Dataset _id
^^^^^^^^^^^

The identity (``_id``) of a dataset must be unique within a Sesam node
instance.

By default, a dataset will have the same identity as the pipe it is
generated from.

You can override the default dataset identity by defining the dataset
property in the pipe’s sink configuration. (reference to sink config).

Once a dataset is generated, its identity cannot be changed. If you need
to change a dataset’s identity, you can edit the dataset property in the
pipe’s sink configuration, delete the sink dataset, and restart the
pipe. This will generate a new dataset with the new identity.

Remember to also update any other configurations that were referencing
the original dataset to reference the new identity.

In the Sesam Management Studio, when you view the list of all datasets
in the Datasets menu, the Dataset column will show you the identity of
all the datasets in that Sesam node.

If you need to reference a dataset from another configuration in Sesam,
you reference the dataset’s identity.

.. seealso::

  TODO

Entity _id
^^^^^^^^^^

The identity (``_id``) of an entity must be unique within the dataset in
which it resides. The identity of an entity is similar to a primary key
in a database table.

What makes an entity unique is usually dictated by the source system the
entity is imported from. This can typically be the primary key(s) of a
database table.

This means that you usually define the identity for entities in inbound
pipes.

If the source system has multiple properties that combined makes the
entity unique, you must combine all these properties into the ``_id``
property to ensure that uniqueness is preserved in Sesam.

In some cases, you can handle this in the source configuration part of
the inbound pipe. SQL sources, for example, allows you to specify
multiple columns from the source database as primary keys. Sesam will
then combine these columns automatically into the ``_id`` during import.

In other cases, you may have to explicitly add the ``_id`` property with
DTL in a transform step in the inbound pipe. This may be relevant when
the source configuration does not support specifying multiple properties
as primary keys.

.. seealso::

  TODO

Entity _id and namespaces
^^^^^^^^^^^^^^^^^^^^^^^^^

By default, the pipe identity of the pipe where the entity originates is
used as namespace for both the entity’s identifier and the entity’s
properties.

Note that there is a slight, but significant, difference in the
placement of the namespace for the entity’s ``_id`` property compared to
its other properties.

For the ``_id`` property, the namespace prefixes the property **value**:

.. code-block:: json

  "_id": "<namespace>:<value>"

For other properties, the namespace prefixes the property **name**:

.. code-block:: json

  "<namespace>:<property-name>": "<value>"

The reason the namespace is put into the value of the ``_id`` is to ensure
that all entities are unique across all source systems.

Example:

An entity imported from a system called `crm` with a `user` table
consisting of a primary key `userId` with value `123`, and a column
`email` with value `john.doe@foo.no` would look something like this:

.. code-block:: json

   {
     "_id": "crm-user:123",
     "crm-user:userId": "123",
     "crm-user:email": "john.doe@foo.com"
   }

Now imagine you have another source where one of the entities are also
identified by `123`.

Unless the namespace is part of the property value of ``_id``, both
entities would have the same ``_id``, namely `123`. So by prefixing this
value with a namespace we ensure that these entities do not come into
conflict with each other.

.. seealso::

  :ref:`namespaced-identifiers`,
  :ref:`namespaces`

The autogenerated property $ids
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Should probably write something sensible about the connection between
``_id`` and $ids somewhere. Maybe related to merge pipes? – ‘Yea, or maybe
add it to the \_ Properties chapter’ -G

.. seealso::

  TODO

.. _tc_dtl-in-practice-3-1:

DTL in practice
~~~~~~~~~~~~~~~

In this section you will learn how to:

- create a pipe from scratch
- view the output of a pipe
- write a greeting to the world with DTL

Create a new pipe
^^^^^^^^^^^^^^^^^

Let us start by creating a new pipe from scratch called ``practice``.
In the Sesam Management Studio, navigate to the **Pipes** view and follow these steps:

- Click the **New pipe** button
- Type in `practice` as the pipe's ``_id``
- In the **Templates** panel:

  - Choose Source System: ``system:sesam-node``
  - Choose Source Provider: ``embedded prototype``
  - Click the **Replace** button to put the chosen Source configuration into the pipe configuration area.
  - Click the **Add DTL transform** button to get a nice starting point to write DTL.

- Lastly, add some test data:

.. code-block:: json

   "entities": [{
     "_id": "1",
     "data": "One"
   }, {
     "_id": "2",
     "data": "Two"
   }]

You should now have the following pipe config:

.. _tc_practice-pipe-config-initial:
.. code-block:: json
  :caption: Practice pipe config - initial
  :linenos:

  {
    "_id": "practice",
    "type": "pipe",
    "source": {
      "type": "embedded",
      "entities": [{
        "_id": "1",
        "data": "One"
      }, {
        "_id": "2",
        "data": "Two"
      }]
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "_id"]
        ]
      }
    }
  }

Save and run the pipe by clicking the **Save** button and then the **Start** button.

In the next section you learn how to view the result of a pipe run.

.. seealso::

  TODO

Pipe output
^^^^^^^^^^^

To view the result of a pipe run, switch to the pipe's **Output** tab.
Here you will see two entities:

::

  practice:1
  practice:2

But they are both empty:

.. code-block:: json
  :linenos:

  {
  }

This is because we only copy the ``_id`` so far.

In the next section you will learn to write your first piece of DTL to make the output a bit more interesting.

.. seealso::

  TODO

Greet the world!
^^^^^^^^^^^^^^^^

Switch back to the **Config** tab.

First, change the ``copy`` so that all source properties are included.
Then add a property called ``greeting`` with the value `Hello, World!`:

Save and start the pipe again.

Switch to the **Output** tab to view the new results.

Now you will see that the output has changed:

.. code-block:: json
  :caption: ``practice:1``
  :linenos:

  {
    "practice:data": "One",
    "practice:greeting": "Hello, World!"
  }

.. code-block:: json
  :caption: ``practice:2``
  :linenos:

  {
    "practice:data": "Two",
    "practice:greeting": "Hello, World!"
  }

You have now learned how to create a new pipe from scratch using templates, write and edit DTL functions,
run a pipe and view it's output.

.. _tc_practice-pipe-config-final:
.. code-block:: json
  :caption: Practice pipe config - final
  :linenos:

  {
    "_id": "practice",
    "type": "pipe",
    "source": {
      "type": "embedded",
      "entities": [{
        "_id": "1",
        "data": "One"
      }, {
        "_id": "2",
        "data": "Two"
      }]
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["add", "greeting", "Hello, World!"]
        ]
      }
    }
  }


.. seealso::

  TODO

###.. _tc_pipe-interaction-with-systems.-2-1:###
.. _tc_systems-as-a-pipe-source-2-2:

Systems as a pipe source
~~~~~~~~~~~~~~~~~~~~~~~~

System configuration (mostly) defines the possibilities pipes have to
pull data.

We need to write about what a system is in the context of a pipe source,
with not only configs but explanations. Keep it simple don’t go into too
many system types (json & SQL?). Write more text than configurations,
draw stuff. (1-N)

.. seealso::

  TODO

.. _tc_how-to-create-a-system-with-templates-2-1:

How to create a system with Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. TODO:
.. We should consider having a consistent example case to build on throughtout these chapters.

.. sidebar:: Summary

  - From **Systems** view: Click **New system**
  - Fill in ``_id``
  - Click **Templates**
  - Choose **System type**
  - Click **Replace**
  - Fill in any remaining details

Let us create a new system from scratch called "`difi`".
In the Sesam Management Studio, navigate to the **Systems** view and follow these steps:

- Click the **New system** button
- Type in "`difi`" as the system's ``_id``
- In the **Templates** panel:

  - Choose System type: ``url prototype``
  - Click the **Replace** button to put the chosen system configuration into the system configuration area
  - Set ``url_pattern`` to "`https://ws.geonorge.no/kommuneinfo/v1/%s`"

You should now have the following system config:

.. _tc_practice-system-config-initial:
.. code-block:: json
  :caption: Practice system config - initial
  :linenos:

  {
    "_id": "difi",
    "type": "system:url",
    "url_pattern": "https://ws.geonorge.no/kommuneinfo/v1/%s",
    "verify_ssl": true
  }

.. note::

  The ``%s`` at the end of the ``url_pattern`` will be substituted by
  the relative url specified in the pipes using this system as a source or sink.

Save the system config by clicking the **Save** button.

You can check the connectivity status by clicking the **Status** tab.

.. seealso::

  Best Practices - Data modelling in Sesam: :ref:`best-practice-naming-conventions`

  Developer Guide - Service Configuration: :ref:`url_system`

  DTL - Beginner: :ref:`dtl-in-practice-3-1`


.. _tc_environment-variables-secrets-2-1:

Environment variables & Secrets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  - Environment variables and secrets are named values used to parameterize configs
  - Environment variables are:

    - unencrypted
    - referenced with: ``"$ENV(my-env-var)"``

  - Secrets are:

    - encrypted
    - referenced with: ``"$SECRET(my-secret)"``

  - Both are defined under **Datahub > Variables**
  - Secrets can also be defined under a system's **Secrets** tab
  - Eases and improves config maintenance

In this section we will cover how environment variables and secrets typically
are used in system configs.

Environment variables and secrets are named values
that can be used to parameterize Sesam configs.

Environment variables are stored and processed as *unencrypted* values,
and are referenced with ``"$ENV(my-env-var)"``.

Secrets are stored and processed as *encrypted* values,
and are referenced with ``"$SECRET(my-secret)"``.

Both are defined in the Sesam Management Studio under **Datahub > Variables**.

Secrets can also be defined locally in a system config under the system's
**Secrets** tab.

.. warning::

  If a system config is deleted, all secrets stored locally in that system config is lost!

It is generally a good idea to put the parts of a configuration that differ between
environments (develop, test, production, etc.) into environment variables.
This includes configs such as server names, database connection strings, API URLs, usernames, etc.

By putting these config parts into environment variables you can define each of them
separately in each Sesam node used for the respective environments,
but keep the actual system config identical in each node.

This is also practical for version control of the config.
You can change the values of the environment variables separate from the actual
system config.

Continuing from the example :ref:`practice-system-config-initial`, let us see how the
introduction of environment variables can improve the system config.
The ``url_pattern`` is a good canditate to be put into an environment variable.
Let us call it `"difi-api"` and reference it from the system config.

First we define the new environment variable under
**Datahub > Variables > Environment variables**:

.. code-block:: json

  "difi-api": "https://ws.geonorge.no/kommuneinfo/v1/%s"

Then we change the system config to reference it:

.. _tc_practice-system-config-env-var-ref:
.. code-block:: json
  :caption: Practice system config with environment variable reference
  :linenos:

  {
    "_id": "difi",
    "type": "system:url",
    "url_pattern": "$ENV(difi-api)",
    "verify_ssl": true
  }

Say we want to access different Difi APIs depending on which environment
we are accessing Difi from, or that Difi decided to change the API URL at some point.
The only thing that we have to update is the value of the ``difi-api``
environment variable.
No changes to the actual system config is required.

.. seealso::

  Concepts - Configuration: :ref:`concepts-environment-variables`

  Concepts - Configuration: :ref:`concepts-secrets`

.. _tc_categories-of-microservices-5-1:
.. _tc_microservices-beginner-5-1:

Microservices: Beginner
-----------------------


.. _tc_what-is-a-microservice-5-1:

What is a microservice?
~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Microservices are...

  - modular self-contained services
  - hosted as docker containers
  - configured and monitored as Sesam Systems

Microservices are modular self-contained software programs that provide a particular service.

In a Sesam perspective they can function as connectors to either pull data from a source system,
push data to a target system or transform data as part of a step inside a pipe.

Microservice code can essentially be written in any programming language, but in Sesam we usually
prefer Python 3.

Microservices are hosted in Sesam as docker containers. They are configured using
system configs and their logs can be inspected through the system's **Status** tab.

.. seealso::

  Getting started: :ref:`getting-started-microservices`

  Developer Guide > Service Configuration > Systems: :ref:`microservice_system`

.. _tc_why-use-microservices-in-sesam-5-1:

Why use Microservices in Sesam?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  When built-in connectors are insufficient, use microservices.

Most of the time you can use Sesam's build-in connectors to access
external systems, but sometimes you will find that you need to connect
to systems that are not natively supported by Sesam.

In these cases you either find an existing microservice and reuse it as is,
tweak it a bit to fit your needs, or simply write your own from scratch.

The Sesam communities at GitHub and DockerHub are great places to look
for microservices to reuse and tweak to your specific needs.

.. seealso::

  `Sesam's community at GitHub <https://github.com/sesam-community>`_

  `Sesam's community at DockerHub <https://hub.docker.com/u/sesamcommunity>`_

.. _tc_how-are-microservices-used-in-sesam-5-1:

How are Microservices used in Sesam?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Microservices in Sesam are:

  - defined in system configs
  - hosted in docker containers

To get a better understanding of how microservices are used in Sesam,
let us look at a concrete example.

Assume we want to pull data from SAP and that we have been provided
the following information about the SAP system:

- hosted at ``https://sap.service.com/api``
- data is exposed as OData
- username ``sap-user``
- password ``sap-very-secret-password``

Looking throught the list of Systems under :ref:`configuration`
we see that Sesam does not have a built-in connector for OData.
However we are in luck, browsing
`Sesam's community at GitHub <https://github.com/sesam-community>`_
we find there are several OData microservices to choose from.

.. TODO: get sap-odata-source into sesam-community!
.. Just using this MS now because of familiarity.

Let us go with the `sap-odata-source` microservice
(https://github.com/ga-hegsvold/sap-odata-source).

Reading up on the docs for this microservice we are provided with
information about where to find the docker image, which docker environment
variables to supply, and also examples of system and pipe configurations.

For this particular microservice there are two authentication alternatives:
"basic" with username and password or "token" with a JWT.
Since we have been supplied a username and password we go with the "basic" option.

Based on the information we now have, we can see that the microservice
requires the following docker environment variables:

`SERVICE_URL` - Base url to the Odata Service API

`AUTH_TYPE` - Authentication method ("basic" or "token")

`USERNAME` - Username to authenticate with the Odata Service

`PASSWORD` - Password to authenticate with the Odata Service

We also need to supply a link to the docker image for the microservice.

When setting up a new system config in Sesam it is a good idea to start with defining
the various Sesam environment variables and secrets needed.
This is to avoid awkward warnings and error messages as Sesam will warn you if there are references
to undefined environment variables and secrets in a system or pipe config.

`AUTH_TYPE` can be hardcoded in the system config as it will most likely be the
same in all Sesam environments (dev, test, prod, etc.).
The remaining docker environment variables will probably differ in the various
Sesam environments so these are good candidates to put into Sesam environment variables
or secrets.
We define these under **Datahub > Variables**:

.. code-block:: JSON

  "sap-service-url": "https://sap.service.com/api",
  "sap-username": "sap-username"

.. warning::
  Passwords and other sensitive values should never be put into Sesam environment variables
  as they are stored in plain text. Put them into secrets instead.

So let us put the SAP password in a secret called ``sap-password``.

With the Sesam environment variables and secrets defined, we can now create a new system config
for the SAP system. Let us call it `sap`:

.. code-block:: JSON
  :linenos:
  :emphasize-lines: 3, 11

  {
    "_id": "sap",
    "type": "system:microservice",
    "docker": {
      "environment": {
        "AUTH_TYPE": "basic",
        "PASSWORD": "$SECRET(sap-password)",
        "SERVICE_URL": "$ENV(sap-service-url)",
        "USERNAME": "$ENV(sap-username)"
      },
      "image": "gamh/sap-odata-source",
      "port": 5000
    },
    "verify_ssl": true
  }

Line 3 is where the system is defined as a microservice.

Line 11 is the reference to the docker image for the microservice.

When the system config is saved, Sesam will automatically try to
spin up a docker container, based on the referenced docker image, to host the microservice.
We will look more into this in the sections below.

.. seealso::

  .. Testing to add refs as bread crumbs with links in each step except first step.
  .. Is this reader-friendly or too much?

  Learn Sesam > :ref:`architecture-and-concepts_beginner-1-1` > :ref:`naming-conventions-1-1`

  Env.var / secrets naming convensions (Should add a section about this under Architecture & Concepts)

  Learn Sesam > :ref:`systems-beginner-2-1` > :ref:`how-to-create-a-system-with-templates-2-1`

  Learn Sesam > :ref:`systems-beginner-2-1` > :ref:`environment-variables-secrets-2-1`

  `OData (Open Data Protocol) <https://www.odata.org/>`_

.. _tc_microservice-hosting-5-1:

Microservice hosting
~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  - Microservice source code is hosted in `Sesam's community at GitHub <https://github.com/sesam-community>`_
  - Microserice docker images are hosted in `Sesam's community at DockerHub <https://hub.docker.com/u/sesamcommunity>`_
  - Auto-build scripts publish docker images to Sesam's community at DockerHub
  - `Sesam Community Guidelines <https://github.com/sesam-community/guidelines>`_

We have already touched on Sesam's communities at GitHub and DockerHub
to find available microservices. Let us take a more detailed look at how
microservice hosting is done with Sesam.

We have `Sesam's community at GitHub <https://github.com/sesam-community>`_
for hosting microservice source code,
and we have `Sesam's community at DockerHub <https://hub.docker.com/u/sesamcommunity>`_
for hosting microservice docker images.

When writing microservices we recommend putting the source code into
Sesam's community at GitHub so that it can be shared and reused in other projects
(unless there are specific restrictions in place).

By configuring the microservices using Sesam's auto-build script, when the
source code is pushed to GitHub, the script will automatically build a docker image
and publish it to Sesam's community at DockerHub.

From there the microservices will be available for use in any Sesam project.

See the `Sesam Community Guidelines <https://github.com/sesam-community/guidelines>`_
for more information on how to use the auto-build script and also how to contribute in general.

.. seealso::

  `Sesam's community at GitHub <https://github.com/sesam-community>`_

  `Sesam's community at DockerHub <https://hub.docker.com/u/sesamcommunity>`_

  `Sesam Community Guidelines <https://github.com/sesam-community/guidelines>`_

.. _tc_running-a-microservice-in-sesam-5-1:

Running a microservice in Sesam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Intro til Running I sesam

Forklare GUI

Pull & Restart

   Status

   Refresh

Forklare Config

Pipe source/sink/http

.. seealso::

  TODO



Introduction to some case.
--------------------------

Represent a case which the reader/participants need to work through.
The case can include multiple dataflows and in total needs to entail the following:

* Multiple input pipes for the same type entity/concept. These must be merged into a global.
* One or more input pipes for different entities/concepts which connect to the main entity/concept. This/these pipe(s) must go into a global which will be hopped to.
* An endpoint system which is interested in the data we retrieve, connect and enhance.
* Possibility to design a dataflow (AC)
* Possibility to code a dataflow  (Dev)
* Possibility to design a integration (AC)
* Planning for eventual consistency (AC)
* Possibility of defining golden-properties. (AC & Dev)
* Microservice usage (AC)
* Microservice creation (Dev)
* Incremental queries/api usage (AC & Dev)
* Creating CLI tests. (Dev)
* Creating mapping files. (AC & Dev)
* Emit children (AC & Dev)
*

Creating a system
-----------------

Some task to make a system.

Creating an input pipe
----------------------

Some task to make an input pipe reading from system created previously.

.. _tc_globals-as-a-concept-1-1:

Globals as a concept
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Why globals

Golden records

Gjør data tilgjengelig

Ref. 1.2.19, 3.2.14

.. seealso::

  TODO

.. _tc_joining-data-1-2:

Joining Data
~~~~~~~~~~~~

When working with data, you will often find yourself in situations where you need to join data. By joining data you get a comprehensive representation of a data object that has relations to other isolated data objects. In general, you join data because it gives you a more complete picture of a data object and its relation to other data objects. This allows you to work more efficiently and logically when you model your data towards a target state.

In Sesam you will also experience the need for joining data, and this is a functionality Sesam excels at. To outline the different possibilities when joining data, given the two data objects "foo" and "bar", the below example will be used. It draws upon the Sesam syntax and as such is something you will be using down the road. Here goes:

.. code-block:: json

	{
	  "_id": "foo",
	  "value": 1,
	  "values": [1, 2, 4, 5]
	}
	{
	  "_id": "bar",
	  "value": 1,
	  "values": [1, 3, 4, 6]
	}

There are four different kinds of joins. In the below outline, "eq" is an abreviation for equals and "foo.value" is to denote that you search in the "foo" data object in the key "value":

- One-to-one join: ["eq", "foo.value", "bar.value"]
- One-to-many: ["eq", "foo.value", "bar.values"]
- Many-to-one: ["eq", "foo.values", "bar.value"]
- Many-to-many: ["eq", "foo.values", "bar.values"]

The rule for joins is very simple: if any of the values overlap, then the join succeeds.

All of the four joins given above succeed for the two data objects given, because they all have overlapping values, i.e. the values 1 and 4.

.. seealso::

  TODO

.. _tc_full-outer-join-merge-1-2:

Full outer Join - Merge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full outer join is something you will experience in the Sesam terminology as a "merge". A merge, like the full outer join, retains all entries from i.e. two merged data objects. Graphically, a full outer join will look like the following:

.. figure:: ../../../training/010_architecture_and_concepts/media/Full_Outer_Join.png
   :align: center
   :alt: Figure – Full Outer Join

   Figure – Full Outer Join

A note on the handling of null values. In Sesam null values are not existing. Meaning, as opposed to a full outer join which will populate empty entries in the join between tables with null values, the merge in Sesam will by default never have to do this. To exemplify, look at the below example:

.. code-block:: json

	{
	  "_id": "first_entity:foo",
	  "first_entity:value": 1,
	  "first_entity:string":"Hello merge",
	  "first_entity:values": [1, 2, 4, 5]
	}
	{
	  "_id": "second_entity:bar",
	  "second_entity:value": 1,
	  "second_entity:string":"This is retained",
	  "second_entity:values": [1, 3, 4, 6]
	}

and the merged result, if we choose to retain the first "_id" of the above two data objects and join the data on the value property:

.. code-block:: json

	{
	  "_id": "first_entity:foo",
	  "first_entity:value": 1,
	  "first_entity:string":"Hello merge",
	  "first_entity:values": [1, 2, 4, 5],
	  "second_entity:value": 1,
	  "second_entity:string":"This is retained",
	  "second_entity:values": [1, 3, 4, 6],
	  "$ids": [
	    "~:first_entity:foo",
	    "~:second_entity:bar"
	  ]
	}

What should immediately get your attention would be the "$ids" property in the merged result. Sesam utilizes this property to keep track of which "_id"s have been merged and as such aids in data governance, as you do your data modelling.

.. seealso::

  TODO


THIS IS WHERE THE PATHS DIVERGE
-------------------------------

From here on out we will give different tasks and go into different depth
for the topics we bring up based on who is taking the course.

Most topics will be covered for both participant groups, but the perspective
shown and tasks given will be different.

For the context of this document I will annotate where AC(architect) and devs
differ for each topic.

DEV
---

.. _tc_merge-as-a-source-3-2:

Merge as a Source
~~~~~~~~~~~~~~~~~

Show config, explain all properties, refer to architecture chapter also.

-  Strategy

-  Identidy - \_id etter merge

-  datasets

.. _tc_merge-as-a-source-3-2-summary:

Summary
^^^^^^^



DEV & AC
--------

.. _tc_global-1-2:

Global
~~~~~~

Global datasets lie at the heart of a well managed Sesam architecture. They are created by global pipes and often consist of aggregated data from several different sources enabling a higher level of semantic structure to a Sesam node. A global dataset is your "one place to go" to find all the data related to a specific concept.

Creating global datasets allows you to:

- 	Semantically group and structure data
		A semantic grouping of the data makes the data itself easier to understand and more intuitive to work with, both in terms of existing architectures and new projects. For existing architectures, separating your data into relatable and recognizable structures allows for more efficient support and error handling. To have all raw source data related to a concept (ie. customer data) directly upstream from a pipe substantially decreases the time you need to localize and to correct a potential issue. 
		Semantic grouping also makes your Sesam architecture more scalable and results in fewer active connections over time.   

-	Setup master data management - Golden records
		One effect of global datasets is the ability to perform active master data management through setting golden records. Golden records are where Sesam architectures may localize and prioritize their master data in order to create a flexible system-wide model. Through golden records you may prioritize which system knows a specific type of data best, which system knows it second best and so on. By ordering systems based on their quality of data for a specific data type Sesam may ensure the highest quality of data possible. Another benefit of golden records are their reusability. Once their logic has been created a golden record may be used by any project downstream from its global dataset, thus saving both time and energy.

		Golden records are created with the ``["coalesce"]`` function, as shown in the example below.



	A global pipe, ``global-person``, has three source datasets, crm-person, hr-person and economy-person. The crm-person dataset has high quality work experience data and medium quality hours logged data. The hr-person dataset has high quality personal information and the economy-person dataset has high quality hours logged data. In our global pipe ``global-person`` we wish to set 3 golden records: email, weekly-hours-billed and hours-pr-project. By using the "coalesce" function we may specify which source dataset has the master data for which specific variable.

	For example we might assume that hr-person should be master for "email", crm-person should be master for "hours-pr-project" and economy-person should be master for weeky-hours-billed. This may be setup by the following logic:

.. code-block:: json
  :linenos:

  ["add", "email",
    ["coalesce",
      ["list", "_S.hr-person:email", "_S.crm-person:Email", "_S.economy-person:e-mail"]
    ]
  ]

In this case, all three source datasets have an email property. If the email property from hr-person is not null it will be used for our global property. If it is null then the Email property from crm-person will be evaluated, and so on. 

.. code-block:: json
  :linenos:	

  ["add", "hours-pr-project",
    ["coalesce",
      ["list", "_S.crm-person:hours-pr-project", "_S.economy-person:hours-pr-project"]
  ]


  ["add", "weekly-hours-billed",
    ["coalesce",
      ["list", "_S.economy-person:weekly-hours-billed", "_S.crm-person:weekly-hours-billed"]
    ]
  ] 

The dataset hr-person does not contain any data regarding "hours-pr-project" or "weekly-hours-billed" and can therefore be left out of the prioritations. 
The dataset hr-person does not contain any data regarding "hours-pr-project" or "weekly-hours-billed" and can therefore be left out of the prioritizations.


.. seealso::

  TODO


Creating a global pipe
----------------------

Task to make a global pipe.
Devs will get the design (pipes to include and eq) and create the config.
Architects pick attributes to join on and get the config.

Important that only 1 answer for the eq produces the output we want - ikke no slingringsrom.

DEV & AC
--------

.. _tc_guidelines-inbound-and-outbound-pipes-1-2:

Guidelines - inbound and outbound pipes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As established above, an important aspect when modelling data in Sesam is the use of globals. Albeit before reaching the global stage and after completion of the global stage, when modelling your data the following guidelines apply:

Inbound pipes
^^^^^^^^^^^^^

As data enters Sesam it is handled in inbound pipes. An inbound pipe should be as generic as possible with regards to the amount of shaping done on the data that flows through to its dataset. The reason being, in order for you to make the best possible modelling decisions downstream, you should look at the "raw" data first to get a complete understanding of the condition of the data. In addition, we want to assume as little as possible about how the data will be used by current and future recipients. Therefore,
if we start shaping and customizing data too soon in the flow, it's much harder, if not impossible, to reuse the data for different purposes later. A rule of thumb is therefore to minimize the amount of DTL used in an inbound pipe and try to just copy everything, or close to everything. Special cases can occur when you need to do some shaping of the data before reaching the global stage. In such cases, you should aim at making the minimal required DTL changes in order for the data to retain as much of its original integrity as possible.

Outbound pipes
^^^^^^^^^^^^^^

Following the flow of data as it leaves the global stage of modelling, the amount of DTL will increase in the preparation pipes. As you might recall, preparation pipes deliver data to the outbound pipes. It is therefore important to consider the state of the data as it enters an outbound pipe. The reason for this being, as with any inbound pipe, that you should aim at minimizing the amount of DTL needed to shape your data further. This will create robust consumable data that can be delivered seamlessly to your target systems as data flows through your outbound pipes. As with inbound pipes, special cases can occur, where you need to do some additional shaping before the data can be presented in a consumable shape for a given target system. Again, aim at making a minimal set of DTL changes.

Summary
^^^^^^^

The amount of DTL in a given pipe with respect to modelling stage in Sesam should increase until the point of modelling stage, where the intent of shaping data is primarily due to target system requirements, as visualized in the below *Figure - DTL Amount*.

.. figure:: ../../../training/010_architecture_and_concepts/media/dtl-amount.png
   :align: center

   Figure – DTL Amount


.. seealso::

  TODO

.. _tc_change-tracking-data-delta-1-2:

Change tracking & data delta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Change tracking and data delta allows Sesam to process and update data only when it changes. This ensures minimal latency and increased agility both when importing data from source systems and when processing data through internal pipes towards target systems.

Firstly, when reading data from a source system, if supported by the source, it may be possible to just ask for the data that have changed since the last time. This mechanism uses entries from the source, such as a last updated time stamp, to ensure that only data that have been created, deleted or modified are processed. 

Secondly, the first time data flows through a pipe in Sesam that pipe's dataset will be created. Datasets consist of entities and on each entity a ``_hash`` property will be created. This ``_hash`` property enables change tracking and data delta when data enters or flows through Sesam. When an entity's ``_hash`` value changes, any downstream pipes register this change and recognizes it as a new sequence number that needs to be processed again.

.. seealso::

  :ref:`entity_data_model`,	:ref:`concepts-datasets`, :ref:`concepts-change-tracking`

  Developer Guide > Entity Data Model > Reserved fields: :ref:`entity_data_model`

.. seealso::

  TODO


Creating a preparation pipe
---------------------------

DEV & AC
--------

Dev får info om funksjonaliteten, men fokuserer mer på configen
AC fokuserer mer på funksjonaliteten, men blir vist konfig & output.

.. _tc_left-join-hops-1-2:

Left Join - Hops
~~~~~~~~~~~~~~~~

In addition to a full outer join it is also relevant to talk about the left join. This is because you in the Sesam terminology will use something we call "hops". The hops is similar to a left join, in that it appends data and returns data even if there are no matches for a particular entry in the join. As such, in cases where you append data, null values in Sesam are retained. A graphical representation of the left join can be viewed in the below figure:

.. figure:: ../../../training/010_architecture_and_concepts/media/Left_Join.png
   :align: center
   :alt: Figure – Left Join

   Figure – Left Join

To illustrate the graphical representation of a left join, the following practical example has been drafted:

.. code-block:: json

	{
	  "_id": "first_entity:foo",
	  "first_entity:value": 1,
	  "first_entity:string":"Hello merge",
	  "first_entity:values": [1, 2, 4, 5]
	}
	{
	  "_id": "second_entity:bar",
	  "second_entity:value": 1,
	  "second_entity:string":"This is retained",
	  "second_entity:values": [1, 3, 4, 6]
	}
	{
	  "_id": "third_entity:the_runt",
	  "third_entity:value": 1,
	  "third_entity:string":"Third's the charm"
	}

When applying the hops, our point of reference will be the first data object from the above and we will name the new property "left_join_result". We will choose to join the data on the "value" property present in all of the above three data objects in order to return the "values" property. Albeit, the "values" property is only present on the first two data objects. The expected result can be seen below:

.. code-block:: json

  {
    "_id": "first_entity:foo",
    "first_entity:value": 1,
    "first_entity:string":"Hello merge",
    "first_entity:values": [1, 2, 4, 5],
    "first_entity:left_join_result": [{"second_entity:values": [1, 3, 4, 6], null}]
  }

As stated earlier, it is important to note that in this case, null values will be returned if the hops is not possible between individual data objects, which can be seen in the new property "left_join_result", where the last entry is null.

.. seealso::

  TODO

.. _tc_hops-3-2:

Hops
~~~~

Basics, uten apply

.. seealso::

  TODO


Hopping with a preparation pipe
-------------------------------

A new preparation pipe which hops, reads from same global.
Uses some of the same values as the opther prep pipe but not 100% match.

Architects create the mapping and get almost the whole pipe config.
For example let them add all the "_S.someattribute" but have everything else ready

Devs create the pipe config and get the mapping.

The value of golden properties can now be understood as we have re-done mapping
twice.


Prioritization of data sources
------------------------------

FUN IDEA FOR A COURSE ONLY THING.
Course teachers act as DBA's / People responsible for two different systems.
We don't know anything about eachothers systems but know everything about our own.
The course participants must ask questions to us one at a time regarding what data
we care about, what data gets updated by our system and where the data we hold come from.

Then the participants must make real decisions when it comes to prioritizing
the origin of golden attributes based on the information we have provided.

No wrong answers as long as justification is good - possibility of showing how
easy it can be to interpret things differently.

Maybe let the DBA's talk to eachother after the participants have answered (?)

.. _tc_coalesce-3-2:

Coalesce
~~~~~~~~

ref 1.2.19

.. seealso::

  TODO


Defining golden properties
--------------------------

Devs use the information above to code the coalesce's.
Architects use the information above to define the mapping and prioritization.

Using a microservice in prep pipe
---------------------------------

Dev, koder microservice eller bare bruker den?
AC går i dybden på hvorfor en microservice er en god løsning og ikke innebygd
sesam funksjon.

HVOR FETT HADDE DET VÆRT OM VI KJØRTE AC & DEV KURS SAMTIDIG
------------------------------------------------------------

AC gjør all design også kommer dev etterpå og implementerer det.
2 instruktører og 2 rom, som møtes for å gjøre oppgaver.
Perfekt mulighet for naturlig overførsel av informasjon fra arkitektur siden
til dev siden.
?????????? :D
