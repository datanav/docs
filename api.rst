.. _api-top:

===
API
===

.. contents:: Table of Contents
   :depth: 2
   :local:


Introduction
============

Sesam provides a RESTful API for controlling the service and for working with the data in the datahub.

If you follow the :ref:`overview-getting-started` guide, the api will be served on the url http://localhost:9042/api . The
rest of this document will assume that the api can be found on this url.

You can explore the api with a web browser or with a commandline tool like `curl <http://manpages.ubuntu.com/manpages/lucid/man1/curl.1.html>`_
or `wget <http://manpages.ubuntu.com/manpages/lucid/man1/wget.1.html>`_.

The most important api urls are:

`/api/pipes <http://localhost:9042/api/pipes>`_:

This returns a list of pipes. For an explanation of what a pipe is, read the :ref:`concepts-pipes` concept definition.


`/api/datasets <http://localhost:9042/api/datasets>`_:

This returns a list of datasets. (For an explanation of what a dataset is, read the :ref:`concepts-datasets` concept definition).

For a full description of the /pipes and /datasets endpoint, read the "Pipes" and
"Dataset" sections in the :ref:`api-reference`.


Examples
--------

In the following we will go through a few examples of what you can do with the api. We will use the `curl <http://manpages.ubuntu.com/manpages/lucid/man1/curl.1.html>`_
command to interact with the api from the command line (If you are using MS Windows you can install for instance cygwin
in order to use the curl command).




Get the a list of all the pipes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    curl http://localhost:9042/api/pipes


Get information about one specified pipe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To only get one specific pipe, add the pipe's "_id" attribute to the pipes-url. To get the pipe with the _id "Northwind:Products",
you would do this::

    curl http://localhost:9042/api/pipes/Northwind:Products

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
pipe you would do this::

   curl --data operation=disable http://localhost:9042/api/pipes/Northwind:Products/pump


To manually start the pipe's pump, you would do this::

   curl --data operation=start http://localhost:9042/api/pipes/Northwind:Products/pump

To stop a running pump, you would do this::

   curl --data operation=stop http://localhost:9042/api/pipes/Northwind:Products/pump


Get a list of all the datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    curl http://localhost:9042/api/datasets


Get information about one specific dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To only get one specific dataset, add the dataset's "_id" attribute to the dataset-url. To get the dataset with the _id "Northwind:Products",
you would do this::

    curl http://localhost:9042/api/datasets/Northwind:Products


Get the content of the dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To see the entities in the dataset, add "/entities?limit=3" to the dataset's url, like this::

    curl http://localhost:9042/api/datasets/Northwind:Products/entities?limit=3

The "limit" parameter limits the number of returned entities to a managable number. Without this parameter, **all**
the entities in the dataset would be returned. Depending on the size of the dataset, that could take a while, so it is
generally a good idea to include a "limit"-parameter.

.. _sdshare_feed_from_dataset:

Get the content of the dataset as SDShare
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To see the entities in the dataset as a SDShare feed, add "/sdshare-fragments" to the dataset's url, like this::

    curl http://localhost:9042/api/datasets/Northwind:Products/sdshare-fragments

Parameters such as ``limit`` also apply to this URL.

The corresponding SDShare collection feed is available from::

    curl http://localhost:9042/api/datasets/Northwind:Products/sdshare-collection

This collection feed URL is usually the URL you need to supply in a SDShare client.

Note that for the conversion of the entities to RDF to work, the entities must either:

    1) be pre-processed to consists of full URIs for all properties (including the ``_id`` property)

*or*:

    2) be pre-processed to CURIEs form **AND** the dataset id need to be registered as en entry in the :ref:`RDF registry <rdf_registry>` with appropriate prefix settings and prefix rules.

See :doc:`rdf-support` for more information on how to prepare your data for RDF output.

.. _api-reference:

API Reference
=============

.. contents::
   :local:
   :depth: 1

.. cornice-autodoc::
   :modules: lake.node.webapp.api.root,
             lake.node.webapp.api.pipes,
             lake.node.webapp.api.receivers,
             lake.node.webapp.api.publishers,
             lake.node.webapp.api.metadata,
             lake.node.webapp.api.datasets,
             lake.node.webapp.api.systems,
             lake.node.webapp.api.status,
             lake.node.webapp.api.logs,
             lake.node.webapp.api.config,
             lake.node.webapp.api.configcheck,
             lake.node.webapp.api.license
