.. _architecture-and-concepts-advanced:

Advanced
--------

.. _hops-1-3:

Hops
~~~~

Dependency tracking

Stacking av hops (dvs flere datasett) - recursion.

Indeksering

.. seealso::

  TODO

.. _incremental system queries-1-3:

Incremental System queries
~~~~~~~~~~~~~~~~~~~~~~~~~~

Inkrementelle spørringer mot databaser,
koble sammen historikk tabell med objekt tabell
for å få oppdatertDato f.eks

.. seealso::

  TODO

.. _subset-1-3:

Subset
~~~~~~

Grabbing the rdf:type or type of data you need from a global.

Reference filter. What are the pros and cons on filter on rdf type vs subset
subset supports 1 rdf, filter supports many.
processing time.

Maybe we keep this and remove "Source Subset" from DTL - 3

.. seealso::

  TODO

.. _dynamic-static-timeseries-data-1-3:

Dynamic, Static & Timeseries Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Dynamic data = frequent updates to the same object
| Static data = rare/never update to the same object
| Timeseries = Frequent new entities about the same object. (f.ex \_id =
  meterpoint & timestamp and attribute attached is reading the last
  hour)

.. seealso::

  TODO

.. _when-to-use-a-microservice-1-3:

When to use a microservice
~~~~~~~~~~~~~~~~~~~~~~~~~~

For everything Sesam is bad at or can’t do.

.. seealso::

  TODO

.. _eventual-consistency:

Eventual Consistency
~~~~~~~~~~~~~~~~~~~~

Dependency tracking causes reprocessing of source entity in the pipe
with the hops.

Idempotency

.. seealso::

  TODO

.. _create-child-emit-children:

Create Child & Emit children
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Change-tracking

.. seealso::

  TODO

.. _tasks-for-architecture-and-concepts-advanced:

Tasks for Architecture and Concepts: Advanced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
