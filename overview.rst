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

The Sesam service is run as either a single Sesam node or as a cluster of Sesam nodes. Each node has the capability to collect, transform and deliver data. However, various topologies of nodes can be used to separate concerns where needed. A cluster of Sesam Nodes can be accessed via single API endpoint. All nodes expose the Sesam API as way to control and introspect the node. When used in a cluster the nodes can be configured to expose an API over all the nodes in the cluster.

For getting started with Sesam a single node will suffice. The Sesam Node is available as a public docker image. If you install and use the docker node you are bound by the Sesam Node EULA agreement.

Docker version 1.9.1 is required. Download Docker `here <http://www.docker.com/>`_.

.. _overview-getting-started:

Getting Started
---------------

Once Docker is installed, pull the Sesam Node docker image, like this:

::

  docker pull sesam/sesam-node

Now you can start the Sesam Node container:

::

  docker run -it --rm -v /sesam/conf:/sesam/conf -v /sesam/data:/sesam/data -v /sesam/logs:/sesam/logs -p 9042:9042 --name sesam-node sesam/sesam-node start -c https://raw.githubusercontent.com/sesam-io/tutorial/master/intro/nodeconfig.json

This will start up the Sesam Node with a :doc:`node configuration file <configuration>` (`nodeconfig.json <https://github.com/sesam-io/tutorial/blob/master/intro/nodeconfig.json>`_) hosted on Github.

The node configuration file contains two pipes that read data from `customers.json <https://github.com/sesam-io/tutorial/blob/master/intro/customers.json>`_ and  `orders.json <https://github.com/sesam-io/tutorial/blob/master/intro/orders.json>`_. Each JSON file consists of an array of :doc:`entities <entitymodel>`. The pipes pump the entities into datasets called ``customers`` and ``orders`` respectively.

There is also a third pipe that reads the ``customers`` dataset and applies a :doc:`DTL <DTLReferenceGuide>` transform on the data. The transform will collect the orders for each customer, calculate the total sum for each order and the total sum for each customer. Customers with total order sum of less than 25.00 are filtered out. The resulting entities are then written to the ``customers-with-orders`` dataset.


Let's look at the data
======================

When the Sesam Node starts up it reads the configuration file and schedules the pumps. It will then start running the pumps at regular intervals. Use the links below to introspect the datasets and the pipes. Replace ``localhost`` with the hostname of your Docker service.

See the contents of the ``customers`` dataset here:

.. parsed-literal::

  `<http://localhost:9042/datasets/customers/entities>`_

See the contents of the ``orders`` dataset here:

.. parsed-literal::

  `<http://localhost:9042/datasets/orders/entities>`_

After a little while you should be able to see the end result in the ``customers-with-orders`` dataset:

.. parsed-literal::

  `<http://localhost:9042/datasets/customers-with-orders/entities>`_

You can also see the data as it is written to the pipe's sink. These entities have been read from the source and put through the DTL transform:

.. parsed-literal::

  `<http://localhost:9042/pipes/customers-with-orders/entities>`_

It may also be useful to see what the entities look like before they are transformed, i.e. what they look like when read from the pipe's source:

.. parsed-literal::

  `<http://localhost:9042/pipes/customers-with-orders/entities?transformed=false>`_

Make your own edits
===================

You may want to try to do some edits to the data files or the configuration file. To do this you must first download the files. Download them directly with ``curl``,

::

   curl -O https://raw.githubusercontent.com/sesam-io/tutorial/master/intro/nodeconfig.json
   curl -O https://raw.githubusercontent.com/sesam-io/tutorial/master/intro/customers.json
   curl -O https://raw.githubusercontent.com/sesam-io/tutorial/master/intro/orders.json
  
or check them out from Git:

::
   
  git clone https://github.com/sesam-io/tutorial sesam-tutorial
  cd sesam-tutorial/intro

You can now stop the running Sesam Node, because we need to start it up again with some slightly different arguments. Press CTRL+C, or run ``docker rm -f sesam-node`` in another terminal window.

Now you can start the Sesam Node container:

::

  docker run -it --rm -v $PWD:/sesam/conf -v /sesam/data:/sesam/data -v /sesam/logs:/sesam/logs -p 9042:9042 --name sesam-node sesam/sesam-node start

The Sesam Node will reload the ``nodeconfig.json`` file at regular intervals, so any edits you make to it will be picked up automatically. The pipes defined in the configuration will pump at regular intervals, so edits to ``customers.json`` and ``orders.json`` will also be reflected in the datasets. Try editing any of the files and see what happens.

Troubleshooting
===============

The ``docker run`` command above binds the current working directory to the ``/sesam/conf`` volume inside of the container. For this to work the ``nodeconfig.json`` file must exist. When the Sesam Node starts it will create two directories ``data``, which contains the node's persistent state - including the datasets, and ``logs``, which contains the human readable log files.

If you're on a Mac and use Virtualbox to host the docker service, then you won't be able to store the ``/sesam/data`` and ``/sesam/logs`` directory directly on the Mac's file system. Instead those files will have to be stored on the virtual machine where the docker daemon runs. Mounting the ``/sesam/conf`` through to the Mac's file system works though, because only read-only access is needed.
