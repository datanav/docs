.. _concepts-pipes:

Pipes
=====

A :ref:`pipe <pipe_section>` is composed of a :ref:`source <concepts-sources>`, a chain of :ref:`transforms <concepts-transforms>`, a :ref:`sink <concepts-sinks>`, and a :ref:`pump <concepts-pumps>`. It is an atomic unit that makes sure that data flows from the source to the sink. It is a simple way to talk about the :ref:`flow <concepts-flows>` of data from a source system to a target system. The pipe is also the only way to specify how entities flow from dataset to dataset.

.. image:: images/pipes-structure.png
    :width: 600px
    :align: center
    :alt: Pipe structure

.. _concepts-sources:

Sources
-------

A :ref:`source <source_section>` exposes a stream of entities. Typically, this stream of entities will be the entities in a dataset, rows of data in a SQL database table, the rows in a CSV file, or JSON data from an API.

.. image:: images/pipes-source.png
    :width: 800px
    :align: center
    :alt: Source

.. NOTE::

    The most common source is the :ref:`dataset source <dataset_source>`, which reads entities from a dataset. But there are also :ref:`sources <source_section>` that can read data from external systems outside of Sesam.

Sources have varying support for :ref:`continuations <continuation-support>`. They accept an additional parameter called a *since* token. This token is used to fetch only the entities that have changed since the location stored in the token. This is used to ask for only the entities that have changed since the last time Sesam asked for them. The since token is an opaque string token that may take any form; it is interpreted by the source only. For example, for a SQL source it might be a datestamp, for a log based source it might be an offset.

Sesam provides a number of out of the box *source* types, such as :ref:`SQL <sql_source>` and :ref:`LDAP <ldap_source>`. It is also easy for developers to expose a :ref:`microservice <extensions-feature>` that can supply data from an external service. The built-in :ref:`json <json_source>` source is able to consume data from these endpoints. These custom data providers can be written and hosted in any language.

To help with this there are a number of template projects hosted on ` Sesam community on GitHub <https://github.com/sesam-community>`_ to help you get started.

.. _concepts-transforms:

Transforms
----------

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
-----

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
-----

A :ref:`scheduler <scheduling-and-signalling>` handles the mechanics of :ref:`pumping <pump_section>` data from a source to a sink. It runs periodically or on a :doc:`cron <cron-expressions>` schedule and reads entities from a source and writes them to a sink.

It's also capable of rescanning the source from scratch at configurable points in time. If errors occur during reading or writing of entities, it will keep a log of the failed entities, and in the case of writes it can retry writing an entity later.

The retry strategy is configurable in several ways and if an end state is reached for a failed entity, it can be written to a *dead letter* dataset for further processing.
