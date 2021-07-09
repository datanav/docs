
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

.. sidebar:: Summary

  Microservices in Sesam are:

  - defined in system configs
  - hosted in docker containers

To get a better understanding of how microservices are used in Sesam,
let us look at a concrete example.

Assume we want to pull data from SAP and that we have been provided
the following information about the SAP system:

- hosted at `https://sap.service.com/api`
- data is exposed as OData
- username `sap-user`
- password `sap-very-secret-password`

Looking throught the list of Systems under :ref:`configuration`
we see that Sesam does not have a built-in connector for OData.
However we are in luck, browsing the
`Sesam community at GitHub <https://github.com/sesam-community>`_
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

  .. Testing to add refs as bread crumbs with links in each step except first step.
  .. Is this reader-friendly or too much?

  Learn Sesam > :ref:`architecture-and-concepts_beginner-1-1` > :ref:`naming-conventions-1-1`

  Env.var / secrets naming convensions (Should add a section about this under Architecture & Concepts)

  Learn Sesam > :ref:`systems-beginner-2-1` > :ref:`how-to-create-a-system-with-templates-2-1`

  Learn Sesam > :ref:`systems-beginner-2-1` > :ref:`environment-variables-secrets-2-1`

  `OData (Open Data Protocol) <https://www.odata.org/>`_

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
