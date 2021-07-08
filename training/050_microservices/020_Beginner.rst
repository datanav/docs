
.. _microservices-beginner-5-1:

Microservices: Beginner
-----------------------


.. _what-is-a-microservice-5-1:

What is a microservice?
~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Microservices are...
  
  - modular self-contained services
  - hosted as docker containers
  - confgured and monitored as Sesam Systems

Microservices are modular self-contained software programs that provide a particular service.

In a Sesam perspective they can function as connectors to either pull data from a source system,
push data to a target system or transform data as part of a step inside a pipe.

Microservice code can essentially be written in any programming language, but in Sesam we usually
prefer Python 3.

Microservices are hosted in Sesam as docker containers. They are configured using
system configs and their logs can be inspected through the system's **Status** tab.

.. seealso::

  Getting started: :ref:`getting-started-microservices`

  Developer Guide > Service Configuration > Systems: :ref:`microservice_system`

.. _why-use-microservices-in-sesam-5-1:

Why use Microservices in Sesam?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System som gjør ting andre systemer ikke kan

.. seealso::

  TODO

.. _how-are-microservices-used-in-sesam-5-1:

How are Microservices used in Sesam?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ekte Use caser

.. seealso::

  TODO

.. _microservice-hosting-5-1:

Microservice hosting
~~~~~~~~~~~~~~~~~~~~

Sesamcommunity Git & Docker

Intro til Hosting

.. seealso::

  TODO

.. _running-a-microservice-in-sesam-5-1:

Running a microservice in Sesam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Intro til Running I sesam

Forklare GUI

Pull & Restart

   Status

   Refresh

Forklare Config

Pipe source/sink/http

.. seealso::

  TODO

.. _types-of-microservices-5-1:

Types of Microservices
~~~~~~~~~~~~~~~~~~~~~~

   Interne

   http-transform

   Source, sink (begge i 1?)

   Eksterne

   Monitorering av Sesam

.. seealso::

  TODO

.. _naming-convention-5-1:

Naming Convention this should probs be under architecture namegiving conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\_id standard system naming convention (source/sink system name)

Repo/microservice naming convention recommendation:
sesam-<system>[-<special-functionality>]

.. seealso::

  TODO

.. _tasks-for-microservices-beginner-tasks-5-1:

Tasks for Microservices: Beginner – Tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run a microservice in Sesam [could be sink, http, source]
