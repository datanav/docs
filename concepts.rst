========
Concepts
========

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
------------

Sesam is a general purpose data integration and processing platform. It is optimised for collecting or receiving data from source systems, transforming data, and providing data for target systems. 

Sesam collects raw data from source systems and stores it in datasets. Data transformations can be defined that process the data residing in datasets to construct new datasets. Transformations can join data across datasets to create new shapes of data. Data from these datasets can be exposed and delivered to other systems. The entire system is driven by the state change of entities. This document introduces the concepts that are key to understanding and working with Sesam. 

.. image:: images/datahub.jpg
    :width: 800px
    :align: center
    :height: 600px
    :alt: Sesam


Sesam produces and consumes streams of data. Each stream contains a number of data entities. Each entity consists of a number of name-value pairs and with some special reserved property names. See the entity data model section for more details. The following is a quick example of the shape of entities that are consumed and exposed by Sesam.

::

    [
        {
            "_id": "1",
            "name": "Bill",
            "dob": "01-01-1980"
        },
        {
            "_id": "2",
            "name": "Jane",
            "dob": "04-10-1992"
        }
    ]


A key concept in Sesam is the *Pipe*. A pipe consists of a datasource, a sink and optionally a list transformations. Each pipe has an associated pump that is scheduled to run at intervals and pull data enties from the datasource, push them through any transformations and deliver the results into the sink.  

*Datasources* are configured to expose data as streams of entities from source systems such as REST APIs and SQL databases. Each datasource is connected to a System. A system represents some external system, such as a web server hosting an API endpoint or a SQL database. The job of the datasource is to convert the underlying data into a uniform representation; JSON, and if possible offer features such as only exposing the entities that have changed. Different datasources offer different levels of support for change detection. 

When first pulling data from a datasource for an external system, such as a SQL database, the sink is a dataset sink. A dataset sink writes the data into a dataset. The dataset is just a log of entities with some additional indexes to support lookups and joins. An entity is only appended to the dataset's log if the data is new or has changed.

Datasets also act as data sources. One of the main uses of a dataset is as a source to a transformation. Transformations are describeded using the Data Transformation Language (DTL). DTL is optimised for ease of use in stream and graph processing for the construction of new entities. DTL transformations can use data from many datasets to construct new entities.

The results of applying a DTL transformation is a new stream of entities that can be delivered into a sink. These sinks can either be another dataset sink or it can be a sink that connects to a target system. 

These concepts are explored in more detail in the following sections.

Sesam Node
----------

We use *Sesam* as the general name for a Sesam service instance. A given service instance is actually comprised of one of more *Sesam Nodes*. A *Sesam Node* is a running process that is capable of hosting components for collection, transforming and delivering data. In addition, each node instance can expose a service API endpoint and a graphical user interface. Nodes can be organised into clusters in order to share workloads. In the case of a cluster the API and user interface is exposed from nodes configured to be front-end nodes.

The *Sesam Node* is provided as a Docker image called sesam/sesam-node. The node requires a configuration file, *nodeconfig.json*, that describe the set of pipes that should be created and managed by the node. Each pipe describes the flow of data from a *datasource* to a *sink*. Optionally, each pipe can also describe a transformation that should be applied to the data on its way through. 

Data flowing into the *Sesam Node* can be stored in Datasets. The *Sesam Node* manages these datasets, and exposes them via the API. Datasets are used as the source for data transformation and also when delivering data to external target systems.   

.. _concepts-datasets:

Datasets
--------

A dataset is the basic means of storage inside the node. A dataset is a log of :doc:`entities <entitymodel>` supported by primary and secondary indexes. A *dataset sink* can write entities to the dataset. The dataset appends the entity to the log if and only if it is new or if it is different from an existing entity with the same identity.

A *dataset source* exposes the entities from the dataset so that they can be streamed through pipes. As the main data structure is a log the source can read from a specific location in the log.

.. image:: images/dataset.jpg
    :width: 800px
    :align: center
    :height: 600px
    :alt: DataSet

Retention Policies
==================

A dataset is an immutable log of data that would left unchecked grow forever. This problem is partly mitigated as entities are only written to the log if they are new or different (based on a hash comparison) from the currently stored version of that entity. To supplement this and ensure that a dataset does not consume all available disk space a retention policy can be defined. A rentention policy describes the general way in which the log should be compacted. The currently available policy is actually the best one and it is 'None'. 


Systems
-------

A *system* is any database or API that could be used as a source of data for the node or as the target of transformed entities coming out of the node. The system components in the node are a way to represent the actual systems being connected, or integrated.

The system component has a couple of uses. Firstly it can be used to introspect the underlying system and provide back lists of possible 'source' or 'sink' targets. Often this information can be used on the command line or in the *Sesam Management Studio* to quickly and efficiently configure how the node consumes or delivers data.


.. _concepts-pipes:

Pipes
-----

A *pipe* is composed of a source, a transformation chain, a sink, and a pump. It is an atomic unit that makes sure that data flows from the source to the sink at defined intervals. It is a simple way to talk about the flow of data from a source system to a target system. The pipe is also the only way to specify how entities flow from dataset to dataset.

.. image:: images/pipes.jpg
    :width: 800px
    :align: center
    :height: 350px
    :alt: Generic pipe concept

.. _concepts-sources:

Sources
=======

A *data source* is a component hosted in the Sesam Node that exposes a stream of entities. Typically, this stream of entities will be the rows of data in a SQL database table, the rows in a CSV file, or json data from an API.

.. image:: images/datasource.png
    :width: 800px
    :align: center
    :height: 450px
    :alt: Generic pipe concept

Some datasources can accept an additional parameter that is an 'offset' token. This token is used to fetch only the entities that have changed since that given offset. This can be used simply to only ask for the entities that have changed since the last time it was asked. An offset is a opaque token that may take any form; it is interpreted by the data source only. For example; for a relational data source it might be a datestamp or for a log based source it might be a location offset.

Sesam provides a number of out of the box *data source* types, such as SQL Database and LDAP. It is also easy for developers to expose a micro service that can supply data from a remote service. The built-in remote data source is able to consume data from these endpoints. These custom data providers can be written and hosted in any language.

.. _concepts-transforms:

Transforms
==========

Entities streaming through a pipe can be transformed on their way from the source to the sink. A transformation chain takes a stream of entities, transforms them, and creates a new stream of entities. There are several different transform types supported: 
	- Data Transformation Langauge Transform. This transform uses the DTL to join and transform data into new shapes.

.. _concepts-sinks:

Sinks
=====

A data *sink* is a components that can consume entities fed to them through 'Sink Writer' objects provided by a 'Data Sink' object. The sink writer has the resposibility to write these entites to the target, handle transactional
boundaries and potentially batching of multiple entities if supported by the target system. The 'Sink Writer' object inherits its parent sink's configuration settings but is immutable to changes to this durings its life time.
Several types of data sinks are supplied with the core service. Using the JSON push sink enables you to transfer entities to remote nodes.

.. _concepts-pumps:

Pumps
=====

The data sync task handles the mechanics of 'pumping' data from a source to a sink. It runs periodically or at a 'cron' schedule and attempts to read entities from a data source and write them to a data sink. It's also capable of
rescanning the data source from scratch at configurable points in time. If errors occur during reading or writing of entities, it will keep a log of the failed entities and in the case of writes it can retry
writing an entity later. The retry strategy is configurable in several ways and if an end state is reached for a failed entity, it can be written to a 'dead letter' dataset for further processing.

Change tracking
===============

Sesam is special in that it really cares when data has changed. The typical pattern is to read data from a datasource and push it to a sink that is writing into a dataset. The dataset is essentially a log of the entities it receives. However if a new log entry was added every time the datasource was checked then log would grow very fast and be of little use. There are mechanisms at both ends to prevent this. When reading data from a datasource it may, if the datasource supports it, be possible to just ask for the entities that have changed since the last time. This uses the knowledge of the datasource, such as a last updated time stamp, to ensure that only entities that have been created, deleted or modified are exposed. On the side of the dataset, regardless of where the data comes from, it is compared with any existnig version of that entity and only updated if they are different. The comparison is done by creating and comparing the hashes of the old and new entity. 


.. _concepts-dtl:

The Data Transformation Language (DTL)
--------------------------------------

The Data Transformation Language is used to construct new data from existing data. DTL transforms can only be applied to data in a dataset. The result of a DTL transform is exposed via DTL provider.

DTL has a simple syntax and model where the user declares how to construct a new data entity. It has commands such as 'add', 'copy', and 'merge'.

.. image:: images/dtl.png
    :width: 800px
    :align: center
    :height: 500px
    :alt: DataSet 

Persisting the results of Transformation
========================================

In general DTL is applied to the entities in a dataset and the resulting entities are push into a sink that writes to a new dataset. The new dataset is then used as a datasource for sinks that write the data to external systems. 

Dependency Tracking
===================

One of the really smart things that Sesam can do is to understand complex dependencies in DTL. This is best described with an example. Imagine a dataset of customer entities and a dataset of address entities. Each address has a property 'customer_id' that is the primary key of the customer entity to which it belongs. A user creates a DTL transform that processes all customers and creates a new 'customer' structure that includes the address as a property. To do this they can use the hops function to connect the customer and address. This DTL transform forms part of  a pipe and as such when a customer entity is updated, added or deleted it will be at the head of the dataset log and get processed the next time the pump runs. But what if the address changes? As far as the expected output the customer itself has also changed? 

This is in essence a cache invalidation of complex queries problem. With Sesam we have solved that problem. We are empowered to solve the problem as we have a dedicated transform langauge. This allows us to introspect the transform to see where the dependencies are. Once we understand the dependencies we can create data structrues and events that are able to understand that a change to an address should put a corresponding customer entity at the front of the dataset log again. Once it is there it will be pulled the next time the pump is run and a new customer entity containing the updated address is exposed.  


Sesam API
---------

The Sesam API is a RESTful API that exposes the current state of a Sesam Node or cluster and allows clients to manage tasks, register new DTL,


