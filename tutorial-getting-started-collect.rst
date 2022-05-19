.. _tutorial_getting_started_collect:

Collect Data
============

In this tutorial we will connect Sesam to two different data sources: your newly created Hubspot account and the Norwegian Central Coordinating Register for Legal Entities, "Enhetsregisteret".
Later in Getting Started we will use the data imported from Enhetsregisteret to improve on the data quality from HubSpot before sending the data to back to HubSpot. 

After having succesfully connected to these providers you will create inbound pipes for each relevant datatype we want to work with.

.. admonition::  Objectives:

    After you complete this tutorial you will have learned the following:

    #. How to create systems
    #. How to create inbound pipes
    #. Import data from a data source into sesam

.. admonition::  Remember:

    #. To `create a HubSpot app developer account here <https://developers.hubspot.com/get-started>`_
    #. To set up a `test account <https://legacydocs.hubspot.com/docs/faq/how-do-i-create-a-test-account>`_
    #. To aquire an `API key <https://knowledge.hubspot.com/integrations/how-do-i-get-my-hubspot-api-key>`_
    
|
|

Import data to HubSpot
^^^^^^^^^^^^^^^^^^^^^^
In order to be able to import data to Sesam we first need to make sure that HubSpot contains data we can later import import. Therefore, the first step is to populate HubSpot with some data by following the steps below:

#. Download the :download:`company data <files/learn-hubspot-company.csv>` and :download:`contact data <files/learn-hubspot-contacts.csv>` and save the csv files locally
#. Log into HubSpot and navigate to your **Companies** section
#. Press **Import** on the right hand side of the page
#. Press **Start an import** and select **File from computer** and click on **Next**
#. Select **Multiple files with associations** and click on **Next**
#. Select **Companies** and **Contacts** and click on **Next** 
#. Upload your downloaded files from step 1 (don't click on the "This file includes a ...." boxes) and click on **Next**
#. Select **Company ID** as common column header and select **Company** as the object it is unique for and click on **Next**
#. Select **Don't import data in unmapped column** and click on **Next**
#. Select **Don't import data in unmapped column** again and click on **Next**
#. Finish the import.

You should be able to see the new companies imported in your HubSpot **Companies** tab.


Create systems
^^^^^^^^^^^^^^

In Sesam, a system is a representation of the connection between Sesam and the outside world.

The Hubspot system
******************

First, we will start by adding a new system for the HubSpot connection. 

Follow the below steps in order to add Hubspot as a system in Sesam:

In the `Sesam portal <https://portal.sesam.io/>`_:

#. Navigate to **Systems**
#. Click on **New system**
#. Paste and save the DTL configuration below
#. Add your hubspot API key in your Sesam subscription as a ``Secret`` by going into ``Datahub`` -> ``Variables``. 
#. Use the ``Secret`` name "hubspot-api-key". 

.. code-block:: json
  :linenos:

    {
      "_id": "hubspot",
      "type": "system:rest",
      "headers": {
        "Content-Type": "application/json"
      },
      "operations": {
        "get_companies": {
          "method": "GET",
          "url": "{{ properties.url }}associations=contacts,companies,deals,tickets,products,quotes&"
        }
      },
      "rate_limiting_delay": 60,
      "rate_limiting_retries": 3,
      "url_pattern": "https://api.hubapi.com/crm/v3/objects/%shapikey=$SECRET(hubspot-api-key)",
      "verify_ssl": true
    }


The Enhetsregistret system
**************************

Now we can add our second system, the "Enhetsregisteret" system.

In the `Sesam portal <https://portal.sesam.io/>`_:

#. Navigate to **Systems**
#. Click on **New system**
#. Paste and save the DTL configuration below

.. code-block:: json
  :linenos:

    {
      "_id": "enhetsregisteret",
      "type": "system:microservice",
      "docker": {
        "image": "sesamcommunity/learn-sesam-crm:v1.1.2",
        "port": 5000
      }
    }

.. note::

  The connection to Enhetsregisteret is a mock connection in this tutorial. The data you will import to Sesam is actually test data generate for this specific tutorial. The connections, as well as the data itself, are very much like how it might look in a real world scenario however and therefore well serves the purposes of Getting started.

After having successfully created both systems, you are now ready to move onto the next step of this tutorial, the creation of inbound pipes. 

|
|

Create inbound pipes
^^^^^^^^^^^^^^^^^^^^

"Inbound pipes" is the naming convention used for pipes that receive their data from a source system.

The Hubspot inbound pipe
************************

The first inbound pipe we want to work on is the pipe that connects to our ``HubSpot`` system. We want to pull in the ``company`` datatype that exists inside the CRM provider. Follow the below steps to create your inbound pipe ``hubspot-company-collect``:

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the DTL configuration below
#. Press **Start** to ensure your pipe runs 
#. Press refresh to see number of entities processed (should be 10). You can also see them in the pipe's output page. 


.. code-block:: json
  :linenos:
  
    {
      "_id": "hubspot-company-collect",
      "type": "pipe",
      "source": {
        "type": "rest",
        "system": "hubspot",
        "id_expression": "{{ id }}",
        "operation": "get_companies",
        "payload_property": "results",
        "properties": {
          "url": "companies?properties=about_us,address,city,country,description,domain,founded_year,is_public,linkedin_company_page,name,numberofemployees,state,timezone,website,zip&"
        }
      },
      "namespaced_identifiers": false
    }



The Enhetsregisteret inbound pipe
*********************************

The last thing to do in this tutorial is to create the inbound pipe for Enhetsregisteret. We want to pull in the ``enhetsregisteret`` datatype from the provider. Again, follow the below steps to create your inbound pipe ``enhetsregisteret-company-collect``:

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the DTL configuration below
#. Press **Start** to ensure your pipe runs 
#. Press refresh to see number of entities processed (should be 10). You can also see them in the pipe's output page. 


.. code-block:: json
  :linenos:
  
    {
      "_id": "enhetsregisteret-company-collect",
      "type": "pipe",
      "source": {
        "type": "json",
        "system": "enhetsregisteret",
        "url": "/enhetsregisteret"
      },
      "transform": {
        "type": "dtl",
        "rules": {
          "default": [
            ["copy", "*"],
            ["add", "_id", "_S.orgnr"]
          ]
        }
      },
      "namespaced_identifiers": false
    }

When done you should have 10 entities in the output of each of the two inbound pipes.

..
  .. note::

      If you want to look closer into the details of the collect phase, look into the tutorials for collect.


