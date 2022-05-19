.. _guide_create_first_synchronization:

Create your first synchronization
=================================

.. toctree::
   :maxdepth: 1
   :hidden:

   Collect <tutorial-getting-started-collect>
   Enrich <tutorial-getting-started-enrich>
   Connect <tutorial-getting-started-connect>
   Transform <tutorial-getting-started-transform>

In this guide we will show you how a general simplistic Sesam synchronization may take form. The goal is to give you an introductionary overview of the 5 standard phases (Collect, Enrich, Connect, Transform and Share) used in all Sesam synchronizations and to see their effects in `HubSpot <https://www.hubspot.com/>`_.

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

    If you do not have a HubSpot account already you can, `create an app developer account here <https://developers.hubspot.com/get-started>`_. Once you have an app developer account you need to set up a `test account <https://legacydocs.hubspot.com/docs/faq/how-do-i-create-a-test-account>`_ in order to `aquire an API key <https://knowledge.hubspot.com/integrations/how-do-i-get-my-hubspot-api-key>`_. You will need this key to access HubSpot's APIs which we need to do in these "Getting Started" Tutorials.

    
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

    **Create your first synchronization:** This guide includes 5 tutorials
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. dropdown:: **1. Collect data**
        :open:

        :badge:`Estimated time: 10 min,badge-light`

        This tutorial will show you how to collect data from HubSpot and Enhetsregistret.

        .. link-button:: tutorial-getting-started-collect
            :type: ref
            :text: Start this tutorial
            :classes: tutorial-start
        
    .. dropdown:: **2. Enrich data**
        :open:

        :badge:`Estimated time: 10 min,badge-light`

        This tutorial will show you how to enrich data you collected from source systems.

        .. link-button:: tutorial-getting-started-enrich
            :type: ref
            :text: Start this tutorial
            :classes: tutorial-start

    .. dropdown:: **Connect data**
        :open:
        
        :badge:`Estimated time: 15 min,badge-light`

        This tutorial will show you how to connect the data your enriched.

            .. link-button:: tutorial-getting-started-connect
                :type: ref
                :text: Start this tutorial
                :classes: tutorial-start

    .. dropdown:: **Transform data**
        :open:

        :badge:`Estimated time: 5 min,badge-light`

        This tutorial will show you how to transform the data and make it ready for sharing with your target system.

        .. link-button:: tutorial-getting-started-transform
            :type: ref
            :text: Start this tutorial
            :classes: tutorial-start


    .. dropdown:: **Share data** (coming soon)
        
        ..
            :badge:`Estimated time: 5 min,badge-light`

        Coming soon

        ..
            This tutorial will show you how to share the data with your target system.

            .. link-button:: tutorial-getting-started-share
                :type: ref
                :text: Start this tutorial
                :classes: tutorial-start
