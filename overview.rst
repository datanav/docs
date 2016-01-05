========
Overview
========

Introduction
============

Sesam is a general purpose data integration and processing platform. It is optimised for collecting data from source systems, transforming that data and delivering it to target systems. What makes Sesam special is its ability to track and process only data that has changed, and its powerful data query and construction language.


Installation
============

Sesam is offered as a cloud service and can also be installed locally. Local installations are managed by Sesam but run on client hardware.

The Sesam service is run as either a single Sesam Node or as a cluster of Sesam nodes. Each node has the capability to collect, transform and deliver data. However, various topologies of nodes can be used to separate concerns where needed. A cluster of Sesam Nodes can be managed by a master node or accessed directly. All nodes expose the Sesam API as way to control and introspect the node. When used in a cluster the master node exposes a common API across all worker nodes.

::

  docker pull sesam/sesam-node

Running Sesam
=============

::

  docker run sesam/sesam-node

Concepts
========

Sesam is a collector, manipulator and producer of data. It collects raw data from source systems and stores it in a datahub in the form of datasets. Data Transformations can then be defined and executed to construct new datasets. Data from these datasets is then exposed and delivered to external systems.

IMAGE - collect, connect and share.

Sesam produces and consumes streams of data. Each stream contains a number of data entities each of whom consists of a number of key / property values and a special property called "_id".

Components called data sources expose data from source systems such as REST APIs and Relational Databases. DataSync tasks run on regular intervals to pull data from a provider and push it to a sink. Datahub sinks write the entities to datasets. A dataset is a log of entities supported by indexes for random access.

Datasets also act as data sources. They can expose the data they contain. However, a more common usage is to transform the data from a dataset into a new shape or representation. This is done using the Data Transformation Language (DTL). The DTL is optimised for ease of use in stream and graph processing and the construction of new data entities. DTL transformations can use data from many datasets to construct new entities.

The results of applying a DTL transformation is a new stream of entities. These are exposed using a source and, like any other stream of entities, can be consumed into a sink. These sinks can either be another dataset sink or it can be a sink that connects to an external system. External systems can be databases, APIs, message queues, etc.

These concepts are explored in more detail in the following sections.

A Sesam Node
============

A Sesam Node is a running process that is capable of hosting instances of the components described below. In addition, each node instance exposes an API and a user interface. Nodes can be organised into clusters with one node acting as the master. In the case of a cluster the API and user interface is exposed from the Master node.

Sesam Node Config
=================

Each Sesam Node has a configuration file or files that describe the set of components that should be instantiated and run by the node. These files are themselves just a serialised set of data entities. Each entity is the configuration for one component. Any changes to the file will result in a component being reconfigured but only if the data for actual component changes.

By convention the config file is called node-config.json and is found in the root folder for the node. (ed - too much detail)

Data Sources
============

A Data Source (source) is a component hosted in the Sesam Node that exposes a stream of entities. Typically, this stream of entities will be the rows of data in a relational database table, the rows in a CSV file, or data from an API.

The source component offers an object called a Data Source Reader which has one capability which is 'getEntities'. This 'reader' object is immune to changes to the configuration of its parent source during its lifetime.

The 'getEntities' method can take an additional parameter that is an 'offset' token. This token can be used to only fetch the entities that have changed *since* that given offset. An offset is a opaque token that may take any form; it is interpreted
by the data source only. For example; for a relational data source it might be a datestamp or for a log based source it might be an index.

Each entity returned by a data source reader is a dictionary that maps keys to values. Values can be simple literals such as string, int, long, etc. They can also be lists or child entities. They can even be lists of entities. There are just three special or reserved keys within an entity, and they are; "_id", "_updated" and "_deleted". [TODO: all keys starting with '_' are reserved - grove] It is a requirement that every entity exposed by a provider has an "_id" property. This identifier should be unique within the set of entities being exposed by that source, but need not be globally unique across all entities.

Sesam offers a number of core built-in data sources but it is also easy for developers to expose a micro service that can supply data from a remote service. The built-in remote data source is able to consume data from these endpoints.

Entity Data Model
=================

Sesam uses an entity data model as the core representation of data. Each entity is a dictionary of key-value pairs. Each key is a string and the value can be either a literal value, a list or another dictionary.

A Sesam entity has a few special keys that should not be messed with. The following data prototype explains these special properties.

::

  {
  	"_id": "the id of the entity. required on all entities.",
  	"_updated": "a token indicating when this was modified",
  	"_deleted": "indicating if the entity should be treated as deleted"
  }

The entity data model supports a wide range of data types including, int, float, URI, datetime etc. Over the wire both a binary and JSON representation is used. To enable datatypes not supported in JSON something else is used. (ed - i forgot what it is)

Reserved fields
---------------

Entity fields starting with ``_`` are reserved. Any such fields will
be ignored when writing an entity to a dataset. Note that the fields
are only reserved at the root level, so child entities can have them.


.. list-table::
   :header-rows: 1
   :widths: 30, 50

   * - Field
     - Description

   * - ``_id``
     - This is the primary key of the entity. The value is always a
       string. Mandatory.

   * - ``_deleted``
     - If ``true`` then the entity is deleted. All other values are
       interpreted as if the entity is not deleted. Optional.

   * - ``_updated``
     - The sequence of the entity. The value must be either a string
       or an integer value. The value is used to tell the order of the
       entities. The value is meant to be opaque, and should not be
       parsed or interpreted by other parties than the data source
       that produced it. The ``_updated`` value can be passed through
       to the ``since`` request parameter in HTTP endpoints. Optional.

   * - ``_previous``
     - A pointer back to the previous version of this entity. The
       value refers to the ``_updated`` field of the previous
       version. Optional. If the field is missing or the value is
       ``null``, then there exists no previous version.

   * - ``_ts``
     - This the real-world timestamp for when the entity was added to
       the datasource. The value is an integer representing the number
       of seconds since epoch (January 1st 1970 UTC). This field is
       used only for informal purposes. Optional.

       
Standard datatypes
------------------

Entities are mapped to and from JSON objects, so they support the same
datatypes as JSON does. Because JSON only supports a limited number of
datatypes there is also limited support for `Transit
<https://github.com/cognitect/transit-format>`_ datatypes.

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Type
     - Description
     - Example
       
   * - Entity (aka object)
     - Like a JSON object where keys are always strings.
     - ``{"a": 123}``
       
   * - List
     - A list of values. Values can be of any type.
     - ``["abc", 123, [4, 5], {"x": "y"}]``
       
   * - String
     - A string value. Maximum size is 4294967296 bytes.
     - ``"abc"``

   * - Integer
     - An integer value. The valid range is between ``-9223372036854775808``
       and ``9223372036854775807``.
     - ``123``

   * - Decimal
     - A decimal number. The valid range is the IEEE 754 binary 64 format,
       because we're currently storing the value as a double-precision
       floating-point number. Note that you may loose precision when using
       this datatype.
     - ``123.456``

   * - Boolean
     - A boolean value. Either ``true`` or ``false``.
     - ``true``

   * - Null
     - A null value. Typically used to represent a missing value.
     - ``null``

Extension types (Transit encoded)
----------------------------------

`Transit <https://github.com/cognitect/transit-format>`_ encoded
values are represented as strings in JSON. The value is prefixed by
"~" and tag character that indicates the type of the value. The
extension types below are currently the only ones supported. Transit
types that are not recognized will be treated as string values.

.. list-table::
   :header-rows: 1
   :widths: 10, 30, 50

   * - Type
     - Description
     - Example
       
   * - URI
     - Uniform Resource Identifier (URI).
     - ``"~rhttp://www.sesam.io/"``

   * - Datetime
     - Date and time with up to nanoseconds precision. The valid range is
       from ``"~t1677-09-21T00:12:43.145224192Z"`` to
       ``"~t2262-04-11T23:47:16.854775807Z"``. Note that the time part
       of the string is mandatory. The fraction of a second is optional.
     - ``"~t2015-01-02T03:04:05.123456789Z"``, ``"~t1973-01-22T23:11:54Z"``

   * - Bytes
     - A base64 encoded binary value.
     - ``"~bAAECAwQF"``


DataHub
=======

The datahub is where Sesam stores all its data. The data it collects from external systems and the data it has transformed is all stored in the datahub. The datahub is comprised of many datasets.

Datasets
========

A dataset is the basic means of storage inside the Sesam datahub. A dataset is a log of entities supported by primary and secondary indexes. A dataset sink can write entities to the dataset. The dataset stores the entity in the log if and only if it is new or different from an existing entity with the same identity.

A dataset (data) source exposes the entities from the log so that they can be consumed by an external system or used by data transormations. As the main data structure is a log the source can read from a specific point in the log.

Data transformations can be applied to datasets. A data transformation takes a stream of entities and transforms them into a new stream of entities. A transform can query across many other datasets in order to create the new entity.

Data Transformation Language (DTL)
==================================

The Data Transformation Language is used to construct new data from existing data. DTL transforms can only be applied to data in a dataset. The result of a DTL transform is exposed via DTL provider.

DTL has a simple syntax and model where the user declares how to construct a new data entity. It has commands such as 'add', 'copy', 'merge' for

Sinks
=====

Sinks are components which can consume entities fed to them through 'Sink Writer' objects provided by a 'Data Sink' object. The sink writer has the resposibility to write these entites to the target, handle transactional
boundaries and potentially batching of multiple entities if supported by the target system. The 'Sink Writer' object inherits its parent sink's configuration settings but is immutable to changes to this durings its life time.
Several types of data sinks are supplied with the core service. Using the JSON push sink enables you to transfer entities to remote nodes.

Data Sync Task
==============

The data sync task handles the mechanics of 'pumping' data from a source to a sink. It runs periodically or at a 'cron' schedule and attempts to read entities from a data source and write them to a data sink. It also is capable of
rescanning the data source from scratch at configurable points in time. If errors occur during reading or writing of entities, it will keep a log of the failed entities and in the case of writes it can retry
writing an entity later. The retry strategy is configurable in several ways and if a end state is reached for a failed entity, it can be written to a 'dead letter' dataset for further processing.

A Data Pipe
===========

A data pipe is any combination of source, sync task and sink. It is a simple way to talk about the flow of data from a source to a target system. The pipe is the only way to specify a stream of entities from a source to a sink in a node.

External Systems
================

An external system is any database, or application API that could be used as a source of data for the DataLake or as the target of transformed entities coming out of the DataLake. The External System components in the DataLake are a way to represent the actual systems being connected, or integrated.

The External System component has a couple of uses. Firstly it can be used to introspect the underlying system and provide back lists of possible 'source' or 'sink' targets. Often this information can be used on the command line or in the Sesam Admin User Interface to quickly and efficiently configure how the DataLake consumes or delivers data.

## Sesam API

The Sesam API is a RESTful API that exposes the current state of a Sesam Node or cluster and allows clients to manage tasks, register new DTL,

## Sesam Client Library


## Sesam Command Line Tool


## Sesam Node Clusters

## Sesam Interactive

Sesam Interactive is a provided as a Jupyter server that is configured to connect to a Sesam Node via the API. The Sesam client library is available in the Jupyter python kernal and as such from any notebook it is possible to interact with the Sesam node and the streams of data it provides.

This setup can be used to explore datasets programmatically and also perform analytics and queries to show how the data in the DataLake can be used.



