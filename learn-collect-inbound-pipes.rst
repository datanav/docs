:orphan:

Inbound pipes
=============

.. toctree::
   :maxdepth: 1
   :hidden:

   Inbound Pipe - REST <tutorial-inbound-pipe-rest>

In this guide we will look closer at inbound pipes in Sesam and how they connect to :doc:`Sesam systems <configuration-systems>`. 

The main difference between inbound pipes and other Sesam pipes is that inbound pipes use Sesam systems as source of data, compared to other pipes that use datasets as data sources. Depending on the external system connected to, the inbound pipes can have different source settings in order to catch all the functionality of each system. This will be explained in detail in the corresponding tutorial. 

.. admonition::  Objectives:
   
   After you complete this guide you will have:

   #. Learned how to create an inbound pipe connected to a Sesam REST system without :ref:`change tracking <concepts-change-tracking>`

.. admonition:: Prerequisites
    
    Before you start this guide you should familiarize youself with:

    - :doc:`index-whatis`
    - :doc:`developer-guide`    
    - :ref:`concepts-pipes`


.. panels::
    :column: col-lg-12 p-2 

    **Inbound pipes:** This guide includes one tutorial 
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. dropdown:: 1. Inbound Pipe - REST
      :open:

      :badge:`Estimated time: 10 min,badge-light`

      This tutorial will show you how to create an inbound pipe connected to a REST system.

      .. link-button:: tutorial-inbound-pipe-rest
          :type: ref
          :text: Start this tutorial
          :classes: tutorial-start