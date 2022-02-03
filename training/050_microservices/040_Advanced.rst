
.. _microservices-advanced-5-3:

Advanced
--------

.. _using-a-microservice-as-output-in-sesam-5-3:

Using a Microservice as Output in Sesam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Ukjent: Business logikk

Eventual Consistency 1.4.30

NB!! \_properties blir med ut!! NB!!

Filter

\_filtered - blir ikke sendt videre

\_deleted - blir sendt videre

Endpoints fjerner namespaces

Batching/streaming

NB! siste batch sendt fra sesam er alltid en tom liste

.. seealso::

  TODO

.. _looking-inside-an-output-microservice-5-3:

Looking inside an Output Microservice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create vs update
 - f.eks skal sende payload mot /create hvis API
   svarer at entitet ikke finnes fra før,
   eller sende mot /update hvis den finnes.

Formattering

Transparens (minst mulig transformasjon i microservice)

transit-encoding fra sesam

Logging

Gi gode feilmeldinger på http, catch spesifikke exceptions

Batching/streaming

NB! siste batch sendt fra sesam er alltid en tom liste

.. seealso::

  TODO

.. _guidelines-for-microservice-development-5-3:

Guidelines for Microservice Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check if it already exists

Documentation: Readme

Define Scope

Gjenbrukbarhet

Sesamutils

Templates

Env var for dynamiske MS’er

Videreutvikling

Release/tagging

Ref. Optimalisering 5.3.17 (yield spesielt)

Requirements.txt

.. seealso::

  TODO

.. _microservices-and-vcs-5-3:

Microservices and Version Control Systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lisenser

For community bruk

For privat bruk

Community github/slack/stackoverflow

Krav til microservices i sesam-community

Videreutvikling

Release/tagging

Byggserver – Travis, Azure ContainerRegistry

For community bruk

For privat bruk

Reference the “5.2.8 Changing a Microservice” for workflow

Ref appendix with complete microservice workflow (create a sequence
diagram Gabriell/Daniel?)

.. seealso::

  TODO

.. _optimizing-a-microservice-5-3:

Optimizing a Microservice
~~~~~~~~~~~~~~~~~~~~~~~~~

Minnebruk

Streaming / Yield

Delta/last seen

Transparens (minst mulig transformasjon i microservice)

.. seealso::

  TODO

.. _microservice-system-types-5-3:

Microservice System types
~~~~~~~~~~~~~~~~~~~~~~~~~

Lots of examples!

How should microservices which read or write to/from these types work?
What have we learned?

Source & Sink

Apier

   Paging

   Update VS Create

Filer

sFtp

SOAP

.. seealso::

  TODO


.. _testing-5-3:

Testing
~~~~~~~



Env vars

Lokal testing

Returnerer riktig format (json som sesam kan lese)

Unit testing

[Experimental] Undersøke:

| [Experimental] Morten? (docker-compose att: Gabriell)
|  

[Experimental] !!NB!! Definer testing i ms // Lag en test-ms-template //
Implementer MVP testing på sesam-community [great expectations
python-lib Daniel har info]!!

.. seealso::

  TODO

.. _proxy-endpoint-5-3:

Proxy Endpoint [Jonas]
~~~~~~~~~~~~~~~~~~~~~~

Kan lage en ms med frontend f.eks og eksponere den fra sesam

.. seealso::

  TODO

.. _chaining-5-3:

Chaining
~~~~~~~~

Ref advanced system 2.4.13.

.. seealso::

  TODO

.. _tasks-for-microservices-advanced-5-3:

Tasks for Microservices: Advanced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run a microservice in Sesam [could be sink, http, source]

Create a microservice
