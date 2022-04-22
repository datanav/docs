.. _tutorial-collect-source-systems:

Source systems in Sesam
=======================

Sesam supports implementing multiple types of :ref:`systems<system_section>`, i.e: JSON, SQL, microservice etc. Each system, regardless of type, will have a defined set of implementation functionalities which can be set in its DTL configuration. As such, the intended usage in Sesam should be taken into consideration when implementing a system.


.. admonition:: Objectives

  You should aim to achieve the following objectives as you go through this tutorial:

  - Get an overview of the different types of source systems provided by Sesam
  - Understand and remember the most important aspects when working with a source system
  - Successfully create a source system in your Sesam subscription

.. admonition:: Prerequisites

  #. You should have completed the :ref:`getting started guide <getting-started>` before starting on this tutorial.
  #. You will need to create a `HubSpot App Developer Account <https://developers.hubspot.com/get-started>`_ in order to connect to the HubSpot API.
  #. After creating your App Developer account, create an App Test Account. You will need this to interact with the HubSpot API. 
  #. Navigate to your settings section and pick the "Integrations" -> "API Key" tab.
  #. Create and save your API Key. 


When a system is used as a source it is especially important to recognize that providing streams of entities as these are updated in the source system as a :ref:`delta stream <delta-stream-processing>`, ensures that Sesam can propagate data changes through a :ref:`Sesam dataflow <creating-a-sesam-dataflow>` quickly and efficiently, even if the amount of data residing in the source system increases exponentially. As such, avoiding bulk readings of data, as the amount of data residing in your source system increases, should be avoided.

With the above in mind, let us create a source system in Sesam.

.. important::
  
  It is important to remember the following about source systems in Sesam:

  - Should provide streams of entities as input to the pipes they are connected to
  - Can provide entities with **any** shape
  - Must provide Sesam with a unique identifier called ``_id``

The source system you will be working with in this tutorial is `HubSpot <https://www.hubspot.com/>`_. You will connect to the HubSpot API in Sesam with the use of the system type :ref:`REST <rest_source>` and you will create operations that support only GET. The datatype you will be requesting is the ``contact`` datatype.

We created a template to get you started in Sesam. Follow these steps to add HubSpot as a system:

#. Log in to `Sesam portal <https:portal.sesam.io>`_
#. Select the subscription you want to work on
#. Navigate to **Systems**
#. Click on **New system**
#. Paste and save the DTL configuration below
#. Add your system secret ``hubspot-jwt`` in the Secrets tab, as highlighted in the code below

.. code-block:: json
  :linenos:
  :emphasize-lines: 7

  {
    "_id": "hubspot",
    "type": "system:rest",
    "operations": {
      "get-contacts": {
        "method": "GET",
        "url": "contacts/v1/lists/all/contacts/all?hapikey=$SECRET(hubspot-jwt)"
      }
    },
    "url_pattern": "https://api.hubapi.com/%s",
    "verify_ssl": true
  }

..
  After having successfully created your REST system, you are now ready to move onto the next tutorial on :ref:`inbound pipes <tutorial-collect-inbound-pipes>` to start using your recently created REST system and import the datatype ``contact``. 

.. hint::

  You should get acquainted with all properties provided in the above DTL configuration. To read about them, you should explore the :ref:`REST <rest_source>` section of the docs.


Test your skills
================

.. dropdown:: What does a system as a pipe source provide?
        
        It provides streams of entities as input to the pipe their are connected to.

.. dropdown:: Can systems as a pipe source provide entities with any shape?
        
        Yes they can.







