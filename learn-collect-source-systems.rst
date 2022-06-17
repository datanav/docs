:orphan:

Source Systems
==============

.. toctree::
   :maxdepth: 1
   :hidden:

   REST Source System <tutorial-source-system-rest>


In this guide we will look closer at source systems in Sesam and how they connect with the outside world. 

A source system in Sesam is any :doc:`Sesam system <configuration-systems>` that is used as a connection between an external data provider and a Sesam :ref:`inbound pipe <concepts-pipes>`. 

Sesam supports connecting to multiple types of external data providers, such as :doc:`REST APIs<configuration-systems-rest>` and :doc:`SQL databases <configuration-systems-sql>` etc. You may even create your own :doc:`microservice system <configuration-systems-microservice>` when extra functionality is needed. Each system, regardless of type, can be individually managed inside the system's configuration.

Whenever possible we should always try to import only data from the external systems that has changed since our last import: *deltas*. This functionality however is generally controlled by the :doc:`inbound pipe <learn-collect-inbound-pipes>`.

.. admonition::  Objectives:
   
   After you complete this tutorial you will have:

   #. Learned how to create a REST source system

.. admonition:: Prerequisites
    
    Before you start this guide you should familiarize youself with:

    - :doc:`What is Sesam <index-whatis>`
    - :doc:`Building Blocks in Sesam <developer-guide>`

.. panels::
    :column: col-lg-12 p-2 

    **Source systems:** This guide includes one tutorial 
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. dropdown:: 1. Source System - REST
      :open:

      :badge:`Estimated time: 5 min,badge-light`

      This tutorial will show you how to create a source system connected to a REST API.

      .. link-button:: tutorial-source-system-rest
          :type: ref
          :text: Start this tutorial
          :classes: tutorial-start