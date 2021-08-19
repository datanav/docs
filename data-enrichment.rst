===============
Data enrichment
===============

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
------------

Data enrichment in Sesam is adding of new properties to an object either by the merging of data from multiple sources or transforming existing properties into new ones. This enrichment is then stored with separate namespeces as global-properties inside global datasets.

.. data-enrichment-Defining global properties:
Defining global properties
==========================

For background on global properties, please read :ref:`here <best-practice-golden-record>`.

There are 3 main reasons to introduce global properties

- There are established standards you want to use
- One will establish standard characteristics that make it easier for consumers of data to know which properties to use
- Properties that can originate in more than one source, where logic must be defined for which source is authoritative

Often when you merge datasets together in a global dataset, you will find that some of the merged datasets contains properties that are the same. In some cases, it is valuable to add one global property to the global dataset that will be the most reliable of these properties.

For instance, let us say we have a person global dataset that merges three datasets from three different sources. All of these datasets contain a property for zipcode, but we know that one of the sources isn’t adequately updated. By adding a global zipcode property, determining which of the sources are the most reliable and using the zipcode from that source as the value, we provide a way for the downstream pipes to get the most reliable information.

Instead of having to define global properties in advance, Sesam is built so that these can be continuously defined and changed over time and as needed. Some recommendations for when to establish global properties:

- In advance, if standardised schema already exists are to be used
- On demand, when a consumer needs properties that may originate in more than one source

If the creation of the global properies needs to use a :ref:`hops <hops_function>` to another global datasets, it is recomended to do this trough feedback loops.

.. data-enrichment-Defining global properties:
Feedback loops
==============

A feedback loop is a downstream pipe from a global, that creates a dataset that is merged back in to the same global. This mechanism is needed to build properies that needs to be created recursively. It is also the recomended way to add properties that is dependent on hops to other dataset. 

Be aware that a feedback pipe will effectivly block the completeness feature if it is not exclude from the completeness chain.
