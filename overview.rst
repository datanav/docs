========
Overview
========

.. contents:: Table of Contents
   :depth: 2
   :local:

.. _overview-introduction:

Introduction
------------

Sesam is offered as service. The service is either hosted for you in the cloud or it is self-hosted. The service has an :doc:`API <api>` that is used to securely communicate with the service over HTTPS. The service subscription is billed monthly.

The terms of service can be found here: https://sesam.io/terms.html. Our privacy policies can be found here: https://sesam.io/privacy.html.

The Sesam service is backed by a centralized portal. The portal is a web service running at `https://portal.sesam.io/ <https://portal.sesam.io/>`_ . The portal is the place were you can sign up for, and manage, your Sesam subscriptions. It is also the place where you go to for the :doc:`Sesam Management Studio <management-studio>`, the user interface for accessing your own Sesam service.

There is also an `experimental version <https://beta.portal.sesam.io/>`_ of the Management Studio where new features are introduced at an earlier stage before they are publicly released in the main portal.

Concepts
--------

Sesam is a Master Data Hub built on a streaming dataflow data integration and processing system. It is optimised for collecting or receiving data from source systems,  :ref:`transforming data <getting-started-transformations>`, and :ref:`pushing or providing data <getting-started-sinks>` to target :ref:`systems <system_section>`.

Data is stored in datasets. A dataset is a log of data entities with additional indexes for efficient random access and lookups. Data is fetched from the source systems on a regular basis and the :doc:`entities <entitymodel>` are stored in the log only if they have changed from the last time the entity was seen.

:doc:`Entities <entitymodel>` in the datasets can be processed using the :doc:`Data Transformation Language <DTLReferenceGuide>`. DTL takes a stream of entities as input and returns a new stream of transformed entities. It can join data from other datasets to create new entities. Data produced via DTL can be stored in new datasets to be exposed or sent to applications that need it.

The final piece of Sesam is to deliver data from a dataset to a :ref:`sink <sink_section>`. Sinks are used to write data into target :ref:`systems <system_section>` or send it to service endpoints.

Sesam provides implementations for many types of :ref:`sources <source_section>`, including :ref:`relational databases <sql_source>` and custom JSON streams. It also provides a number of core Sink implementations such as the :ref:`relational database <sql_sink>` and :ref:`HTTP endpoint sinks <http_endpoint_sink>`.

See the :doc:`Concepts <concepts>` document for more in-depth explanation of the Sesam concepts.

.. _overview-installation:

Installation
------------

You must sign up using the `Sesam Portal <https://portal.sesam.io/>`__ to get access to a Sesam service. The default service type is a cloud based service, but it's also possible to install a self-hosted Sesam. This document assumes a cloud based service.

You can also access an existing Sesam service by registering in the Sesam Portal and obtaining an invitation from someone with management permissions for the existing service.

Once you have have access to a running Sesam service in the portal, you can access the Sesam Management Studio by clicking on its name on the home page in the Portal.

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

    https://service_endpoint/api

Software channels
-----------------

Sesam software is released through a phased rollout scheme. There are four different release channels – commonly called canaries. This is done to give changes and new features some time in non-production environments before they are rolled out to production. The goal is to reduce risk.

The available channels are:

- ``weekly-prod`` is release bi-weekly and is the most stable release. *Use this in production!*
- ``weekly`` is release once a week. Use this in staging environments.
- ``nightly`` is released every night. Use this in development environments.
- ``latest`` is released every time a pull request is merged. Use this only for developent environments, and only when you know what you're doing.

Tooling
-------

Management Studio
=================

The Sesam Management Studio is a user-interface for working with Sesam. The UI exposes the pipes, datasets and operational information for a service instance.

To read more about the Sesam Management Studio, please click :doc:`here <management-studio>`.


Sesam Client
============

The Sesam Client is primarily a tool for running CI tests. To read more about the Sesam Client command line tool, please click :doc:`here <sesam-client>`.
