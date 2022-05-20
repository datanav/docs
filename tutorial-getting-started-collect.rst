.. _tutorial_getting_started_collect:

Collect data
============

In this tutorial we will connect Sesam to two different data sources: your newly created Hubspot account and the Norwegian Central Coordinating Register for Legal Entities, "Enhetsregisteret".
Later in Getting Started we will use the data imported from Enhetsregisteret to improve on the data quality from HubSpot before sending the data to back to HubSpot. 

After having succesfully connected to these providers you will create inbound pipes for each relevant entity type we want to work with.

.. admonition::  Objectives:

    After you complete this tutorial you will have learned the following:

    #. How to create systems
    #. How to create inbound pipes
    #. Import data from a data source into sesam

.. admonition::  Remember:

    #. To `create a HubSpot app developer account here <https://developers.hubspot.com/get-started>`_
    #. To set up a `test account <https://legacydocs.hubspot.com/docs/faq/how-do-i-create-a-test-account>`_
    #. To aquire an `API key <https://knowledge.hubspot.com/integrations/how-do-i-get-my-hubspot-api-key>`_
    
Import data to HubSpot
^^^^^^^^^^^^^^^^^^^^^^
In order to import data into Sesam we first need to make sure that HubSpot contains the data we want to import. Therefore, the first step is to populate HubSpot with some data by following the steps below:

#. Download the :download:`company data <files/learn-hubspot-company.csv>` and :download:`contact data <files/learn-hubspot-contacts.csv>` and save the csv files locally
#. Log into HubSpot and navigate to your **Contacts** > **Companies** section
#. Click **Import** on the right hand side of the page
#. Click **Start an import** and select **File from computer** and click **Next**
#. Select **Multiple files with associations** and click **Next**
#. Select **Companies** and **Contacts** and click **Next** 
#. Upload ``learn-hubspot-company.csv`` under **Company** and ``learn-hubspot-contacts.csv`` under **Contacts** (don't click on the "This file includes a ... column" boxes) and click **Next**
#. Select **Company ID** as common column header and select **Company** as the object it is unique for and click **Next**
#. Select **Don't import data in unmapped column** and click **Next**
#. Select **Don't import data in unmapped column** again and click **Next**
#. Agree to the terms and click **Finish import**

The imported contacts and companies can be found under the **Contacts** tab.

Create systems
^^^^^^^^^^^^^^

In Sesam, a system is a representation of the connection between Sesam and the outside world.

The Hubspot system
******************

First, we will start by adding a new system for the HubSpot connection. 

Follow the below steps in order to add HubSpot as a system in Sesam:

In the `Sesam portal <https://portal.sesam.io/>`_:

#. Navigate to **Datahub** > **Variables** and add your HubSpot API key as a **Secret** named "hubspot-api-key"
#. Navigate to **Systems**
#. Click **New system**
#. Paste and save the configuration below

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
#. Click **New system**
#. Paste and save the configuration below

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

Create inbound pipes
^^^^^^^^^^^^^^^^^^^^

"Inbound pipes" is the naming convention used for pipes that receive their data from a source system.

The HubSpot inbound pipe
************************

The first inbound pipe we want to work on is the pipe that connects to our ``hubspot`` system. We want to pull in the company data that exists inside the CRM provider. Follow the below steps to create your inbound pipe ``hubspot-company-collect``:

#. Navigate to **Pipes**
#. Click **New pipe**
#. Paste and save the configuration below
#. Click **Start** to ensure your pipe runs 
#. Click refresh to see number of entities processed (should be 10). You can also see them in the pipe's output page. 

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

The final thing to do is to pull in the company data from Enhetsregisteret by creating a pipe that connects to our ``enhetsregisteret`` system.
Again, follow the below steps to create your inbound pipe ``enhetsregisteret-company-collect``:

#. Navigate to **Pipes**
#. Click **New pipe**
#. Paste and save the configuration below
#. Click **Start** to ensure your pipe runs 
#. Click refresh to see number of entities processed (should be 10). You can also see them in the pipe's output page. 


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


