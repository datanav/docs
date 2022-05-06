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

    #. To `create a HubSpot developer account here <https://developers.hubspot.com/get-started>`_
    #. To set up a `test account <https://legacydocs.hubspot.com/docs/faq/how-do-i-create-a-test-account>`_
    #. To aquire an `API key <https://knowledge.hubspot.com/integrations/how-do-i-get-my-hubspot-api-key>`_
    #. To import the following :download:`csv file <files/learn-hubspot-embedded-company.csv>` to your HubSpot company data

|
|

Create Systems
^^^^^^^^^^^^^^

In Sesam, a system is a representation of the connection between Sesam and the outside world.

The Hubspot System
******************

First, we will start by adding a new system for the HubSpot connection. 

Follow the below steps in order to add Hubspot as a system in Sesam:

In the `Sesam portal <https://portal.sesam.io/>`_:

#. Navigate to **Systems**
#. Click on **New system**
#. Paste and save the DTL configuration below
#. Add your hubspot API key in your Sesam subscription as a ``Secret`` by going into ``Datahub`` -> ``Variables``. Use the ``Secret`` name "hubspot-api-key". 

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
          "url": "companies?"
        }
      },
      "rate_limiting_delay": 60,
      "rate_limiting_retries": 3,
      "url_pattern": "https://api.hubapi.com/crm/v3/objects/%shapikey=$SECRET(hubspot-api-key)",
      "verify_ssl": true
    }

The Enhetsregistret System
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

Create Inbound Pipes
^^^^^^^^^^^^^^^^^^^^

"Inbound pipes" is the naming convention used for pipes that receive their data from a source system.

The Hubspot Inbound Pipe
************************

The first inbound pipe we want to work on is the pipe that connects to our ``HubSpot`` system. We want to pull in the ``company`` datatype that exists inside the CRM provider. Follow the below steps to create your inbound pipe ``hubspot-company-collect``:

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the DTL configuration below
#. Press **Start** to ensure your pipe runs 

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
        "payload_property": "results"
      },
      "add_namespaces": false
    }

The Enhetsregisteret Inbound Pipe
*********************************

The last thing to do in this tutorial is to create the inbound pipe for Enhetsregisteret. We want to pull in the ``enhetsregisteret`` datatype from the provider. Again, follow the below steps to create your inbound pipe ``enhetsregisteret-company-collect``:

#. Navigate to **Pipes**
#. Click on **New pipe**
#. Paste and save the DTL configuration below
#. Press **Start** to ensure your pipe runs 

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
      "add_namespaces": false
    }

..
  .. note::

      If you want to look closer into the details of the collect phase, look into the tutorials for collect.


