.. _building_blocks:

===============
Building blocks
===============

.. _concepts-streaming:

Streams of entities
-------------------

Sesam consumes and produces streams of :doc:`entities <entitymodel>`. An entity is very much like a JSON object and consists of a number of key-value pairs along with some special reserved property names. See the :doc:`entity data model <entitymodel>` document for more details about entities.

The following are two simple examples showing the shape of entities that can be consumed and exposed by Sesam.

.. code-block:: json
    :linenos:


    [
        {
            "_id": "1",
            "name": "Bill",
            "dob": "01-01-1980"
        },
        {
            "_id": "2",
            "name": "Jane",
            "dob": "04-10-1992"
        }
    ]

Streams of entities flow through :ref:`pipes<concepts-pipes>`. A pipe has an associated :ref:`pump<concepts-pumps>` that is scheduled to regularly pull data entities from the :ref:`source<concepts-sources>` , push them through  :ref:`transforms<concepts-transforms>` then send the results to the :ref:`sink<concepts-sinks>` . 


.. Important::

   Sesam's Service API is not built to serve a large number of concurrent clients. Sesam is primarily an asynchronous batching and stream processing system. The Service API is not meant to be used by user-facing applications that have low latency and high throughput requirements. For that reason we do not currently give any guarantees in this regard. In practice means that if you have such a requirement you should stream the data out of Sesam and host it in a dedicated publishing systems that can scale its endpoints.

.. _concepts-datasets:

Datasets
--------

A dataset is the basic mean of storage inside Sesam. A dataset is a log of :doc:`entities <entitymodel>` supported by primary and secondary indexes. 

A :ref:`dataset sink <dataset_sink>` can write entities to the dataset. An entity is appended to the log if it is new (as in, an entity with a never-before-seen ``_id`` property) or if it is different from the previous version of the same entity.

A content hash is generated from the content of each entity. This hash value is used to determine if an entity has changed over time. The content hashing is what enables :ref:`change tracking <concepts-change-tracking>`.

The :ref:`dataset source <dataset_source>` exposes the entities from the dataset so that they can be streamed through :ref:`pipes <concepts-pipes>`. As the main data structure is a log the source can read from a specific location in the log. Datasets have full :ref:`continuation support <concepts-continuation-support>`.

.. image:: images/dataset-structure.png
    :width: 800px
    :align: center
    :alt: Dataset structure

.. _concepts-config:

.. _concepts-systems:

Systems
-------

A :ref:`system <system_section>` is any database or API that could be used as a source of data for Sesam or as the target of entities coming out of Sesam. The system components provide a way to represent the actual systems being connected or integrated.

The system component has a couple of uses. Firstly it can be used to introspect the underlying system and provide back lists of possible source or sink targets. Often this information can be used on the command line or in the *Sesam Management Studio* to quickly and efficiently configure how Sesam consumes or delivers data.

The other use of the *system* is that it allows configuration that may apply to many *source* definitions, e.g. connection strings, to be located and managed in just one place. 

Systems also provide services like connection pooling and rate limiting.

You can also run your own :ref:`extension systems <concepts-extensions>`.

.. _concepts-pipes:

Pipes
-----

A :ref:`pipe <pipe_section>` is composed of a :ref:`source <concepts-sources>`, a chain of :ref:`transforms <concepts-transforms>`, a :ref:`sink <concepts-sinks>`, and a :ref:`pump <concepts-pumps>`. It is an atomic unit that makes sure that data flows from the source to the sink. It is a simple way to talk about the :ref:`flow <concepts-flows>` of data from a source system to a target system. The pipe is also the only way to specify how entities flow from dataset to dataset.

.. image:: images/pipes-structure.png
    :width: 600px
    :align: center
    :alt: Pipe structure

.. _concepts-sources:

Sources
=======

A :ref:`source <source_section>` exposes a stream of entities. Typically, this stream of entities will be the entities in a dataset, rows of data in a SQL database table, the rows in a CSV file, or JSON data from an API.

.. image:: images/pipes-source.png
    :width: 800px
    :align: center
    :alt: Source

.. NOTE::

    The most common source is the :ref:`dataset source <dataset_source>`, which reads entities from a dataset. But there are also :ref:`sources <source_section>` that can read data from external systems outside of Sesam.

Sources have varying support for :ref:`continuations <concepts-continuation-support>`. They accept an additional parameter called a *since* token. This token is used to fetch only the entities that have changed since the location stored in the token. This is used to ask for only the entities that have changed since the last time Sesam asked for them. The since token is an opaque string token that may take any form; it is interpreted by the source only. For example, for a SQL source it might be a datestamp, for a log based source it might be an offset.

Sesam provides a number of out of the box *source* types, such as :ref:`SQL <sql_source>` and :ref:`LDAP <ldap_source>`. It is also easy for developers to expose a :ref:`microservice <concepts-extensions>` that can supply data from an external service. The built-in :ref:`json <json_source>` source is able to consume data from these endpoints. These custom data providers can be written and hosted in any language.

To help with this there are a number of template projects hosted on ` Sesam community on GitHub <https://github.com/sesam-community>`_ to help you get started.

.. _concepts-transforms:

Transforms
==========

Entities streaming through a pipe can be :ref:`transformed <transform_section>` on their way from the source to the sink. 

A transform chain takes a stream of entities, transforms them, and creates a new stream of entities. There are several different transform types supported; the primary one being the :ref:`DTL transform <dtl_transform>`, which uses the :doc:`Data Transformation Language <DTLReferenceGuide>` (DTL) to join and transform data into new shapes.

.. _concepts-dtl:

DTL has a simple syntax and model where the user declares how to construct a new data entity. It has commands such as 'add', 'copy', and 'merge'. These may operate on properties, lists of values or complete entities.

.. image:: images/pipes-transform.png
    :width: 800px
    :align: center
    :alt: Transform

In general, DTL is applied to entities in a dataset and the resulting entities are pushed into a sink that writes to a new dataset. The new dataset is then used as a source for sinks that write the data to external systems.

.. _concepts-sinks:

Sinks
=====

A :ref:`sink <sink_section>` is a component that can consume entities fed to it by a pump. The sink has the responsibility to write these entities to the target, handle transactional boundaries and potentially batching of multiple entities if supported by the target system.

Several types of sinks, such as the :ref:`SQL sink <sql_sink>`, are available. Using the :ref:`JSON push sink <json_sink>` enables entities to be pushed to custom microservices or other Sesam service instances.

.. image:: images/pipes-sink.png
    :width: 800px
    :align: center
    :alt: Sink

.. NOTE::

    The most common sink is the :ref:`dataset sink <dataset_sink>`, which writes entities to a dataset. But there are also :ref:`sinks <sink_section>` that can write data to external systems outside of Sesam.

.. _concepts-pumps:

Pumps
=====

A :ref:`scheduler <concepts-scheduling-and-signalling>` handles the mechanics of :ref:`pumping <pump_section>` data from a source to a sink. It runs periodically or on a :doc:`cron <cron-expressions>` schedule and reads entities from a source and writes them to a sink.

It's also capable of rescanning the source from scratch at configurable points in time. If errors occur during reading or writing of entities, it will keep a log of the failed entities, and in the case of writes it can retry writing an entity later.

The retry strategy is configurable in several ways and if an end state is reached for a failed entity, it can be written to a *dead letter* dataset for further processing.

.. _concepts-flows:

Flows
-----

:ref:`Pipes <concepts-pipes>` read from sources and writes to sinks. The output of one pipe can be read by many downstream pipes. In this way pipes can be chained together into a directed graph – also called a flow. In some special situations you may also have cycles in this graph. The Sesam Management Studio has features for :ref:`visualising and inspecting flows <management-studio-flows>`.

.. _concepts-environment-variables:

Environment Variables
---------------------

An :ref:`environment variable <environment_variables>` is a named value that you can reference in your configuration. Environment variables are used to parameterize your configuration so that you can easily enable/disable or change certain aspects of your configuration. If you have an environment variable called ``myvariable`` then you can reference it in configuration like this: ``"$ENV(myvariable)"``. 

.. NOTE::

    Do not use environment variables for sensitive values; use :ref:`secrets <concepts-secrets>` instead. Environment variables are global only.

.. _concepts-secrets:

Secrets
-------

:ref:`Secrets <secrets_manager>` are like environment variables except that they are write-only. Once written to the API you cannot read them back out, but you can reference them in your configuration. They should be used for sensitive values like passwords and other credentials. 

A secret can only be used in certain locations of the configuration. If you have a secret called ``mysecret`` then you can reference it in configuration like this: ``"$SECRET(mysecret)"``. 

It is recommended that secrets are local. They can also be global but it is not recommended.


.. _concepts-service-metadata:

Service Metadata
----------------

The :ref:`service metadata <service_metadata_section>` is a singleton configuration entity that is used for service-wide settings.
