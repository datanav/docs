=============================================
Preparations for starting a new Sesam project
=============================================

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
------------

This document introduces what we need to understand and consider before starting on a new project for a customer. So prior to start setting up infrastructure and doing work in Sesam we need to have a plan, or a data model showing how data flows from which systems, how it needs to be connected and transformed and which systems will receive data.

Before we dive straight into data and dataflows we have to take a step back consider the following: there are a few risks that can affect the timeline of the pilot pr project phase, where both start date and end date can be delayed:

• Clear scope of understanding of a pilot
• Appointment of a Project Manager by a customer
• Allocation of personnel by a customer
• Scope and specifications of integrations 
• Understanding of Sesam MasterData HUB

In addition there are other things to consider like can we use other components to do this, what different environments do we need (test, stage, QA), what are the main data flows and if it is a pilot; do we have some best practices?


Considerations before setting up a new Sesam project
----------------------------------------------------

Test environment
================

Trond


Data flows in Sesam
===================

The data from the source system is fed into Sesam through inbound pipes which collects and tags the data for further processing. Each time raw data comes into Sesam, it goes through a main data flow which can be summarised like this

1. Inbound pipe: data from the source system is fed into Sesam through inbound pipes which collects and tags the data for further processing
2. Global pipe: merge data belonging together to generate global datasets
3. Preparation pipe: global datasets are prepared for target systems. It is here most of the logic is added
4. Outbound pipe: sends data to an endpoint and should normally have no logic

.. image:: images/best-practice/sesam-flow.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept  

To further understnd this flow, please have a look at our best practie :ref:`here <data-modelling-workflow>`

Data modelling in Sesam
=======================

Summary
^^^^^^^

Data modelling in Sesam isn't so much about connecting data together by their relations as it is about connecting them by what they represent. A good data model in Sesam hence relies much about having a good knowledge of the data that are read into Sesam and what they represent, in other words what they are. 

Short glossary of terms used in this document:
- :ref:`pipe <concepts-pipes>`: in Sesam terms this is the component that makes sure that data flows from a source to a target at defined intervals.
- Inbound pipe this is used to refer to pipes that reads from an external system and writes the data to a dataset in Sesam.
- Global pipe: this refers to datasets containing global data for reuse throughout the Sesam instance, see description of global datasets below.
- Preparation pipe: this is a pipe that creates the data that will be sent to an external system.
- Outbound pipe: this is used to refer to pipes that reads data from Sesam and sends them to an external system.

.. _datamodelling-Global datasets:

Global datasets
^^^^^^^^^^^^^^^

At the core of data modelling in Sesam are the :ref:`global datasets <data-modellinge-global>`. These are collections of data that pertains to the same concept from different sources. The main purpose of a global dataset is to be the single authorative location to get fresh data about a specific concept from. A general rule is that every dataset that is written to Sesam from an external data source should be put into its appropriate global, however how small it is.

.. _datamodelling-Data modelling:

Data modelling
^^^^^^^^^^^^^^

Although global datasets are at the core of how Sesam organizes its data, modelling does not only take place in how you structure your global datasets. Data modelling in Sesam starts with the inbound pipes, whether you are at the beginning of a project or adding new data. 

Merge data in a global dataset or not
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
One of the purposes of a global dataset is to present a single authoritative truth about a concept or data. It is then logical to merge data from various different sources (or systems) in one global dataset if they define the same kind of object or type. For example, if some of the various sources contain person data, it would be logical to create a global dataset for person data and then merge each entity that refers to the same person. This is done so that when you ask for information about a specific entity, you also get information about that entity from the other systems. In terms of reusability this is a highly versatile way of getting all the data you need.

However, merging data comes with a cost. In certain cases, changing the rules of how the data are merged requires the pipe to be reset and run again. For large datasets this might mean that it will take time before the downstream pipes will get updates.

In some cases, merging the data isn’t logical. For instance, data like countries, counties, cities and streets might be put into a global location dataset, but it is not logical to merge these data. 

Also note that if a global dataset contains merged data, it does not necessarily mean that every other dataset in the global must be merged. Some data might be telling something about an entity but is not necessary the same thing. 

To the point: Data Modelling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let us begin by repeating an important truth about data modelling in Sesam: when modelling in Sesam do not create your data models by how they are related to each other by their properties (as in a standard relational database), but by what the data in the datasets are about.

For example, let us say we have two datasets or tables, ‘employee and ‘child’. In a relational database, these two tables would normally be linked by a one-to-many relation, i.e. an employee can have many children. However, when we look at these two tables from a Sesam perspective, both are in general speaking of a ‘person’. Hence, we should put both the ‘employee’ and ‘child’ table in the same global containing data about a person, ‘global-person’.

What you are trying to accomplish, is to have a set of global datasets that the preparation pipes can choose from, like food items grouped together in a supermarket to easily locate the food items you need. On the other hand, you don’t want the number of global datasets to grow out of hand, making it hard to find.

Start by analyzing the sources and data to determine the needs of the organization. This will have an impact on the data model and more specifically how the global datasets will be organized. It is here the organization needs to think: what is important to me? What data do I use often, and therefore needs to be easily available? The results vary for each organization and each data model.

The use of other components in Sesam projects
-----------------------------------------------

Azure
=====

Google
======

Best practices for pilots
-------------------------


