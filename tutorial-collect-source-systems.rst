.. _tutorial-collect-source-systems:

Source systems in Sesam
=======================

.. admonition:: Prerequisites

  You should have completed the :ref:`getting started guide <getting-started>` before starting on this tutorial.

Sesam supports implementing multiple different :ref:`system types <system_section>`, i.e: JSON, SQL, microservice etc. Each system, regardless of type, will have a defined set of implementation functionalities which can be set in its DTL configuration. As such, the intended usage in Sesam should be taken into consideration when implementing a System.


.. admonition:: Objectives

  What are the objectives of this tutorial? What will the user have on his subscription if this tutorial is finished?

  - Objective 1
  - Objective 2
  - Objective 3

When a System is used as a source it is especially important to recognize that providing streams of entities as these are updated in the source system as a :ref:`delta stream <delta-stream-processing>`, ensures that Sesam can propagate data changes through a :ref:`Sesam dataflow <creating-a-sesam-dataflow>` quickly and efficiently, even if the amount of data residing in the source System increases exponentially. As such, avoiding bulk readings of data, as the amount of data residing in your source System increases, should be avoided.

With the above in mind, let us create a source system in Sesam.

.. important::
  
  It is important to remember the following about source systems in Sesam:

  - Should provide streams of entities as input to the pipes they are connected to
  - Can provide entities with **any** shape
  - Must provide Sesam with a unique identifier called ``_id``

The source system you will be working with in this tutorial is Twelvedata. `Twelvedata <https://twelvedata.com/>`_ provides the user with insight concerned with financial data. You will connect to Twelvedata in Sesam with the use of the system type :ref:`REST <rest_source>` and you will create operations that support only GET. The resources you will request are "stock" and "exchange" information. 

As the REST API for Twelvedata stock exchange is open, you can easily connect and pull data from this system.

We created a template to get you started. Follow these steps to to add `Twelvedata <https://twelvedata.com/>`_ as a system:

#. Log in to `Sesam portal <https:portal.sesam.io>`_
#. Select the subscription you want to work on
#. Navigate to **Systems**
#. Click on **New system**
#. Paste and save the following DTL configuration:

.. code-block:: json
  :linenos:

  {
    "_id": "twelvedata",
    "type": "system:rest",
    "operations": {
      "exchanges": {
        "method": "GET",
        "url": "exchanges"
      },
      "stocks": {
        "method": "GET",
        "url": "stocks"
      }
    },
    "url_pattern": "https://api.twelvedata.com/%s",
    "verify_ssl": true,
    "worker_threads": 2
  }

After having successfully created your REST system, you are now ready to move onto the next tutorial on :ref:`inbound pipes <tutorial-collect-inbound-pipes>` to start using your recently created REST system. 

.. hint::

  You should get acquainted with all properties provided in the above DTL configuration. To read about them, you should explore the :ref:`REST <rest_source>` section of the docs.







