=======
Roadmap
=======

.. contents:: Table of Contents
   :depth: 2
   :local:

This roadmap highlights some of features we are currently working on. This roadmap might be subject to
change.

Scalable architecture everywhere (Q4 2021)
------------------------------------------

Today we have two variants of Sesam (single machine and clustered). The two variants share most of their code, but
some parts are implemented in different ways. This makes some features harder for us to implement, and can cause
slight differences in behaviour between the two variants.

We are looking into how we can get the clustered architecture everywhere.

This architecture is based on Kubernetes
and might open up the possibility of running Sesam in a self-hosted Kubernetes cluster.

Extensions
----------

Microservices are second-class citizens in Management Studio. Setting up a microservice is done using
unstructured documentation (README, etc).

We are looking at how to structure and describe microservices so that
microservices can work and behave as builtin systems in Management Studio.

This will also open up the possibility for us to turn the builtin systems into separate extensions.

Age based deletion marker compaction
------------------------------------

If Sesam has seen an entity it will remember the 'id' for this entity forever. This also applies to entities that was
seen but no longer exists in the source.

These deletion markers are required for incremental synchronizing of data, but once all the consumers have read the
deletion marker it only has historic value.

We are looking into how to be able to configure a time to live on these deletion markers so that old history can be
cleaned up.

Expose invoices and contracts in the portal
-------------------------------------------

Invoices and contracts can be requested through support.

We are looking into how to expose invoices and contracts in the portal to make them more accessible.

Durable data
------------

Data is backed up once every 24 hours. During a disaster recovery data written the last 24 hours can be lost. This is typically not a problem when Sesam is pulling data from sources, as the data that was lost can be pulled again.

For http_endpoint sources and non-idempotent sinks, this can be a problem.

We are looking into how to support durable data as an opt-in payed feature. This feature can then be enabled on relevant pipes.

High level configuration
------------------------

The current user interface is built around configuring pipes, which is a low level building block in Sesam. We have now estabilished best practices that describes the patterns you should use to build a robust and extensible Sesam solution using pipes. We also have schemas for all the built-in systems, and will have schemas for all systems once Extensions are in place.

We are looking into how we can design a high level configuration and corresponding user interface that builds upon these features.

The goal is to make it much easier to configure Sesam, using visual tools and human friendly forms.
