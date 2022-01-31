.. _creating-a-sesam-dataflow:

=========================
Creating a Sesam Dataflow
=========================

The Sesam Dataflow consists of the following steps: *Collect*, *Enrich*, *Connect*, *Transform* and *Share*. Each of these steps ensure data is modelled to a standard which allows Sesam to operate optimally. As such, it is extremely important to get aquainted with these steps, why they are important and what they do. 

.. _collect:

Collect
-------

Collecting data is primarily concerned with raw data and how Sesam operates when pulling data from a source.

.. _collect-push-or-pull:

Push or pull data?
^^^^^^^^^^^^^^^^^^

Sesam prefers to be the active party when scheduling the moving of data as it enters or exits Sesam. Therefore, Sesam prefers to pull data as this increases control and ensures Sesam can administer when data enters Sesam.

With regards to pushing of data, the challenge is that Sesam receives the data but at the same time has no option to request the data again, should the need arise.

.. _collect-raw-data:

Raw data
^^^^^^^^

Data is fed into Sesam through :ref:`an inbound pipe <best-practice-inbound-pipes>`. Firstly, you will do an analysis of the data. Then add a raw pipe to make sure Sesam has a copy of the original data. From the result of the analysis, you will then add properties, in the :ref:`enrich` step, that will enhance the data in terms of modelling, reusability and connectivity.

.. _collect-advantages:

Advantages
^^^^^^^^^^

Importing raw data can be interesting for multiple reasons. When an external system can only push data for example, having a record of the data received allows us to consult previously ingested data or re-run a dataflow without having to request a new data delivery, which can sometimes be impossible. Or if an external system is to be decommissioned, historical data can be preserved within Sesam and made available should the replacing system need it. There are also external systems that prune data which might be necessary for other external systems with a broader lifecycle scope. For example, an ERP system will keep data from procuration to decommission, while the lifespan of data will be shorter in a system focusing on operations.

.. _collect-two-step-approach:

A two step approach
^^^^^^^^^^^^^^^^^^^

To fullfil both goals of raw data retention and the ability to leverage the semantic capabilities of Sesam, an intermediary dataset becomes necessary. A “raw” pipe will be inserted before the input pipe and act as a double-door entrance. Its duties are to interface with the external system and create the verbatim raw dataset. From the input pipe’s point of view, elaborated in the :ref:`enrich` step, the raw dataset is the data source as if it was from the external system itself.

.. _collect-ownership-&-availability:

A word about data ownership and data availability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the case when data is only available within Sesam, Sesam will become the de facto data owner and should be considered and labelled as such in broader architectural documentation and resources. Also, it is necessary to ensure those datasets are preserved, by setting them up as high availability pipes. High availability pipes have built in mechanisms for data redundancy, securing data retention.

.. _collect-test-data:

Test data
^^^^^^^^^

Test data is generated to be able to test that the data behaves as expected.

It is a best practice to build a foundation of test data in the inbound pipe and then build on this as the need for testing arises. This is a smoother option than to try to generate perfect test data at the very beginning. This set of data can consist of ten or so objects, anonymized if required. Make sure it contains the fields required for testing, i.e. if you are testing merging, you need the fields you are merging on (e.g., merging person from HR and ERP system, you need social security number in both datasets).

To read more about test data and how it is set up in Sesam, please click :ref:`here <best-practice-inbound-pipes>`

.. _collect-monitoring:

Monitoring
^^^^^^^^^^

Sesam has a built-in monitoring function to help to ensure data flows as expected and there are no bottlenecks or any stops. A best practice in Sesam is to switch on monitoring in the inbound and the outbound pipes as it will make clear if data is not flowing as expected.

.. _enrich:

Enrich
------

The enrichment step is concerned with adding :ref:`namespaces <concepts-namespaces>` and :ref:`namespaced identifiers <best-practice-namespace>`. Sesam makes use of RDF (https://www.w3.org/RDF/) to apply this enrichment and as such describe what a certain field means. Other types of semantics can be utilized if need be.

.. _semantics-as-a-method-of-enrichment:

Semantics as a method of enrichment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Classifying data in Sesam is done by using semantics to describe properties of a certain field. If one uses RDF or other methods to define semantics of input from sources, it will be easier to understand what a field is in the latter steps in a Sesam dataflow.

As an example, imagine a source having a field called *first name*, albeit in another system a similar field might be called *given name*. Using semantics, you can clarify whether these are the same, where they originate from and how they should be related. By using semantics, like RDF, Uniform Resource Identifiers (URI) can be created. If not using standards, one should make a data catalog that defines the semantics of the input sources and output targets. As such, ensuring that proper enrichment can be carried out.

The following are benefits of semantic enrichment:

- **References to other datasets**: if a property is a reference or relation to another dataset, such as a foreign key field in a relational database, you should add an additional property that contains a reference to that dataset. This should be in the form of a :ref:`namespaced identifier <best-practice-namespace>`. These references are usually key properties when semantically linking data together in a global dataset, :ref:`connect`, but are also useful when connecting data in preparation pipes, :ref:`transform`.

    .. hint::

        - When raw data is linked to data used to categorize it or other metadata, it is advisable to split it; keep data and metadata separate. The metadata used to categorize can be merged into a global like ``global-classification``.

-  :ref:`An RDF type <best-practice-rdf-type>`: this is a property providing a qualifier of what the data is and can be seen as metadata used to relate data and provide a semantic context to the data. When used with a namespace, it keeps track of the origin of the data, as well as the business type. An RDF type is useful in terms of filtering data, both from global datasets and in :ref:`hops <hops_dtl_function>` to other datasets.

.. _connect:

Connect
-------

The raw data, having now been enriched, are ready to be connected to other data from other sources. This can be done in various ways and the next few chapters will describe this in detail. 

.. _connect-global-pipes-datasets:

Global pipes / datasets
^^^^^^^^^^^^^^^^^^^^^^^

When connecting data in Sesam, it is important to understand :ref:`global datasets <best-practice-global-pipes>` as these are collections of data that pertain to the same concept from different sources. 

The main purpose of a global dataset is to be the single authorative location to get fresh data about a specific concept. Generally when we want to start building globals, we start at a high level and work our way into the details. For example, if we work for a business which sells stationary, it will be natural to create globals based on various things we sell: global-paper, global-pens, global-postit, global-equipment etc. This is exactly how we would stock the shelves in a stationary shop. If, however we are a pen specialist, our perspective would be completely different and we would have a global-pencil, global-marker, global-ballpoint global-ink etc. Here we have so many kinds of pens that it does not make sense to have a shelf for printing paper or notebooks, but we would sort the pens after type of pen in the very same way we sort them into various global datasets.

Neither of these two examples are wrong but make sense for each example as their data requirements and use of data are very different, even though a lot of their data is the same. So, when wanting to sort data in globals in order to retrieve it in the :ref:`transform` step, it is important to ensure logical grouping.

A general rule is that every dataset that is written to Sesam from an external data source should be put into its appropriate global, however small it is.

When defining global datasets, there are a few guidelines for modelling:

•   A global dataset should be defined by what the data it contains is.
•   Try to keep the number of global datasets low.
•   Every dataset written to Sesam through an inbound pipe should be put into a global dataset, do not put a dataset into multiple global datasets.
•   If unsure which global a dataset should belong to, choosing one of the candidates is usually good enough, try avoiding creating new global datasets just for one dataset.
•   There is no definite right or wrong way in how you organize your global datasets.
•   Avoid system specific global datasets.

When a global dataset has been defined, there are some questions to be considered in terms of how a global dataset should work:

•   Should data in a global dataset be merged to a single entity or not?
•   Is the data of such a format and quality that a :ref:`golden record <best-practice-golden-record>` can be defined?
•   Would enhancing the data in a global dataset with data from another dataset improve the data for later use?

.. _connect-classification-of-data:

Classification of data
^^^^^^^^^^^^^^^^^^^^^^

How do we decide which data pertains to the same concept? For example a person can potentially end up in global-customer, global-employee or global-person, which one is correct?

In Sesam we recommend a *one dimensional structure*, i.e. data can only belong to one global. Let us use an example; a company has lots of data about persons: customers, clients, prospects, employees and applicants. It is tempting to be able to separate these to generate a global for each. The problem with this is a person with a unique ID can end up in two or more globals (e.g., global-customer and global-person). Then it is the *role* of the person deciding and not the *concept*, which is data about persons.

So how can we differentiate between all the various types of persons? In Sesam we add a category. This is multidimensional, which means you can add several categories to each data type. For a person, this could be "Customer" then we could further add subcategories of customers like "VIP customer", "Private customer" etc. So *top level of classification is one dimensional* and *lower categories and subcategories are multidimensional* as an object can have several categories.

These principles coincide with `Carl Linnaeus <https://en.wikipedia.org/wiki/Linnaean_taxonomy>`__ principles of taxonomy; it is one dimensions that is each species can only belong to one category. He had 7 classifications:

Kingdom
Phylum
Classes
Orders
Family
Genera
Species

When classifying in Sesam, it is advisable to start high up in the hierarchy but not at top as that proves to be too general, but for most data modelling, starting at Phylum or Classes is a good starting point. To further classify deeper down in the hierarchy, we add categories and subcategories.

To meet this requirement for classifying data, as stated previously, we recommend generating a *global-classification* dataset. This contains various metadata that can be picked up and enriched via hops to the data that needs categorization. 

.. _connect_merge-data-or-not:

Merge data in a global dataset or not
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To emphasize: One of the main purposes of a global dataset is to present a single authoritative truth about a concept or data. Therefore, it is important to ask yourself whether data from different systems should be merged in a global or not. 

It is logical to merge data from various systems in one global dataset if they define the same kind of object or type. For example, if some of the various sources contain person data, it would be logical to create a global dataset for person data and then merge each entity that refers to the same person. This is done so that when you ask for information about a specific entity, you also get information about that entity from the other systems. In terms of reusability this is a highly versatile way of getting all the data you need.

.. warning::

    - However, merging data comes with a cost. In certain cases, changing the rules of how the data are merged requires the pipe to be reset and run again. For large datasets this might mean that it will take time before the downstream pipes will get updates.

In some cases, merging the data isn't logical. For instance, data like countries, counties, cities and streets might be put into a global location dataset, but it is not logical to merge these data. For example, if we think of Norway (a country) and Oslo (a city), they both could fit into a global location dataset, both being locations, but we can agree that Norway and Oslo are not the same thing.

Also note that if a global dataset contains merged data, it does not necessarily mean that every other dataset in the global must be merged. Some data might be telling something about an entity but it's not necessarily the same thing.

.. _connect-defining-global-properties:

Defining global properties
^^^^^^^^^^^^^^^^^^^^^^^^^^

For background on global properties, please read :ref:`here <best-practice-golden-record>`.

There are 3 main reasons to introduce global properties:

- These are established standards you want to use.
- One will establish standard characteristics that make it easier for consumers of data to know which properties to use.
- Properties that are conceptually about the same thing, albeit they originate from more than one system, logic must be defined to ensure the desired system is authoritative

Often when you merge datasets together in a global dataset, you will find that some of the merged datasets contain properties that are the same. In some cases, it is valuable to add one global property to the global dataset that will be the most reliable with regards to these properties.

For instance, let us say we have a person global dataset that merges three datasets from three different systems. All of these datasets contain a property for zipcode, but we know that one of the systems isn’t adequately updated. By adding a global zipcode property, determining which of the systems are the most reliable and using the zipcode from that source as the value, we provide a way for the downstream pipes to get the most reliable information.

Instead of having to define global properties in advance, Sesam is built so that these can be continuously defined and changed over time and as needed. Some recommendations for when to establish global properties:

- In advance, if standardised schema are to be used.
- On demand, when a consumer needs properties that may originate from more than one system.

If you need to use a :ref:`hops <hops_dtl_function>` function to another global dataset when creating global properties, it is recommended to do this through feedback loops.

.. _connect-feedback-loops:

Feedback loops
^^^^^^^^^^^^^^

A feedback loop is a downstream pipe from a global, that creates a dataset that is merged back in to the same global. This mechanism is needed to build properies that need to be created recursively. It is also the recommended way to add properties that is dependent on hops to other datasets.

.. warning::

    - Be aware that a feedback pipe will effectively block the completeness feature if it is not excluded from the completeness chain.

.. _transform:

Transform
---------

Transforming data is concerned with late schema binding and as such data formats become relevant.

.. _transform-late-schema-binding:

Late schema binding
^^^^^^^^^^^^^^^^^^^

As everything in Sesam is JSON, Sesam is schemaless. Therefore, Sesam supports any data schema and transforms the data from the global datasets into the target schema before offering it to the target system. In a Sesam dataflow, this is done in :ref:`preparation pipes <best-practice-preparation-pipes>`.

Sesam does not offer automatic schema validation nor business rules validation. Such validation has to be developed outside of Sesam.

.. _transform-data-format:

Data format
^^^^^^^^^^^

Sesam has native connectors to transform its internal JSON format into the most common data formats, like XML, JSON, SQL, CSV, Excel etc. Any format not supported can be delivered using the push mechanism through a microservice. Sesam has a library of `microservices <https://github.com/sesam-community>`_, but in some cases a new microservice has to be developed if Sesam needs to connect to an unfamiliar or special system. This can be necessary because of special data format or security requirements of the targets.

.. _share:

Share
-----

The main benefit of Sesam is its ability to share data by delivering it in the form that each target system asks for. Instead of changing the systems to fit the data, Sesam speaks the target's language.

The core principle of data management with Sesam is to bring data to any target systems in need. The targets will use their optimized data storage to store the new data.

.. _share-transport:

Transport
^^^^^^^^^

Sesam supports both push and publish mechanisms. Push has the advantage of making it possible for Data Managers to control the flow and know the state of the target system. Publish has an advantage that gives the target system control over their dataflow, but supports a limited array of data formats, such as JSON, CSV, XML, RDF, SD-SHARE and only supports HTTPS.
Sesam does not support ad hoc querying on published data. Sesam has a limited support for pre-defined query properties or data subsets.

.. _share-identifiers:

Identifiers
^^^^^^^^^^^

When sending data to a target system, the main challenge is using the right identifiers for the object you update, and also the right identifiers for any references from that object to other objects in the same target system.
The correct ID for the necessary objects is available in the global datasets, and by hopping to them in the outgoing flow, the correct identifiers can be populated.

.. _share-completeness:

Completeness
^^^^^^^^^^^^

To ensure that any composed object is complete before sending it to a target system, the completeness feature(if set) will delay the transfer of incomplete objects to targets. If the completeness feature is not set, incomplete objects will be sent to targets. 

.. _share-generated-identifiers:

Generated identifiers
^^^^^^^^^^^^^^^^^^^^^

In API-based systems the result of the insert or update call should feed back into the target input flow, to handle IDs and errors.