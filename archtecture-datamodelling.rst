==============
Data modelling
==============

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
------------

This document introduces what we need to understand and consider, both in terms of customers current data and how they want to use it, in other words what steps do we need to take before we start a new project.  So prior to start setting up infratstructure and doing work in Sesam we need to have a plan, or a data modell showing how data flows from which systems, how it needs to be connected and transformed and which systems will receive data.

Before we dive straight into data and dataflows we have to take a step back consider the following; there are a few risks that can affect the timeline of the pilot pr project phase, where both start date and end date can be delayed:

•   Clear scope of understanding of a pilot
•   Appointment of a Project Manager by a customer
•   Allocation of personnel by a customer
•   Scope and specifications of integrations 
•   Understanding of Sesam MasterData HUB

This is not a project management document so we will not spend a lot of tie on this, but it is important to bear these points in mind. 

Data modelling in Sesam
-----------------------

Summary
=======

Data modelling in Sesam isn't so much about connecting data together by their relations as it is about connecting them by what they represent. A good data model in Sesam hence relies much about having a good knowledge of the data that are read into Sesam and what they represent, in other words what they are. 

 :doc:`entity data model <entitymodel>`
Short glossary of terms used in this document:
•   :ref:`pipe <concepts-pipes>`: in Sesam terms this is the component that makes sure that data flows from a source to a target at defined intervals.
•   Inbound pipe: this is used to refer to pipes that reads from an external system and writes the data to a dataset in Sesam.
•   Global pipe: this refer to datasets containing global data for reuse throughout the Sesam instance, see description of global datasets below.
•   Preparation pipe: this is a pipe that creates the data that will be sent to an external system.
•   Outbound pipe: this is used to refer to pipes that reads data from Sesam and sends them to an external system.

.. _datamodelling-Global datasets:

Global datasets
===============

At the core of data modelling in Sesam are the :ref:`global datasets <best-practice-global>`. These are collections of data that pertains to the same concept from different sources. The main purpose of a global dataset is to be the single authorative location to get fresh data about a specific concept from. A general rule is that every dataset that is written to Sesam from an external data source should be put into its appropriate global, however how small it is.


.. _datamodelling-Data modelling:

Data modelling
==============

Although global datasets are at the core of how Sesam organizes its data, modelling does not only take place in how you structure your global datasets. Data modelling in Sesam starts with the inbound pipes, whether you are at the beginning of a project or adding new data. 

.. image:: images/dataset-structure.png
    :width: 800px
    :align: center
    :alt: Dataset structure

.. _datamodelling-Inbound pipes / datasets:

Inbound pipes / datasets
========================

Typically when modelling :ref:`an inbound pipe <best-practice-Inbound pipes>`, you will do an analysis of the data. From the result of the analysis you will then add properties that will enhance the data in terms of modelling, reusability and connectivity, such as:

 • **References to other datasets**: if a property is a reference or relation to another dataset, such as a foreign key field in a relational database, you should add an additional property that contains a reference to that dataset. This should be in the form of a :ref:`namespaced identifier <best-practice-namespace>`. These references are usually key properties when semantically link data together in a global dataset but are also useful when connecting data in preparation pipes.
 •  :ref:`An RDF type <best-practice_-rdf type>`: this is a property providing a qualifier of what the data is and can be seen as metadata used to relate data and provide a semantic context to the data. When used with a namespace, it keeps track of the origin of the data, as well as the business type. An RDF type is useful in terms of filtering data, both from global datasets or in :ref:`hops <hops_function>` to other datasets.
 •  **A combination of fields**: a dataset may at times contain data that when combined can form a fuller understanding of the field, like a combination of first name and surname will give the full name of a person. This is especially important if a combination of fields may be a reference to another dataset.

 However, in general, try to keep the inbound data from a data source as untouched and close to its original representation as possible.

The reason why a reference should be in the form of a namespaced identifier is that the field then should be equal to the _id field of the referenced dataset, which is beneficial when making a hops to the referenced dataset.

The benefit of adding a property that is a combination of fields in the inbound pipe and not in a global or preparation pipe is that once it is added, you don't have to repeat the same ETL transformation in every pipe that needs this data. Also, if a combination of fields forms a reference to another dataset and will be used in a hops, it should be added in a dataset prior to that pipe.


.. _datamodelling-Global pipes / datasets:

Global pipes / datasets
=======================

Modelling of the :ref:`global datasets <best-practice-Global pipes>` are centered around defining logical placeholders of the data that is collected in Sesam. These placeholders should be based on what data they contain.

When defining global datasets, there are a few guidelines for modelling:

•   A global dataset should be defined by what the data it contains are.
•   Try to keep the number of global datasets low. 
•   Every dataset written to Sesam through an inbound pipe should be put into a global dataset, do not put a dataset into multiple global datasets.
•   If unsure which global a dataset should belong to, choosing one of the candidates is usually good enough, try avoiding creating new global datasets just for one    dataset.
•   There is no definite right or wrong way in how you organize your global datasets.
•   Avoid system specific global datasets.

When a global dataset has been defined, there are some considerations to be done in terms of how the global dataset should work:

•   Should data in a global dataset be merged to a single entity or not?
•   Is the data of such a format and quality that a golden record can be defined?
•   Would enhancing the data in a global dataset with data from another dataset improve the data for later use?

To read more about global datasets; the benefits and best practice of generating and using them, please see :ref:`here <best-practice-global>`.

.. _datamodelling-Merge data in a global dataset or not:

Merge data in a global dataset or not
=====================================

One of the purposes of a global dataset is to present a single authoritative truth about a concept or data. It is then logical to merge data from various different sources (or systems) in one global dataset if they define the same kind of object or type. For example, if some of the various sources contain person data, it would be logical to create a global dataset for person data and then merge each entity that refers to the same person. This is done so that when you ask for information about a specific entity, you also get information about that entity from the other systems. In terms of reusability this is a highly versatile way of getting all the data you need.

However, merging data comes with a cost. In certain cases, changing the rules of how the data are merged requires the pipe to be reset and run again. For large datasets this might mean that it will take time before the downstream pipes will get updates.

In some cases, merging the data isn’t logical. For instance, data like countries, counties, cities and streets might be put into a global location dataset, but it is not logical to merge these data. 

Also note that if a global dataset contains merged data, it does not necessarily mean that every other dataset in the global must be merged. Some data might be telling something about an entity but is not necessary the same thing. 

.. _datamodelling-Defining global properties and golden records:

Defining global properties and golden records
=============================================

For background on golden records, please read :ref:`here <best-practice-golden-record>`.

Often when you merge datasets together in a global dataset, you will find that some of the merged datasets contains properties that are the same. In some cases, it is valuable to add one global property to the global dataset that will be the most reliable of these properties.

For instance, let us say we have a person global dataset that merges three datasets from three different sources. All of these datasets contain a property for zipcode, but we know that one of the sources isn’t adequately updated. By adding a global zipcode property, determining which of the sources are the most reliable and using the zipcode from that source as the value, we provide a way for the downstream pipes to get the most reliable information.

When modelling we might like to create a set of global properties in the global dataset, usually being the most commonly used properties. In Sesam terminology we call such a collection of data for a golden record, which is a single, well-defined version of all the data entities in an organizational ecosystem. In this context, a golden record is sometimes called the "single version of the truth", where "truth" is understood to mean the reference to which data users can to turn when they want to ensure that they have the correct version of a piece of information.

Adding global properties does not mean that you have to create a golden record, there are many scenarios where adding a property to a global dataset is useful. However, adding a global property should be done with considerations. Remember that having to reset and rerun a global dataset has bigger implications than resetting and rerunning a preparation pipe, as there usually will be more downstream pipes that will be affected by it.

.. _datamodelling-Enhancing global datasets with data from other datasets:

Enhancing global datasets with data from other datasets
=======================================================

This point is quite similar to the above point, with the only difference being that you create global properties by making a `hops <https://docs.sesam.io/DTLReferenceGuide.html#hops>`_ to another dataset (preferably global).   

When modelling your global dataset and seeing the need to create a global property using hops, it is one thing you need to be aware of. Dependency tracking does not work for hops made in a “merge”-pipe. This means that you have to split the global pipe into two separate pipes. One pipe that contains the merge rules and does the merging, this pipe should be given the “merged-“ prefix. The second pipe should have the merged dataset as source and contain the DTL transformations, this should be the global pipe.

In general, try to keep hops from a global pipe to other datasets as minimal as possible. 

.. _datamodelling-To the point: Data Modelling:

To the point: Data Modelling
----------------------------

Let us begin by repeating an important truth about data modelling in Sesam: when modelling in Sesam do not create your data models by how they are related to each other by their properties (as in a standard relational database), but by what the data in the datasets are about.

For example, let us say we have two datasets or tables, ‘employee and ‘child’. In a relational database, these two tables would normally be linked by a one-to-many relation, i.e. an employee can have many children. However, when we look at these two tables from a Sesam perspective, both are in general speaking of a ‘person’. Hence, we should put both the ‘employee’ and ‘child’ table in the same global containing data about a person, ‘global-person’.

What you are trying to accomplish, is to have a set of global datasets that the preparation pipes can choose from, like food items grouped together in a supermarket to easily locate the food items you need. On the other hand, you don’t want the number of global datasets to grow out of hand, making it hard to find.

Start by analyzing the sources and data to determine the needs of the organization. This will have an impact on the data model and more specifically how the global datasets will be organized. It is here the organization needs to think: what is important to me? What data do I use often, and therefore needs to be easily available? The results vary for each organization and each data model.

Sesam as masterdata hub in a larger archtecture
-----------------------------------------------

Azure
=====

Google
======


