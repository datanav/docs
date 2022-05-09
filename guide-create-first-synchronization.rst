.. _guide_create_first_synchronization:

Create your first synchronization
=================================

.. toctree::
   :maxdepth: 1
   :hidden:

   Collect <tutorial-getting-started-collect>
   Enrich <tutorial-getting-started-enrich>

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
    
    - Completed `Sign up tutorial <tutorial-signup>`_

    In this guide, as in the main set of tutorials outside "Getting Started", we will use HubSpot as our baseline. If you do not have a HubSpot account already you can, `create a HubSpot developer account here <https://developers.hubspot.com/get-started>`_. Once you have a developer account you need to set up a `test account <https://legacydocs.hubspot.com/docs/faq/how-do-i-create-a-test-account>`_ in order to `aquire an API key <https://knowledge.hubspot.com/integrations/how-do-i-get-my-hubspot-api-key>`_. You will need this key to access HubSpot's APIs which we need to do in these "Getting Started" Tutorials. You will also have to import the following :download:`csv file <files/learn-hubspot-embedded-company.csv>` to your HubSpot company data.

    
    You should also familiarize youself with:
    - :doc:`What is Sesam <index-whatis>`
    - :doc:`Building Blocks in Sesam <developer-guide>`

|
|

.. panels::
    :column: col-lg-12 p-2 

    **Create your first synchronization:** This guide includes 5 tutorials
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. dropdown:: **1. Collect data**
        :open:

        :badge:`Estimated time: 5 min,badge-light`

        This tutorial will show you how to collect data from the systems HubSpot and Twelvedata.

        .. link-button:: tutorial-getting-started-collect
            :type: ref
            :text: Start this tutorial
            :classes: tutorial-start
        
    .. dropdown:: **2. Enrich data** (coming soon)

        ..
            :badge:`Estimated time: 5 min,badge-light`

        Coming soon

        ..
            This tutorial will show you how to enrich data you collected from your source system(s).

            .. link-button:: tutorial-getting-started-enrich
                :type: ref
                :text: Start this tutorial
                :classes: tutorial-start

    .. dropdown:: **Connect data** (coming soon)
        
        ..
            :badge:`Estimated time: 5 min,badge-light`

        Coming soon

        ..
            This tutorial will show you how to connect the data your enriched.

            .. link-button:: tutorial-getting-started-connect
                :type: ref
                :text: Start this tutorial
                :classes: tutorial-start

    .. dropdown:: **Transform data** (coming soon)

        ..
            :badge:`Estimated time: 5 min,badge-light`

        Coming soon

        ..
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
