
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

To get a better understanding of how microservices work in Sesam,
let us look at a concrete example.

Assume we want to pull data from SAP. SAP provides data as OData.
Sesam does not have a built-in connector for OData.
However we are in luck, browsing the Sesam community at GitHub we
find there are several OData microservices to choose from.

.. get sap-odata-source into sesam-community!

Let us go with the `sap-odata-source` microservice (https://github.com/ga-hegsvold/sap-odata-source).

Reading up on the docs for this microservice we are provided with
information about where to find the docker image, which environment variables
to specify, and also examples of system and pipe configurations.
For this particular microservice there are two authentication alternatives:
"basic" with username and password or "token".

Let us assume we have been supplied a SAP username and password so we go with the "basic" option.
Let us further assume the SAP service is hosted at `https://sap.service.com/api`.

When setting up a new system config in Sesam it is a good idea to start with defining
the various environment variables needed.
This is to avoid awkward warnings and error messages as Sesam will warn you if there are references
to undefined environment variables in a system or pipe config.

Based on the information we have so far the microservice requires the following docker environment variables:

`SERVICE_URL` - Base url to the Odata Service API

`AUTH_TYPE` - Authentication method ("basic" or "token")

`USERNAME` - Username to authenticate with the Odata Service

`PASSWORD` - Password to authenticate with the Odata Service

We also need to supply a link to the docker image for the microservice.

`AUTH_TYPE` can be hardcoded in the system config as it will not likely change.
The remaining docker environment variables are good candidates to put
into Sesam environment variables. So let us do that:

.. code-block:: JSON

  "sap-service-url": "https://sap.service.com/api",
  "sap-username": "my-username"

Let us assume we put the SAP password in a secret called ``sap-password``.

With the environment variables and secrets defined, we can now create a new system config.
Let us call it `sap`:

.. code-block:: JSON
  :linenos:

  {
    "_id": "sap",
    "type": "system:microservice",
    "docker": {
      "environment": {
        "AUTH_TYPE": "basic",
        "PASSWORD": "$SECRET(sap-password)",
        "SERVICE_URL": "https://sap.service.com/api",
        "USERNAME": "$EVN(sap-username)"
      },
      "image": "gamh/sap-odata-source"
      "port": 5000
    },
    "verify_ssl": true
  }

.. seealso::

  OData

  How to define env.varrs

  How to create Systems

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
