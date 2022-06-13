--------------------
REST - Inbound Pipes
--------------------

In this tutorial you will add an inbound pipe, without :ref:`continuation support <continuation_support>`, connected to your REST source system: ``hubspot``.

.. admonition:: Objectives

  After you complete this tutorial you will have:

  - Created an inbound pipe connected to a REST source system
  - Looked at the dataset created by running your inbound pipe
  - Learned about best practices associated with inbound pipes

.. admonition:: Prerequisites

  #. A :ref:`HubSpot REST source system <tutorial-source-systems-rest>`.

By following Sesam best practices, data residing in your external systems are retained in its raw state, or near to, in inbound pipes. As such, inbound pipes should retain data integrity. This provides a set of :ref:`advantages <collect-advantages>` in Sesam that will i.e. allow for you to repurpose a flow of data from an inbound pipe easily as data moves through Sesam towards egress. In addition, by retaining raw state of data in inbound pipes Sesam can focus on integrating data from external systems, as opposed to the external systems themselves. This is primarily because you will have replicated the shape of data in your external system.

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

When done you should have 2 entities in the output of your inbound pipe. As you can see in the **Output** tab, these is no namespace added to any of your properties. This is due to the above property ``namespaced_identifiers: false``. This ensures that Sesam's semantic enrichment is not applied to data at this stage of your synchronization. 

Extending on some of the other properties used in the above configuration the ``id_expression`` is used to tell Sesam which payload property should be used as ``_id`` for each entity produced when running the pipe whilst ``payload_property`` states which property in the HubSpot payload data should be parsed from. Finally, the ``properties`` property allows for you to state which datatype should be fetched from HubSpot in addition to properties and associations that should be retained in the payload for this specific datatype. This is done via the use of `query parameters <https://branch.io/glossary/query-parameters/>`_ in this particular use-case. 

.. note::

  Best practice in Sesam is to always use :ref:`continuation support <continuation_support>` in your inbound pipe when the system you are working on supports it.

After having successfully created your inbound pipe, you are now ready to move onto the next tutorial in this guide, or look at the enrich guide, where you will learn to apply Sesam's :ref:`semantic enrichment <enrich>`.

