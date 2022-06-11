:orphan:

Inbound pipes
=============

.. toctree::
   :maxdepth: 1
   :hidden:

In this guide we will look closer at :ref:`inbound pipes <concepts-pipes>` in Sesam and how they connect to :doc:`Sesam systems <configuration-systems>`. 

The main difference between inbound pipes and other Sesam pipes is that inbound pipes use Sesam systems as their source of data, compared to other pipes that use datasets as data sources. Depending on the external system connected to it, the inbound pipes can have different source settings in order to incorporate all the functionality of each system. This will be explained in detail in the corresponding tutorial. 

In addition, there are some best practices related to inbound pipes that we will cover in both this guide and in each of the tutorials.

.. admonition::  Objectives:
   
   After you complete these tutorials you will have:

   #. Learned how to create an inbound pipe connected to a Sesam REST system without :ref:`change tracking <concepts-change-tracking>`
   #. Learned the best practices associated with inbound pipes

.. admonition:: Prerequisites
    
    Before you start this guide you should familiarize youself with:

    - :doc:`What is Sesam <index-whatis>`
    - :doc:`Building Blocks in Sesam <developer-guide>`    
    - :ref:`Inbound pipes <concepts-pipes>`

.. toctree::
   :maxdepth: 1

   REST inbound pipes <tutorial-rest-inbound-pipes>

.. panels::
    :column: col-lg-12 p-2 

    **Collect:** This guide includes 1 tutorial
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. dropdown:: **1. REST inbound pipes**
        :open:

        :badge:`Estimated time: 5 min,badge-light`

        Create an inbound pipe connected to a REST source system, and understood best practices associated with inbound pipes.

        .. link-button:: tutorial-inbound-pipes-rest.html
            :type: url
            :text: Start this tutorial
            :classes: tutorial-start