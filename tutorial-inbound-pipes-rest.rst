--------------------
REST - Inbound Pipes
--------------------

In this tutorial you will add an inbound pipe, without :ref:`continuation support <continuation_support>` because the HubSpot API does not immediately support it, connected to your REST source system: ``hubspot``.

.. note::

  Best practice in Sesam is to always use :ref:`continuation support <continuation_support>` in your inbound pipe when the system you are working on supports it.

.. admonition:: Objectives

  After you complete this tutorial you will have:

  - Created an inbound pipe connected to a REST source system
  - Looked at the dataset created by running your inbound pipe
  - Learned about best practices associated with inbound pipes

.. admonition:: Prerequisites

  #. A :doc:`HubSpot REST source system <tutorial-source-systems-rest>`.

By following Sesam best practices, data residing in your external systems are retained in its raw state, or near to, in inbound pipes. As such, inbound pipes should retain data integrity. This provides a set of :ref:`advantages <collect-advantages>` in Sesam that will i.e. allow for you to repurpose a flow of data from an inbound pipe easily as data moves through Sesam towards egress. In addition, by retaining raw state of data in inbound pipes Sesam can focus on integrating data from external systems, as opposed to the external systems themselves. This is primarily because you will have replicated the shape of data in your external system.

Before creating your inbound pipe, we want to import some contact and company data into HubSpot. This will make it a lot more interesting for you, as you work with related tutorials down the road. Therefore, follow the below steps **before** moving on: 

#. Download the :download:`company data <files/learn-hubspot-company.csv>` and :download:`contact data <files/learn-hubspot-contacts.csv>` and save the csv files locally
#. Log into HubSpot and navigate to your **Companies** section, found under **Contacts** in the top menu.
#. Click **Import** on the right hand side of the page
#. Click **Start an import** and select **File from computer** and click **Next**
#. Select **Multiple files with associations** and click **Next**
#. Select **Companies** and **Contacts** and click **Next** 
#. Upload ``learn-hubspot-company.csv`` under **Company** and ``learn-hubspot-contacts.csv`` under **Contacts** (don't click on the "This file includes a ... column" boxes) and click **Next**
#. Select **Company ID** as common column header and select **Company** as the object it is unique for and click **Next**
#. Select **Don't import data in unmapped column** and click **Next**
#. Select **Don't import data in unmapped column** again and click **Next**
#. Agree to the terms and click **Finish import**

Upon completion, you can move on and follow the template we created to get you started in Sesam. Follow these steps to add and run your inbound pipe:

#. Navigate to **Pipes**
#. Click **New pipe**
#. Paste and save the configuration below
#. Click **Start** to ensure your pipe runs 
#. Click refresh to see number of entities processed (should be 100). You can also see them in the pipe's **Output** tab. 

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
	      "url": "contacts?properties=city,company,email,firstname,jobtitle,lastname,state,website,twitterhandle&associations=companies&limit=150"
	    }
	  },
	  "namespaced_identifiers": false
	}

When done you should have 100 entities in the output of your inbound pipe. As you can see in the **Output** tab, these is no namespace added to any of your properties. This is due to the above property ``namespaced_identifiers: false``. This ensures that Sesam's semantic enrichment is not applied to data at this stage of your synchronization. 

Extending on some of the other properties used in the above configuration the ``id_expression`` is used to tell Sesam which payload property should be used as ``_id`` for each entity produced when running the pipe whilst ``payload_property`` states which property in the HubSpot payload data should be parsed from. Finally, the ``properties`` property allows for you to state which datatype should be fetched from HubSpot in addition to properties and associations that should be retained in the payload for this specific datatype. This is done via the use of `query parameters <https://branch.io/glossary/query-parameters/>`_ in this particular use-case. 

After having successfully created your inbound pipe, you are now ready to move onto the next tutorial in this guide, or look at the enrich guide, where you will learn to apply Sesam's :ref:`semantic enrichment <enrich>`.

