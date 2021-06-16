==========================
Connect & collect patterns
==========================

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
------------

When starting a new Sesam project it is very important to start thinking of how to organise the data in Sesam; what sort of data do we have, how is it linked in source system and how will it be used? What are the goals and requirements for wanting to use Sesam? Very early on, we start looking at the raw data and needing to consider and plan which globals do we need and how will we generate them. If not, it is guaranteed it will be chaos; we can have data object in more than one global, they can be enriched in one global, and not in another and it is impossible to know which one we should use.

Principles for collecting data is pulling data is best practice. Once data is in sesam through the inbound pipe, a small number of properties can be added to aid connecting and re-using data. This is done mainly by modeling global datasets where we :ref:`merge <getting-started-merging-sources>` data about same object. 

Once this is done we can further enrich data by adding data from other datasets or do other :ref:`transformations <getting-started-transformations>`depending on requirements. 

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
 • When raw data is linked to data used to categorize it or other metadata, it is advisable to split it; keep data and metadata seperate. The metadata used to categorize can be merged into global-classification.
 •  :ref:`An RDF type <best-practice_-rdf type>`: this is a property providing a qualifier of what the data is and can be seen as metadata used to relate data and provide a semantic context to the data. When used with a namespace, it keeps track of the origin of the data, as well as the business type. An RDF type is useful in terms of filtering data, both from global datasets and in :ref:`hops <hops_function>` to other datasets.
 •  **A combination of fields**: a dataset may at times contain data that when combined can form a fuller understanding of the field, like a combination of first name and surname will give the full name of a person. This is especially important if a combination of fields may be a reference to another dataset.

However, aim to keep the inbound data from a data source as untouched and close to its original representation as possible.

The reason why a reference should be in the form of a namespaced identifier is that the field then should be equal to the _id field of the referenced dataset, which is beneficial when making a hops to the referenced dataset.

The benefit of adding a property that is a combination of fields in the inbound pipe and not in a global or preparation pipe is that once it is added, you don't have to repeat the same ETL transformation in every pipe that needs this data. Also, if a combination of fields forms a reference to another dataset and will be used in a hops, it should be added in a dataset prior to that pipe.

Advantages
==========
Importing raw data can be interesting for multiple reasons. When an external system can only push data for example, having a record of the data received will allow to consult previously ingested data or re-run a data flow without having to request a new data delivery, which can sometimes be impossible. Or if an external system is to be decommissioned, historical data can be preserved within Sesam and made available should the replacing system needs it. There are also external systems that prune data that is might necessary for other external system with a broader lifecycle scope. An ERP for example will keep data from procuration to decommission, while the lifespan of data will be shorter an a system focussing on operations.

A two steps approach
====================
To fulfil both goals of raw data retention and ability to leverage the semantic capabilities of Sesam, an intermediary dataset becomes necessary. A “raw” pipe will be inserted before the input pipe and act as a double-door entrance. Its duties are to interface with the external system and create the verbatim raw dataset. From the input pipe’s point of view, the raw dataset is the data source as if it were from the external system itself. The Semantic correlations, Sesamification if you will, is then performed in the input pipe. Namespace identifiers and rdf types are added, and the data is sent to the pertinent global, either as a whole or broken down, depending on the elected conceptual segmentation.

A word about data ownership and data availability
=================================================
In the case of data only available within Sesam, Sesam will become the de facto data owner and should be considered and labelled as such in broader architecture documentation and resources. Also, it is necessary to ensure those datasets are preserved, by setting them up as high availability pipes (links to doc). High availability pipes have built in mechanisms for data redundancy, securing data retention.



Principles of connecting data
-----------------------------

When connecting data in Sesam, it is important to understand :ref:`global datasets <data-modelling-Global pipes>`. The raw data where additional properties were added is now ready to be connected to other data from other sources. This can be done in various ways so next few chapters will describe this in more detail.

.. collecting_data-Global pipes / datasets:

Global pipes / datasets
=======================

These are collections of data that pertains to the same concept from different sources. The main purpose of a global dataset is to be the single authorative location to get fresh data about a specific concept. Generally when we want to start building globals, we start at high level and work our way into the details. For example if we work for a business who sells stationary, it will be natural to create globals based on various things we sell;  global-paper, global-pens, global-postit, global-equipment etc. This is exactly how we would stock the shelves in a stationary shop. If, however we are a pen specialist our perspective would be completely different and we would have a global-pencil, global-marker, global-ballpoint global-ink etc. Here we have so many different kinds of pens it does not make sense to have a shelf for printing paper or notes books but we would sort the pens after type of pen in the very same way we sort them into various global data sets. 

None of these two examples are wrong but make sense for each example as their data requirements and use of data are very different even though a lot of their data is the same. So when wanting to sort data into globals in order to retrieve it and it is logical to search for it, it is important to understand what data we have and how we can group it to build globals in Sesam.

A general rule is that every dataset that is written to Sesam from an external data source should be put into its appropriate global, however how small it is.

When defining global datasets, there are a few guidelines for modelling:

•   A global dataset should be defined by what the data it contains are.
•   Try to keep the number of global datasets low. 
•   Every dataset written to Sesam through an inbound pipe should be put into a global dataset, do not put a dataset into multiple global datasets.
•   If unsure which global a dataset should belong to, choosing one of the candidates is usually good enough, try avoiding creating new global datasets just for one dataset.
•   There is no definite right or wrong way in how you organize your global datasets.
•   Avoid system specific global datasets.

When a global dataset has been defined, there are some considerations to be done in terms of how the global dataset should work:

•   Should data in a global dataset be merged to a single entity or not?
•   Is the data of such a format and quality that a golden record can be defined?
•   Would enhancing the data in a global dataset with data from another dataset improve the data for later use?
•	Structure of data; try to keep it flat if possible.

To read more about global datasets; the benefits and best practice of generating and using them, please see :ref:`here <best-practice-global>`.

Classification of data
^^^^^^^^^^^^^^^^^^^^^^

How do we decide which data pertains to the same concept? For example a person can potentially end up in global-customer, global-employee or global-person, which one is correct? 

In Sesam we recommend a *one dimensional structure*, i.e. data can only belong to one global. Let us use an example; a company has lots of data about persons; both customers, clients, prospects, employees and applicants. It is tempting to be able to separate these to generate a global for each. The problem with this is a person with a unique ID can end up in two or more globals (e.g. global-customer and global-person). Then it is *role* of person deciding and not *concept*; which is data about persons. 

So how can we differentiate between all the various types of person? In Sesam we add a category. This is multidimensionaland  which means you can add several categories to each data type. For a person, this could be "Customer" then we could further add subcategories of customers like "VIP customer", "Private customer" etc. So *top level of classification is one dimensional* and *lower categories and subcategories are multidimensional* as an object can have several categories.

These principles actually coincide with Carl Linnaeus principles of taxonomy; it is one dimensions that is each species can only belong to one category. He had 7 classifications:

Kingdom
Phylum
Classes
Orders 
Family
Genera
Species

When classifying in Sesam, it is advisable to start high up in the hierarchy but not at top as that proves to be too general, but for most data modelling, starting at Phylum or Classes is a good starting point. To further classify deeper down in the hierarchy, we add categories and subcategories.

To meet this requirement for classifying data, we recommend always generating a *global-classification* dataset. This contains various metadata that can be picked up and enriched via hops to the data needing categories. When mentioning splitting of raw data, to "clean it" so that the objects come in clean and the data used to categorize it in the source system can be merged into global classification to generate aggregated sets of metadata used to classify. En example on this can be a product and product type coming in as one data object. The best practice is to split the raw data into two data objects. The product can go into *global-equipment* for example. This depends on context. But it is highly recommended to always havae a *global-classification* dataset mentioned above where we would merge in data object *product type*. Product type is now ready to be used as category for products needing this.

.. collecting_data-Merge data in a global dataset or not:

Merge data in a global dataset or not
=====================================

One of the purposes of a global dataset is to present a single authoritative truth about a concept or data. It is then logical to merge data from various different sources (or systems) in one global dataset if they define the same kind of object or type. For example, if some of the various sources contain person data, it would be logical to create a global dataset for person data and then merge each entity that refers to the same person. This is done so that when you ask for information about a specific entity, you also get information about that entity from the other systems. In terms of reusability this is a highly versatile way of getting all the data you need.

However, merging data comes with a cost. In certain cases, changing the rules of how the data are merged requires the pipe to be reset and run again. For large datasets this might mean that it will take time before the downstream pipes will get updates.

In some cases, merging the data isn't logical. For instance, data like countries, counties, cities and streets might be put into a global location dataset, but it is not logical to merge these data. For example, if we think of Norway (a country) and Oslo (a city), they both could fit into a global location dataset, both being locations, but we can agree that Norway and Oslo is not the same thing.  

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

However, in general, try to keep hops from a global pipe to other datasets as minimal as possible. Separating the global datasets into two datasets in order to enrich the data with data from other datasets also means duplicating the data. Adding data that may change due to dependency tracking may also lead to more processing for the downstream pipes, this is especially true for global datasets as they usually have multiple downstream pipes reading from them. The ideal pattern for doing this is only when the enriched data is necessary for multiple downstream datasets. 

 

Test data
=========

Test data is generated to be able to test that the data behaves as expected.

It is best practice to build a foundation of test data in the inbound pipe and then build on this as the needs for testing arises. This is a smoother option than to try to generate prefect test data at the very beginning. This set of data can consist of 10 objects, anonymize if required and make sure it contains the fields required for testing. E.g. if you are testing merging, you need the fields you are margining on (E.g. mering person from HR and ERP system, you need social security number in both datasets).

To read more about test data and how it is set up in Sesam, please click :ref:`here <data-modelling-Inbound pipes>`

Monitoring
==========

Sesam ha a built in monitoring function to help to ensure data flows as expected and there are no bottlenecks or any stops. Best practice in Sesam is to switch on monitoring in the inbound and the outbound pipes as it will be clear to see if data is not flowing as expected.


