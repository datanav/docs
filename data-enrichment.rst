===============
Data enrichment
===============

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
------------
.. rubric:: Continuous enrichment of data and data model pattern

Data enrichment is the merging of related data from multiple sources to the data platform. Data enrichment in Sesam is continuous, all systems can at any time make data available to the data platform, and onto the systems that need it. Data can also be enrich from within the data model, and data can be fetch from one dataset to complement another.  Data enrichment is typically triggered when data is refreshed, or the pipe reprocessed. Although continuous data enrichment has pitfalls and care should be taken in the design of the data model pattern. Indeed, positive feedback loops can occur and updated data could trigger more updates in a back and forth infinite loop. There are a few tools to prevent this phenomenon, for exemple identify merged entities as such and prevent source pipe to re process them.

.. rubric:: Data refresh and completeness

Certain data updates might require to be applied to a whole dataset at once. Sesam offers a completeness mechanism that allows any processing of the data being updated to be put on hold until the whole dataset has been processed. Note that this mechanism can impede performances of the node when applies to a large global.

.. rubric:: Golden record

Data enrichment and semantic correlation can bind together conflicting data. It is important to define who/which system has the authority and identify the trustworthy elements within the data platform. The “golden record” is the result of this labelling, it encompasses the set of elements that are deemed trustworthy and up to date.


Defining global properties and golden records
=============================================

For background on golden records, please read :ref:`here <best-practice-golden-record>`.

Often when you merge datasets together in a global dataset, you will find that some of the merged datasets contains properties that are the same. In some cases, it is valuable to add one global property to the global dataset that will be the most reliable of these properties.

For instance, let us say we have a person global dataset that merges three datasets from three different sources. All of these datasets contain a property for zipcode, but we know that one of the sources isn’t adequately updated. By adding a global zipcode property, determining which of the sources are the most reliable and using the zipcode from that source as the value, we provide a way for the downstream pipes to get the most reliable information.

When modelling we might like to create a set of global properties in the global dataset, usually being the most commonly used properties. In Sesam terminology we call such a collection of data for a golden record, which is a single, well-defined version of all the data entities in an organizational ecosystem. In this context, a golden record is sometimes called the "single version of the truth", where "truth" is understood to mean the reference to which data users can turn when they want to ensure that they have the correct version of a piece of information.

Adding global properties does not mean that you must create a golden record, there are many scenarios where adding a property to a global dataset is useful. However, adding a global property should be done with considerations. Remember that to reset and rerun a global dataset has bigger implications than resetting and rerunning a preparation pipe, as there usually will be more downstream pipes that will be affected by it.

There are 3 main reasons to introduce global properties

- There are established standards you want to use
- Properties that can originate in more than one source, where logic must be defined for which source is authoritative
- One will establish standard characteristics that make it easier for consumers of data to know which properties to use

Instead of having to define global properties in advance, Sesam is built so that these can be continuously defined and changed over time and as needed. Some recommendations for when to establish global characteristics:

- In advance, if standardised schema already exists to be used
- On demand, when a consumer needs properties that may originate in more than one source

.. collecting_data-Enhancing global datasets with data from other datasets:

Enhancing global datasets with data from other datasets
=======================================================

This point is quite similar to the above point, with the only difference being that you create global properties by making a :ref:`hops <hops_function>` to another global datasets.   

When modelling your global dataset and seeing the need to create a global property using hops, it is one thing you need to be aware of. Dependency tracking does not work for hops made in a “merge”-pipe. This means that you must split the global pipe into two separate pipes. One pipe that contains the merge rules and does the merging, this pipe should be given the “merged-“ prefix. The second pipe should have the merged dataset as source and contain the DTL transformations, this should be the global pipe.

However, in general, try to keep hops from a global pipe to other datasets as minimal as possible. Separating the global datasets into two datasets in order to enrich the data with data from other datasets also means duplicating the data. Adding data that may change due to dependency tracking may also lead to more processing for the downstream pipes, this is especially true for global datasets as they usually have multiple downstream pipes reading from them. The ideal pattern for doing this is only when the enriched data is necessary for multiple downstream datasets. 

Feedback loops
==============

A feedback loop i a downstream pipe from a global, that creates a dataset that is merged back in to the same global. This mechanism is needed to build properies that needs to be created recursively. It is also a way to add data that is dependent on hops to other dataset, without spliting a global in to several staps. A feedback pipe will effectivly block the completeness feature if it is not exclude from the completeness chain.
