===================
Command line client
===================

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
============

Sesam provides a commandline client for controlling the service and for working with the data in the datahub.

The commandline client works by sending http-requests to the Sesam (:ref:`api-top`). You can therefore in principle use
for instance `curl <http://manpages.ubuntu.com/manpages/lucid/man1/curl.1.html>`_ to do everything that you can do with
the commandline client. The purpose of the commandline client is to make the api functionality easier accessable from
the commandline.

Installing the client
=====================

If you followed the :ref:`overview-getting-started` guide, the sesam service will be running on the url http://localhost:9042/api .

The commandline client is distributed as a python package, so you will need python (v3.4 or later) in order to install
and run it:

1. Download and install the latest version of python from https://www.python.org/downloads. Depending on your OS, the
   installer might ask you if you want to add python to the machine's executable path. You want to answer yes to this.
   For instance: the MS Windows installer has a checkbox called "Add Python 3.5 to PATH" that you need to check.
2. Install the sesamclient package with python's package manager "pip". Open a new commandline window and run this command

::

   pip3 install -U sesamclient

The sesam client will now be available on the commandline as "sesam".


Commands overview
=================
The most important thing to know is the "help" option (-h), which is available for the commandline client as a whole, and
for individual commands

::

    sesam -h

    sesam config -h

    sesam get-datasets -h

This will print out detailed usage instructions. This information is also available in
the :ref:`commandline-client-reference` part of this document.


The most important commands are

::

   sesam get-pipes

This returns a list of pipes. For an explanation of what a pipe is, read the :ref:`concepts-pipes` concept definition.

::

   sesam get-datasets

This returns a list of datasets. (For an explanation of what a dataset is, read the :ref:`concepts-datasets` concept definition).


Example usage
=============

In the following section we will go through a few examples of what you can do with the commandline client. For a complete
description of all the commands and options, have a look at the :ref:`commandline-client-reference` section.

Setting the API URL endpoint
----------------------------

You can either supply the URL to the API endpoint using the ``--server_base_url <URL>`` parameter (usually the last one on
the command line), or you can set it permanently for the logged in user using:

::

  sesam config server.base_url <URL>

If none of these options are used, the sesam client will fall back to a default value for the base URL of the API which
is ``http://localhost:9042/api``.

Get the a list of all the pipes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   sesam get-pipes


Get information about one specified pipe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To only get one specific pipe, use the "get-pipe" command with the pipe's "_id". To get the pipe with the _id "Northwind:Products",
you would do this::

   sesam get-pipe Northwind:Products

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

These operations are triggered calling the appropriate command with the pipe's "_id" as the argument. For example:
to disable the "Northwind:Products" pipe you would do this::

   sesam stop-pump Northwind:Products


To manually start the pipe's pump, you would do this::

   sesam start-pump Northwind:Products

To stop a running pump, you would do this::

   sesam stop-pump Northwind:Products


Get a list of all the datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    sesam get-datasets


Get information about one specific dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To only get one specific dataset, use the "get-dataset" command with the dataset's "_id" as an argument.
To get the dataset with the _id "Northwind:Products", you would do this::

    sesam get-dataset Northwind:Products


Get the content of a dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To see the entities in a dataset, use the "get-dataset-entities" command, like this::

    sesam get-dataset-entities --limit 3 Northwind:Products

The "limit" parameter limits the number of returned entities. Without this parameter, **all** the entities in the
dataset would be returned. Depending on the size of the dataset, that could take a while, so it is
generally a good idea to include a "limit"-parameter if you just want to have a quick look at what the dataset
contains.



.. _commandline-client-reference:

Commandline client Reference
============================

This section contains detailed reference documentation for the commandline client. All this information is also available
from the commandline client itself, via the "-h" option. Examples::

   sesam -h

   sesam config -h

   sesam get-datasets -h

.. argparse::
   :module: sesamclient.main
   :func: get_parser_used_by_sphinx_argparse_extension
   :prog: sesam
