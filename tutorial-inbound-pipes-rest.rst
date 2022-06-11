.. _tutorial-rest-inbound-pipes:

--------------------
REST - Inbound Pipes
--------------------

In this tutorial you will add an inbound pipe connected to your REST source system: ``hubspot``.

.. admonition:: Objectives

  After you complete this tutorial you will have:

  - Created an inbound pipe connected a REST source system
  - Looked at the dataset created by running your inbound pipe
  - Learned about best practices associated with inbound pipes

.. admonition:: Prerequisites

  #. A :ref:`HubSpot REST source system <tutorial-rest-source-system>`.

Sesam ensures that data residing in your external systems are retained in its raw state, or near to, in inbound pipes. As such, inbound pipes should retain data integrity. This provides a set of :ref:`advantages <collect-advantages>` in Sesam that will i.e. allow for you to repurpose a flow of data from an inbound pipe easily as data moves through Sesam towards egress. In addition, by retaining raw state of data in inbound pipes Sesam can focus on integrating data from external systems, as opposed to the external systems themselves. This is primarily because you will have replicated the shape of data in your external system.

We created a template to get you started in Sesam. Follow these steps to add and run your inbound pipe:

#. Navigate to **Pipes**
#. Click **New pipe**
#. Paste and save the configuration below
#. Click **Start** to ensure your pipe runs 
#. Click refresh to see number of entities processed (should be 2). You can also see them in the pipe's **Output** tab. 

.. code-block:: json
  
    {
	  "_id": "hubspot-contact-collect",
	  "type": "pipe",
	  "source": {
	    "type": "rest",
	    "system": "hubspot",
	    "id_expression": "{{ id }}",
	    "operation": "get",
	    "payload_property": "results",
	    "properties": {
	      "url": "contacts?properties=city,company,email,firstname,jobtitle,lastname,state,website,twitterhandle&associations=companies"
	    }
	  },
	  "namespaced_identifiers": false
	}

When done you should have 2 entities in the output of your inbound pipe.

.. note::

  Best practice in Sesam is to always use :ref:`continuation support <continuation_support>` in your inbound pipe when the system you are working on supports it.

After having successfully created your inbound pipe, you are now ready to move onto the next tutorial in this guide, or look at the enrich guide, where you will learn to apply Sesam's :ref:`semantic enrichment <enrich>.

