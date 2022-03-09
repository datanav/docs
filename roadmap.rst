=======
Roadmap
=======

This roadmap highlights some of features we are currently working on. This roadmap might be subject to
change.

Planned
-------

.. _roadmap_clustered_architecture:

Clustered architecture everywhere (Q1 2022)
===========================================

Today we have two variants of Sesam (single machine and clustered). The two variants share most of their code, but
some parts are implemented in different ways. This makes some features harder for us to implement, and can cause
slight differences in behaviour between the two variants.

We are looking into how we can get the clustered architecture everywhere.

This architecture is based on Kubernetes
and might open up the possibility of running Sesam in a self-hosted Kubernetes cluster.

.. _property-lineage:

Property lineage (Q1 2022)
==========================

Properties in Sesam originate from external systems or are composed from other properties using DTL. The fact properties
are composed using introspectable DTL in combination with :ref:`schema collection <schema-inferencing>` allows us to continously track property lineage.

We are working on making this lineage data available, as well as looking at ways to visualize it.

Extensions
==========

Microservices are second-class citizens in Management Studio. Setting up a microservice is done using
unstructured documentation (README, etc).

We are looking at how to structure and describe microservices so that
microservices can work and behave as builtin systems in Management Studio.

We are also looking into how we can use OAuth 2.0 Authorization Code Grant Type of authorization for extensions that
talk to providers that support this to make the authorization process more user friendly.

This will also open up the possibility for us to turn the builtin systems into separate extensions.

Age based deletion marker compaction
====================================

If Sesam has seen an entity it will remember the 'id' for this entity forever. This also applies to entities that was
seen but no longer exists in the source.

These deletion markers are required for incremental synchronizing of data, but once all the consumers have read the
deletion marker it only has historic value.

We are looking into how to be able to configure a time to live on these deletion markers so that old history can be
cleaned up.

Expose invoices and contracts in the portal
===========================================

Invoices and contracts can be requested through support.

We are looking into how to expose invoices and contracts in the portal to make them more accessible.

Durable data
============

Data is backed up once every 24 hours. During a disaster recovery data written the last 24 hours can be lost. This is typically not a problem when Sesam is pulling data from sources, as the data that was lost can be pulled again.

For http_endpoint sources and non-idempotent sinks, this can be a problem.

We are looking into how to support durable data as an opt-in payed feature. This feature can then be enabled on relevant pipes.

High level configuration
========================

The current user interface is built around configuring pipes, which is a low level building block in Sesam. We have now estabilished best practices that describes the patterns you should use to build a robust and extensible Sesam solution using pipes. We also have schemas for all the built-in systems, and will have schemas for all systems once Extensions are in place.

We are looking into how we can design a high level configuration and corresponding user interface that builds upon these features.

The goal is to make it much easier to configure Sesam, using visual tools and human friendly forms.

Composite Pipes
===============

Currently you are not able to do DTL with dependency tracking when the source is not a pure dataset source. If the
source type is merge you need to create two pipes in order to merge and hop with dependency tracking.

You also need to create two pipes in order to use "create-child" and "emit_children".

We are looking into how to support this without requiring the user to create two pipes.

Multitenancy
============

Today one subscription can have multiple configuration groups, but they are all part of one big configuration that share one namespace, metadata, environment variables, system roles and access rights.

We are looking into how one subscription can contain multiple standalone configurations in one shared instance.

Note that VPN will be tied to the shared instance so there will be some limitations to the VPN. There will also be limits on how many standalone configurations (tenants) you can have per single and multi compute. This feature will only be available on the 'Clustered architecture'.

The goal is for our partners to be able to serve their customers with standalone configurations from a shared instance.

Public Preview
--------------

The following items are now available for experimental use.

Integrated data browsing
========================

The current 'Databrowser' tool is hard to configure, not integrated into Management Studio and targeted at
external users.

We are looking at making a simpler tool that is integrated into Management Studio so that you
can do more efficient development. This new tool will replace the existing 'Databrowser' tool.

This feature will most likely only be available on the 'Clustered architecture',
so it depends on the 'Clustered architecture everywhere' item on the roadmap.

.. note::
   :ref:`Integrated search <concepts-integrated-search>` is now available for subscriptions running on the
   Clustered Architecture.

General Available
-----------------

The following items are now available for general use.

Self service VPN setup
======================

VPN setup can be requested through support.

We are looking into how to automate this process so that the end user can do this process faster.

.. note::
   :ref:`VPN <concepts-vpn>` is now configurable for subscriptions running on the Clustered Architecture.
