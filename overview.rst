========
Overview
========

.. contents:: Table of Contents
   :depth: 2
   :local:

.. _overview-introduction:

Introduction
------------

Sesam is a general purpose data integration and processing platform. It is optimised for collecting or receiving data from source systems,  :ref:`transforming data <getting-started-transformations>`, and :ref:`pushing or providing data <getting-started-sinks>` to target :ref:`systems <system_section>`.

Data is stored in datasets. A dataset is a log of data entities with additional indexes for efficient random access and lookups. Data is fetched from the source systems on a regular basis and the :doc:`entities <entitymodel>` are stored in the log only if they have changed from the last time the entity was seen.

:doc:`Entities <entitymodel>` in the datasets can be processed using the :doc:`Data Transformation Language <DTLReferenceGuide>`. DTL takes a stream of entities as input and returns a new stream of transformed entities. It can join data from other datasets to create new entities. Data produced via DTL can be stored in new datasets to be exposed or sent to applications that need it.

The final piece of Sesam is to deliver data from a dataset to a :ref:`sink <sink_section>`. Sinks are used to write data into target :ref:`systems <system_section>` or send it to service endpoints.

Sesam provides implementations for many types of :ref:`sources <source_section>`, including :ref:`relational databases <sql_source>` and custom JSON streams. It also provides a number of core Sink implementations such as the :ref:`relational database <sql_sink>` and :ref:`HTTP endpoint sinks <http_endpoint_sink>`.

.. _overview-installation:

Installation
------------

You must sign up using the `Sesam Portal <https://portal.sesam.io/>`__ to get access to a Sesam service. The default service type is a cloud based service, but it's also possible to install a self-hosted Sesam. This document assumes a cloud based service.

You can also access an existing Sesam service by registering in the Sesam Portal and obtaining an invitation from someone with management permissions for the existing service.

Once you have have access to a running Sesam service in the portal, you can access the Sesam Management Studio by clicking on its name on the home page in the Portal.

.. _overview-license:

License
-------

Sesam requires a valid license to function. Without a valid license the pipes will stop running. Instructions for obtaining a valid license can be found in the `Sesam Portal <https://portal.sesam.io/>`__.

Service Instance
----------------

We use *Sesam* as the general name for a Sesam service instance. A given service instance exposes a single API endpoint and user interface. Internally, the service instance consists of configuration and datasets for the storage of data.

A service instance is configured via the API. Configuration in Sesam is quite cool. It is entity based. This means that we can track and understand if the configuration has changed in the same way we understand if any data has changed.

The API offers two ways to upload configuration. The first is via the 'config' endpoint. This allows a complete set of configuration to be uploaded and is typically used when bootstrapping a service instance in QA or production environments. The other way is to use the individual resources exposed via the API. Such as a post to the collection of pipes.


Service API
-----------

The Sesam API is a RESTful API that exposes the current state of a Sesam service instance and allows clients to add and modify configuration, test DTL, introspect datasets, view logs and the operational state of pumps and pipes.

The API can be found at:

::

    http://service_endpoint:9042/api

Tooling
-------

Management Studio
=================

The Sesam Management Studio is a user-interface for working with Sesam. The UI exposes the pipes, datasets and operational information for a service instance.

To read more about the Sesam Management Studio, please click :doc:`here <management-studio>`.


Sesam Client
============

The Sesam Client is primarily a tool for running CI tests. To read more about the Sesam Client command line tool, please click :doc:`here <sesam-client>`.
