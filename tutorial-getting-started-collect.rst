:orphan:

.. _tutorial_getting_started_collect:

Collect data
============

In this tutorial we will look closer at how to connect Sesam to two different data providers: CRM and `Twelvedata <https://twelvedata.com/>`_. CRM is a data provider for i.e. company or person data whilst Twelvedata is a data provider containing financial data such as stock information. After having succesfully connected to these providers you will create inbound pipes for each relevant datatype we want to work with, as we go through a Sesam dataflow in the getting started guide.

.. admonition::  Objectives:

    After you complete this tutorial you will have learned the following:

    #. How to create systems
    #. How to create inbound pipes
    #. Import data from a data source into sesam

|
|

Create systems
^^^^^^^^^^^^^^

First, we will start by adding a new system for Twelvedata, which is an open data source. 

Follow the below steps in order to add Twelvedata as a system in Sesam:

In the `Sesam portal <https://portal.sesam.io/>`_:

#. Navigate to **Systems**
#. Click on **New system**
#. Paste and save the DTL configuration below

.. code-block:: json
  :linenos:

  {
	  "_id": "twelvedata",
	  "type": "system:rest",
	  "operations": {
	    "stocks": {
	      "method": "GET",
	      "url": "stocks"
	    }
	  },
	  "url_pattern": "https://api.twelvedata.com/%s",
	  "verify_ssl": true,
	  "worker_threads": 2
	}

Now we can add our second system, namely the CRM system.

In the `Sesam portal <https://portal.sesam.io/>`_:

#. Navigate to **Systems**
#. Click on **New system**
#. Paste and save the DTL configuration below

.. code-block:: json
  :linenos:

    {
	  "_id": "crm",
	  "type": "system:microservice",
	  "docker": {
	    "image": "sesamcommunity/learn-sesam-crm:v1.0.3",
	    "memory": 512,
	    "port": 5000
	  }
	}

After having successfully created both systems, you are now ready to move onto the next aspect of this tutorial, namely the creation of inbound pipes. 

|
|

Create inbound pipes
^^^^^^^^^^^^^^^^^^^^

Inbound pipes are the naming convention used for pipes that receive their data from a source system. 

The first inbound pipe we want to work on is the inbound pipe that connects to our ``twelvedata`` system. We want to pull in the ``stock`` datatype that exists in the Tvelwedata system. Follow the below steps to create your inbound pipe ``twelvedata-stock-collect``:

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the DTL configuration below
#. Press **Start** to ensure your pipe runs 

.. code-block:: json
  :linenos:
  
  {
    "_id": "twelvedata-stock-collect",
    "type": "pipe",
    "source": {
      "type": "rest",
      "system": "twelvedata",
      "id_expression": "{{ exchange }}-{{ symbol }}",
      "operation": "stocks",
      "payload_property": "data",
    },
    "pump": {
      "cron_expression": "0 6 * * ?"
  	},
    "add_namespaces": false
  }

The last thing to do in this tutorial is to create the inbound pipe for CRM. We want to pull in the ``company`` datatype from CRM. Again, follow the below steps to create your inbound pipe ``crm-company-collect``:

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the DTL configuration below
#. Press **Start** to ensure your pipe runs 

.. code-block:: json
  :linenos:
  
    {
	  "_id": "crm-company-collect",
	  "type": "pipe",
	  "source": {
	    "type": "json",
	    "system": "crm",
	    "completeness": false,
	    "url": "/company"
	  },
	  "add_namespaces": false
	}


Having completed the Collect data tutorial, you are now ready to move onto the Enrich tutorial. 