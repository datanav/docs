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

If you follow the :ref:`getting-started` guide, the api will be served on the url you find on the
management studio "settings" page under the "Connection url" heading. For a cloud instance it will typically be on
the form "https://instance-guid.sesam.cloud/api".

All references to this URL in this document should be substituted with the real URL for your Sesam instance.
The rest of this document will assume that the api can be found on this URL.

The API documentation is also self-hosted and can be explored using the `Swagger <https://swagger.io>`_ user interface
at "<host:port>/api/reference".

Most API calls will require you to authenticate using a `JWT token <https://jwt.io/>`_ .

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

Get a list of all the pipes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With curl:

::

    curlJWT https://instance-guid.sesam.cloud/api/pipes


Get information about one specified pipe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To only get one specific pipe, add the pipe's "_id" attribute to the pipes-url. To get the pipe with the _id "Northwind:Products",
you would do this:

With curl:

::

    curlJWT https://instance-guid.sesam.cloud/api/pipes/Northwind:Products



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



Get a list of all the datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With curl:

::

    curlJWT https://instance-guid.sesam.cloud/api/datasets



Get information about one specific dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To only get one specific dataset, add the dataset's "_id" attribute to the dataset-url. To get the dataset with the _id "Northwind:Products",
you would do this:

With curl:

::

    curlJWT https://instance-guid.sesam.cloud/api/datasets/Northwind:Products



Get the content of the dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To see the entities in the dataset, add "/entities?limit=3" to the dataset's url, like this:

With curl:

::

    curlJWT https://instance-guid.sesam.cloud/api/datasets/Northwind:Products/entities?limit=3

The "limit" parameter limits the number of returned entities to a managable number. Without this parameter, **all**
the entities in the dataset would be returned. Depending on the size of the dataset, that could take a while, so it is
generally a good idea to include a "limit"-parameter.


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


.. _api-reference:

Instance API Reference
======================

..
   TODO pull swagger from somewhere instead of having a copy here
.. openapi:: ./swagger_public.yaml

Portal API Reference
====================

..
   TODO pull swagger from somewhere instead of having a copy here
.. openapi:: ./swagger_portal.yaml

Swagger Files
=============

To access the Swagger endpoint for your instance go to ``https://<your-instance>/api/reference``.

For the Portal API go to the `Autogenerated Swagger Endpoint for the Portal <https://portal.sesam.io/api/reference>`_.


.. _api-config-groups:

Config groups
=============

There are multiple ways to configure a sesam-node. One way is to add and modify single systems and
pipes via these endpoints:

`/api/pipes/{pipe_id}/config GET <./api.html#get--pipes-pipe_id-config>`_

`/api/pipes/{pipe_id}/config PUT <./api.html#put--pipes-pipe_id-config>`_

`/api/systems/{systems_id}/config GET <./api.html#get--systems-system_id-config>`_

`/api/systems/{systems_id}/config PUT <./api.html#put--systems-system_id-config>`_

Another way is to upload the configuration for multiple systems and pipes as via these endpoints:

`/api/config GET <./api.html#get--config>`_

`/api/config PUT <./api.html#put--config>`_

`/api/config/{config-group} GET <./api.html#get--config-config-group>`_

`/api/config/{config-group} PUT <./api.html#put--config-config-group>`_

Regardless of which endpoint is used, each pipe or system is placed in a **config-group**. For the first set of
of endpoints the config-group is specified by adding a "$config-group"-property to the "metadata"-property in
the configuration. Example::

    {
      "_id": "testpipe",
      "type": "pipe",
      "metadata": {
        "$config-group": "my-first-group"
      }
    }

For the second set of endpoints the config-group is specified in the url. In either case, if no config-group is
explicitly given, the pipe/system is placed in the "default" config-group (i.e. the `/api/config PUT <./api.html#put--config>`_
endpoint places the uploaded config into the "default" config-group).

Note: The `/api/config PUT <./api.html#put--config>`_ and `/api/config/{config-group} PUT <./api.html#put--config-config-group>`_
endpoints will replace **all** the config in the specified config-group.
