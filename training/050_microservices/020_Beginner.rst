
.. _microservices-beginner-5-1:

Beginner
--------


.. _what-is-a-microservice-5-1:

What is a microservice?
~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Microservices are...

  - modular self-contained services
  - hosted as docker containers
  - configured and monitored as Sesam Systems

Microservices are modular self-contained software programs that provide a particular service.

In a Sesam perspective they can function as connectors to either pull data from a source system,
push data to a target system or transform data as part of a step inside a pipe.

Microservice code can essentially be written in any programming language, but in Sesam we usually
prefer Python 3.

Microservices are hosted in Sesam as docker containers. They are configured using
system configs and their logs can be inspected through the system's **Status** tab.

.. seealso::

  :ref:`getting-started` > :ref:`getting-started-microservices`

  :ref:`developer-guide` > :ref:`configuration` > :ref:`system_section` > :ref:`microservice_system`

.. _why-use-microservices-in-sesam-5-1:

Why use Microservices in Sesam?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  When built-in connectors are insufficient, use microservices.

Most of the time you can use Sesam's build-in connectors to access
external systems, but sometimes you will find that you need to connect
to systems that are not natively supported by Sesam.

In these cases you either find an existing microservice and reuse it as is,
tweak it a bit to fit your needs, or simply write your own from scratch.

The Sesam communities at GitHub and DockerHub are great places to look
for microservices to reuse and tweak to your specific needs.

.. seealso::

  `Sesam's community at GitHub <https://github.com/sesam-community>`_

  `Sesam's community at DockerHub <https://hub.docker.com/u/sesamcommunity>`_

.. _how-are-microservices-used-in-sesam-5-1:

How are Microservices used in Sesam?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  Microservices in Sesam are:

  - defined in system configs
  - hosted in docker containers

To get a better understanding of how microservices are used in Sesam,
let us look at a concrete example.

Assume we want to pull data from SAP and that we have been provided
the following information about the SAP system:

- hosted at ``https://sap.service.com/api``
- data is exposed as OData
- username ``sap-user``
- password ``sap-very-secret-password``

Looking throught the list of Systems under :ref:`configuration`
we see that Sesam does not have a built-in connector for OData.
However we are in luck, browsing
`Sesam's community at GitHub <https://github.com/sesam-community>`_
we find there are several OData microservices to choose from.

.. TODO: get sap-odata-source into sesam-community!
.. Just using this MS now because of familiarity.

Let us go with the `sap-odata-source` microservice
(https://github.com/ga-hegsvold/sap-odata-source).

Reading up on the docs for this microservice we are provided with
information about where to find the docker image, which docker environment
variables to supply, and also examples of system and pipe configurations.

For this particular microservice there are two authentication alternatives:
"basic" with username and password or "token" with a JWT.
Since we have been supplied a username and password we go with the "basic" option.

Based on the information we now have, we can see that the microservice
requires the following docker environment variables:

`SERVICE_URL` - Base url to the Odata Service API

`AUTH_TYPE` - Authentication method ("basic" or "token")

`USERNAME` - Username to authenticate with the Odata Service

`PASSWORD` - Password to authenticate with the Odata Service

We also need to supply a link to the docker image for the microservice.

When setting up a new system config in Sesam it is a good idea to start with defining
the various Sesam environment variables and secrets needed.
This is to avoid awkward warnings and error messages as Sesam will warn you if there are references
to undefined environment variables and secrets in a system or pipe config.

`AUTH_TYPE` can be hardcoded in the system config as it will most likely be the
same in all Sesam environments (dev, test, prod, etc.).
The remaining docker environment variables will probably differ in the various
Sesam environments so these are good candidates to put into Sesam environment variables
or secrets.
We define these under **Datahub > Variables**:

.. code-block:: JSON

  "sap-service-url": "https://sap.service.com/api",
  "sap-username": "sap-username"

.. warning::
  Passwords and other sensitive values should never be put into Sesam environment variables
  as they are stored in plain text. Put them into secrets instead.

So let us put the SAP password in a secret called ``sap-password``.

With the Sesam environment variables and secrets defined, we can now create a new system config
for the SAP system. Let us call it `sap`:

.. code-block:: JSON
  :linenos:
  :emphasize-lines: 3, 11

  {
    "_id": "sap",
    "type": "system:microservice",
    "docker": {
      "environment": {
        "AUTH_TYPE": "basic",
        "PASSWORD": "$SECRET(sap-password)",
        "SERVICE_URL": "$ENV(sap-service-url)",
        "USERNAME": "$ENV(sap-username)"
      },
      "image": "gamh/sap-odata-source",
      "port": 5000
    },
    "verify_ssl": true
  }

Line 3 is where the system is defined as a microservice.

Line 11 is the reference to the docker image for the microservice.

When the system config is saved, Sesam will automatically try to
spin up a docker container, based on the referenced docker image, to host the microservice.
We will look more into this in the sections below.

.. seealso::

  :ref:`learn-sesam` > :ref:`architecture_and_concepts` > :ref:`architecture-and-concepts_beginner-1-1` > :ref:`naming-conventions-1-1`

  :ref:`learn-sesam` > :ref:`systems` > :ref:`systems-beginner-2-1` > :ref:`how-to-create-a-system-with-templates-2-1`

  :ref:`learn-sesam` > :ref:`systems` > :ref:`systems-beginner-2-1` > :ref:`environment-variables-secrets-2-1`

  `OData (Open Data Protocol) <https://www.odata.org/>`_

  Env.var / secrets naming convensions (Should add a section about this under Architecture & Concepts)

.. _microservice-hosting-5-1:

Microservice hosting
~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Summary

  - Microservice source code is hosted in `Sesam's community at GitHub <https://github.com/sesam-community>`_
  - Microservice docker images are hosted in `Sesam's community at DockerHub <https://hub.docker.com/u/sesamcommunity>`_
  - Auto-build scripts publish docker images to Sesam's community at DockerHub
  - `Sesam Community Guidelines <https://github.com/sesam-community/guidelines>`_

We have already touched on Sesam's communities at GitHub and DockerHub
to find available microservices. Let us take a more detailed look at how
microservice hosting is done with Sesam.

We have `Sesam's community at GitHub <https://github.com/sesam-community>`_
for hosting microservice source code,
and we have `Sesam's community at DockerHub <https://hub.docker.com/u/sesamcommunity>`_
for hosting microservice docker images.

When writing microservices we recommend putting the source code into
Sesam's community at GitHub so that it can be shared and reused in other projects
(unless there are specific restrictions in place).

By configuring the microservices using Sesam's auto-build script, when the
source code is pushed to GitHub, the script will automatically build a docker image
and publish it to Sesam's community at DockerHub.

From there the microservices will be available for use in any Sesam project.

See the `Sesam Community Guidelines <https://github.com/sesam-community/guidelines>`_
for more information on how to use the auto-build script and also how to contribute in general.

.. seealso::

  `Sesam's community at GitHub <https://github.com/sesam-community>`_

  `Sesam's community at DockerHub <https://hub.docker.com/u/sesamcommunity>`_

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

.. _categories-of-microservices-5-1:

Categories of Microservices
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extending on the topic of running microservices in Sesam, the following categories of microservices will be elaborated on in this section:

  - Internal microservices
  - External microservices

Both internal and external microservices will be defined in a Sesam node as systems. However, microservices that connect to a Sesam node via the `Service API <https://docs.sesam.io/api.html>`_ can also be seen on the `Sesam Community on GitHub <https://github.com/sesam-community>`_. These kinds of microservices will not be elaborated on in this section, albeit you should be aware that these microservices exist and that they are also a viable option when extending upon default functionality.


Internal microservices
######################

These kinds of microservices are the ones used with regards to Sesam dataflows. Therefore, these are also the most commonly used. Internal microservices can be used at specific points in time with regards to a dataflow. As such, internal microservices can be used in the beginning, in the middle or at the end of a dataflow, which will respectively, in a Sesam node, turn out as a source system, http-transform system or sink system. Many of these internal microservices can be found on the `Sesam Community on GitHub <https://github.com/sesam-community>`_.


External microservices
######################

External microservices can be hosted inside your Sesam node as a system or outside of your Sesam node in your preferred docker-compatible solution like for example Kubernetes. They do not read or write data into or out of Sesam with regards to a defined dataflow. Rather, they implement their functionality in such a way that does not affect dataflows.

An example of such a microservice is the `Github Autodeployer <https://github.com/sesam-community/github-autodeployer>`_. This microservice connects to the GitHub API and uploads the latest version of files present on the GitHub repository in question to a Sesam node. This allows for continous integration/continous deployment (CICD) workflows and allows for easy peer reviews as changes are made to specific pipe configs.

Additional examples of external examples are listed below:

    - `Statuspage <https://github.com/sesam-community/statuspage>`_
    - `Statuspage Monitoring Pipes <https://github.com/sesam-community/statuspage-monitoring-pipes>`_


.. seealso::

  :ref:`developer-guide` > :ref:`configuration` > :ref:`system_section` > :ref:`microservice_system`

  :ref:`learn-sesam` > :ref:`systems` > :ref:`systems-beginner-2-1` > :ref:`pipe-interaction-with-systems-2-1`

  `Sesam Community at GitHub <https://github.com/sesam-community>`_

  `Sesam Community Guidelines <https://github.com/sesam-community/guidelines>`_

Tasks for Microservices: Beginner – Tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. *What is a microservice in Sesam?*

#. *Why do we use microservices in Sesam?*

#. *Make a microservice successfully run in Sesam.*

    Hint: `Sesam Community at GitHub <https://github.com/sesam-community>`_ is a good place to get inspiration.

    Condition: Successfull, in this case, means that the docker image spins up as intended.

#. *Read data from your newly created microservice into a pipe.*

    Condition: Make sure data flows through the pipe and creates a dataset.
