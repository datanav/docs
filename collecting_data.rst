==========================
Connect & collect patterns
==========================

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
------------

Principles for collecting data is pulling data is best practice. Once data is in sesam through the inbound pipe, a small number of properties can be added to aid connecting and re-using data. This is done mainly by modeling global datasets where we :ref:`merge <getting-started-merging-sources>` data about same object. 

Once this is done we can further enrich data by adding data from other datasets or do other :ref:`transformations <getting-started-transformations> depending on requirements. 

Principles of collecting data
-----------------------------

Push or pull data?
==================

Sesam prefers to be the active party so that we can schedule when data is moved in and out. 

Therefore Sesam prefers pull because then it is Sesam itself that has control of the data, i.e. control of when these are retrieved. At the same Sesam has the opportunity to retrieve the data again without involving a third party. 

The problem with push is that Sesam receives the data but at the same time has no option to request the data again should the need arise.

.. collectiing_data-Raw data:

Raw data
========

Data is fed into Sesam through :ref:`an inbound pipe <data-modelling-Inbound pipes>`. Firstly you will do an analysis of the data. From the result of the analysis you will then add properties that will enhance the data in terms of modelling, reusability and connectivity, such as:

 • **References to other datasets**: if a property is a reference or relation to another dataset, such as a foreign key field in a relational database, you should add an additional property that contains a reference to that dataset. This should be in the form of a :ref:`namespaced identifier <data-modelling-namespace>`. These references are usually key properties when semantically link data together in a global dataset but are also useful when connecting data in preparation pipes.
 •  :ref:`An RDF type <best-practice_-rdf type>`: this is a property providing a qualifier of what the data is and can be seen as metadata used to relate data and provide a semantic context to the data. When used with a namespace, it keeps track of the origin of the data, as well as the business type. An RDF type is useful in terms of filtering data, both from global datasets and in :ref:`hops <hops_function>` to other datasets.
 •  **A combination of fields**: a dataset may at times contain data that when combined can form a fuller understanding of the field, like a combination of first name and surname will give the full name of a person. This is especially important if a combination of fields may be a reference to another dataset.

However, aim to keep the inbound data from a data source as untouched and close to its original representation as possible.

The reason why a reference should be in the form of a namespaced identifier is that the field then should be equal to the _id field of the referenced dataset, which is beneficial when making a hops to the referenced dataset.

The benefit of adding a property that is a combination of fields in the inbound pipe and not in a global or preparation pipe is that once it is added, you don't have to repeat the same ETL transformation in every pipe that needs this data. Also, if a combination of fields forms a reference to another dataset and will be used in a hops, it should be added in a dataset prior to that pipe.

Principles of connecting data
-----------------------------

When connecting data in Sesam, it is important to understand :ref:`global datasets <data-modelling-Global pipes>`. The raw data where additional properties were added is now ready to be connected to other data from other sources. This can be done in various ways so next few chapters will describe this in more detail.

.. collecting_data-Global pipes / datasets:

Global pipes / datasets
=======================

These are collections of data that pertains to the same concept from different sources. The main purpose of a global dataset is to be the single authorative location to get fresh data about a specific concept from. A general rule is that every dataset that is written to Sesam from an external data source should be put into its appropriate global, however how small it is.

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

.. collecting_data-Merge data in a global dataset or not:

Merge data in a global dataset or not
=====================================

One of the purposes of a global dataset is to present a single authoritative truth about a concept or data. It is then logical to merge data from various different sources (or systems) in one global dataset if they define the same kind of object or type. For example, if some of the various sources contain person data, it would be logical to create a global dataset for person data and then merge each entity that refers to the same person. This is done so that when you ask for information about a specific entity, you also get information about that entity from the other systems. In terms of reusability this is a highly versatile way of getting all the data you need.

However, merging data comes with a cost. In certain cases, changing the rules of how the data are merged requires the pipe to be reset and run again. For large datasets this might mean that it will take time before the downstream pipes will get updates.

In some cases, merging the data isn’t logical. For instance, data like countries, counties, cities and streets might be put into a global location dataset, but it is not logical to merge these data. 

Also note that if a global dataset contains merged data, it does not necessarily mean that every other dataset in the global must be merged. Some data might be telling something about an entity but is not necessary the same thing. 

.. collecting_data-Defining global properties and golden records:

Defining global properties and golden records
=============================================

For background on golden records, please read :ref:`here <best-practice-golden-record>`.

Often when you merge datasets together in a global dataset, you will find that some of the merged datasets contains properties that are the same. In some cases, it is valuable to add one global property to the global dataset that will be the most reliable of these properties.

For instance, let us say we have a person global dataset that merges three datasets from three different sources. All of these datasets contain a property for zipcode, but we know that one of the sources isn’t adequately updated. By adding a global zipcode property, determining which of the sources are the most reliable and using the zipcode from that source as the value, we provide a way for the downstream pipes to get the most reliable information.

When modelling we might like to create a set of global properties in the global dataset, usually being the most commonly used properties. In Sesam terminology we call such a collection of data for a golden record, which is a single, well-defined version of all the data entities in an organizational ecosystem. In this context, a golden record is sometimes called the "single version of the truth", where "truth" is understood to mean the reference to which data users can to turn when they want to ensure that they have the correct version of a piece of information.

Adding global properties does not mean that you have to create a golden record, there are many scenarios where adding a property to a global dataset is useful. However, adding a global property should be done with considerations. Remember that < to reset and rerun a global dataset has bigger implications than resetting and rerunning a preparation pipe, as there usually will be more downstream pipes that will be affected by it.

.. collecting_data-Enhancing global datasets with data from other datasets:

Enhancing global datasets with data from other datasets
=======================================================

This point is quite similar to the above point, with the only difference being that you create global properties by making a :ref:`hops <hops_function>` to another dataset (preferably global).   

When modelling your global dataset and seeing the need to create a global property using hops, it is one thing you need to be aware of. Dependency tracking does not work for hops made in a “merge”-pipe. This means that you have to split the global pipe into two separate pipes. One pipe that contains the merge rules and does the merging, this pipe should be given the “merged-“ prefix. The second pipe should have the merged dataset as source and contain the DTL transformations, this should be the global pipe.

In general, try to keep hops from a global pipe to other datasets as minimal as possible. 

Test data
=========

Monitoring
==========

.


