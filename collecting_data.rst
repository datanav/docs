=======
Collect
=======

.. contents:: Table of Contents
   :depth: 2
   :local:

Principles of collecting data
-----------------------------

Push or pull data?
==================

Sesam prefers to be the active party so that we can schedule when data is moved in and out.

Therefore, Sesam prefers to pull because then it is Sesam itself that has control of the data, i.e., control of when these are retrieved. This also means Sesam can retrieve data again without involving a third party.

The problem with push is that Sesam receives the data but at the same time has no option to request the data again, should the need arise.

.. collectiing_data-Raw data:

Raw data
========

Data is fed into Sesam through :ref:`an inbound pipe <best-practice-inbound-pipes>`. Firstly, you will do an analysis of the data. Then add a raw pipe to make sure Sesam has a copy of the original data. From the result of the analysis, you will then add properties that will enhance the data in terms of modelling, reusability and connectivity, such as:

 - **References to other datasets**: if a property is a reference or relation to another dataset, such as a foreign key field in a relational database, you should add an additional property that contains a reference to that dataset. This should be in the form of a :ref:`namespaced identifier <best-practice-namespace>`. These references are usually key properties when semantically linking data together in a global dataset but are also useful when connecting data in preparation pipes.
 - When raw data is linked to data used to categorize it or other metadata, it is advisable to split it; keep data and metadata separate. The metadata used to categorize can be merged into a global like ``global-classification``.
 -  :ref:`An RDF type <best-practice-rdf-type>`: this is a property providing a qualifier of what the data is and can be seen as metadata used to relate data and provide a semantic context to the data. When used with a namespace, it keeps track of the origin of the data, as well as the business type. An RDF type is useful in terms of filtering data, both from global datasets and in :ref:`hops <hops_dtl_function>` to other datasets.
 -  **A combination of fields**: a dataset may at times contain data that can form a fuller understanding of the field when combined, like a combination of first name and surname will give the full name of a person. This is especially important if a combination of fields may be a reference to another dataset.

The reason why a reference should be in the form of a namespaced identifier is that the field should then be equal to the _id field of the referenced dataset, which is beneficial when making a hops to the referenced dataset.

The benefit of adding a property that is a combination of fields in the inbound pipe and not in a global or preparation pipe is that once it is added, you don't have to repeat the same ETL transformation in every pipe that needs this data. Also, if a combination of fields forms a reference to another dataset and will be used in a hops, it should be added in a dataset prior to that pipe.

Advantages
==========
Importing raw data can be interesting for multiple reasons. When an external system can only push data for example, having a record of the data received allows us to consult previously ingested data or re-run a dataflow without having to request a new data delivery, which can sometimes be impossible. Or if an external system is to be decommissioned, historical data can be preserved within Sesam and made available should the replacing system need it. There are also external systems that prune data which might be necessary for other external systems with a broader lifecycle scope. For example, an ERP system will keep data from procuration to decommission, while the lifespan of data will be shorter in a system focusing on operations.

A two step approach
===================
To fullfil both goals of raw data retention and the ability to leverage the semantic capabilities of Sesam, an intermediary dataset becomes necessary. A “raw” pipe will be inserted before the input pipe and act as a double-door entrance. Its duties are to interface with the external system and create the verbatim raw dataset. From the input pipe’s point of view, the raw dataset is the data source as if it was from the external system itself. The semantic correlation, Sesamification if you will, is then performed in the input pipe. Namespace identifiers and rdf types are added, and the data is sent to the pertinent global, either as a whole or broken down, depending on the elected conceptual segmentation.

A word about data ownership and data availability
=================================================
In the case when data is only available within Sesam, Sesam will become the de facto data owner and should be considered and labelled as such in broader architecture documentation and resources. Also, it is necessary to ensure those datasets are preserved, by setting them up as high availability pipes. High availability pipes have built in mechanisms for data redundancy, securing data retention.

Test data
=========

Test data is generated to be able to test that the data behaves as expected.

It is a best practice to build a foundation of test data in the inbound pipe and then build on this as the need for testing arises. This is a smoother option than to try to generate perfect test data at the very beginning. This set of data can consist of ten or so objects, anonymized if required. Make sure it contains the fields required for testing, i.e. if you are testing merging, you need the fields you are merging on (e.g., merging person from HR and ERP system, you need social security number in both datasets).

To read more about test data and how it is set up in Sesam, please click :ref:`here <best-practice-inbound-pipes>`

Monitoring
==========

Sesam has a built-in monitoring function to help to ensure data flows as expected and there are no bottlenecks or any stops. A best practice in Sesam is to switch on monitoring in the inbound and the outbound pipes as it will make clear if data is not flowing as expected.
