.. _api-top:

===========
Service API
===========

.. contents:: Table of Contents
   :depth: 2
   :local:


Introduction
============

Sesam provides a RESTful API for controlling the service and for working with the data in the datahub.

If you follow the :ref:`overview-getting-started` guide, the api will be served on the url you find on the
management studio "settings" page under the "Connection url" heading. For a cloud instance it will typically be on
the form "https://instance-guid.sesam.cloud/api".

All references to this URL in this document should be substituted with the real URL for your Sesam instance.
The rest of this document will assume that the api can be found on this URL.

The API documentation is also self-hosted and can be explored using the `Swagger <http://swagger.io>`_ user interface
at "<host:port>/api/reference".

Most API calls will require you to authenticate using a `JWT token <https://jwt.io/>`_ .

When using the :doc:`Sesam command line client <commandlineclient>`  you can get a token using its ``login`` command:

::

  sesam login --server_base_url https://instance-guid.sesam.cloud/api

This will prompt you for your username and password, download a JWT token and store it locally. All subsequent
``sesam client`` commands will then use this token.

.. _using_jwt_token:

You can also use a commandline tool like `curl <http://manpages.ubuntu.com/manpages/lucid/man1/curl.1.html>`_
or `wget <http://manpages.ubuntu.com/manpages/lucid/man1/wget.1.html>`_ to explore the API. This will be the most
useful approach if you are planning to communicate with Sesam using a script or a program.

When using ``curl`` to access the API url's directly, you will need to supply the JWT token for each HTTP request.
Here's an example that creates an ``alias`` for curl that does this for you (remember to change the example URL to your
real sesam instance URL):

::

    # Create a text-file with the email and password you use to log in to Sesam:
    echo "email=YOUR_EMAIL_ADDRESS&password=YOUR_PASSWORD" > cred.txt

    # Download the authorization token for the specified email and password and store it in an environment variable:
    export SESAM_AUTH_HEADER="Authorization: Bearer $(curl -d @cred.txt https://instance-guid.sesam.cloud/api/jwt)"

    # Make an alias to run curl with the authorization token:
    alias curlJWT='curl -H "$SESAM_AUTH_HEADER"'

You can then substitute ``curl`` with ``curlJWT`` in all calls to the API. The rest of this document assumes that
you have created this alias.

Note that if you are communicating with the API using your own program or script, you must remember to set the HTTP
header property "Authorization" to the string "Bearer " concatenated with the token you get from the command:

::

  curl -d @cred.txt https://instance-guid.sesam.cloud/api/jwt

This was built-in to the shell script snippet we used to set up the ``culrJWT`` alias previously; the
"cred.txt" file contains the text "email=YOUR_EMAIL_ADDRESS&password=YOUR_PASSWORD" without the quotes and substituted
with your real username and password. For security reasons, remember to remove the ``cred.txt`` file after you have
retrieved the JWT token.

The most important api urls are:

``/api/pipes`` (i.e. https://instance-guid.sesam.cloud/api/pipes)

This returns a list of pipes. For an explanation of what a pipe is, read the :ref:`concepts-pipes` concept definition.

``/api/datasets`` (i.e. https://instance-guid.sesam.cloud/api/datasets)

This returns a list of datasets. (For an explanation of what a dataset is, read the :ref:`concepts-datasets` concept definition).

For a full description of the /pipes and /datasets endpoint, read the "Pipes" and
"Dataset" sections in the :ref:`api-reference`.

Examples
--------

In the following we will go through a few examples of what you can do with the api. As mentioned previously, we will use
the ``curlJWT`` alias we created to interact with the api from the command line. If you are using MS Windows you can
install for instance `Cygwin <http://cygwin.com>`_ in order to install and use the curl command (and create the ``curlJWT`` alias).

Get the a list of all the pipes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With curl:

::

    curlJWT https://instance-guid.sesam.cloud/api/pipes

Using the Sesam client (after first having done ``sesam login``- see the start of this document):

::

   sesam get-pipes --server_base_url https://instance-guid.sesam.cloud/api

Get information about one specified pipe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To only get one specific pipe, add the pipe's "_id" attribute to the pipes-url. To get the pipe with the _id "Northwind:Products",
you would do this:

With curl:

::

    curlJWT https://instance-guid.sesam.cloud/api/pipes/Northwind:Products

Using the Sesam client:

::

   sesam get-pipe Northwind:Products --server_base_url https://instance-guid.sesam.cloud/api


Run operations on a pipe
~~~~~~~~~~~~~~~~~~~~~~~~
A pipe typically has a number of operations that can be triggered via the api. These are listed in the
pipeinfo["runtime"]["supported-operations"] attribute. A typical value looks like this::

   "supported-operations": [
               "enable",
               "disable",
               "start",
               "stop"
           ]

These operations are triggered by sending a POST-request to the url /pipes/{pipeID}/pump. For example: to disable the "Northwind:Products"
pipe you would do this:

With curl:

::

   curlJWT --data operation=disable https://instance-guid.sesam.cloud/api/pipes/Northwind:Products/pump

Using the Sesam client:

::

   sesam get-pipe Northwind:Products --server_base_url https://instance-guid.sesam.cloud/api


To manually start the pipe's pump, you would do this:

With curl:

::

   curlJWT --data operation=start https://instance-guid.sesam.cloud/api/pipes/Northwind:Products/pump

::

   sesam start-pump Northwind:Products --server_base_url https://instance-guid.sesam.cloud/api


To stop a running pump, you would do this:

With curl:

::

   curlJWT --data operation=stop https://instance-guid.sesam.cloud/api/pipes/Northwind:Products/pump

Using the Sesam client:

::

   sesam stop-pump Northwind:Products --server_base_url https://instance-guid.sesam.cloud/api


Get a list of all the datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With curl:

::

    curlJWT https://instance-guid.sesam.cloud/api/datasets

Using the Sesam client:

::

   sesam get-datasets --server_base_url https://instance-guid.sesam.cloud/api


Get information about one specific dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To only get one specific dataset, add the dataset's "_id" attribute to the dataset-url. To get the dataset with the _id "Northwind:Products",
you would do this:

With curl:

::

    curlJWT https://instance-guid.sesam.cloud/api/datasets/Northwind:Products

Using the Sesam client:

::

   sesam get-dataset Northwind:Products --server_base_url https://instance-guid.sesam.cloud/api


Get the content of the dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To see the entities in the dataset, add "/entities?limit=3" to the dataset's url, like this:

With curl:

::

    curlJWT https://instance-guid.sesam.cloud/api/datasets/Northwind:Products/entities?limit=3

The "limit" parameter limits the number of returned entities to a managable number. Without this parameter, **all**
the entities in the dataset would be returned. Depending on the size of the dataset, that could take a while, so it is
generally a good idea to include a "limit"-parameter.

Using the Sesam client:

::

   sesam get-dataset-entities Northwind:Products --limit 3 --server_base_url https://instance-guid.sesam.cloud/api


.. _sdshare_feed_from_dataset:

Get the content of the dataset as SDShare
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To see the entities in the dataset as a SDShare feed, add "/sdshare-fragments" to the dataset's url, like this::

    curlJWT https://instance-guid.sesam.cloud/api/datasets/Northwind:Products/sdshare-fragments

Parameters such as ``limit`` also apply to this URL.

The corresponding SDShare collection feed is available from::

    curlJWT https://instance-guid.sesam.cloud/api/datasets/Northwind:Products/sdshare-collection

This collection feed URL is usually the URL you need to supply in a SDShare client.

Note that for the conversion of the entities to RDF to work, the entities must either:

    1) be pre-processed to consists of full URIs for all properties (including the ``_id`` property)

*or*:

    2) be pre-processed to CURIEs form **AND** the dataset id need to be registered as en entry in the :ref:`RDF registry <rdf_registry>` with appropriate prefix settings and prefix rules.

See :doc:`rdf-support` for more information on how to prepare your data for RDF output.

Note that the SDShare feeds are not available through the Sesam client.

.. _api-reference:

API Reference
=============

.. contents::
   :local:
   :depth: 1

.. openapi:: ../lake/node/webapp/swagger_public.yaml

