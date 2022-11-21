.. _guide_create_first_synchronization:

Create your first synchronization
=================================

.. toctree::
   :maxdepth: 1
   :hidden:

   Data Synchronization <guide-create-first-synchronization-data-synchronization>
   Data Management <guide-create-first-synchronization-data-management>

In this guide we will show you how a general simplistic Sesam synchronization may take form. The goal is to give you an introductory overview of the 5 standard phases (Collect, Enrich, Connect, Transform and Share) used in all Sesam synchronizations and to see their effects in `HubSpot <https://www.hubspot.com/>`_.

.. admonition::  Objectives:
   
   After you complete these tutorials you will have:

   #. Created a Collect pipe
   #. Created a Enrich pipe
   #. Created a Connect pipe
   #. Created a Transform pipe
   #. Created a Share pipe
   #. Seen the data synchronized into HubSpot

.. admonition:: Prerequisites

    You need to complete the `Sign up tutorial <tutorial-signup>`_

    In this guide, as in the main set of tutorials outside "Getting Started", we will use HubSpot as our baseline. 

    We recommend that you `create an app developer account <https://developers.hubspot.com/get-started>`_ for these tutorials even if you have a HubSpot account from before. We will upload and download data to and from HubSpot, and do not wish to affect what ever data you may have on your current account. 

    Once you have an app developer account you need to set up a `test account <https://legacydocs.hubspot.com/docs/faq/how-do-i-create-a-test-account>`_ in order to `aquire an API key <https://knowledge.hubspot.com/integrations/how-do-i-get-my-hubspot-api-key>`_. You will need this key to access HubSpot's APIs which we need to do in these "Getting Started" Tutorials.

    
    You should also familiarize youself with:

    - :doc:`What is Sesam <index-whatis>`
    - :doc:`Building Blocks in Sesam <developer-guide>`

.. admonition:: Use-case

    Many customers store their *company contact data* in HubSpot's CRM solution. Instead of each customer manually keeping this data up-to-date, HubSpot wish to automate the process which in turn will let their customers focus more on realizing their business goals.

    Each customer should be able to have their HubSpot company data synchronized with the company data available in the Norwegian Central Coordinating Register for Legal Entities, "Enhetsregisteret". This way, the customers knows that the data available in HubSpot is always up-to-date and of high quality.

|
|

.. panels::
    :column: col-lg-12 p-2 

    **Create your first synchronization:** This guide includes 2 sections
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. dropdown:: **1. Data Synchronization**
        :open:

        :badge:`Estimated time: 20 min,badge-light`

        This section will show you how to synchronize HubSpot data with your Sesam instance.

        .. link-button:: guide-create-first-synchronization-data-synchronization
            :type: ref
            :text: Enter this section
            :classes: tutorial-start
        
    .. dropdown:: **2. Data Management**
        :open:

        :badge:`Estimated time: 30 min,badge-light`

        This section connect, manage and map The HubSpot data to and from the global model.

        .. link-button:: guide-create-first-synchronization-data-management
            :type: ref
            :text: Enter this section
            :classes: tutorial-start
