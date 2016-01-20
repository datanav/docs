========
Overview
========

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
------------

Sesam is a general purpose data integration and processing platform. It is optimised for collecting or receiving data from source systems, transforming data, and pushing or providing data to target systems. Sesam stores data in datasets. A dataset is a log of data entities with additional indexes for efficient random access and lookups. Data is fetched from the source systems on a regular basis and the entities are stored in the log only if they have changed from the last time the entity was seen.

Entities in the datasets can be processed using the Data Transformation Language. DTL takes a stream of entities as input and returns a new stream of transformed entities. It can join data from other datasets to create new entities. Data produced via DTL can be stored in new datasets to be exposed or sent to applications that need it.

The final piece of Sesam is to deliver data from a dataset to a sink. Sinks are used to write data into target systems or send it to service endpoints.

Sesam provides implementations for many types of data sources, including relational databases, LDAP, and MongoDB. It also provides a number of core Sink implementations such as the relational database and HTTP Post sinks.

Installation
------------

The Sesam service is run as either a single Sesam Node or as a cluster of Sesam nodes. Each node has the capability to collect, transform and deliver data. However, various topologies of nodes can be used to separate concerns where needed. A cluster of Sesam Nodes can be accessed via single API endpoint. All nodes expose the Sesam API as way to control and introspect the node. When used in a cluster the nodes can be configured to expose an API over all the nodes in the cluster.

For getting started with Sesam a single node will suffice. The Sesam Node is available as a public docker image. If you install and use the docker node you are bound by the Sesam Node EULA agreement.

::

  docker pull sesam/sesam-node

Getting Started
---------------


::

  docker run sesam/sesam-node

TODO: add information about what volumes to bind.
