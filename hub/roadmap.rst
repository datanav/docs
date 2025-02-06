.. _roadmap:

=======
Roadmap
=======

This roadmap highlights some of features we are currently working on. This roadmap might be subject to
change.

Planned
-------

Self-hosted clustered architecture (Q1 2025)
============================================

Today, self-hosted Sesam only supports the single machine variant. A lot of new features are only offered on the clustered architecture (e.g. Metrics API, Integrated Search), and are therefore not available on self-hosted subscriptions.

We are looking into self-hosting of the clustered architecture. This architecture is based on Kubernetes, and will require a running Kubernetes cluster. We will start testing on the most common Kubernetes services (Google GKE, Amazon EKS and Azure AKS).

Permanent deletion of history for selected entities (Q1 2025)
=============================================================

Datasets in Sesam by default keep a minimum of 2 versions of an entity in order to support dependency tracking. This also means that old data is preserved in the history of the entity.

This history can cause unwanted data to be preserved in the history.

We are looking into how one can mark an entity for permanent deletion so that the history is also cleared of the unwanted data.

Age-based deletion marker compaction (Q2 2025)
==============================================

If Sesam has seen an entity it will remember the 'id' of this entity forever. This also applies to entities that were
seen, but no longer exist in the source.

These deletion markers are required for incremental synchronizing of data, but once all the consumers have read the
deletion marker it only has historic value.

We are looking into how to be able to configure a time-to-live on these deletion markers so that old history can be
cleaned up.

Clustered architecture for GDPR platform (Q3 2025)
==================================================

The GDPR platform subscriptions are still running on the single machine architecture, and are not able to use the latest features.

We are looking into how we can move the GDPR platform to the clustered architecture and how to migrate those subscriptions to the new architecture.

Optimizing resources on multi compute subscriptions (2026)
==========================================================

The single compute subscription has a limitation to the number of pipes it can execute that depends on the data and transformations applied. The multi compute subscription does not have this limitation, but the price and the amount of resources it consumes are significantly higher.

We are looking into how we can optimize the resources on a multi compute subscription so that we consume less resources. Currently on multi compute each pipe is running in a separate worker process, and we will investigate if we can co-locate pipes on the same worker to optimize the resources. This might open up the possibility to offer new subscription plans that are priced in between single and multi compute subscriptions.

High-level configuration (2026)
==================================

The current user interface is built around configuring pipes, which is a low-level building block in Sesam. We have now established best practices that describe the patterns you should use to build a robust and extensible Sesam solution using pipes.

We are looking into how we can design a high-level configuration, and corresponding user interface, that builds upon these features.

The goal is to make it much easier to configure Sesam, using visual tools and human friendly forms.

Public Preview
--------------

The following items are now available for experimental use.

Webhooks
========

Today Sesam needs to pull frequently in order to detect changes in sources. For systems that support signalling through webhooks, this is inefficient and can be annoying for the system that is being pulled from. This is particularly bad for services that offer webhooks, and no other incremental support.

We are looking into how we can support webhooks to receive incremental changes, so that we can eliminate or reduce the polling frequency.

.. note::
  Support for :ref:`webhooks <webhook-feature>` is now available.

Reusable connectors
===================

Today, one can quickly build connectors by configuring our generic systems (e.g. SQL, REST), but there is not a simple way to reuse those configurations.

We are looking into how to package up a set of configurations in such a way that they can be reused across subscriptions.

.. note::
  Support for :ref:`connectors <connectors-feature>` are now available.

Multitenancy
============

Today, one has to get the credentials to the systems one would like to connect from an external source and inject them into a running subscription as secrets. For subscriptions that are built around multiple tenants building such a solution can be time consuming.

We are looking into building a configurable tenant facing application that allows a solution provider to get their tenants to onboard themselves, configure connectors and get insight into operational issues using a simple end user web interface.

This will be built on top of reusable connectors, and support connectors that use OAuth2 flows as well as services with simpler API key credentials.

.. note::
  Support for :ref:`multitenancy <multitenancy-feature>` is now available. Contact support@sesam.io for more information about pricing and how to set it up.

.. _roadmap_property_lineage:

Property lineage
================

Properties in Sesam originate from external systems or are composed from other properties using DTL. The fact properties
are composed using introspectable DTL in combination with :ref:`schema inference <schema_inference>` allows us to continuously track property lineage.

.. note::
  :ref:`Property lineage <property_lineage>` is now offered as part of :ref:`Integrated search <integrated_search>`.

Generally Available
-------------------

The following items are now available for general use.

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
   :ref:`Integrated search <integrated_search>` is now available for subscriptions running on the
   Clustered Architecture.

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
   Developer Pro is now available for new subscriptions and as an upgrade to existing subscriptions.

Self service VPN setup
======================

VPN setup can be requested through support.

We are looking into how to automate this process so that the end user can do this process faster.

.. note::
   :ref:`VPN <vpn-feature>` is now configurable for subscriptions running on the Clustered Architecture.
