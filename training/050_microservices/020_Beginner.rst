
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

  - Microservice source code is hosted in `Sesam's community at GitHub <https://github.com/sesam-community>`_
  - Microserice docker images are hosted in `Sesam's community at DockerHub <https://hub.docker.com/u/sesamcommunity>`_
  - Auto-build scripts publish docker images to Sesam's community at DockerHub
  - `Sesam Community Guidelines <https://github.com/sesam-community/guidelines>`_

We have already touched on the Sesam Community at GitHub and DockerHub
to find available microservices. Let us take a more detailed look at how
microservice hosting is done with Sesam.

There is the `Sesam Community at GitHub <https://github.com/sesam-community>`_
for hosting microservice source code,
and there is the `Sesam Community at DockerHub <https://hub.docker.com/u/sesamcommunity>`_
for hosting microservice docker images.

When writing microservices we recommend putting the source code into
Sesam's community at GitHub so that it can be shared and reused in other projects
(unless there are specific restrictions in place).

By configuring the microservices using Sesam's auto-build script, when the
source code is pushed to GitHub, the script will automatically build a docker image
and publish it to Sesam's DockerHub community.

From there the microservices will be available for use in any Sesam project.

See the `Sesam Community Guidelines <https://github.com/sesam-community/guidelines>`_
for more information on how to use the auto-build script and also how to contribute in general.

.. seealso::

  `Sesam Community at GitHub <https://github.com/sesam-community>`_

  `Sesam Community at DockerHub <https://hub.docker.com/u/sesamcommunity>`_

  `Sesam Community Guidelines <https://github.com/sesam-community/guidelines>`_

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
