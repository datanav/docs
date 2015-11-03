========
Overview
========

Introduction
============

Sesam is a general purpose data integration and processing platform. It is optimised for collecting data from source systems, transforming that data and delivering it to target systems. What makes Sesam special is its ability to track and process only data that has changed, and its powerful data query and construction langauge.   


Installation
============

Sesam is offered as a cloud service and can also be installed locally. Local installations are managed by Sesam but run on client hardware. 

The Sesam service is run as either a single Sesam Node or as a cluster of Sesam nodes. Each node has the capability to collect, transform and deliver data. However, various topologies of nodes can be used to separate concerns where needed. A cluster of Sesam Nodes can be managed by a master node or accessed direclty. All nodes expose the Sesam API as way to control and introspect the node. When used in a cluster the master node exposes a common API across all worker nodes.

docker pull sesam/sesam-node

Running Sesam
=============

docker run sesam/sesam-node 

Concepts
========

Sesam is a collector, manipulator and producer of data. It collects raw data from source systems and stores it in a datahub in the form of datasets. Data Transformations can then be defined and executed to construct new datasets. Data from these datasets is then exposed and delivered to external systems.  

IMAGE - collect, connect and share.

Sesam produces and consumes streams of data. Each stream contains a number of data entities each of whom consists of a number of key / property values and a special property called "_id". 

Components called providers expose data from source systems such as REST APIs and Relational Databases. DataSync tasks run on regular intervals to pull data from a provider and push it to a sink. Datahub sinks store the entities in datasets. A dataset is a log of entities supported by indexes for random access.

Datasets also act as providers. They can expose the data they contain. However, a more common usage is to transform the data from a dataset into a new shape or representation. This is done using the Data Transformation Language (DTL). The DTL is optimised for ease of use in stream and graph processing and the construction of new data entities. DTL transformations can use data from many datasets to construct new entities.

The results of applying a DTL transformation is a new stream of entities. These are exposed using a provider and, like any other stream of entities, can be consumed into sink. These sinks can either be another dataset sink or it can be a sink that connects to an external system. External systems can be databases, APIs, message queues, etc.

These concepts are explored in more detail in the following sections.

A Sesam Node
============

A Sesam Node is a running process that is capaable of hosting instances of the components described below. In addition, each node instance exposes an API and a user interface. Nodes can be organised into clusters with one Node acting as the master. In the case of a cluster the API and user interface is exposed from the Master node.   

Sesam Node Config
=================

Each Sesam Node has a configuration file or files that describe the set of components that should be instantiated and run by the Node. These files are themselves just a serialised set of data entities. Each entity is the configuration for one component. Any changes to the file will result in a component being reloaded but only if the data for actual component changes.

By convention the config file is called node-config.json and is found in the root folder for the node. (ed - too much detail)

Data Providers
==============

(ed - please decide on the name of these things.)
A Data Provider is a component hosted in the Sesam Node that exposes a stream of entities. Typically, this stream of entities will be the rows of data in a relational database table, the rows in a CSV file, or data from an API. 

The provider component offers one capability which is 'getEntities'. This operation can take an additional parameter that is an 'offset' token. This token can be used to only fetch the entities that have changed since that given offset. An offset is just a string token and different providers can interpret it differently.

Each entity returned by a provider is a dictionary that maps keys to values. Values can be simple literals such as string, int, long, etc. They can also be lists or child entities. They can even be lists of entities. There are just three special or reserved keys within an entity, and they are; "_id", "_updated" and "_deleted". It is a requirement that every entity exposed by a provider has an "_id" property. This identifier should be unique within the set of entities being exposed by that provider, but need not be globally unique across all entities. 

Sesam offers a number of core built in providers but it is also easy for developers to expose a micro service that can supply data from a remote service. The built-in remote provider is able to cosume data from these endpoints.

Entity Data Model
=================

Sesam uses a entity data model as the core representation of data. Each entity is a dictionary of key-value pairs. Each key is a string and the value can be either a literal value, a list or another dictionary. 

A Sesam entity has a few special keys that should not be messed with. The following data prototype explains these special properties.

  {
  	"_id": "the id of the entity. required on all entities.",
  	"_updated": "a token indicating when this was modified",
  	"_deleted": "indicating if the entity should be treated as deleted"
  }

The entity data model supports a wide range of data types including, int, float, URI, datetime etc. Over the wire both a binary and JSON representation is used. To enable datatypes not supported in JSON something else is used. (ed - i forgot what it is)

DataHub
=======

The datahub is where Sesam stores all its data. The data it collects from external systems and the data it has transformed is all stored in the datahub. The datahub is comprised of many datasets. 

DataSets
========


Data Transformation Language
============================

Sinks
=====

## A Data Pipe

## External Systems

An external system is any database, or application API that could be used as a source of data for the DataLake or as the target of transformed entities coming out of the DataLake. The External System components in the DataLake are a way to represent the actual systems being connected, or integrated. 

The External System component has a couple of uses. Firstly it can be used to introspect the underlying system and provide back lists of possible 'Providers' or sink targets. Often this information can be used on the command line or in the Sesam Admin User Interface to quickly and efficiently configure how the DataLake consumes or delivers data.

## Sesam API

The Sesam API is a RESTful API that exposes the current state of a Sesam Node or cluster and allows clients to manage tasks, register new DTL, 

## Sesam Client Library


## Sesam Command Line Tool


## Sesam Node Clusters

## Sesam Interactive

Sesam Interactive is a provided as a Jupyter server that is configured to connect to a Sesam Node via the API. The Sesam client library is available in the Jupyter python kernal and as such from any notebook it is possible to interact with the Sesam node and the streams of data it provides. 

This setup can be used to explore datasets programmatically and also perform analytics and queries to show how the data in the DataLake can be used.



