========
Concepts
========

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
------------

Sesam is a collector, manipulator and producer of data. It collects raw data from source systems and stores it in nodes in the form of datasets. Data transformations can be defined and executed to construct new datasets. Data from these datasets can be exposed and delivered to other systems.

Sesam produces and consumes streams of data. Each stream contains a number of data entities each of whom consists of a number of key / property values and a special property called "_id".

Components called data sources expose data from source systems such as REST APIs and relational databases. DataSync tasks run on regular intervals to pull data from a provider and push it to a sink. Datahub sinks write the entities to datasets. A dataset is a log of entities supported by indexes for random access.

Datasets also act as data sources. They can expose the data they contain. However, a more common usage is to transform the data from a dataset into a new shape or representation. This is done using the Data Transformation Language (DTL). The DTL is optimised for ease of use in stream and graph processing and the construction of new data entities. DTL transformations can use data from many datasets to construct new entities.

The results of applying a DTL transformation is a new stream of entities. These are exposed using a source and, like any other stream of entities, can be consumed into a sink. These sinks can either be another dataset sink or it can be a sink that connects to an target system. Systems can be databases, APIs, message queues, etc.

These concepts are explored in more detail in the following sections.

Node
----

A *node* is a running process that is capable of hosting instances of the components described below. In addition, each node instance exposes a service API and a graphical user interface. Nodes can be organised into clusters with one node acting as the master. In the case of a cluster the API and user interface is exposed from the master node.

The node has a configuration file, ```node-config.json``, that describe the set of components that should be instantiated and run by the node. These files are themselves just a serialised set of data entities. Each entity is the configuration for one component. Any changes to the file will result in a component being reconfigured but only if the data for actual component changes.

The node stores entities in datasets. A node can have any number of these.

.. _concepts-datasets:

Datasets
--------

A dataset is the basic means of storage inside the node. A dataset is a log of :doc:`entities <entitymodel>` supported by primary and secondary indexes. A ``dataset`` sink can write entities to the dataset. The dataset stores the entity in the log if and only if it is new or if it is different from an existing entity with the same identity.

A ``dataset`` source exposes the entities from the dataset so that they can be streamed through pipes. As the main data structure is a log the source can read from a specific location in the log.

Systems
-------

A *system* is any database or API that could be used as a source of data for the node or as the target of transformed entities coming out of the node. The system components in the node are a way to represent the actual systems being connected, or integrated.

The system component has a couple of uses. Firstly it can be used to introspect the underlying system and provide back lists of possible 'source' or 'sink' targets. Often this information can be used on the command line or in the *Sesam Management Studio* to quickly and efficiently configure how the node consumes or delivers data.


.. _concepts-pipes:

Pipes
-----

A *pipe* is composed of a source, a transformation chain, a sink, and a pump. It is an atomic unit that makes sure that data flows from the source to the sink at defined intervals. It is a simple way to talk about the flow of data from a source system to a target system. The pipe is the only way to specify how entities stream from dataset to dataset in a node.


.. _concepts-sources:

Sources
=======

A data *source* is a component hosted in the Sesam Node that exposes a stream of entities. Typically, this stream of entities will be the rows of data in a relational database table, the rows in a CSV file, or data from an API.

The source component offers an object called a Data Source Reader which has one capability which is 'getEntities'. This 'reader' object is immune to changes to the configuration of its parent source during its lifetime.

The 'getEntities' method can take an additional parameter that is an 'offset' token. This token can be used to only fetch the entities that have changed *since* that given offset. An offset is a opaque token that may take any form; it is interpreted
by the data source only. For example; for a relational data source it might be a datestamp or for a log based source it might be an index.

Each entity returned by a data source reader is a dictionary that maps keys to values. Values can be simple literals such as string, int, long, etc. They can also be lists or child entities. They can even be lists of entities. There are just three special or reserved keys within an entity, and they are; "_id", "_updated" and "_deleted". [TODO: all keys starting with '_' are reserved - grove] It is a requirement that every entity exposed by a provider has an "_id" property. This identifier should be unique within the set of entities being exposed by that source, but need not be globally unique across all entities.

Sesam offers a number of core built-in data sources but it is also easy for developers to expose a micro service that can supply data from a remote service. The built-in remote data source is able to consume data from these endpoints.


.. _concepts-transforms:

Transforms
==========

Entities streaming through a pipe can be transformed on their way from the source to the sink. A transformation chain takes a stream of entities, transforms them, and creates a new stream of entities. A transform can query across many other datasets in order to enrich or create entities.


.. _concepts-sinks:

Sinks
=====

A data *sink* is a components that can consume entities fed to them through 'Sink Writer' objects provided by a 'Data Sink' object. The sink writer has the resposibility to write these entites to the target, handle transactional
boundaries and potentially batching of multiple entities if supported by the target system. The 'Sink Writer' object inherits its parent sink's configuration settings but is immutable to changes to this durings its life time.
Several types of data sinks are supplied with the core service. Using the JSON push sink enables you to transfer entities to remote nodes.

.. _concepts-pumps:

Pumps
=====

The data sync task handles the mechanics of 'pumping' data from a source to a sink. It runs periodically or at a 'cron' schedule and attempts to read entities from a data source and write them to a data sink. It also is capable of
rescanning the data source from scratch at configurable points in time. If errors occur during reading or writing of entities, it will keep a log of the failed entities and in the case of writes it can retry
writing an entity later. The retry strategy is configurable in several ways and if a end state is reached for a failed entity, it can be written to a 'dead letter' dataset for further processing.

Change tracking
---------------

TODO: explain

Dependency Tracking
-------------------

TODO: explain

Retention Policies
------------------

TODO: explain

.. _concepts-dtl:

The Data Transformation Language (DTL)
--------------------------------------

The Data Transformation Language is used to construct new data from existing data. DTL transforms can only be applied to data in a dataset. The result of a DTL transform is exposed via DTL provider.

DTL has a simple syntax and model where the user declares how to construct a new data entity. It has commands such as 'add', 'copy', 'merge' for


Sesam API
---------

The Sesam API is a RESTful API that exposes the current state of a Sesam Node or cluster and allows clients to manage tasks, register new DTL,


