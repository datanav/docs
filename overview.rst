========
Overview
========

.. contents:: Table of Contents
   :depth: 2
   :local:

.. _overview-introduction:

Introduction
------------
Sesam is a general purpose data integration and processing platform. It is optimised for collecting or receiving data from source systems ,  :ref:`transforming data <getting-started-transformations>`, and :ref:`pushing or providing data <getting-started-sinks>` to target :ref:`systems <system_section>`.

Data is stored in datasets. A dataset is a log of data entities with additional indexes for efficient random access and lookups. Data is fetched from the source systems on a regular basis and the :doc:`entities <entitymodel>` are stored in the log only if they have changed from the last time the entity was seen.

:doc:`Entities <entitymodel>` in the datasets can be processed using the :doc:`Data Transformation Language <DTLReferenceGuide>`. DTL takes a stream of entities as input and returns a new stream of transformed entities. It can join data from other datasets to create new entities. Data produced via DTL can be stored in new datasets to be exposed or sent to applications that need it.

The final piece of Sesam is to deliver data from a dataset to a :ref:`sink <sink_section>`. Sinks are used to write data into target :ref:`systems <system_section>` or send it to service endpoints.

Sesam provides implementations for many types of :ref:`sources <source_section>`, including :ref:`relational databases <sql_source>` and custom JSON streams. It also provides a number of core Sink implementations such as the :ref:`relational database <sql_sink>` and :ref:`HTTP endpoint sinks <http_endpoint_sink>`.

.. _overview-installation:

Installation
------------
You must sign up using the `Sesam Portal <https://portal.sesam.io/>`__ to install Sesam. The default installation type is a cloud based installation, but it's also possible to install Sesam on-premise or in a local cloud environment. This document assumes a cloud based installation.

You can also access an existing Sesam installation by registering in the Sesam Portal and obtaining an invitation from someone with management permissions for the existing installation.

Once you have have access to a running Sesam installation in the portal, you can access the Sesam Management Studio by clicking on its name on the home page in the Portal.

.. _overview-license:

License
-------
Sesam requires a valid license to function. Without a valid license the pipes will stop running.

Instructions for obtaining a valid license can be found in the `Sesam Portal <https://portal.sesam.io/>`__. A month trial license is available for evaluation purposes.