=======
Roadmap
=======

This roadmap highlights some of features we are currently working on. This roadmap might be subject to
change.

Planned
-------

Webhooks (Q1 2023)
==================

Today Sesam needs to pull frequently in order to detect changes in sources. For systems that support signalling through webhooks, this is inefficient and can be annoying for the system that is being pulled from. This is particularly bad for services that offer webhooks, and no other incremental support.

We are looking into how we can support webhooks to receive incremental changes, so that we can eliminate or reduce the polling frequency.

Self-hosted clustered architecture (Q2 2023)
============================================

Today, self-hosted Sesam only supports the single machine variant. A lot of new features are only offered on the clustered architecture (e.g. Metrics API, Integrated Search), and are therefore not available on self-hosted subscriptions.

We are looking into self-hosting of the clustered architecture. This architecture is based on Kubernetes, and will require a running Kubernetes cluster. We will start testing on the most common Kubernetes services (Google GKE, Amazon EKS and Azure AKS).

Reusable connectors (Q2 2023)
=============================

Today, one can quickly build connectors by configuring our generic systems (e.g. SQL, REST), but there is not a simple way to reuse those configurations.

We are looking into how to package up a set of configurations in such a way that they can be reused across subscriptions.

Consumer portal (Q3 2023)
=========================

Today, one has to get the credentials to the systems one would like to connect from an external source and inject them into a running subscription as secrets. For subscriptions that are built around multiple tenants building such a solution can be time consuming.

We are looking into building a configurable consumer portal application that allows a solution provider to get their tenants to onboard themselves, configure connectors and get insight into operational issues using a simple end user web interface.

This will be built on top of reusable connectors, and support connectors that require OAuth2 flows as well as services with simpler API key credentials.

Age-based deletion marker compaction (Q2 2023)
==============================================

If Sesam has seen an entity it will remember the 'id' of this entity forever. This also applies to entities that were
seen, but no longer exist in the source.

These deletion markers are required for incremental synchronizing of data, but once all the consumers have read the
deletion marker it only has historic value.

We are looking into how to be able to configure a time-to-live on these deletion markers so that old history can be
cleaned up.

High-level configuration (Q4 2023)
==================================

The current user interface is built around configuring pipes, which is a low-level building block in Sesam. We have now estabilished best practices that describe the patterns you should use to build a robust and extensible Sesam solution using pipes. We also have schemas for all the built-in systems, and will have schemas for all systems once Extensions are in place.

We are looking into how we can design a high-level configuration, and corresponding user interface, that builds upon these features.

The goal is to make it much easier to configure Sesam, using visual tools and human friendly forms.

Clustered architecture for GDPR platform (Q4 2023)
==================================================

The GDPR platform subscriptions are still running on the single machine architecture, and are not able to use the latest features.

We are looking into how we can move the GDPR platform to the clustered architecture and how to migrate those subscriptions to the new architecture.

Multiple configurations
=======================

Today, one subscription can have multiple configuration groups, but they are all part of one big configuration that shares one namespace, metadata, environment variables, system roles and access rights.

We are looking into how one subscription can contain multiple standalone configurations in one shared instance.

Note that VPN will be tied to the shared instance so there will be some limitations to the VPN. There will also be limits on how many standalone configurations (tenants) you can have per single and multi compute. This feature will only be available on the 'Clustered architecture'.

The goal is for our partners to be able to serve their customers with standalone configurations from a shared instance.

Expose invoices and contracts in the Management Studio
===========================================

Invoices and contracts can be requested through support.

We are looking into how to expose invoices and contracts in the Management Studio to make them more accessible.

Extensions
==========

Microservices are second-class citizens in Management Studio. Setting up a microservice is done using
unstructured documentation (README, etc).

We are looking at how to structure and describe microservices so that
microservices can work and behave as built-in systems in Management Studio.

We are also looking into how we can use OAuth 2.0 Authorization Code Grant Type for extensions that
talk to providers that support this to make the authorization process more user friendly.

This will also open up the possibility for us to turn the built-in systems into separate extensions.

Composite Pipes
===============

Currently, you are not able to do DTL with dependency tracking when the source is not a pure dataset source. If the
source type is "merge" you need to create two pipes in order to merge and hop with dependency tracking.

You also need to create two pipes in order to use "create-child" and "emit_children".

We are looking into how to support this without requiring the user to create two pipes.

Public Preview
--------------

The following items are now available for experimental use.

.. _roadmap_property_lineage:

Property lineage
================

Properties in Sesam originate from external systems or are composed from other properties using DTL. The fact properties
are composed using introspectable DTL in combination with :ref:`schema inferencing <schema-inferencing>` allows us to continously track property lineage.

.. note::
  :ref:`Property lineage <property-lineage>` is now offered as part of :ref:`Integrated search <integrated-search>`.

.. _roadmap_metrics_api:

Metrics API
===========

We are looking into exposing subscription and pipe metrics in a Prometheus-compatible API to make it easy to use metrics in external tools.

This feature will most likely be offered as part of a new data option called "Metrics and monitoring" that bundles metrics and an unlimited number of pipe notifications.

.. note::
   :ref:`Metrics <metrics-api>` is now available for subscriptions running on the Clustered Architecture.

Integrated data browsing
========================

The current 'Databrowser' tool is hard to configure, not integrated into Management Studio and targeted at
external users.

We are looking at making a simpler tool that is integrated into Management Studio so that you
can do more efficient development. This new tool will replace the existing 'Databrowser' tool.

This feature will most likely only be available on the 'Clustered architecture',
so it depends on the 'Clustered architecture everywhere' item on the roadmap.

.. note::
   :ref:`Integrated search <integrated-search>` is now available for subscriptions running on the
   Clustered Architecture.

Generally Available
-------------------

The following items are now available for general use.

.. _roadmap_clustered_architecture:

Clustered architecture on all cloud subscriptions
===========================================================

Today we have two variants of Sesam (single machine and clustered). The two variants share most of their code, but
some parts are implemented in different ways. This makes some features harder for us to implement, and can cause
slight differences in behaviour between the two variants.

We are looking into how we can get the clustered architecture everywhere, and how to migrate all our cloud subscriptions to the new architecture.

.. note::
   All cloud subscriptions are now running on the clustered architecture.


Durable data
============

Data is backed up once every 24 hours. During a disaster recovery data written the last 24 hours can be lost. This is typically not a problem when Sesam is pulling data from sources, as the data that was lost can be pulled again.

For http_endpoint sources and non-idempotent sinks, this can be a problem.

We are looking into how to support durable data as an opt-in payed feature. This feature can then be enabled on relevant pipes.

.. note::
   :ref:`Durable data <durable-data>` is now available on all cloud subscriptions.

.. _roadmap_dev_pro:

Developer Pro
=============

For bigger projects that has a very high pipe count or microservices that require a lot of resources, the current Developer subscription with 1 engine can be underpowered.

We are investigating if we should introduce a new subcription size "Developer Pro" that will run 2 engines and be closer to a "Single" subscription with regards to performance. The fixed price for this new development subscription is estimated to €250/month.

.. note::
   :ref:`Developer Pro <pricing-developer>` is now available for new subscriptions and as an upgrade to existing subscriptions.

Self service VPN setup
======================

VPN setup can be requested through support.

We are looking into how to automate this process so that the end user can do this process faster.

.. note::
   :ref:`VPN <vpn-feature>` is now configurable for subscriptions running on the Clustered Architecture.
