
.. _microservices-beginner-5-1:

Microservices: Beginner
-----------------------


.. _what-is-a-microservice-5-1:

What is a microservice?
~~~~~~~~~~~~~~~~~~~~~~~



Nevn bruksområder

språk

Docker

.. seealso::

  TODO

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

.. sidebar:: Summary

  - Microservice source code is hosted in Sesam's community at GitHub
  - Microserice docker images are hosted in Sesam's community at DockerHub
  - Auto-build scripts publishes docker images to Sesam's community at DockerHub

Sesamcommunity Git & Docker

Intro til Hosting

We have already touched on the Sesam community at GitHub and DockerHub
to search for microservices. Let us take a more detailed look at how
microservice hosting is done in Sesam.

There is the Sesam comminity at GitHub for hosting microservice source code,
and there is the Sesam comminity at DockerHub for hosting the microservice
docker images which enabled Sesam to spin up docker containers as we
covered in the previous sections.

When writing microservices we recommend putting the source code into
Sesam's community at GitHub as Open Source
(unless there are specific restrictions in place).

By configuring the microservices using Sesam's Travis script, when the
source code is pushed to GitHub, Travis will automatically build a docker image
and publish it to Sesam's docker hub community.

From there the microservices will be available for use in virtually any
Sesam project.

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
