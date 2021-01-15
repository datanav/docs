=======
Roadmap
=======

.. contents:: Table of Contents
   :depth: 2
   :local:

This roadmap highlights some of features we are currently working on. This roadmap might be subject to
change.

Background rescanning
---------------------

If you want to do a full rescan of the source of a pipe and the source is huge this will cause the pipe to stop
processing new data for a considerable amount of time.

We are looking at how to be able to do a full rescan while
at the same time process new data so that you can safely do full rescans without causing halt in the
data flow.

Lack of this feature makes it hard to enable 'automatic processing'.

Integrated data browsing
------------------------

The current 'Databrowser' tool is hard to configure, not integrated into Management Studio and targeted at
external users.

We are looking at making a simpler tool that is integrated into Management Studio so that you
can do more efficient development.

This feature will most likely only be available on the 'Scalable architecture',
so it depends on the 'Scalable architecture everywhere' item on the roadmap.

Extensions
----------

Microservices are second-class citizens in Management Studio. Setting up a microservice is done using
unstructured documentation (README, etc).

We are looking at how to structure and describe microservices so that
microservices can work and behave as builtin systems in Management Studio.

This will also open up the possibility for us to turn the builtin systems into separate extensions.

Scalable architecture everywhere
--------------------------------

Today we have two variants of Sesam (single machine and clustered). The two variants share most of their code, but
some parts are implemented in different ways. This makes some features harder for us to implement, and can cause
slight differences in behaviour between the two variants.

We are looking into how we can get the clustered architecture everywhere.

This architecture is based on Kubernetes
and might open up the possibility of running Sesam in a self-hosted Kubernetes cluster.

Age based deletion marker compaction
------------------------------------

If Sesam has seen an entity it will remember the 'id' for this entity forever. This also applies to entities that was
seen but no longer exists in the source.

These deletion markers are required for incremental synchronizing of data, but once all the consumers have read the
deletion marker it only has historic value.

We are looking into how to be able to configure a time to live on these deletion markers so that old history can be
cleaned up.

Logging data access
-------------------

Most of the data in Sesam is structured as an immutable log, so any write or change to Sesam is
automatically logged and audited. Reading of the data is only stored in rotated access logs that is not made
available to the end user.

We are looking into how to audit reads of data and make this available to the end user in a the form of a dataset.