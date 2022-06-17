Collect
=======

In the :ref:`collect <collect>` phase we import data into Sesam. This includes setting up the system configuration for a :doc:`Sesam system <configuration-systems>` that we wish to connect to an external system as well as its corresponding :ref:`inbound pipe <best-practice-inbound-pipes>`. An external system is any any system Sesam can conncet to in order to synchronize data. Examples of external system are SQL databases or REST API's, to mention a few. Sesam provides built-in connectors for many of these external systems. These templates are available for any Sesam user in the system configuration options.  

In the *collect* phase we do not wish to make any changes to the structure or the attributes of the data, but keep it raw. There is much value of having an exact (or as close to as possible) copy of the source data inside the hub. Should we need to make any changes to the logic inside Sesam we would not have to import the data again since we already have the latest raw data available.

.. admonition:: Prerequisites

	In some of these tutorials we will use `HubSpot <https://www.hubspot.com/>`_ as a baseline. If you did not already created a HubSpot test account in :doc:`getting started <guide-getting-started>` we suggest you read the guide for :doc:`Create your first synchronization <guide-create-first-synchronization>` and create a HubSpot test account now.

Learning areas
--------------

.. toctree::
   :maxdepth: 1

   Source systems <learn-collect-source-systems>
   Inbound pipes <learn-collect-inbound-pipes>

.. panels::
    :column: col-lg-12 p-2 

    **Create your first synchronization:** This section includes 2 guides
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. dropdown:: **1. Source systems**
        :open:

        This guide contains tutorials on how to create system configurations to connect to different source systems.

        .. link-button:: learn-collect-source-systems
            :type: ref
            :text: Start this guide
            :classes: tutorial-start
        
    .. dropdown:: **2. Inbound pipes**
        :open:

        This guide contains tutorials on how to create inbound pipes connected to source systems.

        .. link-button:: learn-collect-inbound-pipes
            :type: ref
            :text: Start this guide
            :classes: tutorial-start
