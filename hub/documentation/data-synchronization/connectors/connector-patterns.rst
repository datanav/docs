==================
Connector Patterns
==================

This document describes best practices on building and structuring connectors.

Two step collect
================

All datatypes should use a minimum of two pipes for the collect pipe line. These are named ``-all`` and ``-collect``. This gives extensibility if webhook events if they will be added later. If also gives us the possibility to verify deletion tracked entities in the collect template.

Deletion tracking of webhook events
===================================

Need to disable deletion tracking, as the dataset is never a complete list of entities. If this is not done, you will get false deletes in the collect dataset if they happen to be newer than the last version of the entity in the ``--all`` dataset.

Combine all and webhook events
==============================
When combining the ``-all`` and ``-event`` datasets, one should use the ``merge_datasets`` source as it will pick the version of the entity that has the most recent change. The ``-collect`` will with this pattern be the most representative copy we can get of the external data.

Receiving webhook events
========================
The pipe should be called ``-event``.

Partial webhook events
======================

Need to do a lookup to find the complete entity. Avoid doing the look up in the pipe that receives the event, as the lookup can take time and block the receiver. Instead set up a pipeline with two pipes and call the second one ``-event2``.

Shared webhook endpoint
=======================

If multitenant, receive all in one dataset and use subset expression with tenant id to filter out relevant events into tenant pipes. The tenant pipe should be called ``-event``.

Datatype naming
===============

Tooling currently requires datatype to be without delimiters or whitespace, and convention is to use lowercase. E.g. ``deal-company-association-type`` becomes ``dealcompanyassociationtype``.

Parameterized datatypes
=======================

Some datatypes are driven by other datatypes. E.g. fetching orderlines for each order. If this is the case, then orderlines are parameterized by orders. This should be represented as two datatypes. It is up the client of the connector to decide if they want to synchronise one or both of the data types.

Datatypes with lists of linked objects
======================================

Some datatypes contain a list of related objects in them. E.g. in Tripletex an order contains a list of orderline identifiers, but not any data about the orderline itself. We handle this by setting up a three step collect pipeline. First we have an ``-all`` pipe that uses ``create-child`` for each of the lines in the order. Then we have an ``-all2`` pipe that emits these children and in the ``-collect`` pipe we look up each of these identifiers. This pattern could probaby be improved a bit.

Datatypes should follow the API
===============================

The connector should follow the API as close as possible. This means that if the API exposes data about the same entity in different endpoints, the connector should also expose these endpoints as different data types.

