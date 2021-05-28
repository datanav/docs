.. _architecture-and-concepts_beginner-1-1:

Architecture and Concepts: Beginner
-----------------------------------

.. _different-types-of-architectures-1-1:

Different types of Architectures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When modelling data, integration architectures lay the foundation
for shaping and structuring data as it moves from one system
to another. Within integration architectures the Point-to-Point (P2P) and Enterprise Service Bus
(ESB) architectures have been used extensively. Recently Data-Driven Architecture (DDA) has
enabled data to be used in new ways by focusing on data and its meaning.

To show the evolution of integration architectures and why DDA is the natural step
forward we will first introduce you to P2P and ESB.

.. _point-to-point-1-1:

Point-to-Point (P2P)
^^^^^^^^^^^^^^^^^^^^

This kind of integration architecture is the simplest integration principle and works well
when the number of related systems are limited and low latency is key.
As an example of P2P imagine sending a message generated in one system A to a single receiver
in another system B. System A talks to system B.
It is simple and therefore easy to manage, however what if another system C is
introduced and needs to talk with both system A and system B?
Introducing system C will increase the complexity of the architecture threefold
as we go from one integration between system A and system B, A to B,
to three integrations A to B, A to C and B to C.
In this case P2P may not be your best option as the issue of
scalability starts to present itself.

To illustrate how complexity can make P2P a
non-viable option look at the below Figure 1 – Point-to-Point:

.. figure:: ./media/Point_to_Point.png
   :align: center

   Figure 1 – Point-to-Point


As illustrated on the right-hand side of the above figure “Complex
integration”, you have to maintain multiple connections separately
which can make P2P time consuming and expensive to manage.
Therefore, amongst other things, new architectural principles
have been developed. One of the more prominent ones being the ESB.

Enterprise Service Bus (ESB)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ESB is a more robust integration architecture and plays the critical role of
being the hub where you can connect diverse systems and services in a Service Oriented Architecture (SOA).
The ESB takes on the responsibility of ensuring that data sent from one
system conforms to the requirements in another system by way of a message queue.
This core functionality is an important feature as to why the ESB is such an
established integration architecture. In addition, the ESB aids in
simplifying integration efforts when connecting differing applications
that need to communicate with each other as shown below in Figure 2 – Enterprise
Service Bus.

.. figure:: ./media/Enterprise_Service_Bus.png
   :align: center
   :alt: Figure 2 – Enterprise Service Bus

   Figure 2 – Enterprise Service Bus

Taking into account the positives from using an ESB for your integration architecture - some
challenges still remain unresolved. In recent years the transition towards more
cloud-based solutions, hybrid solutions and the remaining tendency to
focus on the systems in the ESB rather than the data itself has
propelled what is called DDA.

Data-Driven Architecture (DDA)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As opposed to both the P2P and the ESB integration architectures the DDA
does not focus on systems but rather the data these systems store and how
it can be used in a data-centric ecosystem.
This gives us an agile and robust integration architecture.
See Figure 3 – Data-Driven Architecture.

.. figure:: ./media/Data_Driven_Architecture.png
   :align: center
   :alt: Figure 3 – Data_Driven_Architecture

   Figure 3 – Data-Driven Architecture

As opposed to P2P and ESB, DDA is, respectively, scalable and agile - in
that it does not need the “Bus” to orchestrate data flows, rather DDA
relies on retrieving and storing all the data from a system for the purpose of
connecting it internally to enhance and propagate it for usage in outbound flows.

As in all great things there are risks involved.
In order to utilise DDA effectively you need logical and robust principles
to create flexible data flows and models.
This can be achieved by always thinking ahead and leaving room for growth,
which you will learn how to do throughout this course.

.. _datahub-1-1:

Datahub
~~~~~~~

Continuing along the path of building data-centric solutions, the term
"datahub" comes into play. A datahub is recognized by its frictionless
data flow and builds upon the architectural principles presented
in DDA such as storing data. A datahub can be described as a solution that consists of
and relates to multiple different technologies, i.e., a data warehouse, microservices,
databases etc.

A datahub shares data by connecting providers of data with consumers of
data. As such, a datahub mediates and manages how data flows between systems
and makes states of data visible to consumers outside the datahub.

In a sense, you could say that a datahub is a digital representation of
an enterprise and also what Sesam often becomes when it is used
properly. As with any other technologies there are pros and cons.
Some of these are listed below, so you might be able to recognize them
down the road.

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

- Moves data asynchronously.

#Todo Snakke om hvorfor Synchrounousity er pro & con.

Synchronousity and pizza - NOT HOME HERE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Synchronousity

Synchronousity is when an action or request is dependent on a response or reply.

Example:

Imagine having to pay for a pizza delivery in cash.
The delivery person is dependent on receiving cash from you before providing the pizza.

The upside for you is that you can pay in cash and the delivery person knows that you
have confirmed the receivment of the pizza. The downside here is that the delivery person
is dependent on you to come and take the pizza before moving on to other customers.
And the pizza may become cold if you are slow.



Asynchronousity

Asynchronousity is when an action or request is not dependent on a response or reply.

Example:

Imagine now that you have already paid for the pizza which is on it's way to your door.
The delivery person is not dependent on meeting you to provide the pizza, but can
leave it outside your door and notifying you by SMS.

The upside here is that the delivery person is not dependent on a response from you,
but the downside is that if you do not see the notification you may very well go
get the pizza when it has become cold.

.. _sesam_world_map-1-1:

Sesam world map
~~~~~~~~~~~~~~~


.. _the_parts_of_sesam-1-1:

The parts of sesam
~~~~~~~~~~~~~~~~~~

In order to understand Sesam, it is important to understand
the following three central concepts:

- Systems
- Pipes
- Datasets

Systems:
   A system's main feature is to act as the interface to import and export data
   into and out of a Sesam node. The actual import and export is carried out by
   the pipes connected to the systems. Systems are therefore usually found in the
   beginning and end of dataflows, and are often referred to as
   “source systems” or “target systems” respectively. A system could
   connect directly to a database, to a REST API, or simply send data to
   a waiting http endpoint.
   Sesam has several of these system types built
   into the product to simplify the workings inside the portal. In
   situations where the built-in system types are not enough for your
   requirements Sesam also supports hosting custom code in microservice systems.
   These microservices can in turn manipulate and delegate data according to your own
   specifications, making Sesam a very robust and comprehensive product.

Pipes:
   A pipe's main functions are to move and transform data.
   Transformation of data is done through Sesam’s own
   Data Transformation Language (DTL) which allows you to
   add, remove, transform or connect data according to your needs.
   A pipe generally reads from or writes to a system or dataset depending
   on where the pipe is located in the dataflow.

Datasets:
   A dataset's main function is to store data and track changes.
   Datasets are Sesam’s storage units and can be compared
   to i.e., a table in an SQL database. Datasets are where the pipes store the
   data they produce, unless a sink specifies otherwise.
   Sesam stores data in order to perform tracking and indexing in addition
   to acting as a smart cache for the source systems' data.
   A dataset is only updated when data changes.
   You will learn more about these functionalities later in this book.

Entities:
   A dataset consists of a list of entities.
   An entity is a JSON dictionary with the identifying key ``_id``.
   Entities in Sesam can be compared to individual rows in a table and can
   represent anything from a person or a mechanical part to a contract.

|

.. figure:: ./media/Architecture_Beginner_Systems_pipes_datasets_A.png
   :align: center
   :width: 800px
   :height: 80px
   :alt: A general pipeline flow in Sesam depicting the three central parts of a Sesam integration, systems, pipes and datasets. The arrows symbolize the direction of data flow.

   *A general dataflow in Sesam depicting the three central parts of a
   Sesam integration, systems, pipes and datasets. The arrows symbolize
   the direction of data flow.*

|


#TODO SKIPPER REVIEW FOR NÅ PGA ÅPEN PR

.. _the_sesam_portal-1-1:

The Sesam portal
~~~~~~~~~~~~~~~~

Show basics of portal

(Here also refer to a full chapter for portal or from the projects
chapter?)

Integrations, connections and configurations can be accessed inside
the Sesam portal; the user interface of the Sesam product. The Sesam
portal can be accessed at https://portal.sesam.io, and in this section you will
learn the most commonly used parts of the portal so that you can
orient yourself as well as manage existing integrations. For a full
explanation of the workings and functionality of the Sesam portal,
please see :ref:`sesam-management-studio`.

When logging into the portal you will be met with a page like figure "The Sesam Portal"

.. figure:: ./media/Architecture_Beginner_The_Sesam_Portal_A.png
   :align: center
   :alt: The Sesam Portal

   The Sesam Portal


The cards on the Dashboard are often referred to as “subscriptions” or
“nodes” and they represent separate instances of Sesam installations.
Each node comes in different sizes depending on the
requirements of the customer, project or user. In this example you will be
shown the portal inside the node called “Training Node”.
All nodes have the same interface.

When entering the “Training Node” you will be met with the page seen in
figure :ref:`figure_Training_Node_Landing_Page`

.. _figure_Training_Node_Landing_Page:

.. figure:: ./media/Architecture_Beginner_The_Sesam_Portal_B.png
   :align: center
   :alt: Training Node Landing Page

   Training Node Landing Page

In this section we will only focus on the specific parts of the portal
needed to start working with Sesam, namely the “Pipes” page and the
“Systems” page.

Pipes
^^^^^

When entering the “Pipes” page you will be met by figure
:ref:`figure_Training_Node_Landing_Page`. This
figure shows you all the available pipes in your node as well as
some of their corresponding metadata. There are also several search and
filter options available, which are especially handy when trying to
locate one or a set of pipes in a node with many pipes.


.. _figure_Training_Node_Landing_Page:

.. figure:: ./media/Architecture_Beginner_The_Sesam_Portal_C.png
   :align: center
   :alt: Sesam Node Pipe overview

   Sesam Node Pipe overview


If you now enter the pipe called “person-cmm” we can look into more of
details regarding how you may use the portal to navigate, troubleshoot
and configure you pipes.

Upon entering a pipe, you will by default be sent to the pipe’s “Graph”
view, as seen in figure 1.1.6D.

.. figure:: ./media/Architecture_Beginner_The_Sesam_Portal_D.png
   :align: center
   :alt: Pipe Graph view

   Pipe Graph view

The graph view shows you which pipes are upstream and downstream to the
specific pipe you have selected, and it also shows connections to
related pipes (you will learn more about connected pipes later [link
maybe?]). For now, we will focus on four of the pipe’s subpages: Config,
Input, Output and the Execution log.

-  **Config**: The config subpage is where the actual coding takes
   place. This is where you define what this specific pipe is supposed
   to do. A pipe config is written in DTL which you will learn more
   about in section [link]. One

-  **Input**: Whenever a pipe uses one or several datasets as a source,
   the source entities will be displayed here. These are the entities
   the pipe will perform some sort of transformation on.

-  **Output**: The output tab shows the entities after the DTL
   transformation. The way you see the output depends on whether the
   data is stored in a dataset or sent to a target system. There are
   some occasions where there is no output so be seen but for now you
   can assume that there will always be an output to be see for each
   pipe.

-  **Execution log**: The execution log supplies us with information on
   the state of the pipe. If a pipe runs as it should the execution log
   will display information on how many entities it has processed, how
   much time the processing took and much more. If a pipe is not be able
   to process all the data, the execution log will display a failed pipe
   run as well as error messages which may assist you to locate the
   error. The execution log is a vital tool for troubleshooting as it
   not only tells you if a pipe works as it should, but also contains
   detailed information on why a pipe run fails and when they failed.

Systems
^^^^^^^

The systems tab looks very much like the pipe tab in figure 1.1.6C. For
systems we will focus the three most commonly used tabs: Config, Secrets
and Status.

-  **Config**: Like with pipes, the config tab is where you specify what
   the system is supposed to do. There are many different types of
   systems and many of have very different configuration. There are
   however some common traits that apply to most system. These traits
   include authorization parameters, location parameters such as
   IP-addresses, URLs and database names and system types. In the case
   where your system relies on a Microservice you might also have a set
   of environmental variables used by the Microservice.

-  **Secrets**: In the Secrets tab you may store sensitive information
   you do not wish everyone on the node to have access to. These secrets
   are often passwords or token used to authorization and
   authentication. Secrets stored in the system tabs are local secrets
   and may only be used by the specific system in which they are
   defined.

-  **Status**: In the Status tab you can monitor the health of your
   system. When connected to built-in systems this tab shows you whether
   you are connected correctly. When connected to Microservices this tab
   displays connection status and logging provided by the Microservice.


.. _working-language-json-1-1:

Working language JSON
~~~~~~~~~~~~~~~~~~~~~

Something general about JSON

JSON configuration of pipes and systems

DTL also validated as JSON?


.. _naming-conventions-1-1:

Naming conventions
~~~~~~~~~~~~~~~~~~

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
there is a clear and intuitive way of tracking their content.
We use the hr system mentioned above in this example.
There are two tables we would like to read from the hr systems: employee and
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

.. figure:: ./media/Architecture_Beginner_Pipes_A.png
   :align: center
   :width: 835px
   :height: 105px
   :alt: Full pipe flow with generic names.

   Full pipe flow with generic names.

|

.. figure:: ./media/Architecture_Beginner_Pipes_B.png
   :width: 800px
   :height: 100px
   :align: center
   :alt: Example of Full pipe flow with globals.

   Full pipe flow with example names.

.. _systems-1-1:

Systems
~~~~~~~

Short about systems (where in the sesam-world-map)

Something more general about pipes maybe in context of pipes and
datasets

Very low level but enough to set up an inputpipe after maybe?

and refer to systems chapter

Namegivingconventions ref. 1.1.8

Where to make new ref 1.1.6

Systems are one of Sesam’s core sub-structures. Systems can connect to
external providers such as an SQL database, a REST API or a Microservice
to either import or export data to and from Sesam and are therefore the
start and finish points of every integration flow. System may cover
other functionalities as well, but we will cover those special cases in
later parts [ref to later parts].

.. _pipes-1-1:

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


.. _datasets-1-1:

Datasets
~~~~~~~~

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

**Related topics:**

:ref:`dataset-id-3-1`,
:ref:`entities-json-keyvalpairs-1-1`,
:ref:`naming-conventions-1-1`,
:ref:`pipes-1-1`


.. _datasets-vs-tables-1-1:

Datasets vs. tables
~~~~~~~~~~~~~~~~~~~

Examples end ref to 1.1.13

.. _entities-json-keyvalpairs-1-1:

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


.. _globals-as-a-concept-1-1:

Globals as a concept
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Why globals

Golden records

Gjør data tilgjengelig

Ref. 1.2.19, 3.2.14

.. _special-sesam-attributes-1-1:

Special sesam attributes
~~~~~~~~~~~~~~~~~~~~~~~~

Namespaces
^^^^^^^^^^
Namespaces in Sesam are primarily used on properties, and its main functions are to ensure uniqueness across sources and to maintain the origin of the properties. "global-person:fullname" is an example of a namespaced property, where "global-person" is the namespace and "fullname" is the property name.

Namespaced identifiers (NIs) are identifiers (i.e. property values) given a namespace.
"source:reference": "~:foo:bar" is an example of a NI, where "source" is the property namespace, "reference" is the property name, "foo" is the namespace of the referenced data and "bar" is the identifier usually matching an identifier in the referenced data. The "~" is the Sesam syntax for defining a datatype as a NI.

As such, NIs in Sesam are similar to foreign keys in databases in that NIs are a visual indication of how data is connected, and enables easier and more precise joins. However, Sesam does not enforce any relationship between NIs and the referenced properties. You use the functions ["make-ni"] or ["ni"] to create NIs when modelling data in Sesam.

Rdf:type
^^^^^^^^
The RDF type is metadata used to relate data and give some semantic context. When used with a namespace, it keeps track of the origin of the data, as well as the business type. It is composed upon input and will be used to relate and filter like you would use a foreign key.

Using the above NI "~:foo:bar", an RDF type defined property in Sesam could look like the following: ``{"rdf:type": "~:foo:bar"}.``

\_id
^^^^
The identity (_id) of systems, pipes and datasets must be unique and consistent as data moves
via systems, through pipes and into datasets.

The _id of a system is usually defined by the name of your source system i.e., salesforce. In case you need two systems in Sesam that both originate from salesforce, you'll need to make two unique names for each of these i.e., salesforce and salesforce-rest.

For pipes, the _id is typically defined by establishing which properties in the pipe´s dataset are unique across its entities. This could typically be primary key(s) when data is imported from a database or potentially a unique property or even concatenated properties when data is imported from an API.

When data reaches a pipe's dataset, the _id will be identical to what you defined the _id to be, in that pipe's config.


.. _tasks-for-architecture-and-concepts-beginner-1-1:

Tasks for Architecture and Concepts: Beginner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. *What are the main types of integration architectures?*

#. *What type of integration architecture does Sesam support?*

#. *What are the main components in Sesam?*

#. *Which component gives Sesam access to the outside world?*

#. *In what component is data stored in Sesam?*

#. *Which component moves data in Sesam?*

#. *What is the relationship between JSON and Sesam entities?*

#. *What is the difference between a JSON dictionary and an entity in Sesam?*

#. *What moves through Sesam?*

#. *Based on naming conventions: Name the input pipe for this system & table:*

     System name: ``IFS``

     Table name: ``WorkOrder``

     Pipe name: ______

#: *Name the global pipe which merges these three input pipes:*

     ``cab-person``, ``salesforce-user``, ``ifs-employee``.

     Global name: ``global-_____``

#. *In an entity representing a row, how would the column “personalid”
   with row value “123” look after it is read by a pipe named crm-person
   and stored inside an entity of the output dataset?*

#. *What is the difference between and entity stored as a row in a table
   vs in a Sesam Dataset?*
