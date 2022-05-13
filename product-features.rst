Features
--------

.. _concepts-scheduling-and-signalling:

Scheduling and signalling
=========================

The active part of a pipe is called a :ref:`pump <pump_section>`. A pump makes entities flow through the pipe. It can be scheduled to run at regular intervals. These intervals can be specified in seconds or using a :doc:`cron expression <cron-expressions>`. One can also optionally schedule the pipe to do full rescans.

Signalling is an optional feature that automatically signals downstream pipes when data changes upstream. The signal then schedules the pump for immediate execution. This feature allows for new data to flow downstream at a much faster pace than if the pumps just ran at scheduled intervals.

.. _concepts-continuation-support:

Continuation Support
====================

:ref:`Sources <concepts-sources>` can optionally support a since marker which lets them pick up where the previous stream of entities left off - like a "bookmark" in the entity stream. This :ref:`continuation support <continuation_support>` allows a pipe to process changes incrementally. The next time the pipe runs it will continue where the previous run finished. Combined with change tracking this reduces the amount of work that needs to be done.

.. _concepts-change-tracking:

Change Tracking
===============

Sesam is special in that it really cares when data has changed. The typical pattern is to read data from a source and push it to a sink that is writing into a dataset. The dataset is essentially a log of the entities it receives. However, if a new log entry was added every time the source was checked then log would grow very fast and be of little use. There are mechanisms at both ends to prevent this. When reading data from a source, it may be possible to just ask for the entities that have changed since the last time, if the source supports it. This uses the knowledge of the source, such as a last updated time stamp, to ensure that only entities that have been created, deleted or modified are exposed. On the side of the dataset, regardless of where the data comes from, an incoming entity is compared with the existing version of that entity and only updated if they are different. The comparison is done by comparing the hashes of the old and new entity.

.. _concepts-deletion-tracking:

Deletion Tracking
=================

The :ref:`dataset sink <dataset_sink>` is capable of detecting that entities have disappeared from the source. It can do this when the pipe does a full rescan. At the end of a pipe run the sink will write a deleted version of those entities (where the ``"_deleted"`` property is set to ``true``). This is a useful feature particularly when the source itself is not able to emit deletes. It is also useful in the cases where filters or other configuration changes causes previously emitted entities to no longer be produced by the pipe.

.. _concepts-dependency_tracking:

Dependency Tracking
===================

One of the really smart things that Sesam can do is to understand complex dependencies in DTL. This is best described with an example. Imagine a dataset of customers and a dataset of addresses. Each address has a property ``customer_id`` that is the primary key of the customer entity to which it belongs. A user creates a DTL transform that processes all customers and creates a new ``customer-with-address`` structure that includes the address as a property. To do this they can use the :ref:`hops <hops_dtl_function>` function to connect the customer and address. This DTL transform forms part of a pipe and as such when a customer entity is updated, added or deleted it will be at the head of the dataset log and gets processed the next time the pump runs. But what if the address changes? As far as the expected output the customer itself has also changed.

This is in essence a problem of cache invalidation of complex queries. With Sesam, we have solved this problem. We are empowered to solve the problem thanks to our dedicated transform language. This allows us to introspect the transform to see where the dependencies are. Once we understand the dependencies we can create data structures and events that are able to understand that a change to an address should put a corresponding customer entity at the front of the dataset log again. Once it is there it will be pulled the next time the pump is run and a new customer entity containing the updated address is exposed.

.. NOTE::

   Only pipes that use the :ref:`dataset source <dataset_source>` supports dependency tracking. The primary reason for that is a technical one; the tracked entities need to be looked up by id before a specific point in time and fed through the pipe. This is currently only implemented for the ``dataset`` source type. It is unlikely that it can be implemented for other source types as those have latency and ambiguity issues.

.. _concepts-automatic-reprocessing:

Automatic Reprocessing
======================

There are many possible reasons why a pipe may fall out of sync. Configuration may change, datasets may be deleted and then recreated, sources may be truncated, data may be restored from backup, joins to new datasets can be introduced and so on. In these cases the pipe should be reset and it should perform a full rescan to get a new view of the world. Sesam has a feature called :ref:`automatic reprocessing <automatic_reprocessing>` that will detect that the pipe has fallen out of sync and needs to be reset. This is currently an opt-in feature, but if you enable it in the pipe or in :ref:`service metadata <concepts-service-metadata>` the pipe will automatically reset itself and perform a full rescan – making sure that it is no longer out of sync. In some situations it may need to rewind just a little, instead of doing a full rescan - in any case you can then be sure that it is no longer out of sync.

.. _concepts-namespaces:

Namespaces
==========

:ref:`Namespaces <best-practice-namespace>` are inspired by The Resource Description Framework `(RDF) <https://www.w3.org/RDF/>`_. You'll see them in terms of namespaced identifiers - also called NIs. A NI is a special datatype defined in the :doc:`entity data model <entitymodel>`. In essence they are a string consisting of two parts, the namespace and the identifier. ``"~:global-person:john-doe"`` is an example. The ``~:`` is the type part that tells you that it is a namespaced identifier. ``global-person`` in this case is the namespace and ``john-doe`` is the identifier.

Properties can also have namespaces, but here the ``~:`` part is not used. ``global-person:fullname`` is an example of such a namespaced property. Namespaced properties are essential when :ref:`merging <concepts-merging>` to avoid naming collisions and to maintain provenance of the properties.

A namespaced identifier is a unique reference to an abstract thing. It is an identifer. In Sesam it is not a globally unique identifier, but it is a unique identifier inside one Sesam datahub. There are mechanisms in place for collapsing and expanding namespaced identifiers to globally unique identifiers on import and export.

Namespaced identifiers and properties with namespaces will automatically expand to fully qualified Uniform Resource Identifiers (URIs) when exporting to RDF. URIs in RDF are similarly collapsed into namespaced identifiers and properties with namespaces on import. They can also be expanded and collapsed using DTL.

Sesam can `utilize RDF <https://docs.sesam.io/rdf-support.html?highlight=rdf#>`_ for input, transformation or producing data for external consumption.

.. _concepts-global-datasets:

Global datasets
===============

The use of global datasets is described in depth in the :ref:`Best Practice <best-practice-global>` document. The principle is to have one go-to dataset to find data about a specific type of data. A global dataset typically co-locates and :ref:`merges <concepts-merging>` data from many different sources.

.. _concepts-merging:

Merging
=======

An essential feature that enables :ref:`global datasets <concepts-global-datasets>` is the ability to merge different entities into one entity representing the same thing. Organizations often have multiple systems that share overlapping information about employees, customers, products etc. The :ref:`merge source <merge_source>` lets you define equivalence rules that enables you to merge entities. The merge source is able to merge incrementally producing a stream of entities that have been merged – or unmerged (when an equivalence rule no longer applies).

.. _concepts-transit-encoding:

Transit encoding
================

Sesam's entity data model is a `JSON <https://www.json.org/json-en.html>`_ compatible data model. JSON itself supports a limited number of data types, so in order to make the model richer, the entity data model supports a subset of the `Transit <https://github.com/cognitect/transit-format>`_ data types. Transit encoding is a technique for encoding a larger set of data types in JSON. See the :doc:`entity data model <entitymodel>` for more information about this encoding.

.. _schema-inferencing:

Schema inferencing
==================

Data in Sesam is dynamically typed. Properties can be added or removed and their types changed over time. Schema validation can be enforced, but it is optional. This dynamism makes the system agile. Automatic schema inferencing is enabled by default. Sesam tracks the changes to entities and will automatically generate a schema for the source entities and sink entities of pipes. In practice this means that you can see the structure of the data that went into the pipe and the data that came out of the pipe. This feature is the foundation that :ref:`property lineage <property-lineage>` builds on.

.. _schema-models:

Schema models
=============

A model is a set of entity types. An entity type is a JSON schema, so in practice a model is an array of JSON schemas.

The purpose of a model is to serve as mechanism for grouping entity types, but also allow the user to add descriptions of properties to the JSON schema. Those descriptions are then aggregated up on the property landing page in the Management Studio.
Schema inferencing generates entity types for the pipe source and pipe sink. The sink entity types are automatically mapped to implicit models. You can find these in ``Browse`` > ``Models`` in the Management Studio. You can also filter entity types by model in ``Browse`` > ``Entity types``.

There are three built-in implicit models:

- ``Global`` contains the sink entity types of global pipes
- ``Input`` contains the sink entity types of inbound pipes
- ``Output`` contains the sink entity types of outbound pipes

An implicit model will also be generated for each unique pipe id prefix (the pipe id up until the first "``-``" character), e.g. the ``hubspot-contact`` and ``hubspot-company`` pipes both end up in the ``hubspot`` model.

You can customize what implicit models a pipe is put into by setting the pipe property ``metadata.models`` to an array of model ids, e.g. ``["foo", "bar"]``.

Explicit models can be uploaded through the :ref:`/api/models <api-reference>` APIs.


.. _concepts-configgroup:

Config groups
=============

See :ref:`the config groups API <api-config-groups>` for more information.

.. _concepts-compaction:

Compaction
==========

A dataset is an append-only immutable log of data that would, left unchecked, grow forever. This problem is partly mitigated as entities are only written to the log if they are new or different (based on a content hash comparison) from the most recent version of that entity. To supplement this and ensure that a dataset does not consume all available disk space a retention policy can be defined. A retention policy describes the general way in which the log should be compacted. The default policy is to keep two versions of every entity. This is the minimal number of versions to keep in order to make dependency tracking work. A time-based policy is also available allowing you to say how old and entity can be before it becomes a candidate for :ref:`compaction <pipe_compaction>`.

.. _concepts-completeness:

Completeness
============

:ref:`Completeness <completeness>` is a feature that you typically enable on outgoing pipes. It makes sure that all pipes that this pipe is dependent on have run before it processes the source entities of this pipe. The timestamp of the source entity is compared with the completeness timestamp that was inherited from its upstream and dependent pipes. This feature effectively holds back the processing of source entities until it can be sure that dependent pipes have completed. This is useful when you want to have a final entity version before you send it to the target system. It also reduces the number of times you have to send the entity to the target system as there might be several state transitions until the entity can be considered complete.

.. _concepts-circuit-breakers:

Circuit Breakers
================

A :ref:`circuit breaker <circuit_breakers_section>` is a safety mechanism that one can enable on the :ref:`dataset sink <dataset_sink>`. The circuit breaker will trip if a larger than expected number of entities are written to a dataset in a pipe run. When tripped, the pipe will refuse to run and it has to be untripped manually. This safety mechanism is there to prevent unforeseen tsunamis of changes and to prevent them from propagating downstream.

.. _concepts-durable-data:

Durable Data
============

For cloud subscriptions, data is backed up to an external service once every 24 hours. During a disaster recovery data written the last 24 hours can be lost. This might not a huge problem when Sesam is pulling data from sources, as the data that was lost can be pulled again. For pipes with http_endpoint sources and non-idempotent sinks, this will most likely be a problem. In our cloud subscriptions you now have the possibility to request that a pipes data is stored in three replicas. This reduces the likelihood of data loss. Note that this incurs a 3x increase in data size for the pipes that has this feature enabled.

This feature can be enabled on a pipe by setting the pipe's :ref:`metadata.durable <pipe_metadata_durable>` property to ``true``.

.. _concepts-notifications:

Notifications
=============

Monitoring of pipes can be enabled. Once a pipe is being monitored, you can add :doc:`notification rules <notifications>` to pipes and be alerted when those rules are triggered. You can get notification alerts in the user-interface or by email.

.. _concepts-metrics-api:

Metrics API
===========

If Monitoring and Metrics is enabled, you can access subscription and pipe metrics in the :ref:`Prometheus-compatible metrics API <api-metrics>` endpoint from your external monitoring tools.

.. _concepts-extensions:

Extensions
==========

Sesam provides a finite number of :ref:`systems <concepts-systems>`, but you can build and run your own microservice extension systems. The :ref:`microservice system <microservice_system>` allows you to use custom Docker images to host them inside the Sesam service.


.. _concepts-integrated-search:

Integrated Search
=================

Integrated Search is now available for all subscriptions with clustered architecture. This is how you can activate the new feature:

- Login to portal.sesam.io

- Select the subscription you want to use

- Navigate to Subscription on the left menu

- Click on Products tab

- Click on “Enable Integrated Search”

If your subscription is not yet on a clustered architecture please take contact with support to start the migration.

Integrated data browsing gives you more insight into your data and relationships within. Once enabled, globals are
indexed and available for free text search and navigation. Note that this incurs a 2x increase in data size needed for
global pipes.

.. _concepts-bring-your-own-key:

Bring Your Own Key
==================

In a hosted Sesam subscription data is stored on disks and backups are written to a remote geo-replicated storage account. By default these disks and the associated storage account are encrypted by a platform managed key. In practice this means that it is the cloud provider that manages the encryption keys. Sesam has also implemented support for bring your own key (BYOK). In practice Sesam then manages the encryption key for you. The advantage is that you can then decide to revoke the key when you need to. Note that this generally requires that the data then must be able to be reloaded by Sesam afterwards. This is an opt-in feature that can be enabled on new single subscriptions. It is not yet supported for multi subscriptions. Contact `support <https://support.sesam.io/>`_ if you would like to enable BYOK for a new subscription.


Network Policy
==============

One has the option of blocking all public access through it or denying all except for a whitelist of ip addresses and ranges. In the new architecture it is possible to push the IP white listing down to the reverse proxy and also allow public access and restricted access to pipes through custom rules on the pipes. There are no restrictions on outgoing traffic currently.

.. _concepts-vpn:

VPN
===

You can extend Sesam into your own network using a IPSec-based Virtual Private Network. You can configure VPN under
Subscriptions Settings in the Management Studio. Note that there is a additional surcharge for VPN, see
:doc:`pricing` for more information.

To enable the VPN feature on your subscription:

- Login to portal.sesam.io

- Navigate to Subscription on the left menu

- Click on Products tab

- Tick the checkbox "Enable VPN"


Navigate to Subscription on the left menu and select the new VPN tab. This is where the rest of the configuration will be done.

Take note of the Sesam Peer VPN Gateway and Sesam address spaces and configure your on-premises VPN device accordingly.
You can find a list of supported VPN devices and configuration guides at `https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-devices <https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-devices>`_.

Finally under "Add or modify VPN details" fill in the required fields to setup the actual connection between sesam and your on-premises:

 - Gateway Address:  on-premises VPN device IP address or FQDN.

 - Address Spaces: Sesam will route the address range that you specify to the on-premises VPN device IP address.

 - PSK: a string of characters that is used as an authentication key between sesam and on-premises VPN device.

Status Page
===========

Sesam hosts a status page at `https://status.sesam.io/ <https://status.sesam.io/>`_. There you will find the real-time operational status of the Sesam services. Any incidents will be reported there, but you can also register and get emails when there are changes in the operational status. A notification badge will also be shown in the :doc:`Sesam Management Studio <management-studio>` when incidents occur. If you have other custom requirements there is also a provisional `Status API <https://status.sesam.io/api>`_ that you can use.

.. _concepts-software-channels:

Software channels
=================

Sesam software is released through a phased rollout scheme. There are four different release channels – commonly called canaries. This is done to give changes and new features some time in non-production environments before they are rolled out to production. The goal is to reduce risk.

The available channels are:

- ``weekly-prod`` is release bi-weekly and is the most stable release. *Use this in production!*
- ``weekly`` is release once a week. Use this in staging environments.
- ``nightly`` is released every night. Use this in development environments.
- ``latest`` is released every time a pull request is merged. Use this only for developent environments, and only when you know what you're doing.

.. Note::
  We can for any reason choose to not promote new versions of any software channel, build dates will correspond to a minimum, not a maximum age.

Weekly and nightly upgrades are performed between 00-03 CET. Weekly upgrades are performed night to Monday.
Security hotfixes will not wait for the scheduled window. Downgrades are not supported.
