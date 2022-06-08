:orphan:

Inbound pipes
=============

.. toctree::
   :maxdepth: 1
   :hidden:

In this guide we will look closer at :ref:`inbound pipes <concepts-pipes>` in Sesam and how they connect to :doc:`Sesam systems <configuration-systems>`. 

The main difference between inbound pipes and other Sesam pipes is that inbound pipes uses Sesam systems as source of data, compared to other pipes that uses datasets as data sources. Depending on the external system connected to, the inbound pipes can have different source settings in order to catch all the functionality of each system. This will be explained in detail in the corresponding tutorial. 

In addition, there are some best practices related to inbound pipes that we will cover in both this guide and in each of the tutorials.

.. admonition::  Objectives:
   
   After you complete these tutorials you will have:

   #. Learned how to create an inbound pipe connected to a Sesam REST system without :ref:`change tracking <concepts-change-tracking>`
   #. Learned the best practices associated with inbound pipes

.. admonition:: Prerequisites
    
    Before you start this guide you should familiarize youself with:

    - :doc:`What is Sesam <index-whatis>`
    - :doc:`Building Blocks in Sesam <developer-guide>`    
    - :doc:`Inbound pipes <concepts-pipes>`