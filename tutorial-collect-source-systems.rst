.. _tutorial-collect-source-systems:

------------------------
Source systems in Sesam
------------------------

In this tutorial we will look closer at source systems in Sesam. A source system is any system that is used in Sesam as a source to a connected :ref:`pipe <concepts-pipes>`. Sesam supports implementing multiple types of :ref:`systems <system_section>`, i.e: JSON, SQL, microservice etc. Each system, regardless of type, will have a defined set of implementation functionalities which can be set in its configuration. As such, the intended usage in Sesam should be taken into consideration when implementing a system.

.. admonition:: Objectives

  You should aim to achieve the following objectives as you go through this tutorial:

  - Get an overview of the different types of source systems provided by Sesam
  - Understand and remember the most important aspects when working with a source system
  - Successfully create a source system in your Sesam subscription

.. admonition:: Prerequisites

  #. Create a `HubSpot app developer account here <https://developers.hubspot.com/get-started>`_
  #. Set up a `test account <https://legacydocs.hubspot.com/docs/faq/how-do-i-create-a-test-account>`_
  #. Aquire an `API key <https://knowledge.hubspot.com/integrations/how-do-i-get-my-hubspot-api-key>`_

When a system is used as a source it is especially important to recognize that providing streams of entities, as these are updated in the source system as a :ref:`delta stream <delta-stream-processing>`, ensures that Sesam can propagate data changes through a :ref:`Sesam dataflow <creating-a-sesam-dataflow>` quickly and efficiently. This holds true even if the amount of data residing in the source system increases exponentially. As such, bulk readings of data as the amount of data residing in your source system increases, should be avoided.

With the above in mind, let us create a source system in Sesam.

.. important::
  
  It is important to remember the following about source systems in Sesam:

  - Should provide streams of entities as input to the pipes they are connected to
  - Can provide entities with **any** shape
  - Each entity must have a unique identifier, or some combination of properties that can be used as one 

The systems you will be working with in this tutorial are `HubSpot <https://www.hubspot.com/>`_ and the Norwegian Central Coordinating Register for Legal Entities, “Enhetsregisteret”. You will connect to the HubSpot API with the use of the system type :ref:`REST <rest_source>`, and connect to “Enhetsregisteret” with the use of the system type :ref:`URL <url_system>`. For now you will only create operations that support GET for both systems.

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

Finally, follow the below steps again to add enhetsregisteret as a system:

#. Navigate to Systems
#. Click on New system
#. Paste and save the configuration below

.. code-block:: json
  :linenos:

  {
    "_id": "enhetsregisteret",
    "type": "system:url",
    "url_pattern": "http://hotell.difi.no/download/%s"
  }

After having successfully created your REST system, you are now ready to move onto the next tutorial on :ref:`inbound pipes <tutorial-collect-inbound-pipes>` to start using your recently created REST system and import the datatype ``contact``. 

.. hint::

  You should get acquainted with all properties provided in the above configuration. To read about them, you should explore the :ref:`REST <rest_source>` and :ref:`URL <url_system>` sections of the docs.

.. panels::
    :column: col-lg-12 p-2 

    **Test your skills**
    ^^^^^^^^^^^^^^^^^^^^

    .. dropdown:: What does a system as a pipe source provide?
          
          It provides streams of entities as input to the pipes they are connected to.

    .. dropdown:: Can systems as a pipe source provide entities with any shape?
          
          Yes they can, as long as the stream exposes a json array.




