========
Overview
========

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
------------

Sesam is a general purpose data integration and processing platform. It is optimised for collecting or receiving data from source systems, transforming data, and pushing or providing data to target systems. Sesam stores data in datasets. A dataset is a log of data entities with additional indexes for efficient random access and lookups. Data is fetched from the source systems on a regular basis and the entities are stored in the log only if they have changed from the last time the entity was seen.

Entities in the datasets can be processed using the Data Transformation Language. DTL takes a stream of entities as input and returns a new stream of transformed entities. It can join data from other datasets to create new entities. Data produced via DTL can be stored in new datasets to be exposed or sent to applications that need it.

The final piece of Sesam is to deliver data from a dataset to a sink. Sinks are used to write data into target systems or send it to service endpoints.

Sesam provides implementations for many types of data sources, including relational databases, LDAP, and MongoDB. It also provides a number of core Sink implementations such as the SQL and HTTP Post sinks.

Installation
------------

`Installation instructions <https://beta.sesam.in/#installation>`_ can be found on the `Sesam Beta website <https://beta.sesam.in/#installation>`_. Once it is installed and running, you can check the Sesam Management Studio `here <http://localhost:9042/gui>`_.

.. _overview-getting-started:

Getting Started
---------------

Now that you have Sesam running, lets start using it. Sesam does not yet contain any configuration nor any data, so lets get hold of some. We've prepared a sample project that showcases some of the core features of Sesam. The files are hosted on Github.

Check out the project files using ``git``:

::
   
  git clone https://github.com/sesam-io/tutorial sesam-tutorial
  cd sesam-tutorial/intro


If you don't have a Git client, then you can download the project files as a zip-file using ``curl``:

::

  curl -o sesam-tutorial.zip https://codeload.github.com/sesam-io/tutorial/zip/master
  unzip sesam-tutorial.zip
  mv tutorial-master sesam-tutorial
  cd sesam-tutorial/intro

The project contains three files. ``sesam.conf.json`` is the configuration file. ``customers.json`` and ``orders.json`` contain JSON data for customers and their orders.

First we'll start an HTTP server to serve the JSON files containing the data. To do this we can use the built-in Python HTTP server that serves the files in the current directory. The Sesam service instance will then be able to download the data files from there.

::
   
  $ ls -lh
  total 24
  -rw-r--r--  1 geir.gronmo  wheel   269B May 31 13:10 customers.json
  -rw-r--r--  1 geir.gronmo  wheel   505B May 31 13:10 orders.json
  -rw-r--r--  1 geir.gronmo  wheel   1.7K May 31 13:10 sesam.conf.json
  
  $ python3 -m http.server
  Serving HTTP on 0.0.0.0 port 8000 ...

Now we're serving the ``customers.json`` and ``orders.json`` files through the web server on port 8000.

Before we import the Sesam service instances's we'll have to edit the ``sesam.conf.json``. Open the file in a text editor and replace ``YOUR-IP-HERE`` with the IP address of your machine, i.e. the IP address of the web server you just started. Hint: use the ``ifconfig`` or ``ipconfig`` command to find it.

In order to import the configuration file(s) from the command line we'll have to install the ``sesam`` client command line tool. It can be installed with the ``pip3 install -U sesamclient`` command (Python3 only).

::

  $ pip3 install -U sesamclient
  Collecting sesamclient
  Requirement already up-to-date: PyInstaller==3.2 in /usr/local/lib/python3.5/site-packages (from sesamclient)
  Requirement already up-to-date: pyyaml==3.11 in /usr/local/lib/python3.5/site-packages (from sesamclient)
  Requirement already up-to-date: appdirs==1.4.0 in /usr/local/lib/python3.5/site-packages/appdirs-1.4.0-py3.5.egg (from sesamclient)
  Requirement already up-to-date: nose==1.3.7 in /usr/local/lib/python3.5/site-packages/nose-1.3.7-py3.5.egg (from sesamclient)
  Requirement already up-to-date: requests==2.10.0 in /usr/local/lib/python3.5/site-packages (from sesamclient)
  Requirement already up-to-date: python-dateutil==2.5.3 in /usr/local/lib/python3.5/site-packages (from sesamclient)
  Requirement already up-to-date: ijson==2.3 in /usr/local/lib/python3.5/site-packages (from sesamclient)
  Requirement already up-to-date: setuptools in /usr/local/lib/python3.5/site-packages (from PyInstaller==3.2->sesamclient)
  Requirement already up-to-date: six>=1.5 in /usr/local/lib/python3.5/site-packages (from python-dateutil==2.5.3->sesamclient)
  Installing collected packages: sesamclient
    Found existing installation: sesamclient 0.1.7
      Uninstalling sesamclient-0.1.7:
        Successfully uninstalled sesamclient-0.1.7
  Successfully installed sesamclient-0.2.18

Now that the ``sesam`` tool is installed we can use it to import the configuration file:

::
   
  $ sesam import *.conf.json
  Read 4 config entities from these config-files:
   sesam.conf.json

This will import the ``sesam.conf.json`` :doc:`configuration file <configuration>` into the Sesam service instance via its service API.

The configuration file contains two pipes that read data from ``customers.json`` and  ``orders.json``. Each JSON file consists of an array of :doc:`entities <entitymodel>`. The pipes pump the entities into datasets called ``customers`` and ``orders`` respectively.

There is also a third pipe that reads the ``customers`` dataset and applies a :doc:`DTL <DTLReferenceGuide>` transform on the data. The transform will collect the orders for each customer, calculate the total sum for each order and the total sum for each customer. Customers with total order sum of less than 25.00 are filtered out. The resulting entities are then written to the ``customers-with-orders`` dataset.


Let's look at the data
======================

When Sesam starts up it reads the configuration file and schedules the pumps. It will then start running the pumps at regular intervals. Use the links below to introspect the datasets and the pipes. Replace ``localhost`` with the hostname of Sesam service instance.

See the contents of the ``customers`` dataset here:

.. parsed-literal::

  `<http://localhost:9042/api/datasets/customers/entities>`_

See the contents of the ``orders`` dataset here:

.. parsed-literal::

  `<http://localhost:9042/api/datasets/orders/entities>`_

After a little while you should be able to see the end result in the ``customers-with-orders`` dataset:

.. parsed-literal::

  `<http://localhost:9042/api/datasets/customers-with-orders/entities>`_

You can also see the data as it is written to the pipe's sink. These entities have been read from the source and put through the DTL transform:

.. parsed-literal::

  `<http://localhost:9042/api/pipes/customers-with-orders/entities>`_

It may also be useful to see what the entities look like before they are transformed, i.e. what they look like when read from the pipe's source:

.. parsed-literal::

  `<http://localhost:9042/api/pipes/customers-with-orders/entities?transformed=false>`_

Make your own edits
===================

You may want to try to do some edits to the data files or the configuration file.

The Sesam service will reload the data files at regular intervals, so any edits you make to it will be picked up automatically. The pipes defined in the configuration will pump at regular intervals, so edits to ``customers.json`` and ``orders.json`` will also be reflected in the datasets. Try editing any of the files and see what happens.

If you edit the configuration file, then you must reimport it.

What to do next?
================

First, we strongly recommend reading the :doc:`concepts section <concepts>` to understand the sesam way of thinking. Then, there are three main things to 'do' with Sesam; get data in the hub, transform data, and get it out to other systems. 

To get more data into the hub take a look at the datasource component types that are natively supported. The :doc:`configuration <configuration>` section details the datasource component types and how to configure them.

If you don't see one here that you need then you can also create your own simple service to expose JSON data that can be consumed by Sesam. The documentation on :doc:`developer extension points <extension-points>` has more examples and links to templates for C#, Node.js, Java and Python.

If you are looking to transform data into new shapes, or validate it against schema rules, please take a look at the different kinds of transforms that can be used in a pipe. :doc:`DTL <DTLReferenceGuide>` is a very powerful language that can reshape, and connect data from multiple datasets. 

Finally, when you have data you want to deliver out to other systems or just expose for them to consume it you can use the sink components. The :doc:`configuration <configuration>` has documentation on all the natively supported sinks. Again, if there is not a sink for a system you have it is straight forward to set up sesam to push data to a custom service. 
