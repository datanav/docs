------------------
REST Source System
------------------

In this tutorial you will add a REST source system to your Sesam subscription.

.. admonition:: Objectives

  You should aim to achieve the following objectives as you go through this tutorial:

  - Successfully create a REST source system in your Sesam subscription
  - Get aquainted with the different properties available for the REST source system

.. admonition:: Prerequisites

  #. A HubSpot test account.

The external system you will be working with in this tutorial is `HubSpot <https://www.hubspot.com/>`_ and you will connect to HubSpot with the use of a :ref:`REST source <rest_source>`. For now you will only create operations that support GET. Operations in your system configuration allows for you to define endpoints you can query when you use your REST source system in an inbound pipe.

We created a template to get you started in Sesam. Follow these steps to add HubSpot as a system:

#. Navigate to Systems
#. Click on New system
#. Paste and save the configuration below
#. Add your hubspot API key in your Sesam subscription as a Secret by going into Datahub -> Variables.
#. Use the Secret name “hubspot-api-key”.

.. code-block:: json
  :linenos:

  {
    "_id": "hubspot",
    "type": "system:rest",
    "headers": {
      "Content-Type": "application/json"
    },
    "operations": {
      "get": {
        "method": "GET",
        "url": "{{ properties.url }}&"
      }
    },
    "rate_limiting_delay": 60,
    "rate_limiting_retries": 3,
    "url_pattern": "https://api.hubapi.com/crm/v3/objects/%shapikey=$SECRET(hubspot-api-key)",
    "verify_ssl": true
  }

.. note::

  Best practice in Sesam is to always use :ref:`continuation support <continuation_support>` when the system you are working on supports it.

After having successfully created your REST system, you are now ready to move onto the next tutorial in this guide, or look at the :ref:`REST - Inbound Pipes <tutorial-inbound-pipes-rest>` where you will import the datatype ``contact`` from your recently created HubSpot REST system. 

.. hint::

  You should get acquainted with all properties provided in the above configuration. To read about them, you should explore the :ref:`REST <rest_source>` section of the docs.
