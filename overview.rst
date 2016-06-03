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

Now that you have Sesam running, lets start using it.

Download project files
======================

The Sesam service does not yet contain any configuration nor any data, so lets get hold of some. We've prepared a sample project that showcases some of the core features of Sesam. The files are hosted on Github.

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

The project contains three files:

* ``sesam.conf.json`` is the configuration file.
* ``customers/customers.json`` contain customer data.
* ``orders/orders.json`` contain order data.

::

  $ ls -l
  drwxr-xr-x  3 nobody  wheel   102 Jun  2 11:48 customers
  drwxr-xr-x  3 nobody  wheel   102 Jun  2 09:49 orders
  -rw-r--r--  1 nobody  wheel  1921 Jun  2 09:50 sesam.conf.json
  
  $ ls -l customers/
  -rw-r--r--  1 nobody  wheel  269 Jun  2 09:49 customers.json
  
  $ ls -l orders/
  -rw-r--r--  1 nobody  wheel  505 Jun  2 09:49 orders.json

Serve data files
================

First we'll start an HTTP server to serve the JSON files containing the data. To do this we can use the built-in Python HTTP server that serves the files in the current directory. The Sesam service instance will then be able to download the data files from there.

::

  $ python3 -m http.server
  Serving HTTP on 0.0.0.0 port 8000 ...

Now we're serving the ``customers.json`` and ``orders.json`` files through the web server on port 8000. Look at what's being served by running the following ``curl`` command. Alternatively you can open the URLs in your web browser.

::
   
  $ curl http://localhost:8000/customers/customers.json
  [
      {"_id": "1",
       "first_name": "John",
       "last_name": "Smith",
       "age": 42},
      {"_id": "2",
       "first_name": "Maria",
       "last_name": "Hawkins",
       "age": 32},
      {"_id": "3",
       "first_name": "Pam",
       "last_name": "Curie",
       "age": 21}
  ]

::

  $ curl http://localhost:8000/orders/orders.json
  [
      {"_id": "1000",
       "customer_id": "1",
       "items": [
           {"ean": "978-1852493110", "price": 22.10, "quantity": 2 }
       ],
       "discount": 4.20},
      {"_id": "1001",
       "customer_id": "1",
       "items": [
           {"ean": "978-0937381939", "price": 73.50, "quantity": 1 },
           {"ean": "978-0060005719", "price": 10.40, "quantity": 1 }
       ]},
      {"_id": "1002",
       "customer_id": "2",
       "items": [
           {"ean": "978-0195367133", "price": 39.95, "quantity": 1 }
       ]}
  ]

As you you can see, the JSON files all contain arrays of objects, aka :doc:`entities <entitymodel>`.

Install the ``sesam`` command line tool
=======================================

In order to import the configuration file(s) from the command line we'll have to install the `sesam command line client <commandlineclient.html>`_ first. It can be installed with the ``pip3 install -U sesamclient`` command (Python3 only).

::

  $ pip3 install -U sesamclient
  Collecting sesamclient
  ...
  Successfully installed sesamclient-x.y.z

Edit the configuration files
============================

Before we import the configuration into the Sesam service we'll have to edit the ``sesam.conf.json``. Open the file in a text editor and replace the two ``YOUR-IP-HERE`` tokens with the IP address of your machine, i.e. the IP address of the web server you just started. Hint: use the ``ifconfig`` (or ``ipconfig``) command to find it.

If your IP address is ``10.4.100.94`` then the two ``customer-system`` and ``order-system`` URL `systems <concepts.html#systems>`_ entities should look like this:

::
   
    {
        "_id": "customer-system",
        "type": "system:url",
        "base_url": "http://10.4.100.94:8000/customers/"
    },

::
   
    {
        "_id": "order-system",
        "type": "system:url",
        "base_url": "http://10.4.100.94:8000/orders/"
    },

Import the configuration file
=============================

Now that the ``sesam`` tool is installed we can use it to import the configuration file:

::
   
  $ sesam import *.conf.json
  Read 5 config entities from these config-files:
   sesam.conf.json

The imports the ``sesam.conf.json`` :doc:`configuration file <configuration>` into the Sesam service instance via its `service API <api.html>`_ running at ``http://localhost:9042/api/``. As you can see from the output, five configuration entities were imported. Of those, three are `pipes <concepts.html#pipes>`_ and two are `systems <concepts.html#systems>`_.

The configuration file contains two `pipes <concepts.html#pipes>`_ that read data from ``customers.json`` and  ``orders.json``. Each JSON file consists of an array of :doc:`entities <entitymodel>`. The pipes pump the entities into datasets called ``customers`` and ``orders`` respectively.

There is also a third pipe that reads the ``customers`` dataset and applies a :doc:`DTL <DTLReferenceGuide>` transform on the data. The transform will collect the orders for each customer, calculate the total sum for each order and the total sum for each customer. Customers with total order sum of less than 25.00 are filtered out. The resulting entities are then written to the ``customers-with-orders`` dataset.

If you now look at the Sesam Management Studio you'll now see that there are two systems, ``order-system`` and ``customer-system``. They both point towards the *datahub*, which means that the data is flowing in that direction.

.. image:: images/studio-after-import.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept


Let's look at the data
======================

When Sesam starts up it reads the configuration file and schedules the pumps. It will then start running the pumps at regular intervals. Use the links below to introspect the datasets and the pipes. Replace ``localhost`` with the hostname of Sesam service instance.

See the contents of the ``customers`` dataset here:

.. parsed-literal::

  `<http://localhost:9042/api/datasets/customers/entities>`_

::

  $ curl -s http://localhost:9042/api/datasets/customers/entities | python3 -m json.tool --sort-keys
  [
      {
          "_deleted": false,
          "_hash": "96a224b5a726e512329924148906c7f9",
          "_id": "1",
          "_previous": null,
          "_ts": 1464862200576348,
          "_updated": 0,
          "age": 42,
          "first_name": "John",
          "last_name": "Smith"
      },
      {
          "_deleted": false,
          "_hash": "e93d14baf12d457cd095c852535b5e61",
          "_id": "2",
          "_previous": null,
          "_ts": 1464862200576496,
          "_updated": 1,
          "age": 32,
          "first_name": "Maria",
          "last_name": "Hawkins"
      },
      {
          "_deleted": false,
          "_hash": "833e9ce9bd1d70546f934cd505e09c54",
          "_id": "3",
          "_previous": null,
          "_ts": 1464862200576636,
          "_updated": 2,
          "age": 21,
          "first_name": "Pam",
          "last_name": "Curie"
      }
  ]

See the contents of the ``orders`` dataset here:

.. parsed-literal::

  `<http://localhost:9042/api/datasets/orders/entities>`_

::

  $ curl -s http://localhost:9042/api/datasets/orders/entities | python3 -m json.tool --sort-keys
  [
      {
          "_deleted": false,
          "_hash": "9f941366206e74c4e3ff583665bad61e",
          "_id": "1000",
          "_previous": null,
          "_ts": 1464862211437648,
          "_updated": 0,
          "customer_id": "1",
          "discount": "~f4.20",
          "items": [
              {
                  "ean": "978-1852493110",
                  "price": "~f22.10",
                  "quantity": 2
              }
          ]
      },
      {
          "_deleted": false,
          "_hash": "f9e5976f46173bc95847def79eaf22f8",
          "_id": "1001",
          "_previous": null,
          "_ts": 1464862211437926,
          "_updated": 1,
          "customer_id": "1",
          "items": [
              {
                  "ean": "978-0937381939",
                  "price": "~f73.50",
                  "quantity": 1
              },
              {
                  "ean": "978-0060005719",
                  "price": "~f10.40",
                  "quantity": 1
              }
          ]
      },
      {
          "_deleted": false,
          "_hash": "ce51eccc66843a0d156c6c9742c428e7",
          "_id": "1002",
          "_previous": null,
          "_ts": 1464862211438129,
          "_updated": 2,
          "customer_id": "2",
          "items": [
              {
                  "ean": "978-0195367133",
                  "price": "~f39.95",
                  "quantity": 1
              }
          ]
      }
  ]

The customer and order data read into Sesam ended up in two datasets, ``customers`` and ``orders``. When entities are written into the dataset some extra metadata properties are added. You can see these in the output above. They all start with and underscore character ("``_``").

* ``_id``: This is the *primary key* of the entity.
* ``_deleted``: A boolean flag that says if the entity is deleted or not.
* ``_hash``: A hash signature value that is generated from the entity data. This hash is used to find out if the entity has changed or not. When writing to a dataset only actual changes are written to it, so if the hash is the same then the entity is not updated.
* ``_ts``: A real-world timestamp saying when the entity was added to the dataset (in milliseconds since January 1st).
* ``_updated``: The sequence number of the entity in the dataset.
* ``_previous``: A pointer to the sequence number of the previous version of the entity. In our example data these are all ``null`` because we have not made any changes yet.

Transformed output
==================

After a little while, when the datasets are loaded and the ``customers-with-orders`` pump has run, you should be able to see the end result in the ``customers-with-orders`` dataset:

.. parsed-literal::

  `<http://localhost:9042/api/datasets/customers-with-orders/entities>`_

::

  $ curl -s http://localhost:9042/api/datasets/customers-with-orders/entities | python3 -m json.tool --sort-keys
  [
      {
          "_deleted": false,
          "_hash": "6dc1762b8a10fef2c3f21e42adebfa97",
          "_id": "1",
          "_previous": null,
          "_ts": 1464862214782937,
          "_updated": 0,
          "name": "John Smith",
          "order_count": 2,
          "orders": [
              {
                  "items": [
                      {
                          "ean": "978-0937381939",
                          "price": "~f73.50",
                          "quantity": 1
                      },
                      {
                          "ean": "978-0060005719",
                          "price": "~f10.40",
                          "quantity": 1
                      }
                  ],
                  "total": "~f83.90"
              },
              {
                  "discount": "~f4.20",
                  "items": [
                      {
                          "ean": "978-1852493110",
                          "price": "~f22.10",
                          "quantity": 2
                      }
                  ],
                  "total": "~f40.00"
              }
          ],
          "total": "~f123.90",
          "type": "customer"
      },
      {
          "_deleted": false,
          "_hash": "938545634032901188497db3c621a5ba",
          "_id": "2",
          "_previous": null,
          "_ts": 1464862214783137,
          "_updated": 1,
          "name": "Maria Hawkins",
          "order_count": 1,
          "orders": [
              {
                  "items": [
                      {
                          "ean": "978-0195367133",
                          "price": "~f39.95",
                          "quantity": 1
                      }
                  ],
                  "total": "~f39.95"
              }
          ],
          "total": "~f39.95",
          "type": "customer"
      }
  ]

It may also be useful to see what the entities look like before they are transformed, i.e. what they look like when read from the pipe's source:

.. parsed-literal::

  `<http://localhost:9042/api/pipes/customers-with-orders/entities?transformed=false>`_
  
You can also see the data as it is written to the pipe's sink. These entities have been read from the source and put through the DTL transform:

.. parsed-literal::

  `<http://localhost:9042/api/pipes/customers-with-orders/entities>`_

Make your own edits
===================

You may want to try to do some edits to the data files or the configuration file.

The Sesam service will reload the data files at regular intervals, so any edits you make to it will be picked up automatically. The pipes defined in the configuration will pump at regular intervals, so edits to ``customers.json`` and ``orders.json`` will also be reflected in the datasets. Try editing any of the files and see what happens.

If you edit the configuration file, then you must reimport it.

Let's add a new order for the customer with id ``2`` (Maria Hawkins). Open ``orders.json`` in your favourite text editor and add the following at the end of the JSON array:

::

    {"_id": "1003",
     "customer_id": "2",
     "items": [
         {"ean": "978-0295332333", "price": 19.95, "quantity": 1 }
     ]}


After the ``orders`` pump has run we can then see that the new order has been added to the ``orders``dataset:

::
   
  $ curl -s http://localhost:9042/api/datasets/orders/entities | python3 -m json.tool --sort-keys
  [
      ...,
      {
          "_deleted": false,
          "_hash": "ab2a87d29ac4f6ead83e6e954e1f65e9",
          "_id": "1003",
          "_previous": null,
          "_ts": 1464936747758861,
          "_updated": 3,
          "customer_id": "2",
          "items": [
              {
                  "ean": "978-0295332333",
                  "price": "~f19.95",
                  "quantity": 1
              }
          ]
      }
  ]

What happens next is a little piece of magic. Sesam does something called `dependency tracking <concepts.html#dependency-tracking>`_. It figures out that Maria Hawkins has received a new order, and that her ``customers`` entity must be reprocessed. Dependency tracking adds her existing entity to the head of the dataset with ``_tracked`` property set to ``true``. It is able to do this because it can infer it from the DTL transformation rules in the ``customers-with-orders`` pipe.

::
   
  $ curl -s http://localhost:9042/api/datasets/customers/entities | python3 -m json.tool --sort-keys
  [
      ...,
      {
          "_deleted": false,
          "_hash": "e93d14baf12d457cd095c852535b5e61",
          "_id": "2",
          "_previous": 1,
          "_tracked": true,
          "_ts": 1464936749252271,
          "_updated": 3,
          "age": 32,
          "first_name": "Maria",
          "last_name": "Hawkins"
      }
  ]

The result of this is then that the entity is processed by the ``customers-with-orders`` pipe, effectively reprocessing the customer entity. The result of this will then look like this:

::

  $ curl -s http://localhost:9042/api/datasets/customers-with-orders/entities | python3 -m json.tool --sort-keys
  [
      ...,
      {
          "_deleted": false,
          "_hash": "938545634032901188497db3c621a5ba",
          "_id": "2",
          "_previous": null,
          "_ts": 1464862214783137,
          "_updated": 1,
          "name": "Maria Hawkins",
          "order_count": 1,
          "orders": [
              {
                  "items": [
                      {
                          "ean": "978-0195367133",
                          "price": "~f39.95",
                          "quantity": 1
                      }
                  ],
                  "total": "~f39.95"
              }
          ],
          "total": "~f39.95",
          "type": "customer"
      },
      {
          "_deleted": false,
          "_hash": "ded8824e5ec508efc6bbbc036afa052e",
          "_id": "2",
          "_previous": 1,
          "_ts": 1464936772791645,
          "_updated": 2,
          "name": "Maria Hawkins",
          "order_count": 2,
          "orders": [
              {
                  "items": [
                      {
                          "ean": "978-0195367133",
                          "price": "~f39.95",
                          "quantity": 1
                      }
                  ],
                  "total": "~f39.95"
              },
              {
                  "items": [
                      {
                          "ean": "978-0295332333",
                          "price": "~f19.95",
                          "quantity": 1
                      }
                  ],
                  "total": "~f19.95"
              }
          ],
          "total": "~f59.90",
          "type": "customer"
      }
  ]

The end result is that Maria Hawkins now have *two* orders. The ``total`` property has also been updated to reflect the fact that there is a new order. Note also that the ``_previous`` property now has a value. It points back to the previous version of the entity. This way Sesam can track the history of entities.

What to do next?
================

First, we strongly recommend reading the :doc:`concepts section <concepts>` to understand the sesam way of thinking. Then, there are three main things to 'do' with Sesam; get data in the hub, transform data, and get it out to other systems. 

To get more data into the hub take a look at the datasource component types that are natively supported. The :doc:`configuration <configuration>` section details the datasource component types and how to configure them.

If you don't see one here that you need then you can also create your own simple service to expose JSON data that can be consumed by Sesam. The documentation on :doc:`developer extension points <extension-points>` has more examples and links to templates for C#, Node.js, Java and Python.

If you are looking to transform data into new shapes, or validate it against schema rules, please take a look at the different kinds of transforms that can be used in a pipe. :doc:`DTL <DTLReferenceGuide>` is a very powerful language that can reshape, and connect data from multiple datasets. 

Finally, when you have data you want to deliver out to other systems or just expose for them to consume it you can use the sink components. The :doc:`configuration <configuration>` has documentation on all the natively supported sinks. Again, if there is not a sink for a system you have it is straight forward to set up sesam to push data to a custom service. 
