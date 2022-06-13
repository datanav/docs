:orphan:

Source Systems
==============

.. toctree::
   :maxdepth: 1
   :hidden:


In this guide we will look closer at source systems in Sesam and how they connect with the outside world. 

A source system in Sesam is any :doc:`Sesam system <configuration-systems>` that is used as a connection between an external data provider and a Sesam :ref:`inbound pipe <concepts-pipes>`. 

Sesam supports connecting to multiple types of external data providers, such as :doc:`REST APIs<configuration-systems-rest>` and :doc:`SQL databases <configuration-systems-sql>` etc. You may even create your own :doc:`microservice system <configuration-systems-microservice>` when extra functionality is needed. Each system, regardless of type, can be individually managed inside the system's configuration.

Whenever possible we should always try to import only data from the external systems that has changed since our last import: *deltas*. This functionality however is generally controlled by the :doc:`inbound pipe <learn-collect-inbound-pipes>`.

.. admonition::  Objectives:
   
   After you complete these tutorials you will have:

   #. Learned how to create a REST source system
   #. Learned how to create an SQL source system conditional DTL transform
   #. Learned how to create a conditional DTL sink

.. admonition:: Prerequisites
    
    Before you start this guide you should familiarize youself with:

    - :doc:`What is Sesam <index-whatis>`
    - :doc:`Building Blocks in Sesam <developer-guide>`

.. toctree::
   :maxdepth: 1

   REST source system <tutorial-source-systems-rest>
   SQL source system
   Conditional DTL sink

.. panels::
    :column: col-lg-12 p-2 

    **Collect:** This guide includes 3 tutorials
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. dropdown:: **1. REST source system**
        :open:

        :badge:`Estimated time: 5 min,badge-light`

        Understand the most important aspects when working with a REST source system, and create your first REST system.

        .. link-button:: tutorial-source-systems-rest.html
            :type: url
            :text: Start this tutorial
            :classes: tutorial-start
        
    2. SQL source system (coming soon)
        
    ..
        :open:
        
        :badge:`Estimated time: 5 min,badge-light`

        Lorem ipsum

        .. link-button:: tutorial-upload-baseline-config.html
            :type: url
            :text: Start this tutorial
            :classes: tutorial-start


    3. Conditional DTL sink (coming soon)
        
    ..
        :open:

        :badge:`Estimated time: 10 min,badge-light`

        Lorem ipsum

        .. link-button:: xx.html
            :type: url
            :text: Start this tutorial
            :classes: tutorial-start