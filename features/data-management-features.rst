.. _data-management-features:

.. rst-class:: center-title

================
Data Management
================

Sesam offer a set of features that will give you the edge when it comes to Master Data Management and data integration. Below is a list of core features Sesam offers.

|
|
|


.. panels::
    :body: text-left
    :container: container-lg pb-3
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2 custom-card

    **Data Transformation Language**

    DTL allows to describe transformations performed on streams of data in order to create and shape datasets.

    .. link-button:: ../data-transformation-language
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Automatic Reprocessing**

    Perform automatic reset of pipes when they have fallen out of sync.

    .. link-button:: /features/automatic-reprocessing
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Namespaces**

    A namespaced identifier (NI) is a unique reference to an abstract thing.

    .. link-button:: /features/namespaces
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Merging**

    Gives global datasets the ability to merge different entities into one entity representing the same thing.

    .. link-button:: /features/merging-feature
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Global datasets**

    The recommended way of organizing the data in Sesam is to model and store the data in global datasets.

    .. link-button:: /features/global-datasets
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Dependency Tracking**

    Understand complex data dependecies in Data Transformation Language.

    .. link-button:: /features/dependency-tracking
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Schema Inferencing**

    See the structure of the data that went into the pipe and the data that came out of it.

    .. link-button:: /features/schema-inferencing
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Schema Models**

    Schema inferencing generates entity types for the pipe source and pipe sink.

    .. link-button:: /features/schema-models
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Integrated Search**

    Integrated data browsing gives you more insight into your data and relationships within.

    .. link-button:: /features/integrated-search
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Property Lineage**

    Property lineage lets you inspect the dependencies between properties in your data.

    .. link-button:: /features/property-lineage
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Completeness**

    Makes sure that all pipes that a specific pipe is dependent on have run before it processes the source entities of this pipe.

    .. link-button:: /features/completeness-feature
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Compaction**

    A retention policy that ensures that a dataset does not consume all available disk space.

    .. link-button:: /features/compaction-feature
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Config Groups**

    Configure your sesam subscription by adding and modifying single systems and pipes via specific endpoints.

    .. link-button:: /features/api-config-groups
            :type: ref
            :text: Read more
            :classes: read-more

|

.. toctree::
   :maxdepth: 1
   :hidden:

    Automatic Reprocessing <automatic-reprocessing>
    Namespaces <namespaces>
    Merging <merging-feature>
    Global datasets <global-datasets>
    Dependency Tracking <dependency-tracking>
    Schema Inferencing <schema-inferencing>
    Schema Models <schema-models>
    Integrated Search <integrated-search>
    Property Lineage <property-lineage>
    Completeness <completeness-feature>
    Compaction <compaction-feature>
    Config Groups <api-config-groups>
