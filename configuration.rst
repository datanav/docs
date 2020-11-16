.. _configuration:

===========================
Service Configuration Guide
===========================

.. contents:: Table of Contents
   :depth: 2
   :local:

General
=======

The *Sesam* service is configured using one or more `JSON <https://en.wikipedia.org/wiki/JSON>`_ files.
These configuration files can be imported through the service API. They can also be created and edited using the :doc:`Sesam Management Studio <management-studio>`.

Conceptually, the configuration files contains definitions for *Systems* and *Pipes*.

The configuration is a *JSON array* of :ref:`system <system_section>` and :ref:`pipe configurations <pipe_section>`. The configuration :doc:`entities <entitymodel>` are
*JSON objects* of the form:

::

    [
        {
            "_id": "some-solution-wide-unique-id",
            "name": "Name of component",
            "type": "component-type",
            "some-property": "some value"
        },
        {
            "_id": "some-other-solution-wide-unique-id",
            "name": "Name of other component",
            "type": "component-type",
            "some-other-property": "some other value"
        }
    ]

It should be noted that all ``_id`` property values must be unique across across the solution. This means unique within the *sesam.conf.json* file but also across all files when a multiple file configuration is used.


.. _environment_variables:

Environment variables
=====================

You can insert the values of environment variables into configuration using the syntax "$ENV(variable)" in place of
property values. You can manage these environment variables using a HTTP client with the :ref:`Environment Manager API <api-reference>`.

An example, given a uploaded environment variable JSON file containing:

::

    {
       "server-ip": "10.10.10.1"
    }


You can refer to this property in your configuration by reference:

::

    {
       "_id": "my-system",
       "type": "oracle",
       "host": "$ENV(server-ip)"
       ..
    }

You can also compose a property that consists of several environment variables:

::

   {
     "_id": "my-system",
     "type": "url",
     "base_url": "http://$ENV(my-domain):$ENV(my-port)",
     "..": ".."
   }

Note that when using properties that contain multiple environment variables you cannot nest them inside each other,
and the resulting property will always be a string.

You can combine environment variables and *secrets*, but they cannot be nested within each other. For secret variables
see the :ref:`Secrets manager API <secrets_manager>` for details on how to upload them and their syntax.

Environment variables applies to both System and Pipe configuration entities.

.. _service_metadata_section:

Service metadata
================

There is an optional special configuration entity used to represent
the service instance's metadata. The metadata is used to
specify properties that apply to the service instance itself. This
entity can either be added as a normal configuration entity, edited in
the UI or updated with the Service API.

Example:

::

   {
      "_id": "node",
      "type": "metadata",
      "namespaced_identifiers": true,
      "namespaces": {
         "default": {
           "example": "http://example.org/",
           "fifa": "http://www.fifa.com/"
         }
      },
      "global_defaults": {
         "use_signalling_internally": false,
         "default_compaction_type": "sink",
      },
      "dependency_tracking": {
         "dependency_warning_threshold": 10000,
         "dependency_error_threshold": 50000,
         "dependency_warning_threshold_total_bytes": 33554432,
         "dependency_error_threshold_total_bytes": 134217728,
         "enable_hops_thresholds": true
      }
   }

Properties
----------

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``namespaced_identifiers``
     - Boolean
     - Flag used to enable namespaced identifers support for the service as a whole. Pipes inherit the value of the ``namespaced_identifiers`` property less explictly overridden.
     - ``false``
     -

   * - ``namespaces.default``
     - Dict
     - A dictionary of namespace to URI expansions. This expansion
       mapping is used to expand namespaced identifiers into fully
       qualified URIs, e.g. by those components that provide RDF
       support.

       A few expansion mappings come built-into the system. These
       are always available unless explicity overridden:

       ::

          "_": "http://example.org/",
          "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
          "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
          "owl": "http://www.w3.org/2002/07/owl#",
          "foaf": "http://xmlns.com/foaf/0.1/",
          "wgs84": "http://www.w3.org/2003/01/geo/wgs84_pos#",
          "xsd": "http://www.w3.org/2001/XMLSchema#",
          "dc": "http://purl.org/dc/elements/1.1/",
          "skos": "http://www.w3.org/2004/02/skos/core#",
          "dcterms": "http://purl.org/dc/terms/",
          "gs": "http://www.opengis.net/ont/geosparql#",
     -
     -

   * - ``global_defaults.use_signalling_internally``
     - Boolean
     - Flag used to globally enable signalling support between internal pipes (i.e. dataset to dataset pipes). If enabled, a pipe
       run is scheduled as soon as the input dataset changes (it does not interrupt any already running pipes).
       Setting this option to ``true`` will enable signalling for all :ref:`dataset-type sources <dataset_source>` in the
       installation. You can turn on this feature individually by setting the ``supports_signalling`` flag on the
       :ref:`dataset source <dataset_source>` (including variants like
       :ref:`merge <merge_source>`, :ref:`union datasets <union_datasets_source>` and
       :ref:`merge datasets <merge_datasets_source>` sources). Note that signalling support is "best-effort" only; signals are not persisted so
       delivery is not guaranteed. For this reason, pipes in such flows should always have scheduled interval as a "backup".
       Also note that if the scheduled interval on a pipe is less than 2 minutes or if the scheduling is cron based, signalling will
       be disabled for the pipe source (if it's only set globally). However, if you set ``supports_signalling`` explicitly
       on the pipe source it will be turned on regardless of the pump schedule.
     - ``false``
     -

   * - ``global_defaults.default_compaction_type``
     - Enum<String>
     - Specifies the default compaction type. It can be set to ``"background"`` or ``"sink"``. Background compaction will run once every 24 hours. Sink compaction will run every time the pipe runs.
     - ``"sink"``
     -

   * - ``global_defaults.max_entity_bytes_size``
     - Enum<String>
     - Defines the maximum size in bytes of an individual entity as it is stored in a dataset.
     - ``104857600`` (100MB)
     -

       .. _service_metadata_dependency_tracking_dependency_warning_threshold:

   * - ``dependency_tracking.dependency_warning_threshold``
     - Integer
     - The number of entities that dependency tracking can keep in memory at a given time. If this number is exceeded then a warning message is written to the log.
     - ``10000``
     -

       .. _service_metadata_dependency_tracking_dependency_error_threshold:

   * - ``dependency_tracking.dependency_error_threshold``
     - Integer
     - The number of entities that dependency tracking can keep in memory at a given time. If this number is exceeded then the pump will fail. Do not set this value too high as it may cause excessive memory usage.
     - ``50000``
     -

       .. _service_metadata_dependency_tracking_dependency_warning_threshold_total_bytes:

   * - ``dependency_tracking.dependency_warning_threshold_total_bytes``
     - Integer
     - The number of bytes that dependency tracking can keep in memory at a given time. If this number is exceeded then a warning message is written to the log.
     - ``33554432`` (32MB)
     -

       .. _service_metadata_dependency_tracking_dependency_error_threshold_total_bytes:

   * - ``dependency_tracking.dependency_error_threshold_total_bytes``
     - Integer
     - The number of bytes that dependency tracking can keep in memory at a given time. If this number is exceeded then the pump will fail.  Do not set this value too high as it may cause excessive memory usage.
     - ``134217728`` (128MB)
     -

       .. _service_metadata_dependency_tracking_enable_hops_thresholds:

   * - ``dependency_tracking.enable_hops_thresholds``
     - Boolean
     - If ``true``, then warning and error thresholds that apply for dependency tracking also apply for regular ``"hops"`` expressions. It is recommended that you set this property to ``true`` in development environments.
     - ``false``
     -

.. _pipe_section:

Pipes
=====

A pipe defines the flow of data from a *source* to a *sink* on some schedule as defined by the pump settings.
Optionally, a pipe may define an ordered list of transforms that are applied to entities as they flow from the
*source* to the *sink*. As the name implies, a pump "pumps" data in the form of entities from the source to the
sink at regular or scheduled intervals. A chain of transforms can be placed in between the source and the sink, so that entities
are transformed on their way to the sink.

The pipe configuration consists of a :ref:`source <source_section>`, :ref:`transform <transform_section>`,
:ref:`sink <sink_section>` and a :ref:`pump <pump_section>`.

Note that the forward slash character ("``/``") is not allowed in the pipe ``_id`` property.

Prototype
---------
The following *json* snippet shows the general form of a pipe definition.

::

    {
        "_id": "pipe-id",
        "name": "Name of pipe",
        "description": "This is a description of the pipe",
        "comment": "This is a comment",
        "type": "pipe",
        "source": {
        },
        "transform": {
        },
        "sink": {
        },
        "pump": {
        }
    }

Note that if no ``name`` property is explicitly set for the source, sink or pump configurations one will be generated based on the ``name`` of the pipe (i.e. the contents of this property postfixed with "source", "sink" or "pump" respectively).

.. _pipe_batching:

Batching
--------

Pipes support batching if the sink supports batching. It does this by
accumulating source entities in a buffer before writing the batch to
transforms and the sink. The size of each batch can be specified using
the ``batch_size`` property on the pipe. The default batch size
is 100.

Note that the sink may have its own ``batch_size`` property. This is
useful if the pipe has transforms that produce more entities than the
number of entities taken as input.

Properties
----------

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``_id``
     - String
     - The id of the pipe, this should be unique within a Sesam service instance. Note that you cannot use the ``/``
       character in the id property.
     -
     - Yes

   * - ``name``
     - String
     - A human readable name of the component.
     -
     -

   * - ``description``
     - String or list of strings
     - A human readable description of the component (optional).
     -
     - Yes

   * - ``comment``
     - String or list of strings
     - A human readable comment on the component (optional).
     -
     -

   * - ``type``
     - String
     - The type of the component, for pipes the only allowed value is "pipe"
     -
     - Yes

   * - ``batch_size``
     - Integer(>=1)
     - The number of source entities to consume before writing to the sink. The batch size
       can be used to buffer up entities so that they can be written together to the sink in
       one go. The sink must support batch for the bulking to happen. This may increase the
       throughput of the pipe, at the cost of extra memory usage. If the batch fails,
       then entities will be retried individually.
     - 100
     -

   * - ``checkpoint_interval``
     - Integer(>=1)
     - Specifies how often the pipe offset is saved. It says how many batches
       must be processed before the pipe offset is saved the next time. Note that the pipe
       offset is always saved at the end of the sync if it changed.

       The default value is 10000/``batch_size`` = 100, i.e. the
       checkpoint happens every 100 batches.
     - 100
     -

   * - ``disable_set_last_seen``
     - Boolean
     - If this flag is set to ``true``, it will no longer be possible to reset or set the 'last seen' parameter for this
       pipe. The primary use case for this property is when you need to protect the pipe from accidental resets.
     - ``false``
     -

   * - ``source``
     - Object
     - A configuration object for the :ref:`source <source_section>` component of the pipe.
     -
     - Yes

   * - ``transform``
     - Object/List
     - Zero or more configuration objects for the :ref:`transform <transform_section>` components of the pipe.
       The default is to do no transformation of the entities. If a list of more than one transform components is
       given, then they are chained together in the order given. This means that the output of the first transform
       is passed as the input of the second, and so on. The output of the last transform is then passed to the
       sink. The first transform gets its input from the source.
     -
     -

   * - ``sink``
     - Object
     - A configuration object for the :ref:`sink <sink_section>` component of the pipe. If omitted, it defaults to
       a :ref:`dataset sink <dataset_sink>` with its ``dataset`` property set to same as the pipe's ``_id`` property.
     -
     -

   * - ``pump``
     - Object
     - A configuration object for the :ref:`pump <pump_section>` component of the pipe.
     -
     -

   * - ``dependency_tracking.dependency_warning_threshold``
     - Integer
     - The number of entities that dependency tracking can keep in memory at a given time. If this number is exceeded then a warning message is written to the log. The default value is inherited from the :ref:`service metadata <service_metadata_dependency_tracking_dependency_warning_threshold>`.
     - ``10000``
     -

   * - ``dependency_tracking.dependency_error_threshold``
     - Integer
     - The number of entities that dependency tracking can keep in memory at a given time. If this number is exceeded then the pump will fail. The default value is inherited from the :ref:`service metadata <service_metadata_dependency_tracking_dependency_error_threshold>`.  Do not set this value too high as it may cause excessive memory usage.
     - ``50000``
     -

   * - ``dependency_tracking.dependency_warning_threshold_total_bytes``
     - Integer
     - The number of bytes that dependency tracking can keep in memory at a given time. If this number is exceeded then a warning message is written to the log. The default value is inherited from the :ref:`service metadata <service_metadata_dependency_tracking_dependency_warning_threshold_total_bytes>`.
     - ``33554432`` (32MB)
     -

   * - ``dependency_tracking.dependency_error_threshold_total_bytes``
     - Integer
     - The number of bytes that dependency tracking can keep in memory at a given time. If this number is exceeded then the pump will fail. The default value is inherited from the :ref:`service metadata <service_metadata_dependency_tracking_dependency_error_threshold_total_bytes>`.  Do not set this value too high as it may cause excessive memory usage.
     - ``134217728`` (128MB)
     -

   * - ``dependency_tracking.enable_hops_thresholds``
     - Boolean
     - If ``true``, then warning and error thresholds that apply for dependency tracking also apply for regular ``"hops"`` expressions. The default value is inherited from the :ref:`service metadata <service_metadata_dependency_tracking_enable_hops_thresholds>`. It is recommended that you set this property to ``true`` in development environments.
     - ``false``
     -

.. _namespaces:

Namespaces
----------

Namespaces can be used by :ref:`entity identifiers <id_field>`, entity property names and the :ref:`namespaced identifier datatype <ni_data_type>`. A namespaced identifier consists of two parts; a namespace and an identifier. The namespace part can consist of any character, including colons. The identifier part can consist of any character except colons (``:``).

Example of an entity with namespaces:

::

  {
    "_id": "user:123",
    "user:username": "erica",
    "user:first_name": "Erica",
    "user:manager": "~:user:101"
  }

.. NOTE::

   Namespaced identifiers can be enabled by setting the
   ``namespaced_identifiers`` property to ``true`` in the pipe
   configuration (see below) or the service metadata. The former
   enables it for just the one pipe. The latter enables it for all
   pipes - except for those pipes that have explicitly disabled it.

.. NOTE::

   Some of the DTL functions are namespace aware and they will behave
   slightly differently when namespaces are enabled. See the section
   on :ref:`namespaces <namespace_aware_functions>` in the DTL
   reference guide for more details.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``namespaced_identifiers``
     - Boolean
     - Flag used to enable namespaced identifers support on the pipe. The default value is read from the service metadata. If not specified in the service metadata then the default value is ``false``.
     - Service metadata default
     -

   * - ``namespaces.identity``
     - String
     - The namespace used for identifiers. The default value is the pipe's id.
     - ``pipe.id``
     -

   * - ``namespaces.property``
     - String
     - The namespace used for properties. The default value is the pipe's id.
     - ``pipe.id``
     -

   * - ``add_namespaces``
     - Boolean
     - If ``true`` then the current identity namespace will be added to ``_id`` and the current property namespace will be added to all properties. The namespaces are added before the first transform. This property is normally only specified on inbound pipes.

       If ``namespaced_identifiers`` is enabled in the service metadata then the source default value is used. The following sources has a default value of ``true``: :ref:`csv <csv_source>`, :ref:`ldap <ldap_source>`, :ref:`sql <sql_source>`, :ref:`embedded <embedded_source>`, :ref:`http_endpoint <http_endpoint_source>`, and :ref:`json <json_source>`.
     - Source default
     -

   * - ``remove_namespaces``
     - Boolean
     - If ``true`` then namespaces will be removed from ``_id``, properties and namespaced identifier values. The namespaces are removed after the last transform. This property is normally only specified on outbound pipes.

       If ``namespaced_identifiers`` is enabled in the service metadata then the sink default value is used. The following sinks has a default value of ``true``:  :ref:`csv_endpoint <csv_endpoint_sink>`, :ref:`elasticsearch <elasticsearch_sink>`, :ref:`mail <mail_message_sink>`, :ref:`rest <rest_sink>`, :ref:`sms <sms_message_sink>`, :ref:`solr <solr_sink>`, :ref:`sql <sql_sink>`, :ref:`http_endpoint <http_endpoint_sink>`, and :ref:`json <json_push_sink>`.
     - Sink default
     -

.. _pipe_compaction:

Compaction
----------

Compaction deletes the oldest entities in a dataset and reclaims space for those
entities in the dataset's indexes.

Datasets that are written to by pipes using the :ref:`dataset sink <dataset_sink>` are compacted incrementally as
the pipe writes new entities to the dataset by default (compaction type "sink" enabled). If sink compaction is disabled,
the dataset is automatically compacted once every 24 hours (compaction type "background" in the global settings or
compaction.sink set to ``false``). The default is to keep the last two versions of every
entity up until the current time.

.. NOTE::

   Compaction will only be performed up to the lowest offset for which there exists a pipe doing dependency tracking on the dataset. Each pipe doing dependency tracking keeps a tracking offset on the dataset so that it knows which entities to perform dependency tracking for. It is this tracking offset that compaction cannot go beyond. This is done so that those pipes should not fall out of sync. If the compaction did not hold off then we could not guarantee that the output of those pipes are correct.

   Be aware that disabled pipes also hold off compaction. If the pipes are to be disabled for a long time then it is better to remove the pipe, or alternatively comment out the hops.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``compaction.automatic``
     - Boolean
     - If ``true`` then the dataset is a candidate for automatic compaction.
     - ``true``
     - No

   * - ``compaction.sink``
     - Boolean
     - If ``true`` then the dataset sink will perform dataset compaction. This will make compaction happen incrementally as new entities are written to the dataset. If this is enabled, then automatic compaction won't run for the dataset itself, but dataset index compaction will be scheduled. Note that dataset index compaction does not require a lock on the dataset.
     - ``true``
     - No

   * - ``compaction.keep_versions``
     - Integer
     - The number of unique versions of an entity to keep around. The default is ``2``.
       The value must be greater than or equal to ``0``. If set to ``0`` then a time
       threshold must be set explicitly.

       .. WARNING::

          A value less than ``2`` means that dependency tracking is best effort only,
          and it will not be able to find all reprocessable entities. Do full or partial
          rescans as a counter measure.

     - ``2``
     - No

   * - ``compaction.time_threshold_hours``
     - Integer
     - Specifies the threshold for how old entities must be before they are considered
       for compaction. This property is usually used when you want to keep entities
       around for a certain time.
     - ``null``
     - No

   * - ``compaction.time_threshold_hours_pump``
     - Integer
     - Same as ``compaction.time_threshold_hours``, but applies to the pipe's pump
       execution dataset. Pump execution datasets are always trimmed by time.  The
       default is 30 days, which is the minimum value allowed.
     - ``720``
     - No

   * - ``compaction.growth_threshold``
     - Float
     - The growth factor required for the automatically scheduled compaction to kick
       in. The default value is that there must have been 10% new offsets written to
       the dataset since the last compaction. ``1.0`` is the minimum value allowed.
     - ``1.10``
     - No

.. _circuit_breakers_section:

Circuit breakers
----------------

A circuit breaker is a safety mechanism that one can enable on the
:ref:`dataset sink <dataset_sink>`. The circuit breaker will trip if
the number of entities written to a dataset in a pipe run exceeds a
certain configurable limit.

A tripped circuit breaker will prevent the pipe from running.
It can either be rolled back or committed. Rolling it back
will delete any entities that were written in the pipe run before the
circuit breaker was tripped. Committing it will expose the uncommitted
entities. Both operations resets the circuit breaker so that pipe can
run again.

Compaction will not be performed datasets with a tripped circuit
breaker. It is also not possible to repost entities to these datasets.

The `service API <api.html#post--datasets-dataset_id>`_ can be used to
reset the circuit breaker.

Resetting
---------

When the configuration of a pipe is modified in such a way that the entities the pipe
produces changes (for instance by changing the DTL transform of the pipe), the pipe's "last-seen"
value must be cleared in order to reprocess already seen entities with the new pipe
configuration.

This can be done by setting the "last-seen" value to an empty string with the
`update-last-seen <./api.html#api-reference-pump-update-last-seen>`__ operation in the Service API.

.. _automatic_reprocessing:

Automatic reprocessing
----------------------

Datasets that are input to a pipe or datasets that are hop-ed to by a pipe may be deleted. When this happens the data output by a pipe is no longer in sync with the input data. By default a pipe will not reset automatically if this happens, but it will maintain a list of datasets that are out of sync. Alternatively one can set the reprocessing policy to ``automatic`` so that such resets happen automatically.


Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``reprocessing_policy``
     - Enum<String>
     - Specifies the policy that the pipe uses to decide if a pipe needs to be reset or not.

       - ``continue`` (the default) means that the pipe will continue processing input entities, and not reset the pipe, even though there might be factors indicating the the pipe should be reset.

       - ``automatic`` means that the pipe will automatically reset the pipe when it finds that there are factors that indicate that the pipe should be reset. The rationale for resetting the pipe is so that input entities can the reprocessed so that the output is correct.
     - ``continue``
     - No


.. _completeness:

Completeness
------------

When a pipe completes a successful run the sink dataset will inherit the smallest completeness timestamp value of the source datasets and the related datasets. Inbound pipes will use the current time as the completeness timestamp value. This mechanism has been introduced so that a pipe can hold off processing source entities that are more recent than the source dataset's completeness timestamp value. The propagation of these timestamp values is done automatically. Individual datasets can be excluded from completeness timestamp calculation via the ``exclude_completeness`` property on the pipe. One can enable the completeness filtering feature on a pipe by setting the ``completeness`` property on the :ref:`dataset source <dataset_source>` to ``true``.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``exclude_completeness``
     - List<String>
     - A list of dataset ids that should not contribute to the completeness timestamp value. Any
       dataset listed in this property will be ignored when calculating the dataset sink
       completeness timestamp value.
     - ``[]``
     -


Example configuration
---------------------

The following example shows a pipe definition that exposes data from a SQL database table called ``customers``, and feeds it into a sink that writes the data into a dataset called ``Northwind:Customers``.

::

   {
       "_id": "northwind-customers",
       "name": "Northwind customers",
       "type": "pipe",
       "source": {
           "type": "sql",
           "system": "Northwind",
           "table": "Customers"
       },
       "sink": {
           "type": "dataset",
           "dataset": "Northwind:Customers"
       },
       "pump": {
           "schedule_interval": 3600
       },
       "compaction": {
           "keep_versions": 2,
           "time_threshold_hours": 48
       }
   }

.. _source_section:

Sources
=======

Sources provide *streams* of :doc:`entities <entitymodel>` as input to
the :ref:`pipes <pipe_section>` which is the building blocks for the
data flows in Sesam. These entities can take *any* shape (i.e. they
can also be nested), and have a single required property:
**_id**. This ``_id`` field must be *unique within a flow* for a
specific logical entity. There may exist multiple *versions* of this
entity within a flow, however.

Prototype
---------

The following *json* snippet shows the general form of a source definition.

::

    {
        "type": "a-source-type",
        "comment": "This is a comment",
        ..
    }

The only universally required property is ``type``.

Properties
----------

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``type``
     - String
     - The type of the source, the allowed types are described below
     -
     - Yes

   * - ``comment``
     - String or list of strings
     - A human readable comment on the source (optional).
     -
     -


.. _continuation_support:

Continuation support
--------------------

Sources can optionally support a ``since`` marker which lets them pick
up where the previous stream of entities left off - like a "bookmark"
in the entity stream. The ``since`` marker is opaque to the rest of
the Sesam components and it is assumed to be interpretable *only by
the source*. Within an entity the marker is carried in the
``_updated`` property if supported by its source.

Sesam supports a diverse set of core data sources. They are all
described below.

There are three characteristics that describe continuation
support. All sources have these and there are three properties
available to describe them. The properties can be fixed, have a
default value or be calculated from other properties (aka dynamic) on
the source. The table below explains them in detail.

.. NOTE::

   It is important that you do not to set any of these properties to
   ``true`` unless the source actually have these
   characteristics. Doing so can mean that the pump is not able track
   changes properly.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Description

   * - ``supports_since``
     - Does the source make use of the 'since' parameter if it gets
       passed one?

       This property is typically used to disable the tracking of the
       ``since`` marker. Sometimes it is not necessary to perform the
       tracking as the source won't make use of it anyway.

       .. NOTE::

          If you set ``supports_since`` to ``true`` then you should
          also make sure that you set either ``is_since_comparable`` to
          ``true`` or ``is_chronological`` to ``true`` — or *both*
          depending on the strategy you want.

   * - ``is_since_comparable``
     - Can you compare two ``_updated`` values using lexical/bytewise
       comparison and decide their relative order?

       This property is used to specify if the values of two
       entities's ``_updated`` properties are always comparable. If
       the property can contain values of different types or
       structures, then it may not be possible to use lexical/bytewise
       comparison of the two values to decide order.

       .. NOTE::

          If you set ``is_since_comparable`` to ``true`` then you
          should also make sure that ``supports_since`` is set to
          ``true``.

   * - ``is_chronological``
     - Does the source hand out entities in chronological order, i.e.
       in increasing order?

       If the entities are sorted in chronological other, then the
       pump can shift its ``since`` marker for each new entity in the
       stream. It can also store it away more often. This is a good
       characteristic to have as it makes the source able to continue
       where it left off even though the previous run did not complete
       fully. If the property is set to ``false`` then it can only
       know at the end of the run what the new ``since`` marker is.

       .. NOTE::

          If you set ``is_chronological`` to ``true`` then you
          should also make sure that ``supports_since`` is set to
          ``true``.

The strategy for tracking the ``since`` marker is chosen like this — and in this specific order:


1. If ``supports_since`` is ``true`` and ``is_chronological`` is ``true`` then continuation support is enabled and the *chronological* strategy is chosen. This strategy will store ``_updated`` values in the order we see them.

2. If ``supports_since`` is ``true`` and ``is_since_comparable`` is ``true`` then continuation support is enabled and the *max* strategy is chosen. This strategy will store the maximum ``_updated`` value seen in the run.

3. If none of the above apply, then continuation support is disabled. No tracking of the ``since`` marker is then done.

The table below shows which strategy is chosen depending on the value of the properties:

.. list-table::
   :header-rows: 1
   :widths: 25, 25, 25, 25

   * - ``supports_since``
     - ``is_since_comparable``
     - ``is_chronological``
     - Strategy

   * - ``false``
     - ``false``
     - ``false``
     - None

   * - ``false``
     - ``false``
     - ``true``
     - None

   * - ``false``
     - ``true``
     - ``false``
     - None

   * - ``false``
     - ``true``
     - ``true``
     - None

   * - ``true``
     - ``false``
     - ``false``
     - None

   * - ``true``
     - ``false``
     - ``true``
     - Chronological

   * - ``true``
     - ``true``
     - ``false``
     - Max

   * - ``true``
     - ``true``
     - ``true``
     - Chronological

If continuation support is enabled for a pipe then the ``since``
marker is stored in the ``last-seen`` property on the pump. Note that
one can use the pump's `update-last-seen
<api.html#post--pipes-pipe_id-pump>`_ operation in the :doc:`api` to
update or reset the ``last-seen`` value manually. This is useful in
cases where one wants to reprocess the data from scratch for some
reason. The :doc:`api` can also tell you what the current
``last-seen`` value is.

.. _dataset_source:

The dataset source
------------------

The dataset source is one of the most commonly used sources in a Sesam installation. It simply presents a stream of entities from a
dataset stored in Sesam. Its configuration is very simple and looks like:

Prototype
^^^^^^^^^

::

    {
        "type": "dataset",
        "dataset": "id-of-dataset",
        "include_previous_versions": false,
        "include_replaced": true,
        "supports_signalling": false
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``dataset``
     - String
     - | A dataset id
     -
     - Yes

   * - ``subset``
     - Array
     - | An ``eq`` DTL expression where the left hand side is the index expression and the right hand side is the value that represents the subset. If the subset is specified then only entities that are in that subset will be read from the source.
       |
       | Example: ``["eq", "_S.category", "tank"]``

       .. NOTE:: Make sure that you use indexes version 2 when you use subsets. The reason is that these support deletes. Indexes version 1 does not.
     -
     - No

   * - ``completeness``
     - Boolean
     - If set to ``true``, the dataset source completeness filtering feature is enabled. This will instruct the source to only return source entities that have a ``_ts`` value that is older than or equal to the completeness timestamp value of the source dataset.
     - ``false``
     -

   * - ``include_previous_versions``
     - Boolean
     - If set to ``false``, the dataset source will only return the latest
       version of any entity for any unique ``_id`` value in the dataset. This is the default behaviour.
     - ``false``
     -

   * - ``include_replaced``
     - Boolean
     - If set to ``false``, the dataset source will filter out entities where the ``$replaced`` property is ``true``. This typically used when reading from datasets that have been produced by the :ref:`merge <merge_source>` source.
     - ``true``
     -

   * - ``supports_signalling``
     - Boolean
     - Flag used to enable or disable signalling support between internal pipes (dataset to dataset pipes). If enabled, a pipe
       run is scheduled as soon as the input dataset(s) changes. It does not interrupt any already running pipes.

       See ``global_defaults.use_signalling_internally`` in the :ref:`service metadata <service_metadata_section>` section for more details.

       If signalling is turned on globally, you will have to explicitly set ``supports_signalling`` to ``false`` to
       disable it on individual pipes where you don't want to automatically schedule runs on changes. Note that it is
       automatically disabled (if not explicitly enabled on the source) if the schedule interval is less than 2 minutes or a cron
       expression has been used.
     - ``false``
     -


Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``true`` (Fixed)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``true`` (Fixed)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "dataset",
            "dataset": "northwind:customers",
            "include_previous_versions": true
        }
    }

.. _merge_source:

The merge source
----------------

The merge source is a source that is able to infer the sameness of
entities across multiple datasets. The source uses a set of equality
rules to figure out which entities are the same. Equality is resolved
transitively, so if A is the same as B and B is the same as C then A,
B and C are all considered the same.

Deletes will be output for entity ids that are no longer
applicable. This typically happens when an entity is first merged with
one entity and then later merged with some other entities, and the id
of the resulting entity changes. Those entities will also have the
``$replaced`` property set to ``true``.

If an entity is deleted in its source dataset then the entity will not
be merged, but instead output as a standalone entity with ``_deleted``
set to ``true``.

Prototype
^^^^^^^^^

::

    {
        "type": "merge",
        "version": 2,
        "datasets": ["one d1", "two d2", "three d3"],
        "equality": [
             ["eq", "d1.field1", "d2.field1"],
             ["eq", "d2.field2", "d3.field2"]
        ],
        "supports_signalling": false
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``version``
     - Number
     - There are two different versions of the merge source. Note that the default value is ``1`` for compatibility reasons. Version ``1`` is deprecated. Use version ``2`` if this is a new pipe.
     - ``1``
     - No

   * - ``datasets``
     - List<String{>=1}>
     - A list of one or more datasets that are to be merged. Each item in this list is a pair of dataset id and dataset alias. A given dataset can only appear once in this list. The syntax is the same as in the ``datasets`` property in :ref:`hops <hops_function>`.
     -
     - Yes

   * - ``initial_datasets``
     - List<String{>=0}>
     - By default the source will be considered populated if all the datasets in the ``datasets``  property have been populated. If some of these datasets will never be populated then this property can be used to list the datasets that must be populated before the source is considered populated. You should normally not have to use this property.

       See also the :ref:`dataset sink <dataset_sink>` property ``set_initial_offset``.
     -
     -

   * - ``equality``
     - List<EqFunctions{>=0}>
     - A list of zero or more ``eq`` functions that are to be used to decide which entities are the same. The functions must follow the rules for :ref:`joins <joins>` in DTL.
     -
     - No

   * - ``identity``
     - String
     - Specifies the strategy for how to create the ``_id`` of the resulting entities.

       * ``"composite"`` - The default, which is to create an id
         composed of all the ids of the entities involved and the
         offset of the dataset from which they originates.

         Example: ``"0|one1|1|two1|1|two2|2|three3"``. This particular
         id consists of four entity ids from three datasets. If it is
         the result of the prototypical merge source shown above, then
         ``one1`` is the id of an entity from the ``d1`` dataset,
         ``two1`` and ``two2`` are ids of entities from the ``d2``
         dataset, and ``three3`` is the id of an entity from the
         ``d3`` dataset.

         The parts of the composite id are first ordered by the offset
         of the dataset in the ``datasets`` property, then by the
         entities' ``_id`` property. This results in a deterministic
         entity id.

       * ``"first"`` - Similar to the ``composite`` strategy, but uses
         the entity id of the first entity given the same ordering
         rules as above.

         Example: ``"one1"``.
     - ``"composite"``
     - No

   * - ``strategy``
     - String
     - The strategy to use to combine the properties of the merged
       entities. This affects how the resulting entities look.

       The examples below illustrate the results of merging the
       following three entities in this particular order (ids omitted for brevity):
       ``{"x":1}``, ``{"y": [2, 1]}``, ``{"y": 2, "z": [3, 3]}``

       * ``"default"`` - The default is to union all the values, which
         results in all properties being lists of all the values from
         all the entities. This is similar to how the
         :ref:`merge-union <dtl_transform-merge-union>` DTL function
         works. Duplicates are not removed.

         Example: ``{"x": [1], "y": [2, 1, 2], "z": [3, 3]}``

       * ``"compact"`` - Similar to the default strategy, but tries to
         compact the property values; duplicate values are removed,
         properties with empty lists are dropped, and list properties
         with a single value are turned into single valued properties.

         Example: ``{"x": 1, "y": [2, 1], "z": 3}``

       * ``"list"`` - Returns an entity with a ``$merged`` property
         which contains a list of the merged entities. This strategy
         can be used to implement custom strategies.

         | Example:
         | ``{"$merged": [``
         |   ``{"x": 1},``
         |   ``{"y": [2, 1]},``
         |   ``{"y": 2, "z": [3, 3]}]}``

     - ``"default"``
     - No

   * - ``supports_signalling``
     - Boolean
     - Flag used to enable or disable signalling support between internal pipes (dataset to dataset pipes). If enabled, a pipe
       run is scheduled as soon as the input dataset(s) changes. It does not interrupt any already running pipes.

       See ``global_defaults.use_signalling_internally`` in the :ref:`service metadata <service_metadata_section>` section for more details.

       If signalling is turned on globally, you will have to explicitly set ``supports_signalling`` to ``false`` to
       disable it on individual pipes where you don't want to automatically schedule runs on changes. Note that it is
       automatically disabled (if not explicitly enabled on the source) if the schedule interval is less than 2 minutes or a cron
       expression has been used.
     - false
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``true`` (Fixed)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``true`` (Fixed)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Below you'll find three datasets ``A``, ``B`` and ``C`` and a pipe configuration
that uses the ``merge`` source.

Dataset ``A``:

::

   [
       {"_id": "a1", "f1": 1},
       {"_id": "a2", "f1": 2}
   ]

Dataset ``B``:

::

   [
       {"_id": "b1", "f1": 1, "f2": "x"},
       {"_id": "b2", "f1": 3}
   ]

Dataset ``C``:

::

   [
       {"_id": "c1", "f3": "X"},
       {"_id": "c2", "_deleted": true, "f3": "Y"},
       {"_id": "c3", "_deleted": true, "f3": "X"},
   ]


Pipe configuration:

::

   {
       "_id": "result",
       "source": {
           "type": "merge",
           "datasets": ["A a", "B b", "C c"],
           "equality": [
               ["eq", "a.f1", "b.f1"],
               ["eq", "b.f2", ["lower", "c.f3"]],
           ]
       }
   }

Given the above we should expect an output that looks like this:

::

   [
       {"$ids": ["a1", "b1", "c1"], "_id": "0|a1|1|b1|2|c1", "_updated": 0,
        "f1": [1, 1], "f2": "x", "f3": "X"},
       {"$ids": ["a2"], "_id": "0|a2", "_updated": 1, "f1": 2},
       {"$ids": ["b2"], "_id": "1|b2", "_updated": 2, "f1": 3},
       {"$ids": ["c2"], "_deleted": true, "_id": "2|c2", "_updated": 3, "f3": "Y"},
       {"$ids": ["c3"], "_deleted": true, "_id": "2|c3", "_updated": 4, "f3": "X"}
   ]

Entities ``a1``, ``b1`` and ``c1`` have been merged. Entities ``a2``
and ``b2`` did not match any other entities. Deleted entities, like
``c2`` and ``c3``, are never merged with any other entities.

The merged entities are combined so that the properties and their
values are merged in the resulting entity. ``null`` values are kept
intact. List values appear in a consistent order and may contain
duplicate values.

The ``_updated`` property is a sequence number that increases every
time a new entity is generated by the source. Entities appear in
chronological order.

The ``_id`` property is a composite id that consists of the dataset
offset and entity id joined by the ``|`` character. The dataset offset
is the index of the dataset in the ``datasets`` property in the pipe
configuration. The composite parts are ordered by dataset offset and
entity in order to get consistent ids.

The ``$ids`` property contains all the original entity ids of the
entities merged into the entity. Note that an entity id will not be
added to this list if the original entity has the ``$ids``
property. Because of how properties are merged the ``$ids`` will end
up being a union of all the orginal entity ids excluding the entity
ids of the merge entities themselves. This is useful when merging
already merged entities downstream.

.. WARNING::

   This applies only to merge sources using version ``1``.

   Do not remove a dataset from the ``datasets`` property nor change
   the order of the datasets in the ``datasets`` property. Doing so
   may lead to inconsistent results. Adding or renaming datasets is OK
   though as this won't affect the order of the datasets. If you need
   to do this then you should reset the pipe and maybe also delete the
   target dataset.

.. _union_datasets_source:

The union datasets source
-------------------------

The union datasets source is similar to the ``dataset source``, except
it can process several datasets at once and keep track of each one in
its ``since`` marker handler. The union datasets source reads its
datasets in order, exhausting each one before moving to the next.

The entity ``_id`` property in entities is prefixed by the dataset
id separated by the ``:`` character. This is done to prevent unwanted
identity collisions. The entity id ``dave`` from the ``men`` dataset
will end up with the id ``men:dave``, and the entity id ``claire``
from the ``women`` dataset will end up with the id ``women:claire``.

Prototype
^^^^^^^^^

::

    {
        "type": "union_datasets",
        "datasets": ["id-of-dataset1", "id-of-dataset2"],
        "include_previous_versions": false,
        "supports_signalling": false
    }

Properties
^^^^^^^^^^

The configuration of this source is identical to the ``dataset``
source, except ``datasets`` can be a list of datasets ids.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``datasets``
     - List<String>
     - A list of datasets ids.
     -
     - Yes

   * - ``initial_datasets``
     - List<String{>=0}>
     - By default the source will be considered populated if all the datasets in the ``datasets``  property have been populated. If some of these datasets will never be populated then this property can be used to list the datasets that must be populated before the source is considered populated. You should normally not have to use this property.

       See also the :ref:`dataset sink <dataset_sink>` property ``set_initial_offset``.
     -
     -

   * - ``include_previous_versions``
     - Boolean
     - If set to ``false``, the
       data source will only return the latest version of any entity for
       any unique ``_id`` value in the dataset. This is the default behaviour.
     - false
     -

   * - ``supports_signalling``
     - Boolean
     - Flag used to enable or disable signalling support between internal pipes (dataset to dataset pipes). If enabled, a pipe
       run is scheduled as soon as the input dataset(s) changes. It does not interrupt any already running pipes.

       See ``global_defaults.use_signalling_internally`` in the :ref:`service metadata <service_metadata_section>` section for more details.

       If signalling is turned on globally, you will have to explicitly set ``supports_signalling`` to ``false`` to
       disable it on individual pipes where you don't want to automatically schedule runs on changes. Note that it is
       automatically disabled (if not explicitly enabled on the source) if the schedule interval is less than 2 minutes or a cron
       expression has been used.
     - false
     -

   * - ``prefix_ids``
     - Boolean
     - If set to ``false``, then the entity ids will not be prefixed with the dataset id.
     - true
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``true`` (Fixed)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``true`` (Fixed)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "union_datasets",
            "datasets": ["northwind:customers", "northwind:orders"],
            "include_previous_versions": true
        }
    }

.. _merge_datasets_source:

The merge datasets source
-------------------------

The merge datasets source is similar to the ``dataset source``, except
it can process several datasets at once and keep track of each one in
its ``since`` marker handler.

The merge datasets source reads its all of its datasets and returns
entities ordered by their ``_ts`` field. It knows how to deal with
identities, so that only the *latest* version of entities are returned.

Entity ids are not modified in any way.

Prototype
^^^^^^^^^

::

   {
       "type": "merge_datasets",
       "datasets": ["id-of-dataset1", "id-of-dataset2"],
       "strategy": "latest",
       "supports_signalling": false
    }

Properties
^^^^^^^^^^

The configuration has two primary properties, ``datasets`` which must
be a list of datasets ids and ``strategy`` for choosing the merge
strategy.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``datasets``
     - List<String>
     - A list of datasets ids.
     -
     - Yes

   * - ``initial_datasets``
     - List<String{>=0}>
     - By default the source will be considered populated if all the datasets in the ``datasets``  property have been populated. If some of these datasets will never be populated then this property can be used to list the datasets that must be populated before the source is considered populated. You should normally not have to use this property.

       See also the :ref:`dataset sink <dataset_sink>` property ``set_initial_offset``.
     -
     -

   * - ``strategy``
     - String
     - The name of the strategy to use to merge entities. Valid
       options are "``latest``" (the default) and "``all``".

       The "``latest``" strategy returns the version of the entity with
       the newest timestamp (as given in the ``_ts`` field). It will
       return the entity from the dataset that contains the latest
       version. This strategy is useful when only the latest version
       of an entity among the given datasets are of interest.

       The "``all``" strategy returns a merged version of the entity that
       contains all latest versions from all datasets. The individual
       dataset entities are keyed under the dataset id that they came
       from. The entities are ordered by the timestamp of the latest
       version of that entity. The returned entity contains all latest
       versions from all datasets where is appears. This strategy is
       useful when all datasets provide data for the resulting
       entity. In a lot of cases one may want to use it with a
       transform, so that only the entity can be shaped in a way that
       is more useful downstream.
     - "latest"
     -

   * - ``supports_signalling``
     - Boolean
     - Flag used to enable or disable signalling support between internal pipes (dataset to dataset pipes). If enabled, a pipe
       run is scheduled as soon as the input dataset(s) changes. It does not interrupt any already running pipes.

       See ``global_defaults.use_signalling_internally`` in the :ref:`service metadata <service_metadata_section>` section for more details.

       If signalling is turned on globally, you will have to explicitly set ``supports_signalling`` to ``false`` to
       disable it on individual pipes where you don't want to automatically schedule runs on changes. Note that it is
       automatically disabled (if not explicitly enabled on the source) if the schedule interval is less than 2 minutes or a cron
       expression has been used.
     - false
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``true`` (Fixed)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``true`` (Fixed)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "merge_datasets",
            "datasets": ["products", "products-metadata"]
        }
    }


.. _diff_datasets_source:

The diff datasets source (Experimental)
---------------------------------------

The diff datasets source is similar to the ``merge dataset source``, except that
it also compares the entities from the datasets. The comparison produces a diff and filters out
entities that are equal.

For each merged entity (same as the ``all`` strategy in ``merge dataset source``)
an additional ``$diff`` property is also generated. The diff contains the datasets and values for
the properties that are not equal across all the datasets.

Entity ids are not modified in any way.

Prototype
^^^^^^^^^

::

   {
       "type": "diff_datasets",
       "datasets": ["id-of-dataset1", "id-of-dataset2"]
    }

Properties
^^^^^^^^^^

The configuration only requires the property ``datasets`` which must
be a list of datasets ids.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``datasets``
     - List<String>
     - A list of datasets ids.
     -
     - Yes

   * - ``initial_datasets``
     - List<String{>=0}>
     - By default the source will be considered populated if all the datasets in the ``datasets``  property have been populated. If some of these datasets will never be populated then this property can be used to list the datasets that must be populated before the source is considered populated. You should normally not have to use this property.

       See also the :ref:`dataset sink <dataset_sink>` property ``set_initial_offset``.
     -
     -

   * - ``whitelist``
     - List<String>
     - The names of the properties to include in the comparison. If there is a
       ``blacklist`` also specified, the whitelist will be filtered against the contents of the
       blacklist.
     -
     -

   * - ``blacklist``
     - List<String>
     - The names of the properties to exclude from the comparison. If there is a
       ``whitelist`` also specified, the blacklist operates on the values of the whitelist (and not
       the properties present in the entities).
     -
     -


   * - ``treat_lists_as_sets``
     - Boolean
     - Flag to indicate if you want to ignore duplicates and ordering of lists in the entities
       you are comparing. This option also affects lists nested deeper inside the entity.
     - false
     -


   * - ``ignore_deletes``
     - Boolean
     - Flag to indicate if you want to ignore deleted entities during the comparison. By default
       there will be produced a difference if one of the datasets contains a deleted entity while
       the other datasets does not contain the deleted entity.

       If ``true`` the deleted entities are treated as if they don't exist.
     - false
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``true`` (Fixed)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``true`` (Fixed)


Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "diff_datasets",
            "datasets": ["product", "other-products"]
        }
    }

Example result
^^^^^^^^^^^^^^

::

   {
       "_id": "some-product",
       "$diff": {
           "price": {
               "products": "price-from-products",
               "other-products": "price-from-other-products",
           }
       }
    }


.. _embedded_source:

The embedded source
-------------------

This is a data source that lets you embed the data inside the configuration of the source. This is convenient when you have a small and static dataset. Do not use this source to hold a large number of entities.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 30, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``entities``
     - List<Entity>
     - Contains the list of entities is to be served by the source.
     -
     - Yes

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Default)

   * - ``is_since_comparable``
     - ``true`` (Default)

   * - ``is_chronological``
     - ``false`` (Default)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

Example:

::

    {
        "source": {
            "type": "embedded",
            "entities": [
                {"_id": "a", "title": "A"},
                {"_id": "b", "title": "B"},
                {"_id": "c", "title": "C"}
            ]
        }
    }


.. _sql_source:

The SQL source
--------------

The `SQL <https://en.wikipedia.org/wiki/SQL>`_ database source is one of the most commonly used data sources.
In short, it presents `database relations <https://en.wikipedia.org/wiki/Relation_(database)>`_ (i.e. ``tables``,
``views`` or ``queries``) as a entity stream to Sesam.

The SQL source has several options, all of which are presented below with their default values:

Prototype
^^^^^^^^^

::

    {
        "system": "id-of-system",
        "table": "name-of-table",
        "primary_key": ["list","of","key","names"],
        "query": "SQL query string",
        "updated_query": "SQL query string for 'since' support in queries",
        "updated_column": "column-name-for-since-support-in-tables",
        "whitelist": ["columns","to","include"],
        "blacklist": ["columns","to","exclude"],
        "fetch_size": 1000,
        "preserve_null_values": false,
        "schema": "default-schema-name-if-included"
    }


Column types
^^^^^^^^^^^^

See the :ref:`supported column types <sql_types>` list for a overview of which RDBMS column types
are supported and how they are mapped to :ref:`Sesam types <entity_data_types>`. Note that if your ``table`` or
``query`` property refer to relations with unsupported column types, you will either have to use the ``blacklist``
configuration property to ignore them, or write a custom ``query`` that coerces the non-supported column to a
supported type.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 30, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - Must refer to a :ref:`SQL system <sql_system>` component by ``id``. The role of this component is provide
       services like connection pooling and authentication for the data sources using it
     -
     - Yes

   * - ``table``
     - String
     - If ``table`` is given, it must refer to a fully qualified table name in the database system,
       not including schema, which if needed must be set separately. The ``table`` and ``query``
       properties are mutually exclusive with ``table`` used if both are present. TODO: are table names case sensitive?
     -
     - Yes

   * - ``primary_key``
     - List<String> or String
     - The value of this property can be a single string with the name of the column
       that contains the ``primary key`` (PK) of the table or query, or a list of strings
       if it is a compound primary key. If the property is not set and the ``table``
       property is used, the data source component will attempt to use table metadata
       to deduce the PK to use. In other words, you will have to set this property if
       the ``query`` property us used.
     -
     -

   * - ``query``
     - List<String> or String
     - Must be a valid query in the dialect of the ``RDBMS`` represented by the
       ``system`` property. You will also have to configure the primary key(s)
       of the query in the ``primary_key`` property. Note: mutually exclusive with the
       ``table`` property with ``table`` taking precedence. If a list of strings is given, they will be
       converted to a single string by concatenation with the newline character.
     -
     - Yes

   * - ``updated_column``
     - String
     - If the underlying relation contains information about updates, the data source is
       able to support ``since`` markers. You can provide the name of the column to use
       for such queries here. This must be a valid column name in the ``table`` or ``query``
       result sets and it must be of a data type that supports larger or equal (">=") tests
       for the ``table`` case.
     -
     -

   * - ``updated_query``
     - List<String> or String
     - If the ``query`` property is set, the ``since`` support must be expressed by a
       full query including any test needed. A single variable binding
       ``:since`` must be included somewhere in the query string - for example
       "select * from view_name v where v.updates >= :since". If a list of strings is given, they will be
       converted to a single string by concatenation with the newline character.
     -
     -

   * - ``schema``
     - String
     - If a specific schema within a database is needed, you must provide its name in this property.
       Do *not* use schema names in the ``table`` property.
     -
     -

   * - ``whitelist``
     - List<String>
     - The names of the columns to include in the generated entities. If there is a ``blacklist`` also specified, the
       whitelist will be filtered against the contents of the blacklist.
     -
     -

   * - ``blacklist``
     - List<String>
     - The names of the columns to exclude from the generated entities. If there is a ``whitelist`` also specified, the
       blacklist operates on the values of the whitelist (and not the whole columnset).
     -
     -

   * - ``preserve_null_values``
     - Boolean
     - If set to ``true`` will include null values in the entities produces by this source. By default they are omitted.
     - False
     -

   * - ``fetch_size``
     - Integer
     - The fetch size of the result sets (number of rows in a cursor fetch) to get from the database
     - 1000
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Dynamic: ``true`` if ``updated_column`` set)

   * - ``is_since_comparable``
     - ``true`` (Default)

   * - ``is_chronological``
     - ``false`` (Dynamic: if ``table`` and ``updated_column`` set then defaults to ``true``, if ``query`` then it can be set explicitly)

   * - ``is_chronological_full``
     - ``false`` (Dynamic: ``true`` if ``is_chronological`` is effectively ``true`` and this property is not explicity set to ``false``)

       If this property is set to ``false`` then a full run will not
       consider the source to be chronological even though it is
       chronological in incremental runs.

       .. NOTE::

          In practice this avoids doing an order by when doing full runs,
          but at the cost of not saving pipe offsets and supporting
          incremental deletion tracking if it fails to complete.

          We have seen SQL tables where only the latest rows have
          an value in the updated column. In that case it is not that
          useful to use order by and to save pipe offsets
          incrementally.


Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

Example with a single table:

::

    {
        "source": {
            "type": "sql",
            "system": "Northwind",
            "table": "Customers"
        }
    }

Example with a single table, where the primary key is in a column named ``table_id`` and the updated datestamp is
in a column called ``updated``. This enables us to switch on ``since`` support:

::

    {
        "source": {
            "type": "sql",
            "system": "my_system",
            "table": "my_table",
            "primary_key": "table_id",
            "updated_column": "updated"
        }
    }

Example with custom query:

::

    {
        "source": {
            "type": "sql",
            "system": "Northwind",
            "query": "select * from Customers",
            "primary_key": "CustomerID"
        }
    }

Example with a custom query from a table called ``my_table`` where the primary key is in a column named ``table_id``
and the updated datestamp is in a column called ``updated``. This enables us to switch on ``since`` support:

::

    {
        "source": {
            "type": "sql",
            "system": "my_system",
            "query": "select * from my_table",
            "primary_key": "table_id",
            "updated_column": "updated",
            "updated_query": "select * from my_table where updated >= :since"
        }
    }

.. _conditional_source:

The conditional source
----------------------

The conditional source selects an active source based on a key typically controlled by an environment variable.
It is typically used in devops to be able to use the same configuration in different type of environments (i.e. development,
staging, production). The actual source to use is resolved at runtime when the parent pipe is created.

The configuration options are:

Prototype
^^^^^^^^^

::

    {
       "type": "conditional",
       "condition": "$ENV(current-environment)",
       "alternatives": {
           "dev": {
               "type": "embedded",
               ..
           },
           "test": {
               "type": "sql",
               ..
           },
           "prod": {
               "type": "sql",
               ..
           }
       }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``condition``
     - String
     - The key to look up in ``alternatives`` for the actual source to use at runtime. Typically an environment variable.
       Note that all possible enumerations of this value need to exist in ``alternatives``.
     -
     - Yes

   * - ``alternatives``
     - Object
     - A dictionary of actual source configurations keyed by the enumerated value of ``condition``.
     -
     - Yes


.. _csv_source:

The CSV source
--------------

The CSV data source translates the rows of files in `CSV format <https://en.wikipedia.org/wiki/Comma-separated_values>`_
to entities.

The configuration options are:

Prototype
^^^^^^^^^

::

    {
       "type": "csv",
       "system": "a-valid-url-or-microservice-system-id",
       "url": "url-to-csv-file",
       "has_header": true,
       "field_names": ["mappings","from","columns","to","properties"],
       "auto_dialect": true,
       "dialect": "excel",
       "encoding": "utf-8",
       "decode_error_strategy": "strict-or-replace",
       "primary_key": ["list","of","column","names"],
       "whitelist": ["list","of","column","names","to","include"],
       "blacklist": ["list","of","column","names","to","exclude"],
       "preserve_empty_strings": false,
       "delimiter": ","
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``url``
     - String
     - The URL of the ``CVS`` file to load.
     -
     - Yes

   * - ``system``
     - String
     - The ID of the :ref:`URL system <url_system>` or :ref:`microservice system <microservice_system>` component to use.
     -
     - Yes

   * - ``has_header``
     - Boolean
     - Flag that indicates to the source that the first row in the ``CSV`` file contains the names of the columns.
       If this property is set to ``false``, you will have to provide a list of column names in the ``field_names``
       property.
     - true
     -

   * - ``field_names``
     - List
     - If set, specifies the names of the columns. It takes precedence over the header in the CSV file if present.
     -
     -

   * - ``auto_dialect``
     - Boolean
     - Flag that hints to the source that it should try to guess the dialect of the ``CSV`` file on its own. Note
       that if ``dialect`` is explicitly set, ``auto_dialect`` is ignored.
     - true
     -

   * - ``dialect``
     - String
     - Encodes what type of CSV file the file is. This is basically presets of the other properties.
       The recognised values are ``"excel"``, ``"excel_tab"`` and ``"unix_dialect"``.
       Note that if ``dialect`` is explicitly set, ``auto_dialect`` is ignored. If both ``auto_dialect`` is ``false`` and
       no ``dialect`` has been explicitly set, the dialect chosen will be ``excel``.
     -
     -

   * - ``encoding``
     - String
     - The character set to used to encode the text in the CSV file
     - "UTF-8"
     -

   * - ``decode_error_strategy``
     - String
     - A enumeration of "strict" and "replace" that tells the character decoder how to deal with illegal characters
       in the input data. The default is "strict" which raises an error and stops processing. The "replace" option
       will log a warning and attempt to replace the offending character(s) with the unicode special character for
       "replacement character", see https://en.wikipedia.org/wiki/Specials_%28Unicode_block%29 for more details.
       Use the "replace" option with extreme care as it can lead to data loss if you're not absolutely sure of what
       you are doing. The preferred option should always be to try the fix the data at the source.
     - "strict"
     -

   * - ``primary_key``
     - List<String> or String
     - The name of the column(s) to use as ``_id`` in the generated entities. It can be either a list of strings
       (if the identity is a compound value) or a single column name (i.e. a string). The column name(s) are case
       sensitive and must match the contents of either ``field_names`` or the header of the CSV file.
     -
     - Yes

   * - ``whitelist``
     - List<String>
     - The names of the columns to include in the generated entities. If there is a ``blacklist`` also specified, the
       whitelist will be filtered against the contents of the blacklist.
     -
     -

   * - ``blacklist``
     - List<String>
     - The names of the columns to exclude from the generated entities. If there is a ``whitelist`` also specified, the
       blacklist operates on the values of the whitelist (and not the whole columnset).
     -
     -

   * - ``preserve_empty_strings``
     - Boolean
     - If set to ``true`` will include column values that are empty strings. By default these are omitted.
     - False
     -

   * - ``delimiter``
     - String
     - The character or string to use as the ``CSV`` field separator (delimiter)
     - ","
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Default)

   * - ``is_since_comparable``
     - ``true`` (Default)

   * - ``is_chronological``
     - ``false`` (Default)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "csv",
            "url": "http://blog.plsoucy.com/wp-content/uploads/2012/04/countries-20140629.csv",
            "primary_key": "Code",
            "encoding": "iso-8859-1"
        }
    }

.. _rdf_source:

The RDF source
--------------

The RDF data source is able to read `RDF <https://www.w3.org/TR/2004/REC-rdf-primer-20040210/>`_ data
in `N-Triples <https://www.w3.org/TR/2014/REC-n-triples-20140225/>`_, `Turtle <https://www.w3.org/TR/turtle/>`_, `N3 <https://www.w3.org/TeamSubmission/n3/>`_ or `RDF/XML <https://www.w3.org/TR/rdf-syntax-grammar/>`_ format and turn this into entities.

See the :doc:`rdf-support` document for more detail on working with RDF in Sesam.

It will transform triples on the form ``<subject-uri> <predicate-uri> "value" OR <object-uri>`` into
entities on the form:

::

    {
        "_id": "<subject-uri>",
        "<predicate-uri>": "value" OR "~robject-uri"
    }


`RDF Blank Nodes <https://en.wikipedia.org/wiki/Blank_node>`_ (aka BNodes) will be turned into child entities.

Prototype
^^^^^^^^^

::

    {
       "type": "rdf",
       "system": "url--or-microservice-system-id",
       "url": "url-to-rdf-file",
       "sort_lists": true,
       "format": "nt-ttl-or-xml"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The ID of the :ref:`URL system <url_system>` or :ref:`microservice system <microservice_system>` component to use.
     -
     - Yes

   * - ``url``
     - String
     - The URL of the ``RDF`` file to load - it can contain multiple subjects
       (with ``blank node`` hierarchies) and each unique non-blank subject will
       result in a single root entity.
     -
     - Yes

   * - ``format``
     - String
     - The type of ``RDF`` file referenced by the ``url`` property. It is
       an enumeration that can take following recognized values: ``"nt"`` for
       N-Triples, ``"ttl"`` for Turtle, ``"n3"`` for N3 or ``"xml"`` for ``RDF/XML`` files.
     - "nt"
     -

   * - ``sort_lists``
     - Boolean
     - If the ``sort_lists`` is set to ``true`` any resulting entity properties containing lists of values (due to
       them having the same RDF predicate) will be sorted, making the output predictable. This applies in a recursive
       fashion.
     - true
     -

   * - ``is_sorted``
     - Boolean
     - Indicates that the input data is sorted on RDF subject. If the ``is_sorted`` is set to ``true`` and the
       ``format`` property is ``nt`` (N-Triples), the RDF source will attempt to parse the input data sequentially and
       emit a new entity when the RDF subject changes, without loading the entire RDF file into memory first.
       Note that the input data cannot contain `RDF Blank Nodes <https://en.wikipedia.org/wiki/Blank_node>`_ (aka
       BNodes) in this case. The property has no effect on formats other than ``nt``.
     - false
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Default)

   * - ``is_since_comparable``
     - ``true`` (Default)

   * - ``is_chronological``
     - ``false`` (Default)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "rdf",
            "url": "http://www.snee.com/rdf/elvisimp.rdf",
            "format": "xml",
        }
    }

.. _sdshare_source:

The SDShare source
------------------

The SDShare data source can read `RDF <https://www.w3.org/TR/2004/REC-rdf-primer-20040210/>`_ from `ATOM feeds <https://tools.ietf.org/html/rfc4287>`_ after the
`SDShare specification <http://sdshare.org>`_. See the :doc:`rdf-support` document for more information about working with RDF data
in Sesam.


It has the following properties:

Prototype
^^^^^^^^^

::

    {
       "type": "sdshare",
       "system": "url-or-microservice-system-id",
       "sort_lists": true,
       "url": "url-to-sdshare-fragments-feed"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The ID of the :ref:`URL system <url_system>` or :ref:`microservice system <microservice_system>` component to use.
     -
     - Yes

   * - ``url``
     - String
     - The URL of the SDShare fragments feed to consume.
     -
     - Yes

   * - ``sort_lists``
     - Boolean
     - If the ``sort_lists`` is set to ``true`` any resulting entity properties containing lists of values (due to
       them having the same RDF predicate) will be sorted, making the output predictable. This applies in a recursive
       fashion.
     - true
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``true`` (Default)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``false`` (Default)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "sdshare",
            "url": "https://open.sesam.io/sdshare/server/1/fragments/enhetsregisteret"
        }
    }

.. _ldap_source:

The LDAP source
---------------

The LDAP source provides entities from a `LDAP catalog <https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol>`_
configured by a :ref:`LDAP system <ldap_system>`.

It supports the following properties:

Prototype
^^^^^^^^^

::

    {
        "type": "ldap",
        "system": "ldap-system-id",
        "search_base": "*",
        "search_filter": "(objectClass=organizationalPerson)",
        "attributes": "*",
        "id_attribute": "cn",
        "page_size": 500,
        "attribute_blacklist": ["a","list","of","attributes","to","exclude"]
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - ID of the LDAP system component to use
     -
     - Yes

   * - ``search_base``
     - String
     - The base LDAP search expression to use when looking for records
     - "*"
     -

   * - ``search_filter``
     - String
     - LDAP filter expression to apply to all records found by the ``search_base`` expression
     - "(objectClass=organizationalPerson)"
     -

   * - ``attributes``
     - String
     - A wildcard expression specifying which attributes to include in the entity.
     - "*"
     -

   * - ``id_attribute``
     - String
     - Sets which of the LDAP attributes to use for the ``_id`` property of a entity.
     - "cn"
     -

   * - ``page_size``
     - Integer
     - The default number of records to read at a time from the LDAP service.
     - 500
     -

   * - ``attribute_blacklist``
     - List
     - A list of attribute names (as strings) to exclude from the record when constructing entities.
     - []
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Fixed)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``false`` (Fixed)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "ldap",
            "system": "example_ldap",
            "search_base": "ou=Example,dc=example,dc=org"
        }
    }


.. _json_source:

The JSON source
---------------


The JSON source can read entities from a `JSON <https://en.wikipedia.org/wiki/JSON>`_ resource available over `HTTP <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_ (i.e. served by a web server). The data must conform to the :doc:`JSON Pull Protocol <json-pull>`.

If the ``supports_since`` property is set to *true*, then the ``since`` request parameter is added to the URL to
signal that we want only changes that happened after the since marker.

Prototype
^^^^^^^^^

::

    {
       "system": "system-id",
       "type": "json",
       "url": "url-to-json-data",
       "supports_signalling": false
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`URL system <url_system>` or :ref:`microservice system <microservice_system>` component to use.
     -
     - Yes

   * - ``url``
     - String
     - The URL of the ``JSON`` data to load. Note that the data must conform to the :doc:`JSON Pull Protocol <json-pull>`.
     -
     - Yes

   * - ``supports_signalling`` (experimental)
     - Boolean
     - Flag used to enable or disable signalling support between internal pipes (dataset to dataset pipes). If enabled, a pipe
       run is scheduled as soon as the input dataset(s) changes. It does not interrupt any already running pipes.
     - ``false``
     -

   * - ``page_size``
     - Integer(>=1)
     - If the page size is specified then the source will download the data across multiple requests until there is no more data left to download. The ``limit`` request parameter is passed to the endpoint to cap the number of entities in each response.

       .. NOTE::

          Paging is only available if the source has ``supports_since``, ``is_chronological`` and ``is_since_comparable`` all set to ``true``.
     - No paging
     -

   * - ``subset``
     - Array
     - | An ``eq`` DTL expression where the left hand side is the index expression and the right hand side is the value that represents the subset. If the subset is specified then only entities that are in that subset will be read from the source.
       |
       | Example: ``["eq", "_S.category", "tank"]``

       .. NOTE:: For this to work the source must support subsets.
     -
     - No

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Default)

   * - ``is_since_comparable``
     - ``true`` (Default)

   * - ``is_chronological``
     - ``false`` (Default)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "json",
            "system": "some-url-or-microservice-system",
            "url": "test.json",
        }
    }

The empty source
----------------

Sometimes it is useful for debugging or development purposes to have a data source that doesn't produce any entities:

Prototype
^^^^^^^^^

::

    {
        "type": "empty"
    }

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Fixed)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``true`` (Fixed)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "source": {
            "type": "empty"
        }
    }


.. _http_endpoint_source:

The HTTP endpoint source
------------------------

This is a special data source that registers an `HTTP <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_
receiver endpoint that one can post entities to. Entities posted here will be written to the pipe's sink.

A pipe that references the ``HTTP endpoint`` source will not pump any
entities, in practice this means that a pump is not configured for the
pipe; the only way for entities to flow through the pipe is by posting
them to the HTTP endpoint.

It exposes two URLs:

.. list-table::
   :header-rows: 1
   :widths: 50, 60

   * - URL
     - Description

   * - ``http://localhost:9042/api/receivers/mypipe/entities``
     - JSON Push endpoint

   * - ``http://localhost:9042/api/receivers/mypipe/sdshare-push-receiver``
     - SDShare Push receiver endpoint

JSON Push protocol
^^^^^^^^^^^^^^^^^^

The JSON Push protocol is described in additional detail in the
:doc:`JSON Push Protocol <json-push>` document. The serialisation of
entities as `JSON <https://en.wikipedia.org/wiki/JSON>`_ is described in more detail :doc:`here
<entitymodel>`. Both individual entities and lists of entities can be
posted. This endpoint is compatible with :ref:`The JSON push sink
<json_push_sink>`.

The JSON Push endpoint supports `HTTP POST <https://en.wikipedia.org/wiki/POST_(HTTP)>`_ of
both a single JSON object and a list of JSON objects. The HTTP request's ``content-type``
`header <https://en.wikipedia.org/wiki/List_of_HTTP_header_fields>`_ element must be set to ``application/json`` in this case.

SDShare Push protocol
^^^^^^^^^^^^^^^^^^^^^

The SDShare Push protocol is described `here
<https://github.com/SesamResearch/sdshare-push/blob/master/spec.md>`__.

The SDShare Push endpoint supports receiving `RDF <https://www.w3.org/TR/2004/REC-rdf-primer-20040210/>`_
in `N-Triples <https://www.w3.org/TR/2014/REC-n-triples-20140225/>`_ form. In this case the URL
parameters have to include at least one ``resource`` parameter describing which resources the
N-Triples payload contains statements about. If you include a ``resource`` parameter that there
are no statements about in the N-Triples body, an empty entity is generated with its ``_deleted``
flag set to ``true``. Note that the ``graph`` parameter of the protocol is ignored - the destination
of the entities generated from the N-Triples payload must be configured in the pipe's ``sink``
section. This type of HTTP request expects the ``content-type`` to be ``application/n-triples`` or
``text/plain``. See the :doc:`rdf-support` document for more detail on working with RDF in Sesam.


Prototype
^^^^^^^^^

::

    {
        "type": "http_endpoint"
    }


Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``auto_populate_dataset``
     - Boolean
     - If true (the default) the sink dataset will be marked as populated initially. This property can only be
       specified if the sink is of type ``dataset``.
     - ``true``
     - No


Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Fixed)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``false`` (Fixed)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The pipe configuration given below will expose the
``my-entities`` receiver endpoint and write any data it receives
into the ``my-entities`` dataset:

::

    {
        "_id": "my-entities",
        "type": "pipe",
        "source": {
            "type": "http_endpoint"
        }
    }



.. _sparql_source:

The SPARQL source
-----------------

The SPARQL source fetches `RDF <https://www.w3.org/TR/2004/REC-rdf-primer-20040210/>`_ data about subjects from a
`triplestore <https://en.wikipedia.org/wiki/Triplestore>`_ exposing a `SPARQL compliant <https://www.w3.org/TR/rdf-sparql-query/>`_ endpoint.
The endpoint of the source is configured either directly or implicitly by a :ref:`URL system <url_system>`. The source uses
two SPARQL queries to construct entities; the fragment query is a SPARQL ``SELECT`` query that gets a list of subjects
to get data for and their modification times and a fragment query, which is a SPARQL ``CONSTRUCT`` query that
gathers all relevant statements about a particular subject. The latter is then used to generate the stream of entities.

See the :doc:`rdf-support` document for more detail on working with RDF in Sesam.

Prototype
^^^^^^^^^

::

    {
        "type": "sparql",
        "system": "url-system-id",
        "url": "sparql-endpoint",
        "fragments_query": "SPARQL select query",
        "fragment_query": "SPARQL construct query"
        "since_default": "0001-01-01T00:00:00Z"
    }


Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`URL System <url_system>` component to use.
     -
     - Yes

   * - ``fragments_query``
     - List<String> or String
     - A SPARQL ``SELECT`` query that should return exactly two bound variables: ``id`` which should contain a unique subject
       and ``updated`` which should contain its modification time in ISO UTC format (or "0001-01-01T00:00:00Z" if not
       available in the data). If you would like the source to have continuation support, then you must include a filter based on the
       ``updated`` content compared to the current since moniker. You must use a variable expansion ``${since}`` for this
       purpose. The query result set should always be ordered by the "?updated" variable. If a list of strings is given,
       they will be converted to a single string by concatenation with the newline character.
     -
     - Yes

   * - ``fragment_query``
     - List<String> or String
     - A SPARQL ``CONSTRUCT`` query that should return all the relevant statements for a particular subject selected
       by the ``fragments_query`` query. The query should use the expansion variable "${uri}" to filter or select
       the correct subject to construct the statements to return.  If a list of strings is given, they will be
       converted to a single string by concatenation with the newline character.
     -
     - Yes

   * - ``since_default``
     - String
     - A string literal to use when querying the triplestore the first time.
     - "0001-01-01T00:00:00Z"
     -

Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Dynamic: ``true`` if ``${since}`` in ``fragments_query``)

   * - ``is_since_comparable``
     - ``true`` (Default)

   * - ``is_chronological``
     - ``false`` (Default)

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity.

::

    {
        "source": {
            "type": "sparql",
            "url": "http://localhost:8890/sparql",
            "fragments_query": [
                "PREFIX sdshare: <http://www.sdshare.org/2012/extension/>",
                "SELECT DISTINCT ?id ?updated WHERE {",
                 "    ?id sdshare:lastmodified ?updated",
                 "} FILTER (?updated >= \"${since}\"^^xsd:dateTime) ORDER BY ?updated",
            ],
            "fragment_query": [
                "CONSTRUCT { ?subject ?property ?value } WHERE {",
                "  ?subject ?property ?value .",
                "} FILTER (?subject = <${uri}>)",
            ]
        },
    }


.. _transform_section:

Transforms
==========

Transforms sit between the source and the sink. Entities passed from a
source to a sink, can optionally be passed through a chain of
transforms before they are passed on to the sink. This makes it
possible to reshape the entities on their way to the sink. Transforms
can also be used to filter entities and construct new entities.

Transforms can be configured on a pipe by specifying the
"``transform``" property. The field is optional, and can contain
either a transform configuration object or a list of them.

::

   {
       "_id": "mypipe",
       "name": "Name of pipe",
       "type": "pipe",
       ...
       "source": {
          ...
       },
       ..
       "transform": {
          "name": "name of transform (NOTE: deprecated)",
          "comment": "This is a comment",
          "description": "description of the transform (optional)"
           ...the rest of the transform configuration goes here...
       }
    }}



.. _dtl_transform:

The DTL transform
-----------------

This is a transform that lets you apply :doc:`Data Transformation Language <DTLReferenceGuide>`
transformations on the entities stream produced by the data source.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 3, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``rules``
     - Object
     - The named rules of the DTL transform. The ``default`` named rule is required and is the rule that will be applied on the source entity. The other rules can be applied via the :ref:`apply <apply_function>` and :ref:`apply-hops <apply_hops_function>` DTL functions.
     -
     - Yes

   * - ``id_required``
     - Boolean
     - If ``true`` then the DTL transform will fail if the target entity's ``_id`` property is either missing or is not a string. It will also do so if the arguments to :ref:`"create" <dtl_transform_create>` and  :ref:`"create-child" <dtl_transform_create_child>` is not a dict or is missing the ``_id`` property or the ``_id`` property is of a non-string type. If the value is ``false`` then it will not fail in these situation. Instead the values will be ignored.
     - ``true``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Pipe configuration that reads entities from the
``Northwind:Customers`` dataset and transforms them using the Data
Transformation Language before writing them to the
``customer-with-orders`` dataset.

::

   {
       "_id": "customer-with-orders",
       "name": "Customers with orders",
       "type": "pipe",
       "source": {
          "type": "dataset",
          "dataset": "Northwind:Customers"
       },
       "transform": {
           "type": "dtl",
           "rules": {
               "default": [
                   ["copy", "_id"],
                   ["add", "name", "_S.ContactName"],
                   ["add", "orders", ["apply", "order", ["hops", {
                       "datasets": ["Northwind:Orders o"],
                       "where": [
                           ["eq", "_S._id", "o.CustomerID"]
                       ]
                   }]]]
               ],
               "order": [
                   ["add", "order_id", "_S.OrderID"],
                   ["add", "order_date", "_S.OrderDate"]
               ]
           }
       }
   }


The JSON Schema validation transform
------------------------------------

A transform that validates entities against a `JSON Schema <http://json-schema.org/>`_ document.
If the document is valid then the field referenced by ``key_valid`` will be set to true, otherwise
false. Any validation error messages will be added to the field
referenced by ``key_errors``.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 3, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``schema``
     - Object
     - The JSON schema to validate entities against.
     -
     - Yes

   * - ``key_valid``
     - String
     - The field to store the validation result. This is a boolean value,
       which is true if the entity is valid, otherwise false.
     - ``"valid"``
     -

   * - ``key_errors``
     - String
     - The field to store the validation error messages. The error messages
       is a list of strings. The field is only added if the entity is invalid.
     - ``"errors"``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

   {
       "_id": "men-validated",
       "type": "pipe",
       "source": {
           "type": "dataset",
           "dataset": "men"
       },
       "transform": {
           "type": "json_schema",
           "schema": {
               "type" : "object",
               "properties" : {
                   "name" : {"type" : "string"},
                   "born" : {"type" : "string"}
               },
               "required": ["name", "born"]
           }
       }
   }

If the following entities where pushed through the pipe:

::

   [
    {"_id": "3",
     "name": "Jim"},
    {"_id": "5",
     "name": "Bob",
     "born": "1972-03-12"}
   ]

then these would come out:

::

   [
    {"_id": "3",
     "valid": false,
     "errors": [
       "'born' is a required property"
     ],
     "name": "Jim"},
    {"_id": "5",
     "valid": true,
     "name": "Bob",
     "born": "1972-03-12"}
   ]

.. _conditional_transform:

The conditional transform
-------------------------

The conditional transform selects an active transform based on a key typically controlled by an environment variable.
It is typically used in devops to be able to use the same configuration in different type of environments (i.e. development,
staging, production). The actual transform to use is resolved at runtime when the parent pipe is created.

The configuration options are:

Prototype
^^^^^^^^^

::

    {
       "type": "conditional",
       "condition": "$ENV(current-environment)",
       "alternatives": {
           "dev": {
               "type": "dtl",
               ..
           },
           "test": {
               "type": "dtl",
               ..
              },
           "prod": {
               "type": "dtl",
               ..
           }
       }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``condition``
     - String
     - The key to look up in ``alternatives`` for the actual transform to use at runtime. Typically an environment variable.
       Note that all possible enumerations of this value need to exist in ``alternatives``.
     -
     - Yes

   * - ``alternatives``
     - Object
     - A dictionary of actual transform configurations keyed by the enumerated value of ``condition``.
     -
     - Yes


.. _http_transform:

The HTTP transform
------------------

This transform performs `HTTP POST <https://en.wikipedia.org/wiki/POST_(HTTP)>`_ requests to a HTTP capable
endpoint. The service at the endpoint then transforms the entities contained in the request body and returns them in
the `HTTP response message <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Response_message>`_ .

The HTTP endpoint must accept ``application/json`` and the response must also be ``application/json``.

The endpoint must support lists of entities only, i.e. it should expect to receive a
`JSON array <https://en.wikipedia.org/wiki/JSON>`_ and it should always return a JSON array. If the endpoint returns
anything other than a "2xx Success" `HTTP status code <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>`_,
the transform will raise an exception.

The endpoint is free to decide how the entities are transformed. It'll just have to produce a list of zero or more
entities from the entities it was posted. This means that entities can be transformed, filtered out or new ones created.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 3, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`URL system <url_system>` or :ref:`microservice system <microservice_system>` component to use.
     -
     - Yes

   * - ``url``
     - Object
     - The URL to HTTP POST entities to.
     -
     - Yes

   * - ``batch_size``
     - Integer
     - The maximum number of entities to POST in each request. If there are
       more entities than this then they'll be split across multiple HTTP
       requests.
     - 100
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

  {
      "_id": "my-http-transform-service",
      "type": "system:url",
      "base_url": "http://localhost:8080/transforms/"
  },
  {
      "_id": "deduplicated-men",
      "type": "pipe",
      "source": {
          "type": "dataset",
          "dataset": "men"
      },
      "transform": {
          "type": "http",
          "system":"my-http-transform-service",
          "url": "http://localhost:8080/transforms/deduplicate",
          "batch_size": 5
      }

.. _lower_keys_transform:

The lower keys transform
------------------------

This transform transforms all the keys of an entity to lower case (optionally recursively).

Prototype
^^^^^^^^^

::

    {
        "type": "lower_keys",
        "recurse": false
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``recurse``
     - Boolean
     - An optional flag to indicate whether to do the case conversion recursively or not (default is false, which means
       no recursion).
     - false
     -

Example
^^^^^^^

With the default transform configuration:

::

    {
        "type": "lower_keys",
    }

And given the the input entity:

::

    {
        "_id": "http://psi.test.com/2",
        "Born": "1980-01-23",
        "CODE": "AB32",
        "Status": {
            "http://psi.foo.com/married": true,
            "Spouse": "Pam",
            "URL1": "~rhttp://www.foo.com",
            "URL2": "~rhttp://psi.foo.com/url2",
            "CODE": 123,
            "Child": {
                "t_c": "C",
                "http://psi.test.com/hello": "http://psi.foo.com/world",
                "http://psi.tests.com/S": "bye"
            }
        }
    }

The transform will output the following transformed entity:

::

    {
        "_id": "http://psi.test.com/2",
        "born": "1980-01-23",
        "code": "AB32",
        "status": {
            "http://psi.foo.com/married": true,
            "Spouse": "Pam",
            "URL1": "~rhttp://www.foo.com",
            "URL2": "~rhttp://psi.foo.com/url2",
            "CODE": 123,
            "Child": {
                "t_c": "C",
                "http://psi.test.com/hello": "http://psi.foo.com/world",
                "http://psi.tests.com/S": "bye"
            }
        }
    }

Note that only the root keys are transformed. If the ``recurse`` property is set to ``true`` in the configuration,
however, the result would instead become:

::

    {
        "_id": "http://psi.test.com/2",
        "born": "1980-01-23",
        "code": "AB32",
        "status": {
            "http://psi.foo.com/married": true,
            "spouse": "Pam",
            "url1": "~rhttp://www.foo.com",
            "url2": "~rhttp://psi.foo.com/url2",
            "code": 123,
            "child": {
                "t_c": "C",
                "http://psi.test.com/hello": "http://psi.foo.com/world",
                "http://psi.tests.com/s": "bye"
            }
        }
    }

The upper keys transform
------------------------

This transform transforms all the keys of an entity to upper case (optionally recursively).
The transform mirrors the :ref:`lower case transform <lower_keys_transform>` exactly except for the keys being
transformed to upper case. See previous section for details.

The undirected graph transform
------------------------------

The undirected graph transform transforms a list of properties representing nodes in a graph into all its
possible sets of edges, forming a complete graph. The transform will generate all possible edges in the
graph, which will be twice the number of entities as there are values in the aggregate of the list of properties given.
See the example section for an example.

Prototype
^^^^^^^^^

::

    {
        "type": "undirected_graph",
        "nodes": ["_id", "sameAs"],
        "from": "from-property",
        "to": "to-property"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``nodes``
     - List<String>
     - A list of entity property names that should be used to pick the nodes of the graph. The properties must refer
       to a value that is either a string or a URI, or a list of strings or URIs. No other value types are allowed in
       the transform.
     - ["_id", "sameAs"]
     -

   * - ``from``
     - String
     - The name of the property to use as "from" point in the generated entity for an edge in the graph.
     - "from"
     -

   * - ``to``
     - String
     - The name of the property to use as the "to" point in the generated entity for an edge in the graph.
     - "to"
     -

Example
^^^^^^^

Given the configuration:

::

    {
        "transform": [
           {
             "type": "undirected_graph",
             "nodes": ["_id", "map"],
             "from": "from",
             "to": "to"
           }
        ]
    }

And the input entity:

::

    {
       "_id": "foo",
       "map": ["bar", "zoo"]
    }

The transform will output the following edges of the graph as entities on its output stream:

::

   {
       "_id": "foo.bar",
       "from": "foo",
       "to": "bar"
   }

   {
       "_id": "foo.zoo",
       "from": "foo",
       "to": "zoo"
   }

   {
       "_id": "bar.foo",
       "from": "bar",
       "to": "foo"
   }

   {
       "_id": "bar.zoo",
       "from": "bar",
       "to": "zoo"
   }

   {
       "_id": "zoo.foo",
       "from": "zoo",
       "to": "foo"
   }

   {
       "_id": "zoo.bar",
       "from": "zoo",
       "to": "bar"
   }

.. _emit_children_transform:

The emit children transform
---------------------------

This transform will emit all child entities of its source
entities. All entities in the ``$children`` property that have an
``_id`` property will be emitted. The parent entity will not be
emitted.

Properties
^^^^^^^^^^

There are currently no properties on this transform.

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

  {
      "_id": "children",
      "type": "pipe",
      "source": {
          "type": "dataset",
          "dataset": "parents-with-children"
      },
      "transform": {
          "type": "emit_children"
      }


.. _xml_transform:

The XML transform
-----------------

This transform will render entities on the form described in the :ref:`XML endpoint sink <xml_endpoint_sink>` to a string and
embed it in the entity, which is then passed on to the transform chain.

Prototype
^^^^^^^^^

The properties are identical to the :ref:`XML endpoint sink <xml_endpoint_sink>`, except for the additional ``xml-property``:

::

    {
        "type": "xml",
        "root-attributes": {
           "xmlns": "http://www.example.org/ns1",
           "xmlsn:foo": "http://www.example.org/ns2",
           "xmlns:bar": "http://www.example.org/ns3"
        },
        "xml-property": "xml-property-to-use",
        "include-xml-decl": false,
        "skip-deleted-entities": true
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``root-attributes``
     - Object
     - An object containing the attributes to include on the root element. This is where you typically declare
       your namespaces, schema and so on.
     -
     -

   * - ``include-xml-decl``
     - Boolean
     - If set to ``true`` includes a default XML header: ``<?xml version="1.0" encoding="UTF-8" standalone="yes"?>``
     - false
     -

   * - ``xml-property``
     - String
     - The property that will hold any XML generated
     -
     - Yes

   * - ``skip-deleted-entities``
     - Boolean
     - This can be set to ``false`` to make deleted entities appear in the XML output. The default is that
       deleted entities does not appear.
     - true
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

This is how a XML transform would look like in the context of a pipe (source and sink configs omitted for brevity):

::

   {
       "_id": "my-pipe",
       "transform": {
           "type": "xml",
            "root-attributes": {
               "xmlns": "http://www.example.org/ns1",
               "xmlns:foo": "http://www.example.org/ns2"
            },
            "xml-property": "xml"
       }
   }

Given the input entity:

::

  {
    "_id": "1",
    "name": "Entity 1",
    "id": "entity-1",
    "<foo:tag>": [{
        "id": "child",
        "name": "Child entity",
        "<section>": [
          {"<from>": "0"},
          {"<to>": "999"}
        ]
    }]
  }

it will produce the transformed entity:

::

  {
    "_id": "1",
    "name": "Entity 1",
    "id": "entity-1",
    "<foo:tag>": [{
        "id": "child",
        "name": "Child entity",
        "<section>": [
          {"<from>": "0"},
          {"<to>": "999"}
        ]
    }],
    "xml": "<foo:tag xmlns=\"http://www.example.org/ns1\" xmlns:foo=\" .. </foo:tag>"
  }


.. _rdf_transform:

The RDF transform
-----------------

This transform will render entities to a N-Triples string and embed it in the entity, which is then passed on
to the transform chain.

Prototype
^^^^^^^^^

::

    {
        "type": "rdf",
        "rdf-property": "rdf-property-to-use"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``rdf-property``
     - String
     - The property that will hold any RDF generated
     -
     - Yes


Example configuration
^^^^^^^^^^^^^^^^^^^^^

This is how a RDF transform would look like in the context of a pipe (source and sink configs omitted for brevity):

::

   {
       "_id": "my-pipe",
       "transform": {
           "type": "rdf",
            "rdf-property": "rdf"
       }
   }

Given the input entity:

::

  {
    "_id": "x:1",
    "x:name": "Entity 1",
    "x:id": "entity-1",
    "foo:prop": [{
        "x:id": "child",
    }]
  }


And these namespaces in the metadata configuration:

::

    "namespaces": {
        "default": {
            "x": "http://x.org/",
            "foo": "http://foo.org/",
        }
    }


it will produce the transformed entity:

::

  {
    "_id": "x:1",
    "x:name": "Entity 1",
    "x:id": "entity-1",
    "foo:child": [{
        "x:id": "child",
    }]
    "rdf": "<http://x.org/1> <http://x.org/name> \"Entity 1\".\n<http://x.org/1> <http://x.org/id> \"entity-1\".\n<http://x.org/1> <http://foo.org/child> _:x1.\n_:x1 <http://x.org/id> \"child\".\n"
  }

.. _REST_transform:

The REST transform
------------------

This transform can communicate with a REST service using HTTP requests.

Note that the shape of the entities piped to this transform must conform to certain criteria, see the
:ref:`notes <rest_transform_expected_rest_entity_shape>` later in the section.

Also note that, in contrast to the REST sink, the REST transform also supports the GET operation.

Prototype
^^^^^^^^^

::

    {
        "type": "rest",
        "system" : "rest-system",
    }


Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req


   * - ``system``
     - String
     - The id of the :ref:`REST system <rest_system>` to use.
     -
     - Yes

   * - ``response-property``
     - String
     - The name of the property to store the result returned from the REST service. Note that if the ``replace-entity``
       property is set to ``true`` and the service returns JSON data, this JSON data will be returned as entities. If
       the data type is not JSON, the result will be an empty entity with the same ``_id`` as the original with
       the ``response-property`` set to the contents of the request reponse body as a string. If ``replace-entity`` is
       set to ``false``, the ``response-property`` will be added to the original entity and set to the contents of the
       request reponse body as a string or a parsed JSON structure if that is the returned content type.

     - ``"response"``
     -

   * - ``replace-entity``
     - Boolean
     - This property controls if the entity should be replaced with the JSON contents of the response or if the
       original entity should be kept. See the ``response-property`` for more detail on how this works. The default
       is to keep the original entity and add a ``reponse`` property holding the result of the REST operation.

     - ``false``
     -

   * - ``response-include-content-type``
     - Boolean
     - This property controls if the output entity should include the Content-Type of the response in a
       ``content-type`` property. Note that this property is ignored if ``replace-entity`` is set to ``true`` and
       the response is JSON.

     - ``false``
     -

.. _rest_transform_expected_rest_entity_shape:

Expected entity shape
^^^^^^^^^^^^^^^^^^^^^

The entities must be transformed into a particular form before being piped to the REST transform. The general form
expected is:

::

  {
    "_id": "1",
    "properties": {
        "foo": "bar",
        "zoo": 1,
        "baz": [1,2,3]
    },
    "operation": "some-named-operation",
    "payload": "<some>string-value</some>"
  }

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req


   * - ``properties``
     - Object
     - Any non-payload properties you need should go into the toplevel child entity ``properties``. You can then address
       these properties in the Jinja templates for operation ``url`` properties using the "{{ properties.key_name }}" syntax.
     -
     -

   * - ``operation``
     - String
     - The contents of this property must refer to one of the named ``operations`` registered with the transform's :ref:`REST system <rest_system>`.
     -
     - Yes

   * - ``payload``
     - String or Object
     - The payload for the operation specified. It can be a string or an object. You can also omit it, in which case
       the empty string will be used instead (for example for "DELETE" methods). All string payloads will be encoded
       as UTF-8.
     -
     -


Example entities:

String as payload:

::

  {
    "_id": "1",
    "properties": {
        "foo": "bar",
        "zoo": 1,
        "baz": [1,2,3]
    },
    "operation": "some-named-operation",
    "payload": "<some>string-value</some>"
  }

Object as payload (set operation ``payload-type`` to "json", "json-transit" or "form"  in the :ref:`REST system <rest_system>` the transform uses):

::

  {
    "_id": "2",
    "properties": {
        "foo": "bar",
        "zoo": 1,
        "baz": [1,2,3]
    },
    "operation": "some-other-operation",
    "payload": {
        "payload": "property",
        "child": {
          "foo": "bar"
        }
    }
  }

Multi-part form request if ``payload-type`` is "form", otherwise use "json" or "json-transit" for this type of entity:

::

  {
    "_id": "3",
    "operation": "some-third-operation",
    "payload": [
      {
        "foo": "bar"
      },
      {
        "zoo": "foo"
      }
    ]
  }

Example configuration
^^^^^^^^^^^^^^^^^^^^^

See the :ref:`REST system example <rest_system_example>` section for how to configure the operations we refer to in
these examples:

::

    {
        "type" : "pipe",
        "transform" : {
            "type" : "rest",
            "system" : "our-rest-service",
        }
    }

Example input entities:

::

    [
      {
          "_id": "bob",
          "operation": "get-man",
          "properties": {
              "collection_name": "study-group-1"
          }
      }
    ]


Example output entities:

::

    [
      {
          "_id": "bob",
          "operation": "get-man",
          "properties": {
              "collection_name": "study-group-1"
          },
          "response": {
              "name": "Bob Maker"
              "email": "bob.maker@example.com"
          }
      }
    ]

.. _sink_section:

Sinks
=====

Sinks are at the receiving end of pipes and are responsible for
writing entities into a internal dataset or a target system.

Sinks can support batching by implementing specific methods and
accumulating entities in a buffer before writing the batch. The size of
each batch can be specified using the ``batch_size`` property on the
pipe. See the section on :ref:`batching <pipe_batching>` for more
information.

Prototype
---------

The following *json* snippet shows the general form of a sink definition.

::

    {
        "type": "a-sink-type",
        "comment": "This is a comment",
        ..
    }

The only universally required property is ``type``.

Properties
----------

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``type``
     - String
     - The type of the sink, the allowed types are described below
     -
     - Yes

   * - ``comment``
     - String or list of strings
     - A human readable comment on the sink (optional).
     -
     -

.. _conditional_sink:

The conditional sink
--------------------

The conditional sink selects an active sink based on a key typically controlled by an environment variable.
It is typically used in devops to be able to use the same configuration in different type of environments (i.e. development,
staging, production). The actual sink to use is resolved at runtime when the parent pipe is created.

The configuration options are:

Prototype
^^^^^^^^^

::

    {
       "type": "conditional",
       "condition": "$ENV(current-environment)",
       "alternatives": {
           "dev": {
               "type": "null",
               ..
           },
           "test": {
               "type": "sql",
               ..
           },
           "prod": {
               "type": "sql",
               ..
           }
       }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``condition``
     - String
     - The key to look up in ``alternatives`` for the actual sink to use at runtime. Typically an environment variable.
       Note that all possible enumerations of this value need to exist in ``alternatives``.
     -
     - Yes

   * - ``alternatives``
     - Object
     - A dictionary of actual sink configurations keyed by the enumerated value of ``condition``.
     -
     - Yes


.. _dataset_sink:

The dataset sink
----------------

The dataset sink writes the entities it is given to an identified dataset. The configuration looks like:

Prototype
^^^^^^^^^

::

    {
        "type": "dataset",
        "dataset": "id-of-dataset"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``dataset``
     - String
     - The id of the dataset to write entities into. Note: if it doesn't exist before
       entities are written to the sink, it will be created on the fly.

       .. NOTE::

          The dataset id cannot contain forward slash characters (``/``) nor can it
          reference a ``system:`` dataset.
     -
     - Yes

   * - ``set_initial_offset``
     - Enum<String>
     - This property specifies when the sink should set the initial offset on its dataset.

       When the initial offset is set then the dataset is considered to be *populated*.

       - ``if-source-populated`` (the default) means that the pipe will set the initial offset
         when the source is populated and the pipe has consumed all the source entities. This
         is a very useful default as the populated flag will propagate automatically downstream once
         datasets get populated upstream.
       - ``never`` means that the pipe will never set the initial offset.
       - ``always`` means that the pipe will always set the initial offset when the pipe completed
         successfully.
       - ``initially`` means that the pipe will set the initial offset at the start of the pump run.
       - ``onload`` means that the initial offset will be set when the pipe is loaded / configured.

     - ``if-source-populated``
     -

   * - ``indexes``
     - String or Array
     - If set to ``"$ids"`` then an index on the ``$ids`` property will be automatically
       maintained. This index will then be used by the dataset browser to look up
       entities both by ``_id`` and ``$ids``.

       If the value is an array then it can contain index expressions that should be
       maintained on the sink dataset. This is typically used for declaring subset indexes.
     - ``[]``
     -

   * - ``track_children``
     - Boolean
     - If ``true`` then the ``$children`` property will be compared against the previous
       version of the entity and a delta produced. This will cause the ``$children``
       property to be updated on entities just before they are written to the dataset.

       This is a special feature that can be used in combination with the
       ``["create-child", ...]`` DTL function and the ``emit_children`` pipe transform.
       The purpose is to be able to detect deleted children entities when doing
       incremental syncs.

       The effective value of this property is inferred to be ``true``
       if any of the pipe's transforms use the ``create-child`` DTL
       function. It is possible to override this by setting the
       property's value to ``false``.
     - Inferred
     -

   * - ``enable_optimistic_locking``
     - Boolean
     - If ``true`` then the ``_updated`` property in each entity will be compared against the previous
       version of the entity. If the ``_updated`` property of at least one entity doesn't match, an error
       will raised and no entities will be written to the target dataset.

       The purpose is to be guard against two agents trying to update the same entity at the same time; in some
       cases one doesn't want the last edit to "win" automatically. The typical usecase is a pipe with a
       ``http_endpoint`` source where the http endpoint can be accessed by several independant processes
       that use the sesam instance as a storage service. In this case the pipe should *not* have any transforms,
       since the http_endpoint will send the resulting entity back to the calling process; if the entity has been
       transformed by DTL or some other transform, the result might make little sense to the calling process.

     - ``false``
     -

   * - ``circuit_breaker_threshold_factor``
     - Decimal
     - Specifying this property will enable a :ref:`circuit breaker <circuit_breakers_section>` on
       the pipe. It specifies a factor that is used to calculate the circuit breaker limit. Note
       that this is a factor and not a percentage, e.g. ``0.32`` means 32% and ``1.5`` means 150%.
       If the factor is ``0.5`` and the dataset already contains 100 entities, then the circuit
       breaker will trip if it sees more than 50 new entities.
     - ``null``
     - No

   * - ``circuit_breaker_threshold_count``
     - Integer
     - Specifying this property will enable a :ref:`circuit breaker <circuit_breakers_section>` on
       the pipe. The count specifies the circuit breaker limit directly. The limit defines how many
       new entities can be written to the dataset before the circuit breaker trips. If this property
       is set to ``100``, then 100 entities can be written before it trips.

       .. NOTE::

          If both ``circuit_breaker_threshold_factor`` and ``circuit_breaker_threshold_count`` are
          specified then the maximum value of those two are used as the circuit breaker limit. The
          count is in this case typically used to specify the lower limit.
     - ``null``
     - No

   * - ``deletion_tracking``
     - Boolean
     - If ``true`` (the default), then after a full run any entities that existed in the dataset before
       the run but that weren't seen during the run will be deleted.

       If ``false``, then any existing entities in the dataset will not be touched. This is only
       useful in very special circumstances.
     - ``true``
     - No

   * - ``bitset_commit_interval``
     - Integer
     - Specifies how often dataset bitsets and dataset compaction changes are written to disk. The higher the number the fewer writes, but at the cost of having to redo the work if the pipe fails before completion. The changes are always written to disk once the pipe completes.
     - ``1000000``
     - No

   * - ``prevent_multiple_versions``
     - Boolean
     - If ``true`` then the pipe will fail if a new version of an existing entity is attempted written to the sink dataset. This is useful if one wants to prevent multiple versions of the same entity to be written to the sink dataset.
     - ``false``
     - No

   * - ``suppress_filtered``
     - Boolean
     - The default value is ``false`` unless it is a full sync and the source is of type ``dataset`` and ``include_previous_versions`` is ``false`` [*]. The purpose of this property is to make it possible to opt-in or opt-out of a specific optimization in the pipe. The optimization is to suppress entities that are filtered out in a transform early so that they are not passed to the sink. This optimization should only be used when the pipe produces exactly one version per ``_id`` in the output. The optimization is useful when the pipe filters out a lot of entities.
     - ``false`` [*]
     - No

   * - ``max_entity_bytes_size``
     - Enum<String>
     - Defines the maximum size in bytes of an individual entity as it is stored in a dataset.
     - ``104857600`` (100MB)
     -


Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "dataset",
            "dataset": "Northwind:Customer",
        }
    }

.. _databrowser_sink:

The Sesam Databrowser sink
--------------------------

The databrowser sink writes the entities it is given to a Solr index
to be displayed by the Sesam Databrowser application. The input
entities are transformed to special Databrowser JSON documents before
being sent off for indexing.

This sink supports :ref:`batching <pipe_batching>`.

The configuration looks like:

Prototype
^^^^^^^^^

::

    {
        "type": "databrowser",
        "system": "solr-system-id",
        "batch_size": 100,
        "commit_within": null,
        "commit_at_end": true,
        "keep_existing_solr_ids": false,
        "maintain_id_links": false
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`Solr system <solr_system>` component to use.
     -
     - Yes

   * - ``batch_size``
     - Integer
     - The maximum number of documents to post to solr in one http request
     - 100
     -
   * - ``commit_within``
     - Integer
     - The number of seconds to wait until committing, i.e. invalidating the Solr
       caches. This is used to set up commit batching. The default is null
       (i.e. not set) which means that a commit will be issued at the end of the
       sync if ``commit_at_end`` is true. Do not set this too low as it will cause
       a lot of overhead on the Solr server.
     - null
     -

   * - ``commit_at_end``
     - Boolean
     - If true, then the sink will issue a commit at the end of the sync. In general
       it is best to rely on ``commit_within`` instead or just let the Solr server
       itself decide the commit interval.
     - true
     -

   * - ``keep_existing_solr_ids``
     - Boolean
     - This can be set to ``true`` in order to try to reuse the existing solr-id of an entity, even if
       the solr-ids of the entity no longer contains the solr-id that exists on the solr server.
       The cons of doing this is that it requires a http-request to solr for *each and every*
       entity, so it is *very* expensive. This option should therefore be set to false in
       cases where the id-problem is not likely to occur.
     - false
     -

   * - ``maintain_id_links``
     - Boolean
     - This can be set to ``true`` in order to maintain links to documents in the Solr index. If the current
       document doesn't exist in the solr index (via its ``id`` property), but there is a match in the ``ids`` property
       of some other document(s), this setting will force the new document to use ab existing id from the index.
       This makes sure any links to an existing document in the Solr index is kept (for example bookmarked documents).
       The option only has an effect if the ``keep_existing_solr_ids`` option is set to ``true``.
     - true
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "databrowser",
            "url": "http://localhost:8893/solr/my_index"
        }
    }

.. _json_push_sink:

The JSON push sink
------------------

The JSON push sink implements a simple HTTP based protocol where
individual entities or lists of entities are ``POSTed`` as JSON data
to an :ref:`HTTP endpoint <url_system>`.

The protocol is described in additional detail in the :doc:`JSON Push
Protocol <json-push>` document. The serialisation of entities as JSON
is described in more detail :doc:`here <entitymodel>`.

This sink is compatible with :ref:`The HTTP endpoint source
<http_endpoint_source>`.

This sink supports :ref:`batching <pipe_batching>`.

Prototype
^^^^^^^^^

::

    {
        "type": "json",
        "system": "url-system-id",
        "url": "url-to-http-endpoint",
        "headers": {
            "some-header": "some-value"
        },
        "batch_size": 100
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`URL system <url_system>` component to use.
     -
     - Yes

   * - ``url``
     - String
     - The full URL to HTTP service implementing the ``JSON push protocol`` described.
     -
     - Yes

   * - ``batch_size``
     - Integer
     - The maximum number of entities to POST in each request. If there are
       more entities than this then they'll be split across multiple HTTP
       requests.
     - 100
     -

   * - ``headers``
     - Dict<String,String>
     - A optional set of header values to set in HTTP request made using this sink. Both keys and values must
       evaluate to strings.
     -
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "json",
            "url": "http://localhost:9042/api/receivers/foo/entities"
        }
    }

An example using a custom "application/json" content-type header needed by some non-standard compliant servers:

::

    {
        "sink": {
            "type": "json",
            "url": "http://localhost:9042/api/receivers/foo/entities",
            "headers": {
                "content-type": "application/json; charset=UTF-8"
            }
        }
    }


.. _sdshare_push_sink:

The SDShare push sink
---------------------

The SDShare push sink is similar to the :ref:`JSON push sink <json_push_sink>`, but instead of posting JSON it
translates the inbound entities to ``RDF`` and ``POSTs`` them in N-Triples form to a :ref:`HTTP endpoint <url_system>`
implementing the ``SDShare push protocol``.

Prototype
^^^^^^^^^

::

    {
        "type": "sdshare",
        "system":"url-system-id",
        "url": "url-to-http-endpoint",
        "graph": "uri-of-graph-to-post-to"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`URL system <url_system>` component to use.
     -
     - Yes

   * - ``url``
     - String
     - The full URL to HTTP service implementing the ``SDShare push protocol``.
     -
     - Yes

   * - ``graph``
     - String
     - A URI representing a graph to post the ``RDF ntriples`` to
     -
     - Yes

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "sdshare",
            "url": "http://localhost:8001/sdshare_push_service"
        }
    }

.. _sms_message_sink:

The SMS message sink
--------------------

The SMS message sink is capable of sending ``SMS`` messages based on the entities it receives. The message to send can be
constructed either by inline templates or from templates read from disk. These templates are assumed to be ``Jinja``
templates (http://jinja.pocoo.org/) with the entities properties available to the templating context. The template file
name can either be inlined in the configuration or embedded in the input entity. The SMS service to use must be
configured separately as a :ref:`system <system_section>` and its ``_id`` property given in the ``system`` property.
Currently, only the :ref:`Twilio provider <twilio_system>` is supported.

Prototype
^^^^^^^^^

::

    {
        "type": "sms",
        "system": "sms-system-id",
        "body_template": "static jinja template as a string",
        "body_template_property": "id-of-property-for-body-template",
        "recipients": "static,comma,separated,list,of,international,phonenumbers",
        "recipients_property": "id-of-property-to-get-recipients-from",
        "from_number": "static-international-phone-number-to-use-as-from-number",
    }

Properties
^^^^^^^^^^

The configuration must contain at most one of ``body_template`` or ``body_template_property``:

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`Twilio provider <twilio_system>` component to use.
     -
     - Yes

   * - ``body_template``
     - String
     - Should contain a ``Jinja template`` to use for constructing messages. The template will have access to all entity properties by name.
     -
     - Yes

   * - ``body_template_property``
     - String
     - Should contain a ``id`` of a property of the incoming entity to use for looking up the ``Jinja template``
       (i.e for inlining the templates in the entities). It should not be used at the same time as ``body_template``
       or ``body_template_file*``
     - "body_template"
     -

   * - ``recipients``
     - String
     - Should contain a comma-separated list of internationalised phone-numbers to send the message constructed to.
       If this is not inlined in the entities via ``recipients_property`` (see below) the property is required.
     -
     - Yes

   * - ``recipients_property``
     - String
     - Should contain the id of the property to look up the recipients from the entity itself (i.e for inlining the
       recpients). If ``recipients`` (see abowe) is not specified, this property is mandatory and the propery
       referenced by it must exists and be valid for all entities.
     - "recipients"
     - Yes

   * - ``from_number``
     - String
     - An international phone number to use as the sender of all messages
     -
     - Yes

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity. The
examples assume a :ref:`system component <system_section>` (i.e. a :ref:`Twilio service <twilio_system>`) has been
configured earlier:

::

    {
        "sink": {
            "type": "sms",
            "system": "twilio_service",
            "body_template": "SMS message: {{ message_prop_id }}",
            "recipients": "+4799887766,+4788776655",
            "from_number": "+4766554433"
        }
    }

In the above example the entities sent to the sink should have at least a single property ``message_prop_id``, i.e.:

::

    {
        "_id": "message_id",
        "message_prop_id": "This is the message to send",
        "some_other_property": "Some other value"
    }

An example where the template to use is included in the entity written to the sink:

::

    {
        "sink": {
            "type": "sms",
            "system": "twilio_service",
            "body_template_property": "body_template_property_id",
            "recipients": "+4799887766,+4788776655",
            "from_number": "+4766554433"
        }
    }

For the example above the entities sent to the sink should have at least a single property ``body_template_property_id``
and it also needs to have the properties references in the embedded template:

::

    {
        "_id": "message_id",
        "body_template_property_id": "SMS message: {{ message_prop_id }}",
        "message_prop_id": "This is the message to send",
        "some_other_property": "Some other value"
    }

You can also store the Jinja templates on disk and reference them in the same way via filenames instead of embedding
the templates in config or the entities themselves.


.. _solr_sink:

The Solr sink
-------------

The Solr sink writes the entities it is given to a Solr index.

The ``_id`` property is used as the document id. All other properties,
except the ones at the root level matching ``_*`` or ``$*`` are added
to the document. Notice the limitations described in the next section.

This sink supports :ref:`batching <pipe_batching>`.

Limitations
^^^^^^^^^^^

Due to the limited document structure allowed by Solr, there are some
restrictions on the form of the entities accepted by the sink:

* Only "flat" entities are allowed - any child entities must be removed or merged into the root entity before being sent to the sink.
* Lists properties are supported, but they can only contain a single type of property.
* Lists cannot contain other lists or entities.

If the document does not adhere to these rules, then an error is raised.

Prototype
^^^^^^^^^

::

    {
        "type": "solr",
        "system": "solr-system-id",
        "commit_within": null,
        "commit_at_end": true
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`Solr system <solr_system>` component to use.
     -
     - Yes

   * - ``commit_within``
     - Integer
     - The number of seconds to wait until committing, i.e. invalidating the Solr
       caches. This is used to set up commit batching. The default is null
       (i.e. not set) which means that a commit will be issued at the end of the
       sync if ``commit_at_end`` is true. Do not set this too low as it will cause
       a lot of overhead on the Solr server.
     - null
     -

   * - ``commit_at_end``
     - Boolean
     - If true, then the sink will issue a commit at the end of the sync. In general
       it is best to rely on ``commit_within`` instead or just let the Solr server
       itself decide the commit interval.
     - true
     -


.. _elasticsearch_sink:

The Elasticsearch sink
----------------------

The Elasticsearch sink writes the entities it is given to an
Elasticsearch server/cluster.

The ``_id`` property is used as the document id. All other properties,
except the ones at the root level matching ``_*`` or ``$*`` are added
to the document.

If the input entity has the property ``$index`` then this is the index
into which the document is written. The ``$type`` property is used as
the document type. Note that default values for ``$index`` and
``$type`` can be specified on the :ref:`Elasticsearch system
<elasticsearch_system>`.

This sink supports :ref:`batching <pipe_batching>`.

Prototype
^^^^^^^^^

::

    {
        "type": "elasticsearch",
        "system": "elasticsearch-system-id",
        "default_index": null,
        "default_type": null
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`Elasticsearch system <elasticsearch_system>` component to use.
     -
     - Yes

   * - ``default_index``
     - String
     - The index to insert the documents into. This the default value for
       the ``$index`` property on the indexable entities. Note that this is
       overridable on each entity.
     - null
     -

   * - ``default_type``
     - String
     - The document type to use for the entities. This the default value for
       the ``$type`` property on the indexable entities. Note that this is
       overridable on each entity.
     - null
     -

.. _sparql_sink:


The SPARQL sink
---------------

The SPARQL sink converts entities to RDF statements and writes them to a graph in a triplestore via a SPARQL compatible
endpoint.

Prototype
^^^^^^^^^

::

    {
        "type": "sparql",
        "system": "id-of-url-system"
        "url": "sparql",
        "update_url": "sparql-update",
        "graph": "http://uri.of/graph",
        "do_diff": false,
        "write_sdshare_updated": true
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``url``
     - String
     - The URL part of the SPARQL endpoint to use, see the ``url_pattern`` property of the :ref:`URL system <url_system>`
       for how this is substituted into the System URL.
     -
     - Yes

   * - ``update_url``
     - String
     - The URL part of the SPARQL endpoint to use for updates if it is different from ``url``. See the ``url_pattern``
       property of the :ref:`URL system <url_system>` for how this is substituted into the System URL.
     -
     -

   * - ``system``
     - String
     - The id of a :ref:`URL system <url_system>` component to use. Note that only ``basic`` and ``digest``
       ``authentication`` schemes are supported by the SPARQL sink.
     -
     - Yes

   * - ``graph``
     - String
     - A full URI for the graph to write the entities into.
     -
     - Yes

   * - ``do_diff``
     - Boolean
     - Tell the sink to compute the difference between the target graph RDF statements and the RDF statements generated
       by converting the input entity to RDF. This ensures the minimum number of write operations to the endpoint.
       This does however come with the cost of (many) more read operations. Use this option if your entities are large
       and/or there is large amounts of changes flowing through the sink on average.
     - false
     -

   * - ``write_sdshare_updated``
     - Boolean
     - Tell the sink to automatically insert SDShare updated predicates with the generated RDF statements written to
       the endpoint. Note that the local UTC time is currently used for this timestamp.
     - true
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "sparql",
            "url": "http://virtuoso.example.com:8890/sparql",
            "graph": "http://example.com/fylketest",
            "do_diff": true,
            "write_sdshare_updated": true
    }

.. _sql_sink:

The SQL sink
------------

The `SQL <https://en.wikipedia.org/wiki/SQL>`_  sink writes entities to a
`relational database <https://en.wikipedia.org/wiki/Relational_database>`_ `table <https://en.wikipedia.org/wiki/Table_(database)>`_.
You will have to configure and provide a :ref:`SQL system <sql_system>` id in the ``system`` property.

The expected form of an entity to be written to the sink is:

::

    {
        "columnname1": value,
        "columnname2": another_value,
    }

This sink supports :ref:`batching <pipe_batching>`.

Note that identiy columns (columns with automatically assigned values) are currently not supported by the SQL sink, however
there is a potential :ref:`workaround <mssql-identity-columns>` for non-primary key identity columns for MS SQL based systems.

Prototype
^^^^^^^^^

::

    {
        "type": "sql",
        "system": "id-of-sql-system"
        "primary_key": ["list","of","key","names"],
        "table": "name-of-table",
        "schema": "default-schema-name-if-included",
        "batch_size": 100,
        "use_bulk_operations": false,
        "keep_failed_bulk_operation_files": false,
        "bulk_operation_timeout": 600,
        "bulk_operation_queue_size": 3,
        "schema_definition": [],
        "create_table_if_missing": false,
        "timestamp": "name-of-collumn-to-add-timestamp-into",
        "truncate_table_on_first_run": false
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`SQL system <sql_system>` component to use.
     -
     - Yes

   * - ``table``
     - String
     - Refers to a fully qualified table name in the database system, not including schema, which if needed must be
       set separately.
     -
     - Yes

   * - ``primary_key``
     - List<String> or String
     - The value of this property can be a single string with the name of the column
       that contains the ``primary key`` (PK) of the table, or a list of strings
       if it is a compound primary key. If the property is not set the component will
       attempt to use table metadata reflection to deduce the PK to use.
     -
     -

   * - ``schema``
     - String
     - If a specific schema within a database is needed, you must provide its name in this property.
       Do *not* use schema names in the ``table`` property.
     -
     -

   * - ``timestamp``
     - String
     - Defines a name of a property (column) that is added to each entity, containg a timestamp in UTC.
       If the corresponding column exist in the target table, the value will be written to that column.
     - ``sesam-timestamp``
     -

   * - ``use_bulk_operations``
     - Boolean
     - Some database types supports bulk upload of data. Bulk uploading is typically much faster than doing
       updates with ``INSERT`` and ``UPDATE`` SQL statements, but may not be feasible in all cases (some bulk
       operations requires Sesam to have extra permissions in the database, for instance). Only some
       sql systems supports bulk operations, see :ref:`the documentation of the SQL systems <sql_system>` for
       details.
     - ``false`` for now; will be changed to ``true`` at some future date.
     -

   * - ``keep_failed_bulk_operation_files``
     - Boolean
     - Bulk operations typically involve writing some temporary files to disk. These files are normally
       deleted when the bulk operation is finished, but while debugging a problem it can be useful to
       keep the files when the bulk operation failes. This option can be set to ``true`` to keep all the
       files that are relevant for the failing bulk operation. You have to have access to the server's
       harddisk in order to see the files (the location of the bulk-files is written in the node's log-file).
       Note: The files are written to a temporary folder, and are deleted the next time the node restarts.
     - ``false``
     -

   * - ``bulk_operation_timeout``
     - Integer
     - The maximum number of seconds to wait for a bulk operation to finish. This is only applicable if both
       ``truncate_table_on_first_run`` and ``use_bulk_operations`` is set to ``true`` (and the SQL system supports
       bulk operations). This value should be set to the maximum number of seconds a bulk operation is expected to
       use for a single batch. It will typically depend on both the size of the batches, the size of the data and the
       performance of the receiving RDBM system.
     - ``600``
     -

   * - ``bulk_operation_queue_size``
     - Integer
     - The maximum number of bulk operation batches to queue for upload at any given time. This shouldn't normally
       be changed from the default. Higher numbers will consume more disk space.
     - ``3``
     -

   * - ``bulk_operation_buffer_size``
     - Integer
     - The maximum number of bytes of the temporary bulk file to be held in memory before flushing it to disk.
       You should not normally change this value. A higher value will consume more memory. If it set too high, it might
       result in the system running out of memory. If it is set too low, it might slow down the writing of the temporary bulk
       file resulting in poor performance. The default is 50 Mb.
     - ``50000000``
     -

   * - ``batch_size``
     - Integer
     - The maximum number of rows to insert into the database table in one operation
     - ``1000`` or ``use_bulk_operations`` is ``true``, ``100`` otherwise.
     -

   * - ``truncate_table_on_first_run``
     - Boolean
     - A flag that indicates that the target table should be truncated/emptied the first time a pump runs
       (for example on the first run, or when its offset has been set to zero manually). Please note that
       the truncating operation is executed in a separate transaction, so if any subsequent inserts should fail
       the truncating operation will not be rolled back.

       Note: combining this option with ``use_bulk_operations`` enables the sink to do a direct bulk copy operation to the
       target table on first run, which is much faster than using a temporary table which is the default method.
     - ``false``
     -

   * - ``create_table_if_missing``
     - Boolean
     - A flag that indicates that the target table should be created if it is missing the first time a pump runs
       (for example on the first run, or when its offset has been set to zero manually). If this property is ``true``
       then a proper schema definition must be supplied in the ``schema_definition`` property. Note that this property
       requires that the user defined in the :ref:`SQL system <sql_system>` have the necessary privileges to create and drop
       tables in the target database/schema.
     - ``false``
     -

   * - ``recreate_table_on_first_run``
     - Boolean
     - If combined with ``create_table_if_missing`` this property will make the sink drop and then recreate the table
       on the first run, or if the pipe is reset (based on the information in ``schema_definition`` which must also be
       provided).
     - ``false``
     -

   * - ``schema_definition``
     - List<Object>
     - A list of column definitions that guides the sink when creating a new table when the ``create_table_if_missing``
       is set to ``true``. See :ref:`SQL sink schema definition format <sql_sink_schema_definition_format>` for more
       details on how this element works.
     -
     -

   * - ``whitelist``
     - List<String>
     - Deprecated. The names of the properties (columns) to include when inserting rows into the target tablke. If there is a
       ``blacklist`` also specified, the whitelist will be filtered against the contents of the blacklist.
     -
     -


   * - ``blacklist``
     - List<String>
     - Deprecated. The names of the properties (columns) to exclude from inserts into the target table. If you are looking
       for a way to filter out identity columns, there exists a :ref:`workaround <mssql-identity-columns>` for MS SQL based systems.
     -
     -


Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "sql",
            "system": "my-sql-system",
            "table": "customers"
        }
    }


SQL sink schema definition format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _sql_sink_schema_definition_format:

The schema definition format consists of a list of objects for each property that exists in the input entities. These
objects are in essence column definitions and correspond directly to columns in the target table. The initial schema
definition can be generated from analysing the entities produced by the pipe the sink belongs to by using the API or
in the management studio. After being generated it can then be manually edited or augmented.

If the entities in the source dataset changes shape, or you change the shape of the entities produced by the pipe
by adding (or editing existing) DTL transforms attached to it, you may need to regenerate (or manually update) the
schema definition accordingly.

If the schema definition does not match the shape or value ranges of the entities that the sink is attempting to
insert (or update) in the resulting table, the sink will generate run time errors in the pump execution log.

Each object is on the form:

::

    {
        "source_property": "name_of_property",
        "name": "name_of_column",
        "type": "string|integer|decimal|float|bytes|datetime|date|time|uuid|boolean",
        "max_size|max_value": 1234,
        "min_size|min_value": 1234,
        "precision": 10,
        "scale": 2,
        "allow_null": true|false,
        "primary_key": true|false,
        "index": true|false,
        "default": "default-value"
    }


The ``name`` property must correspond to a column in the target table and the ``source_property`` is the corresponding
property in the entity. In the case of the ``primary_key`` set to ``true`` and/or ``allow_null`` set to ``false``,
the property must exist in all entities. Note that at least one column definition in the schema definition list must
have ``primary_key`` set to ``true``. If you edit the ``name`` property, you must take care that it is an exact,
case-sentitive match with the definiton in the schema for the table.

The ``type`` property is automatically mapped to the appropriate target RDBMS column type, based on the information
in the ``max_size``/``max_value`` and ``min_size``/``min_value`` properties. For example, an ``integer`` type may
translate to a ``bigint`` if the value range is outside +-2^31 (i.e larger than 32 bits) or a ``tinyint`` if it fits within
a unsigned byte range (0..255). The translation table for the currently supported systems is listed below.

If the ``index`` property for a column definition is set to ``true``, the table creation will add a default type
of index to the column for the particular target RDBMS system.

The ``precision`` and ``scale`` properties are valid only for ``decimal`` type columns and define the total number
of digits and the fractional digits respectively. I.e. the decimal number "10.3" would have a ``precision`` of "3"
and an ``scale`` of "1".

The optional ``default`` property contains what value to use if the property is not present in the entity. If a
default value for a particular column has been set in the table schema, this value should match the schema value.


Translation table for the :ref:`Microsoft SQL server <mssql_system>` and :ref:`Microsoft Azure SQL Data Warehouse server <mssql-azure-dw_system>`:


.. list-table::
   :header-rows: 1
   :widths: 20, 20, 20, 30

   * - Type
     - Range/size
     - Column type
     - Comment

   * - ``string``
     - <= 8000
     - nvarchar(size)
     - Unicode

   * - ``string``
     - > 8000
     - nvarchar(MAX)
     - Unicode

   * - ``bytes``
     - <= 8000
     - varbinary(size)
     -

   * - ``bytes``
     - > 8000
     - varbinary(MAX)
     -

   * - ``integer``
     - -9223372036854775808 - 9223372036854775808
     - integer
     - 64 bit/8 bytes

   * - ``integer``
     - -2147483648 - 2147483647
     - int
     - 32 bit/4 bytes

   * - ``integer``
     - -32768 - 32768
     - smallint
     - 16 bit/1 word/2 bytes

   * - ``integer``
     - 0 - 255
     - tinyint
     - 8 bit/1 byte

   * - ``decimal``
     - Any
     - decimal(precision,scale)
     -

   * - ``float``
     - 53 bit precision
     - float
     - Double precision IEEE-754 number

   * - ``datetime``
     - 0001-01-01T00:00:00.000000Z - 9999-12-31T23:59:59.999999Z
     - datetime2
     -

   * - ``date``
     - 0001-01-01 - 9999-12-31
     - date
     - Coerced from ``datetime`` values or pre-formatted strings

   * - ``time``
     - 00:00:00.000000 - 23:59:59.999999
     - time
     - Coerced from ``datetime`` values or pre-formatted strings

   * - ``boolean``
     - true | false
     - bit
     - Coerced to ``0`` or ``1``

   * - ``uuid``
     - Any valid UUID
     - uniqueidentifier
     - Preformatted strings on the format ``xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`` can also be used


.. _mail_message_sink:

The Email Message sink
----------------------

The mail message sink is capable of sending mail messages based on the entities it receives. The message to send can be
constructed either by inline templates or from templates read from disk. These templates are assumed to be ``Jinja
templates`` (http://jinja.pocoo.org/) with the entities properties available to the templating context. The template file
name can either be embedded in the configuration or in the input entity. The mail server settings have to
be registered in a :ref:`SMTP system <smtp_system>` component in advance and its ``_id`` put in the ``system``
property of the sink.

Prototype
^^^^^^^^^

::

    {
        "type": "mail",
        "system": "smtp-system-id",
        "body_template": "static jinja template as a string",
        "body_template_property": "id-of-property-to-get-as-a-body-template",
        "text_body_template": "static text only jinja template as a string",
        "text_body_template_property": "id-of-property-to-get-as-a-text-body-template",
        "subject_template": "static jinja template as a string",
        "subject_template_property": "id-of-property-to-get-as-a-subject-template",
        "recipients": "static,comma,separated,list,of,email,addresses",
        "recipients_property": "id-of-property-to-get-recipients-from",
        "mail_from": "static@email.address"
    }

Properties
^^^^^^^^^^

The configuration must contain at most one of ``body_template`` or ``body_template_property``. The same applies to
``subject_template`` and ``subject_template_property``.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``system``
     - String
     - The id of the :ref:`SMTP system <smtp_system>` to use.
     -
     - Yes

   * - ``body_template``
     - String
     - Should contain a ``Jinja template`` to use for constructing messages. The template will have access to all entity properties by name.
     -
     - Yes

   * - ``body_template_property``
     - String
     - Should contain a ``id`` of a property of the incoming entity to use for looking up the ``Jinja template``
       (i.e for inlining the templates in the entities). It should not be used at the same time as ``body_template``.
     - "body_template"
     -

   * - ``subject_template``
     - String
     - Should contain a ``Jinja template`` to use for constructing subjects for the email messages. The template
       will have access to all entity properties by name
     -
     - Yes

   * - ``subject_template_property``
     - String
     - Should contain a ``id`` of a property of the incoming entity to use for looking up the ``Jinja template``
       (i.e for inlining the templates in the entities). It should not be used at the same time as ``subject_template``.
     - "subject_template"
     -

   * - ``text_body_template``
     - String
     - Should contain a ``Jinja template`` to use for constructing plain-text messages. The template will have access to all entity properties by name.
     -
     -

   * - ``text_body_template_property``
     - String
     - Should contain a ``id`` of a property of the incoming entity to use for looking up the ``Jinja template``
       (i.e for inlining the templates in the entities) used to construct plain text messages. It should not be used at the same time as ``text_body_template``
     - "text_body_template"
     -

   * - ``recipients``
     - String
     - Should contain a comma-separated list of email addresses to send the message constructed to. If this is not
       inlined in the entities via ``recipients_property`` (see below) this property is mandatory.
     -
     - Yes

   * - ``recipients_property``
     - String
     - Should contain the id of the property to look up the recpients from the entity itself (i.e for inlining the
       recpients). If ``recipients`` (see abowe) is not specified, this property is mandatory and the propery
       referenced by it must exists and be valid for all entities.
     - "recipients"
     -

   * - ``mail_from``
     - String
     - An email address to use as the sender of all messages
     -
     - Yes

   * - ``unhandled_template_variable_replacement``
     - String
     - Specifies how unhandled variables in the templates are handled. debug: the '{{variable_name}}'-string is kept.
       empty_string: {{variable_name}} is replaced with an empty string. strict: an error is raised.
       The default is 'debug'.
     - "debug"
     -



Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "mail",
            "system": "our-smtp-server",
            "body_template": "Mail message body: {{ message_prop_id }}",
            "subject_template": "Subject: {{ subject_prop_id }}",
            "recipients": "foo@bar.com,info@example.com",
            "mail_from": "all@of.us"
        }
    }

In the above example the entities sent to the sink should have at least the properties ``subject_prop_id`` and ``message_prop_id``, i.e.:

::

    {
        "_id": "message_id",
        "message_prop_id": "This is the message to send",
        "subject_prop_id": "This is the subject of the message to send",
        "some_other_property": "Some other value"
    }

A note on multi-part messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To send multi-part email messages containing both a HTML and a plain-text version, you should provide templates for both
``body_template`` (or ``body_template_property``) and ``text_body_template`` (or ``text_body_template_property``).
The former should then contain your HTML message and the latter your plain-text version. If you omit the ``text_*``
properties and the body template contains HTML, the sink will attempt to extract a text-only version of the HTML
on a best-effort basis; i.e. this might not preserve the information contained in the HTML in the desired way.

The null sink
-------------

The null sink is the equivalent of the empty data source; it will discard any entities written to it and do nothing (it
never raises an error):

Prototype
^^^^^^^^^

::

    {
        "type": "null"
    }

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

::

    {
        "sink": {
            "type": "null"
        }
    }


.. _http_endpoint_sink:

The HTTP endpoint sink
----------------------

This is a special data sink that registers an HTTP publisher endpoint
that one can get entities from.

A pipe that references the ``HTTP endpoint`` sink will not pump any
entities, in practice this means that a pump is not configured for the
pipe; the only way for entities to flow through the pipe is by
retrieving them from the HTTP endpoint.

It exposes these URLs:

.. list-table::
   :header-rows: 1
   :widths: 50, 60

   * - URL
     - Description

   * - ``http://localhost:9042/api/publishers/mypipe/entities``
     - JSON entities endpoint

   * - ``http://localhost:9042/api/publishers/mypipe/entities/some_filename.json``
     - JSON entities endpoint - filename in URL variant

   * - ``http://localhost:9042/api/publishers/mypipe/sdshare-collection``
     - SDShare collections feed

   * - ``http://localhost:9042/api/publishers/mypipe/sdshare-fragments``
     - SDShare fragments feed

The serialisation of entities as JSON is described in more detail
:doc:`here <entitymodel>`. This endpoint is compatible with :ref:`The
JSON source <json_source>`.

Note that any URL parameters given to these endpoints are bound to a DTL variable named ``_B``
and is available to any DTL transform on the pipe in which the endpoint sink is a part, see
:ref:`DTL Variables <variables>` for more details.

The SDShare protocol is described `here
<http://www.sdshare.org/spec/sdshare-v1.0.html>`__.

The exposed URLs may support additional parameters such as ``since`` and ``limit`` - see
the `API reference <./api.html#get--publishers-pipe_id-sdshare-collection>`__ for the full details.

Prototype
^^^^^^^^^

::

    {
        "type": "http_endpoint"
    }


Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``filename``
     - String
     - This property provides a hint to HTTP clients on what filename to use when downloading data (via the
       ``Content-Disposition`` header property). Note that this property is not entirely standardized yet, so to be
       compatible with most HTTP clients, the filename should be ASCII characters only. For the same reason, quotes or
       backward or forward slashes should be avoided. If this property is not set, the contents will be served inline.
     -
     -

   * - ``content_disposition``
     - String
     - This property provides a hint to HTTP clients how to render the file data. The valid values are ``attachment``
       and ``inline``. It is used in the ``Content-Disposition`` header and the behaviour is client specific.
     - ``attachment``
     -


Example configuration
^^^^^^^^^^^^^^^^^^^^^

The pipe configuration given below will expose the ``my-entities``
publisher endpoint and read the entities from the ``my-entities``
dataset::


    {
        "_id": "my-entities",
        "name": "My published entities endpoint",
        "type": "pipe",
        "sink": {
            "type": "http_endpoint"
        }
    }


.. _csv_endpoint_sink:


The CSV endpoint sink
---------------------

This is a data sink that registers an HTTP publisher endpoint that one can get entities in
`CSV format <https://en.wikipedia.org/wiki/Comma-separated_values>`_ from.

A pipe that references the ``CSV endpoint`` sink will not pump any
entities. In practice this means that a pump is not configured for the
pipe; the only way for entities to flow through the pipe is by
retrieving them from the CSV endpoint using a client that supports the HTTP protocol.

It exposes the URLs:

.. list-table::
   :header-rows: 1
   :widths: 100

   * - URL

   * - ``http://localhost:9042/api/publishers/mypipe/csv``
   * - ``http://localhost:9042/api/publishers/mypipe/csv/some_filename.csv``

The exposed URL may support additional parameters such as ``since`` and ``limit`` - see
the `API reference <./api.html#get--publishers-pipe_id-csv>`__ for the full details.

Note that you can optionally specify the filename to use in the ``Content-Disposition`` header of the HTTP response as
the last path element of the URL.

Prototype
^^^^^^^^^

::

    {
        "type": "csv_endpoint",
        "columns": ["properties","to","use","as","columns"],
        "quoting": "all|minimal|non-numeric|"none",
        "delimiter": ","
        "doublequote": true
        "include_header": true,
        "escapechar": null,
        "lineterminator": "\r\n",
        "quotechar": "\"",
        "encoding": "utf-8",
        "skip-deleted-entities": true,
        "filename": "my_data.csv",
        "content_disposition": "attachment"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``columns``
     - List<String>
     - A list of string keys to look up in the entity to construct the CSV columns. If ``include_header`` is set to
       ``true`` (which is the default), this list will also be included as the first line of the CSV file.
     -
     - Yes

   * - ``quoting``
     - Enum<String>
     - A string from the set of "all", "minimal", "non-numeric" and "none" that describes how the fields of the CSV
       file will be quoted. A value of "all" means all fields will be quoted, even if they don't contain the ``quotechar``
       or ``delimiter`` characters. A value of "non-numeric" means all non-numeric values will be quoted. The "minimal"
       setting (the default) means only fields with contents that need to be quoted will be quoted. Finally, the ``none``
       value means do not quote (note this can produce broken CSV files if there are values that have to be quoted).
     - ``"minimal"``
     -

   * - ``delimiter``
     - String
     - The character to use as field separator. It will also affect which fields will be quoted if the ``quoting`` setting
       is set to ``minimal"`` (which is the default). The default value is to use the comma (``","``) character.
     - ``","``
     -

   * - ``doublequote``
     - Boolean
     - Controls how instances of ``quotechar`` appearing inside a field should themselves be quoted. When set to
       ``true`` (the default), the character is doubled (repeated). When set to ``false``, the ``escapechar`` property
       setting is used as a prefix to the ``quotechar``. If ``doublequoting`` is set to ``true` but ``escapechar`` is
       not set, the backward slash character (``\``) is used as prefix.
     - ``true``
     -

   * - ``include_header``
     - Boolean
     - Controls if the ``columns`` property should be included as the header of the CSV file produced.
     - ``true``
     -

   * - ``escapechar``
     - String
     - A one-character string used by the sink to escape ``delimiter`` characters in fields if ``quoting`` is set to
       ``none`` and the ``quotechar`` if ``doublequote`` is set to ``false``. The default is ``null`` which disables
       escaping (except if ``doublequote`` is set to ``true``, in which case the default is ``\``).
     - ``null``
     -

   * - ``lineterminator``
     - String
     - A character sequence to use as the EOL marker in the CSV output. The default is carriage return plus linefeed
       (``"\r\n"``).
     - ``"\r\n"``
     -

   * - ``quotechar``
     - String
     - A one-character string that controls how to quote field values. The default is the double quote character. See
       ``doublequote`` and ``escapechar`` for related settings.
     - ``"\""``
     -

   * - ``encoding``
     - String
     - Which encoding to use when converting the output to string values. The default is ``utf-8``. See
       `section 7.2.3 on this page <https://docs.python.org/3/library/codecs.html#codec-base-classes>`_ for a list of
       valid values.
     - ``"utf-8"``
     -
      .. _csv_endpoint_sink_param_skip_deleted_entities:

   * - ``skip-deleted-entities``
     - Boolean
     - This can be set to ``false`` to make deleted entities appear in the CSV output. The default is that
       deleted entities does not appear. If you set this to ``true`` you will also most likely want to include
       the "_deleted" attribute in the ``columns`` list, so that rows that represents deleted entities can be
       recognized. (If you need to rename or reformat the "_deleted" attribute you can do that by adding a
       :ref:`DTL transform <dtl_transform>` to the pipe.)
     - ``true``
     -

   * - ``filename``
     - String
     - This property provides a hint to HTTP clients on what filename to use when downloading data (via the
       ``Content-Disposition`` header property). Note that this property is not entirely standardized yet, so to be
       compatible with most HTTP clients, the filename should be ASCII characters only. For the same reason, quotes or
       backward or forward slashes should be avoided. If this property is not set, the contents will be served inline.
     -
     -

   * - ``content_disposition``
     - String
     - This property provides a hint to HTTP clients how to render the file data. The valid values are ``attachment``
       and ``inline``. It is used in the ``Content-Disposition`` header and the behaviour is client specific.
     - ``"attachment"``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The pipe configuration given below will expose the ``my-entities``
publisher endpoint and read the entities from the ``my-entities``
dataset, picking the ``_id``, ``foo`` and ``bar`` properties as columns in the CSV file:

::

    {
        "_id": "my-entities",
        "name": "My published csv endpoint",
        "type": "pipe",
        "sink": {
            "type": "csv_endpoint"
            "columns": ["_id", "foo", "bar", "zoo"],
            "filename": "my_data.csv"
        }
    }

The data will be available at ``http://localhost:9042/api/publishers/my-entities/csv`` (or alternatively
``http://localhost:9042/api/publishers/my-entities/csv/some_other_filename.csv``)


.. _xml_endpoint_sink:

The XML endpoint sink
---------------------

This is a data sink that registers an HTTP publisher endpoint
that one can get the entities in XML format from.

A pipe that references the ``XML endpoint`` sink will not pump any
entities; the only way for entities to flow through the pipe is by retrieving them from the endpoint using the HTTP protocol.

It exposes the URL:

.. list-table::
   :header-rows: 1
   :widths: 100

   * - URL

   * - ``http://localhost:9042/api/publishers/mypipe/xml``
   * - ``http://localhost:9042/api/publishers/mypipe/xml/some_filename.xml``

Note that the shape of the entities must conform to certain criteria, see the :ref:`notes <expected_xml_entity_shape>`
later in the section.

The exposed URL may support additional parameters such as ``since`` and ``limit`` - see
the `API reference <./api.html#get--publishers-pipe_id-xml>`_ for the full details.

Note that you can optionally specify the filename to use in the ``Content-Disposition`` header of the HTTP response as
the last path element of the URL.

Prototype
^^^^^^^^^

::

    {
        "type": "xml_endpoint",
        "wrapper": "wrapper-tag",
        "root-attributes": {
           "xmlns": "http://www.example.org/ns1",
           "xmlsn:foo": "http://www.example.org/ns2",
           "xmlns:bar": "http://www.example.org/ns3"
        },
        "include-xml-decl": false,
        "skip-deleted-entities": true,
        "filename": "my_data.xml"
        "content_disposition": "attachment"
    }


Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``wrapper``
     - String
     - If included, the XML produced from all entities will wrapped in a single top level tag with the value
       of this property (``<wrapper-value>..entity-tags..</wrapper-value>``)
     -
     -

   * - ``root-attributes``
     - Object
     - An object containing the attributes to include on the root element (i.e. on the ``wrapper`` tag if it is defined,
       or on the tag defined on the first entity level). This is where you typically declare your namespaces, schema
       and so on.
     -
     -

   * - ``include-xml-decl``
     - Boolean
     - If set to ``true`` includes a default XML header: ``<?xml version="1.0" encoding="UTF-8" standalone="yes"?>``
     - false
     -

   * - ``skip-deleted-entities``
     - Boolean
     - This can be set to ``false`` to make deleted entities appear in the XML output. The default is that
       deleted entities does not appear.
     - true
     -

   * - ``filename``
     - String
     - This property provides a hint to HTTP clients on what filename to use when downloading data (via the
       ``Content-Disposition`` header property). Note that this property is not entirely standardized yet, so to be
       compatible with most HTTP clients, the filename should be ASCII characters only. For the same reason, quotes or
       backward or forward slashes should be avoided. If this property is not set, the contents will be served inline.
     -
     -

   * - ``content_disposition``
     - String
     - This property provides a hint to HTTP clients how to render the file data. The valid values are ``attachment``
       and ``inline``. It is used in the ``Content-Disposition`` header and the behaviour is client specific.
     - ``attachment``
     -


.. _expected_xml_entity_shape:

Expected entity shape
^^^^^^^^^^^^^^^^^^^^^
The entities must be transformed into a particular form before being piped to the XML endpoint sink. The general form
expected is:

::

  {
    "_id": "1",
    "name": "Entity 1",
    "id": "entity-1",
    "<foo:tag>": [{
        "id": "child",
        "name": "Child entity",
        "<section>": [
          {"<from>": "0"},
          {"<to>": "999"}
        ]
    }]
  }

There must be exactly one property starting with '<' and ending with '>' in an entity, although it can contain
child entities in as many levels as you want (also in lists).

All non-tag properties, except those beginning with a ``_`` letter will be included as attribute values on the tag
specified. A "tag"-property value can either be a single literal, a single object or a list of objects. Note that
any non-object items in lists are ignored (i.e. lists, literals and null values).

The property names must be valid XML attribute or tag names (`QNames <https://en.wikipedia.org/wiki/QName>`_).
All literal values in tags or attributes will be `XML escaped <https://www.liquid-technologies.com/XML/EscapingData.aspx>`_.

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The pipe configuration given below will expose the ``my-entities`` publisher endpoint and read the entities from the ``my-entities``
dataset:

::

  {
     "sink": {
         "type": "xml_endpoint",
         "wrapper": "baz",
         "root-attributes": {
            "xmlns": "http://www.example.org/ns1",
            "xmlsn:foo": "http://www.example.org/foo",
            "xmlns:xsi": "http://www.w3.org/2000/10/XMLSchema-instance",
            "xsi:schemaLocation": "http://example.com/myschema.dtd",
            "zoo": "bar"
         },
         "filename": "example.xml"
     }
  }

The following output will be produced (here reformatted/pretty-printed):

::

    <baz xmlns="http://www.example.org/ns1"
         xmlns:foo="http://www.example.org/foo"
         xmlns:xsi="http://www.w3.org/2000/10/XMLSchema-instance"
         xsi:schemaLocation="http://example.com/myschema.dtd"
         zoo="bar">
      <foo:tag name="Entity 1"
               id="entity-1">
         <section id="child"
                  name="Child entity">
            <from>0</from>
            <to>999</to>
         </section>
      </foo:tag>
    </baz>

The XML document will be available at ``http://localhost:9042/api/publishers/my-entities/xml``  (or alternatively
``http://localhost:9042/api/publishers/my-entities/xml/some_other_filename.xml``)

.. _rest_sink:

The REST sink
-------------

This is a data sink that can communicate with a REST service using HTTP requests.

Note that the shape of the entities piped to this sink must conform to certain criteria, see the
:ref:`notes <rest_expected_rest_entity_shape>` later in the section.

Prototype
^^^^^^^^^

::

    {
        "type": "rest",
        "system" : "rest-system",
    }


Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req


   * - ``system``
     - String
     - The id of the :ref:`REST system <rest_system>` to use.
     -
     - Yes

.. _rest_expected_rest_entity_shape:

Expected entity shape
^^^^^^^^^^^^^^^^^^^^^

The entities must be transformed into a particular form before being piped to the RESTsink. The general form
expected is:

::

  {
    "_id": "1",
    "properties": {
        "foo": "bar",
        "zoo": 1,
        "baz": [1,2,3]
    },
    "operation": "some-named-operation",
    "payload": "<some>string-value</some>"
  }

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req


   * - ``properties``
     - Object
     - Any non-payload properties you need should go into the toplevel child entity ``properties``. You can then address
       these properties in the Jinja templates for operation ``url`` properties using the "{{ properties.key_name }}" syntax.
     -
     -

   * - ``operation``
     - String
     - The contents of this property must refer to one of the named ``operations`` registered with the sink's :ref:`REST system <rest_system>`.
     -
     - Yes

   * - ``payload``
     - String or Object
     - The payload for the operation specified. It can be a string or an object. You can also omit it, in which case
       the empty string will be used instead (for example for "DELETE" methods). All string payloads will be encoded
       as UTF-8.
     -
     -


Example entities:

String as payload:

::

  {
    "_id": "1",
    "properties": {
        "foo": "bar",
        "zoo": 1,
        "baz": [1,2,3]
    },
    "operation": "some-named-operation",
    "payload": "<some>string-value</some>"
  }

Object as payload (set operation ``payload-type`` to "json", "json-transit" or "form"  in the :ref:`REST system <rest_system>` the sink uses):

::

  {
    "_id": "2",
    "properties": {
        "foo": "bar",
        "zoo": 1,
        "baz": [1,2,3]
    },
    "operation": "some-other-operation",
    "payload": {
        "payload": "property",
        "child": {
          "foo": "bar"
        }
    }
  }

Multi-part form request if ``payload-type`` is "form", otherwise use "json" or "json-transit" for this type of entity:

::

  {
    "_id": "3",
    "operation": "some-third-operation",
    "payload": [
      {
        "foo": "bar"
      },
      {
        "zoo": "foo"
      }
    ]
  }

Example configuration
^^^^^^^^^^^^^^^^^^^^^

See the :ref:`REST system example <rest_system_example>` section for how to configure the operations we refer to in
these examples:

::

    {
        "type" : "pipe",
        "sink" : {
            "type" : "rest",
            "system" : "our-rest-service",
        }
    }

Example input entities:

::

    [
        {
            "_id": "john",
            "operation": "update-man",
            "properties": {
                "id": "john",
                "age": 21,
                "sex": "M",
                "collection_name": "study-group-1"
            },
            "payload": "<man id=\"john\">john</man>"
        },
        {
            "_id": "mary",
            "operation": "update-woman",
            "properties": {
                "id": "mary",
                "age": 23,
                "sex": "F",
                "collection_name": "study-group-2"
            },
            "payload": {
              "id": "mary",
              "age": 23
            }
        },
        {
            "_id": "bob",
            "operation": "delete-man",
            "properties": {
                "collection_name": "study-group-1"
            }
        }
    ]


.. _system_section:

Systems
=======

A system component represents a computer system that can provide data entities. Its task is to provide common properties
and services that can be used by several data sources, such as connection pooling, authentication settings,
communication protocol settings and so on.

You can manage any secret property values you do not want to be exposed in the API (or in log files) by using the :ref:`Secrets manager API <secrets_manager>`.

Note: as with pipe components, you are not allowed to use the forward slash character ("``/``") in system id's.

All systems share a number of common properties:

Prototype
---------

::

    {
        "_id": "a_system_id",
        "type": "system:some-type-of-system",
        "name": "The Foo System",
        "description": "This is a description of the system",
        "comment": "This is a comment",
        "worker_threads": 10,
        "metadata": {
           "some_key": "some_value"
        }
    }

Properties
----------

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``_id``
     - String
     - A unique ID identifying the system. Any pipe sink or source that uses the system must have a corresponding
       ``system`` property matching this value.
     -
     - Yes

   * - ``name``
     - String
     - A human readable name for this system
     -
     -

   * - ``description``
     - String or list of strings
     - A human readable description of the component (optional).
     -
     - Yes

   * - ``comment``
     - String or list of strings
     - A human readable comment on the component (optional).
     -
     -

   * - ``metadata``
     - Object<string, Object>
     - A object providing metadata for the system. The keys are strings while the values can be any valid JSON object
       (literals, lists or other objects).
     -
     -

   * - ``worker_threads``
     - Integer
     - The maximum number of concurrent pipes running using this system
     - 10
     -


.. _sql_system:

The SQL systems
---------------

The SQL system components represents a `RDBMS <https://en.wikipedia.org/wiki/Relational_database_management_system>`_
and contains the necessary information to establish a connection to the RDBMS and manage these connections among the
sources that read from it. It can also provide source configurations for reading from all tables it can introspect
from the RDBMS `schema <https://en.wikipedia.org/wiki/Database_schema>`_.

The common properties for all SQL systems are:

Prototype
^^^^^^^^^

::

    {
        "_id": "sql_system_id",
        "type": "system:oracle|oracle_tns|mssql|mysql",
        "name": "The Foo Database",
        "db-type-specific-property":"some-value",
        "timezone": "UTC",
        "pool_size": 10,
        "pool_timeout": 30,
        "pool_max_overflow": 10,
        "pool_recycle": 1800
    }

Column type mapping
^^^^^^^^^^^^^^^^^^^

See the :ref:`supported column types <sql_types>` section for a overview of which column types are supported
for each RDBMS system and how they are mapped to :ref:`Sesam types <entity_data_types>`.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``timezone``
     - String
     - The local timezone for the database server. It is used for any date(time) objects returned that doesn't have any
       timezone information. The default is the UTC timezone. All the official timezone names are supported,
       i.e. "UTC", "GMT", "EST" etc. You can also use the indirect "Continent/City" format, for example "Europe/Oslo"
       (see `the complete list <http://twiki.org/cgi-bin/xtra/tzdatepick.html>`_ for which cities are supported).

       .. WARNING::

          Non-timezone datetime values that are read from  a ``sql``
          source that uses the system will be shifted from the specified
          timezone to UTC. Note that the ``_updated`` property will
          not be shifted.

     - "UTC"
     -

   * - ``pool_size``
     - Integer
     - The target maximum number of concurrent connections to the database
     - 10
     -

   * - ``pool_timeout``
     - Integer
     - The number of seconds to wait before giving up on getting a connection from the connection pool.
     - 30
     -

   * - ``pool_max_overflow``
     - Integer
     - How many connections over the ``pool_size`` are allowed before refusing to establish a incoming connection. This
       means that the absolute hard limit of connections in a connection pool is ``pool_size`` + ``pool_max_overflow``.
     - 10
     -

   * - ``pool_recycle``
     - Integer
     - This configuration option prevents the pool from using a particular connection that has passed a certain age,
       and is appropriate for database backends such as MySQL that automatically close connections that have been stale
       after a particular period of time. Note that this doesn't affect any open/active connections.
     - 1800
     -

The specific SQL systems available are:

.. _oracle_system:

The Oracle system
-----------------

The Oracle SQL system represents a `Oracle RDBMS <https://en.wikipedia.org/wiki/Oracle_Database>`_ available on the network.
See the :ref:`supported column types <oracle_types>` list for a overview of which Oracle column types are supported
and how they are mapped to :ref:`Sesam types <entity_data_types>`.

Prototype
^^^^^^^^^

::

    {
        "_id": "sql_system_id",
        "type": "system:oracle",
        "name": "The Oracle Database",
        "username":"username-here",
        "password":"secret",
        "host":"fqdn-or-ip-address-here",
        "port": 1521,
        "database": "database-name",
        "coerce_to_decimal": false
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``username``
     - String
     - Username to use when connecting to the database.
     -
     - Yes

   * - ``password``
     - String
     - Password to use when connecting to the database.
     -
     - Yes

   * - ``host``
     - String
     - Host name or IP address to the database server. Must be DNS resolvable if non-numeric.
     -
     - Yes

   * - ``port``
     - Integer
     - Database IP port.
     - 1521
     -

   * - ``database``
     - String
     - Name/id of database to connect to.
     -
     - Yes

   * - ``coerce_to_decimal``
     - Boolean
     - If set to `true`, it will force the use of the decimal type for all "numeric" types (i.e. numbers with precision
       and scale information). What type the column data ends up as is not clearly defined by the current oracle
       backend driver so in some cases it may yield a float value instead of a decimal value. This property should
       always be set to `true` if your flows care if numeric values are floats or decimals. The default value is `false`.
     - ``false``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Example Oracle configuration:

::

    {
        "_id": "oracle_db",
        "name": "Oracle test database",
        "type": "system:oracle",
        "username": "system",
        "password": "oracle",
        "host": "oracle",
        "database": "XE",
        "coerce_to_decimal": true
    }


.. _oracle_tns_system:

The Oracle TNS system
---------------------

The Oracle SQL system represents a Oracle RDBMS configured using a `TNS name <http://www.orafaq.com/wiki/Tnsnames.ora>`_
See the :ref:`supported column types <oracle_types>` list for a overview of which Oracle column types are supported
and how they are mapped to :ref:`Sesam types <entity_data_types>`.

Prototype
^^^^^^^^^

::

    {
        "_id": "sql_system_id",
        "type": "system:oracle_tns",
        "name": "The Oracle Database",
        "username":"username-here",
        "password":"secret",
        "tns_name": "tns-name-here",
        "coerce_to_decimal": false
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``username``
     - String
     - Username to use when connecting to the database.
     -
     - Yes

   * - ``password``
     - String
     - Password to use when connecting to the database.
     -
     - Yes

   * - ``tns_name``
     - String
     - A fully qualified `Oracle TNS name <http://www.orafaq.com/wiki/Tnsnames.ora>`_
     -
     - Yes

   * - ``coerce_to_decimal``
     - Boolean
     - If set to `true`, it will force the use of the decimal type for all "numeric" types (i.e. numbers with precision
       and scale information). What type the column data ends up as is not clearly defined by the current oracle
       backend driver so in some cases it may yield a float value instead of a decimal value. This property should
       always be set to `true` if your flows care if numeric values are floats or decimals. The default value is `false`.
     - ``false``
     -


Example configuration
^^^^^^^^^^^^^^^^^^^^^

Example Oracle TNS configuration:

::

    {
        "_id": "oracle_db",
        "name": "Oracle test database",
        "type": "system:oracle_tns",
        "username": "system",
        "password": "oracle",
        "tns_name": "(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = foo)(PORT = 1521)) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = BAR)))"",
        "coerce_to_decimal": true
    }


.. _mssql_system:

The MSSQL system
----------------

The MSSQL system represents a `Microsoft SQL Server <https://en.wikipedia.org/wiki/Microsoft_SQL_Server>`_ available over the network.
See the :ref:`supported column types <sql_server_types>` list for a overview of which SQL Server column types
are supported and how they are mapped to :ref:`Sesam types <entity_data_types>`.

Prototype
^^^^^^^^^

::

    {
        "_id": "sql_system_id",
        "type": "system:mssql",
        "name": "The Microsoft SQL Server Database",
        "username":"username-here",
        "password":"secret",
        "host":"fqdn-or-ip-address-here",
        "tds_version":"7.4",
        "instance": "named-instance",
        "port": 1433,
        "database": "database-name"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``username``
     - String
     - Username to use when connecting to the database.
     -
     - Yes

   * - ``password``
     - String
     - Password to use when connecting to the database.
     -
     - Yes

   * - ``host``
     - String
     - Host name or IP address to the database server. Must be DNS resolvable if non-numeric.
     -
     - Yes

   * - ``instance``
     - String
     - The name of the SQL Server "named instance", if applicable. Note that if ``instance`` is set, ``port`` will be
       ignored as SQL Server will assign a "named instance" a random port by default. Be aware that using such
       "port-less" named instances potentially has consequences for the configuration of firewall rules as well
       (i.e. for both TCP and UDP port ranges, please consult the SQL Server DBA or SQL Server manual for details).
     -
     -

   * - ``port``
     - Integer
     - Database IP port. Note: ignored if ``instance`` is set, see the previous section.
     - 1433
     -

   * - ``database``
     - String
     - Name/id of database to connect to.
     -
     - Yes

   * - ``tds_version``
     - String
     - Version of the `TDS protocol <https://en.wikipedia.org/wiki/Tabular_Data_Stream>`_ to use for the driver.
       Note that the default is ``null`` which means it's not set. This will tell the database driver to attempt to
       auto-detect the protocol version, which should work in most cases. However, if you experience unknown or general
       connection errors, you can try to specify the TDS protocol version string manually (typically on the
       form "7.0", "7.4" etc).
     -
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Example MS SQL Server configuration:

::

    {
        "_id": "sqlserver_db",
        "name": "MS SQL Server test database",
        "type": "system:mssql",
        "username": "user",
        "password": "password",
        "host": "localhost",
        "port": 1433,
        "database": "testdb"
    }

.. _mssql-azure-dw_system:

The Microsoft Azure SQL Data Warehouse system
---------------------------------------------

This system type represents a `Microsoft Azure SQL Data Warehouse server <https://docs.microsoft.com/en-us/azure/sql-data-warehouse/sql-data-warehouse-overview-what-is>`_ running in Azure.

See the :ref:`supported column types <sql_server_types>` list for a overview of which SQL Server column types
are supported and how they are mapped to :ref:`Sesam types <entity_data_types>`.

Prototype
^^^^^^^^^

::

    {
        "_id": "sql_system_id",
        "type": "system:mssql-azure-dw",
        "name": "A Microsoft Azure SQL Data Warehouse server",
        "username":"username-here",
        "password":"secret",
        "host":"fqdn-or-ip-address-here",
        "port": 1433,
        "database": "database-name"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``username``
     - String
     - Username to use when connecting to the database.
     -
     - Yes

   * - ``password``
     - String
     - Password to use when connecting to the database.
     -
     - Yes

   * - ``host``
     - String
     - Host name or IP address to the database server. Must be DNS resolvable if non-numeric.
     -
     - Yes

   * - ``port``
     - Integer
     - Database IP port.
     - 1433
     -

   * - ``database``
     - String
     - Name/id of database to connect to.
     -
     - Yes

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Example MS SQL Server configuration:

::

    {
        "_id": "sqlserver_db",
        "name": "MS Azure DW SQL Server test database",
        "type": "system:mssql-azure-dw",
        "username": "user",
        "password": "password",
        "host": "myserver.database.windows.net",
        "port": 1433,
        "database": "testdb"
    }

.. _mssql-bulk-operations:

Bulk operations in Microsoft SQL server and Azure SQL Data Warehouse systems
----------------------------------------------------------------------------

Both Microsoft SQL Server and Azure SQL Data Warehouse support bulk operations
for uploading data. Sesam uses the
`bcp utility <https://docs.microsoft.com/en-us/sql/tools/bcp-utility>`_ for bulk uploading.

When a pipe has been configured with a :ref:`SQL sink <sql_sink>` that has the ``use_bulk_operations``
parameter set to ``true``, this happens when the pipe runs:

1. Sesam creates a temporary database table named "SESAM_BULK_TMP_<table>" (where ``<table>`` is the
   name of the table the sink writes to).
2. Sesam writes a temporary file to the local disk that is formatted in a way that the
   bcp utility  understands.
3. Sesam runs the bcp utility, which will upload the content of the file to the temporary table.
4. Sesam runs a ``MERGE`` sql statement that updates the target table with the contents of the temporary table
   (inserting and updating rows as required).
5. Sesam drops the temporary database table.

For this method to work, Sesam must have permissions to create and drop tables in the database. If
for some reason that is not possible, the ``use_bulk_operations`` parameter in the sql sink can be
set to ``false`` to make the sink use the (slower) ``INSERT`` and ``UPDATE`` sql statements to upload data.

.. _mssql-identity-columns:

Identity columns in MS SQL server
---------------------------------

Identity columns (columns with automatically assigned values) are not supported by the SQL sink machinery.
However, for MS SQL based servers there is a workaround for this problem: instead of writing to the table directly,
you can define a "writable view" of the table that omits the identity columns and write to that instead. See more information
here: https://docs.microsoft.com/en-us/sql/relational-databases/views/modify-data-through-a-view

Note that this does not work for primary key columns.

.. _mysql_system:

The MySQL system
----------------

The MySQL system represents a `MySQL database <https://en.wikipedia.org/wiki/MySQL>`_ available over the network:
See the :ref:`supported column types <mysql_types>` list for a overview of which MySQL column types are supported and
how they are mapped to :ref:`Sesam types <entity_data_types>`.

Prototype
^^^^^^^^^

::

    {
        "_id": "sql_system_id",
        "type": "system:mysql",
        "name": "The MySQL Database",
        "username":"username-here",
        "password":"secret",
        "host":"fqdn-or-ip-address-here",
        "port": 3306,
        "database": "database-name"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``username``
     - String
     - Username to use when connecting to the database.
     -
     - Yes

   * - ``password``
     - String
     - Password to use when connecting to the database.
     -
     - Yes

   * - ``host``
     - String
     - Host name or IP address to the database server. Must be DNS resolvable if non-numeric.
     -
     - Yes

   * - ``port``
     - Integer
     - Database IP port.
     - 3306
     -

   * - ``database``
     - String
     - Name/id of database to connect to.
     -
     - Yes

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Example MySQL configuration:

::

    {
        "_id": "sqlserver_db",
        "name": "MySQL test database",
        "type": "system:mysql",
        "username": "user",
        "password": "password",
        "host": "localhost",
        "port": 3306,
        "database": "testdb"
    }

.. _postgresql_system:

The PostgreSQL system
---------------------

The PostgreSQL system represents a `PostgreSQL RDBMS <https://en.wikipedia.org/wiki/PostgreSQL>`_ available on the network.
See the :ref:`supported column types <postgresql_types>` list for a overview of which PostgreSQL column types are supported
and how they are mapped to :ref:`Sesam types <entity_data_types>`.

Prototype
^^^^^^^^^

::

    {
        "_id": "sql_system_id",
        "type": "system:postgresql,
        "name": "The PostgreSQL Database",
        "username":"username-here",
        "password":"secret",
        "host":"fqdn-or-ip-address-here",
        "port": 5432,
        "database": "database-name",
        "sslmode": "prefer"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``username``
     - String
     - Username to use when connecting to the database.
     -
     - Yes

   * - ``password``
     - String
     - Password to use when connecting to the database.
     -
     - Yes

   * - ``host``
     - String
     - Host name or IP address to the database server. Must be DNS resolvable if non-numeric.
     -
     - Yes

   * - ``port``
     - Integer
     - Database IP port.
     - 5432
     -

   * - ``database``
     - String
     - Name/id of database to connect to.
     -
     - Yes

   * - ``sslmode``
     - String
     - The ssl mode to use. The value has to be one of "disable", "allow", "prefer", "require", "verify-ca" or "verify-full".
       Please consult the `PostgreSQL documentation <https://www.postgresql.org/docs/10/static/libpq-ssl.html>`_  for
       the full details of what these modes entail.
     - ``"prefer"``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

Example PostgreSQL configuration:

::

    {
        "_id": "postgresql_db",
        "name": "PostgreSQL test database",
        "type": "system:postgresql",
        "username": "user",
        "password": "pw",
        "host": "test.postgresql.mydomain.com",
        "database": "test"
    }

.. _ldap_system:

The LDAP system
---------------

The LDAP system contains the configuration needed to communicate with a
`LDAP <https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol>`_ system. It is used by
:ref:`LDAP sources <ldap_source>` to stream entities from LDAP catalogs.
Note that `Microsoft ActiveDirectory <https://en.wikipedia.org/wiki/Active_Directory>`_ is also supported
through its LDAP-compatible interface/API.

It supports the following properties:

Prototype
^^^^^^^^^

::

    {
        "host": "FQDN of LDAP host",
        "port": 389,
        "use_ssl": false,
        "username": "authentication-username-here",
        "password": "authentication-password-here",
        "charset": "latin-1"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``host``
     - String
     - The fully qualified domain name (``FQDN``) of the LDAP host server
     - "localhost"
     -

   * - ``port``
     - Integer
     - The TCP port of the LDAP service.
     - 389
     -

   * - ``use_ssl``
     - Boolean
     - Indicates to the client whether to use a secure socket layer (``SSL``) or not when communicating with the LDAP service
     - false
     -

   * - ``username``
     - String
     - The user to authenticate as against the LDAP service. If not set, no authentication will be attempted.
     -
     -

   * - ``password``
     - String
     - The password to use for authenticating with the LDAP service. Required if ``username`` is set.
     -
     - Yes

   * - ``charset``
     - String
     - The charset used to encode strings in the LDAP database. Defaults to ``"latin-1"`` aka ``"ISO-8859-1"``,
       as ``"UTF-8"`` is usually not the default encoding in LDAP catalogs at the time of writing.
     - "latin-1"
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "example_ldap",
        "name": "Example LDAP server",
        "type": "system:ldap",
        "host": "ldap.example.org",
        "port": 389,
        "username": "example\\some-user",
        "password": "********"
    }


.. _smtp_system:

The SMTP system
---------------

The SMTP system represents the information needed to connect to a `SMTP <https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol>`_
server for sending emails. It is used in conjunction with the :ref:`mail message sink <mail_message_sink>` to construct
and send emails based on the entities it receives.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:smtp",
        "smtp_server": "localhost",
        "smtp_port": 25,
        "smtp_username": null,
        "smtp_password": null,
        "use_tls": false,
        "max_per_hour": 1000
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``smtp_server``
     - String
     - Contains a ``FQDN`` of the ``SMTP service`` to use
     - "localhost"
     -

   * - ``smtp_port``
     - Integer
     - The TCP port to use when talking to the ``SMTP service``
     - 25
     -

   * - ``smtp_username``
     - String
     - The username to use when authenticating with the ``SMTP service``. If not set, no authentication is attempted.
     -
     -

   * - ``smtp_password``
     - String
     - The password to use if ``smtp_username`` is set. It is mandatory if the ``smtp_username`` is provided.
     -
     - Yes

   * - ``use_tls``
     - Boolean
     - Indicating to the client to use ``TLS encryption`` when communicating with the ``SMTP service``.
     - false
     -

   * - ``max_per_hour``
     - Integer
     - The maximum number of messages to send for any hour. It is used for stopping run-away message sending in
       development or testing. Note that any message not sent will be logged but discarded.
     - 1000
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-smtp-server",
        "name": "Our SMTP Server",
        "type": "system:smtp",
        "smtp_server": "localhost",
        "smtp_port": 25,
        "smtp_username": "some-user",
        "smtp_password": "*********",
        "max_per_hour": 100000
    }

.. _solr_system:

The Solr system
---------------

The Solr system represents the information needed to connect to a `Apache Solr <https://en.wikipedia.org/wiki/Apache_Solr>`_
server for indexing JSON documents. It is used in conjunction with the :ref:`Solr sink <solr_sink>` or the :ref:`Sesam Databrowser sink
<databrowser_sink>` sinks.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:solr",
        "url": "http://localhost:8983/solr/",
        "timeout": 30,
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``url``
     - String
     - Contains a full URL to the Solr dataset to read/write documents from
     - "http://localhost:8983/solr/"
     -

   * - ``timeout``
     - Integer
     - The number of seconds to wait for a response from the Solr server.
     - 30
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-solr-server",
        "name": "Our Solr Server",
        "type": "system:solr",
        "url": "http://localhost:8983/solr/"
    }

.. _elasticsearch_system:

The Elasticsearch system
------------------------

The Elasticsearch system represents the information needed to connect
to an `Elasticsearch <https://en.wikipedia.org/wiki/Elasticsearch>`_ server/cluster for indexing JSON documents. It is
used in conjunction with the :ref:`Elasticsearch sink <elasticsearch_sink>`.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:elasticsearch",
        "hosts": ["localhost:9200"]
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``hosts``
     - List<String>
     - Contains a list of host+port pairs, or full URL to the Elasticsearch server(s)
     - ``["localhost:9200"]``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-elasticsearch-server",
        "name": "Our Elasticsearch Server",
        "type": "system:elasticsearch",
        "hosts": ["localhost:9200"]
    }

.. _twilio_system:

The Twilio system
-----------------

The `Twilio <https://en.wikipedia.org/wiki/Twilio>`_ system is a ``SMS system`` used with
:ref:`SMS message sinks <sms_message_sink>` to construct and send SMS messages from entities.

It has the following properties:

Prototype
^^^^^^^^^

::

    {
        "_id": "system-id",
        "name": "Service name",
        "type": "system:twilio",
        "account": "twilio-account-number",
        "token": "twilio-api-token",
        "max_per_hour": 1000,
        "proxy":  "socks5://user:password@socksproxy:1234"
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``account``
     - String
     - The ``Twilio`` account number
     -
     - Yes

   * - ``token``
     - String
     - The ``Twilio`` API token
     -
     - Yes

   * - ``max_per_hour``
     - Integer
     - The maximum number of messages to send for any hour. It is used for stopping run-away message sending in
       development or testing. Note that any message not sent will be logged but discarded.
     - 1000
     -

   * - ``proxy``
     - String
     - A optional property that specifies a SOCKS5 proxy for the system. If authentication is used, the embedded
       username and passord should be put into system secrets, i.e. ``$SECRET(username):$SECRET(password)@..``.
     -
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
         "_id": "twilio_service",
         "name": "Twilio Service",
         "type": "system:twilio",
         "account": "12334567890",
         "token": "ABCD-ADEF-FAA1-1234",
         "max_per_hour": 100000
    }

.. _url_system:

The URL system
--------------

The URL system represents a `HTTP server <https://en.wikipedia.org/wiki/Web_server>`_ (i.e. a web server)
serving `HTTP requests <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_ from a base url.
It supports the ``HTTP`` and ``HTTPS`` protocols. It provides session handling, connection pooling and authentication
services to sources and sinks which need to communicate with a HTTP server.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:url",
        "url_pattern": "http://host:port/path/%s",
        "verify_ssl": false,
        "username": null,
        "password": null,
        "jwt_token": null,
        "headers": {
            "MY_HEADER": "some-value",
            "MY_OTHER_HEADER": "$ENV(key-for-other-value)",
            "MY_SECRET_HEADER": "$SECRET(secret-key)"
        },
        "oauth2": {
            "client_id": "my-client-id",
            "client_secret": "$SECRET(client-secret)",
            "token_url": "https://oath2-enabled-server:port/path/to/service/for/access/token",
            "scope": ["scope1", "scope2"]
            "extra": {
               "some": "extra-params",
               "to": "include-in-token-request"
            }
        },
        "proxies": {
            "http": "socks5://mysocksproxy:1234",
            "https": "socks5://user:password@mysslsocksproxy:1234",
        },
        "authentication": "basic",
        "connect_timeout": 60,
        "read_timeout": 1800
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``url_pattern``
     - String
     - Similar to ``base_url`` except one can use the ``%s`` token to tell where relative URLs are to be inserted into the ``url_pattern`` to produce absolute URLs. If ``%s`` is omitted then the relative URL is appended to the ``url_pattern``.
     -
     - Yes

   * - ``base_url``
     - String
     - Deprecated. Use the ``url_pattern`` property instead. The full URL of the base url of the HTTP server. Relative URLs are URL joined against this base URL to produce absolute URLs. Note that you may want a ``/`` at the end of the value.
     -
     -

   * - ``verify_ssl``
     - Boolean
     - Indicate to the client if it should attempt to verify the SSL certificate when communicating with the
       HTTP server over SSL/TLS.
     - ``false``
     -

   * - ``username``
     - String
     - The username to use when authenticating with the HTTP server. Note that you also have to specify
       authentication protocol in ``authentication`` and ``password`` for this property to have any effect.
     -
     -

   * - ``password``
     - String
     - The password to use if ``username`` and ``authentication`` is set. It is mandatory if ``username`` is provided.
     -
     - Yes*

   * - ``jwt_token``
     - String
     - If ``authentication`` is set to ``jwt``, this property must hold the `JWT <https://jwt.io/>`_ token to use
       towards the remote server.
     -
     -

   * - ``headers``
     - Dict<String,String>
     - A optional set of header values to set as defaults in request made using the URL system. Both keys and values must
       evaluate to strings. Note that any "Authorization" header provided in this object is automatically overwritten
       when using the ``jwt_token`` property.
     -
     -

   * - ``authentication``
     - String
     - What kind of authentication protocol to use. Note that authentication is opt-in only and the default is no
       authentication. Allowed values is either "basic", "digest", "ntlm" or "jwt". Note that ``username``, ``password`` or ``jwt_token``
       might be also required depending on the authentication scheme selected.
     -
     -

   * - ``oauth2``
     - Dict<String,String>
     - A optional set of properties that specifies support for automatic fetching of JWT access tokens from a oauth2
       enabled provider. The profile supported is "client credentials", which means you will need a ``client_id`` and
       ``client_secret`` from your oauth2 provider. Additionally, you must provide a ``token_url`` URL to a service which
       generates JWT access tokens. Optionally you can define a list of scopes (in ``scope``) for your client. Note that
       this option cannot be combined with ``JWT`` authentication or the ``jwt_token`` property. Also note that the
       oauth2 specification mandates TLS secured transport for both the token endpoint and the target defined in
       ``url_pattern``. You can add optional extra parameters to the token request in the ``extra`` subattribute.
     -
     -

   * - ``proxies``
     - Dict<String,String>
     - A optional set of properties that specifies a set of SOCKS5 proxies for the URL system. The keys represents url-
       prefixes (for example 'http' and 'https') and the values of the HTTP(S) or SOCKS5 servers that the requests matching the
       prefixes should be passed through. The values should be on the form ``socks5://username:password@domain_or_ip:port``
       or .``http(s)://username:password@domain_or_ip:port``
       The ``username:password@..`` syntax is optional. If used, the embedded username and passord should be put into system
       secrets, i.e. ``$SECRET(username):$SECRET(password)@..``.
     -
     -

   * - ``connect_timeout``
     - Integer
     - Number of seconds to wait for connecting to the HTTP server before timing out. A value of ``null`` means
       wait indefinitely.
     - ``60``
     -

   * - ``read_timeout``
     - Integer
     - Number of seconds to wait for the HTTP server to respond to a request before timing out. A value of ``null``
       means wait indefinitely.
     - ``1800``
     -

   * - ``ignore_invalid_content_length_response_header``
     - Boolean
     - Normally, the URL system will throw an error if the ``Content-Length`` header is present and
       contains an invalid value. The ``ignore_invalid_content_length_response_header`` property can be set to
       ``true`` in order to attempt to ignore such errors.
     - ``false``
     -

[1] Exactly one of ``base_url`` and ``url_pattern`` must be specified.

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-http-server",
        "name": "Our HTTP Server",
        "type": "system:url",
        "base_url": "http://our.domain.com/files"
    }

Example with ntlm configuration:

::

    {
        "_id": "our-http-server",
        "name": "Our HTTP Server",
        "type": "system:url",
        "authentication": "ntlm",
        "username": "domain\\user",
        "password": "secret",
        "base_url": "http://our.domain.com/files"
    }



.. _rest_system:

The REST system
---------------

The REST system represents a REST service (i.e. a web server) serving
`HTTP requests <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_ from a base url using the REST
vocabulary of GET, PUT, POST and PATCH.

It is used by the :ref:`REST sink <rest_sink>`.

It supports the ``HTTP`` and ``HTTPS`` protocols. It provides session handling, connection pooling and authentication
services to sources and sinks which need to communicate with a HTTP server.

The REST system is an extension of the URL system, so all configuration properties of the :ref:`URL system <url_system>`
apply. We'll only cover the REST system specific properties in this section.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:rest",
        "url_pattern": "http://host:port/path/%s",
        "verify_ssl": false,
        "username": null,
        "password": null,
        "authentication": "basic",
        "jwt_token": null,
        "connect_timeout": 60,
        "read_timeout": 1800,
        "operations": {
            "get-operation": {
                "url" : "/a/service/that/supports/get/{{ _id }}",
                "method": "GET"
            },
            "delete-operation": {
                "url" : "/a/service/that/supports/delete/{{ _id }}",
                "method": "DELETE"
            },
            "put-operation": {
                "url" : "/some/service/that/supports/put",
                "method": "PUT",
                "headers": {
                    "Content-type": "application/json"
                },
                "payload-type": "json"
            },
            "post-operation": {
                "url" : "/some/service/that/supports/post",
                "method": "POST",
                "payload-type": "form"
            },
            "patch-operation": {
                "url" : "/some/service/that/supports/patch",
                "headers": {
                    "Content-type": "application/xml"
                },
                "method": "PATCH"
            }
        }
    }

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``<any url system property>``
     -
     - The REST system extends the URL system, so any property from the URL system can be applied.
     -
     -

   * - ``operations``
     - Object
     - An object containing the registered operations allowed for the REST service. See the next section for details.
       At least one operation need to be registered for the system.
     -
     - Yes

Operation properties
^^^^^^^^^^^^^^^^^^^^

You can register as many named "operations" as you like with the system (even using the same type of "method").
A operation configuration looks like:

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req


   * - ``url``
     - String
     - A URL or URL part. The property supports the ``Jinja`` template (http://jinja.pocoo.org/) syntax with the entities properties
       available to the templating context. The expanded string is then substituted into the system's ``url_pattern`` property in
       place of its ``%s`` placeholder marker to get the final URL to use for the operation.
     -
     - Yes

   * - ``method``
     - String
     - A enumeration of "GET", "POST", "PUT", "DELETE" and "PATCH" (note: case sensitive) that represents the HTTP operation
       that the operation should execute on the ``url`` specified.
     -
     - Yes

   * - ``headers``
     - Dict<String,String>
     - An optional object that contain key-value mappings for the HTTP request header. Entries in this dictionary
       will override any default ``headers`` property defined on the system (see previous section).
     -
     -

   * - ``params``
     - Objects
     - An optional object that contain key-value mappings for any HTTP parameters.
     -
     -

   * - ``payload-type``
     - String
     - A enumeration of "json", "json-transit" and "form", that denotes how to treat the ``payload`` property of the
       entity (see the :ref:`expected entity shape <rest_expected_rest_entity_shape>` section of the :ref:`REST sink <rest_sink>` for details). If you
       specify "json", the payload contents will serialized to JSON (without transit encoding). If you specify "json-transit"
       you will get a transit-encoded JSON document. If "form" is used, the contents will be used to construct a
       HTML FORM for the request. In this case, if the property contains a list, the request will use a multi-part form.
       If ``payload-type`` is omitted, the contents of the ``payload`` property will be assumed to be a string.
     -
     -


.. _rest_system_example:

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-rest-service",
        "name": "Our REST service",
        "url_pattern": "http://our.domain.com/api/%s",
        "type": "system:rest",
        "operations": {
            "get-man": {
                "url" : "men/{{ properties.collection_name }}/{{ _id }}",
                "method": "GET"
            },
            "get-woman": {
                "url" : "women/{{ properties.collection_name }}/{{ _id }}",
                "method": "GET"
            },
           "delete-man": {
               "url" : "men/{{ properties.collection_name }}/{{ _id }}",
               "method": "DELETE"
           },
           "delete-woman": {
               "url" : "women/{{ properties.collection_name }}/{{ _id }}",
               "method": "DELETE"
           },
           "update-man": {
               "url" : "men/{{ properties.collection_name }}/",
               "method": "POST",
               "headers": {
                   "Content-type": "application/xml"
               }
           },
           "update-woman": {
               "url" : "women/{{ properties.collection_name }}/",
               "method": "POST",
               "headers": {
                   "Content-type": "application/json"
               },
               "payload-type": "json"
           }
        }
    }

.. _microservice_system:

The microservice system
-----------------------

The microservice system is similar to the :ref:`URL system <url_system>`, except that it also spins up the microservice that it defines. This system can be used with the :ref:`JSON source <json_source>`, the :ref:`HTTP transform <http_transform>` and the :ref:`JSON push sink <json_push_sink>`.

The ``docker`` property lets one specify a Docker container that should be spun up. Note that the microservice system does not have the ``base_url`` property. The reason is that it is able to figure out this itself.

The microservice system supports private repositories.

A microservice must communicate with the outside world using either the ``HTTP`` protocol (the default) or the ``HTTPS`` protocol. Set the ``use_https`` property to ``true`` to enable ``HTTPS``.

The system provides session handling, connection pooling and authentication services to sources, transforms and sinks which need to communicate with the microservice.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-microservice",
        "name": "Name of microservice",
        "type": "system:microservice",
        "docker": {
            "image": "some-repo/some-image:some-tag",
            "port": 5000,
            "username": null,
            "password": null,
            "memory": 128,
            "cpu_quota": 25,
            "cpu_period": 100,
            "cpuset_cpus": null,
            "environment": {
                "SOME-VARIABLE": "SOME-VALUE",
                "OTHER-VARIABLE": {
                    "key1": "value1",
                    "key2": "value2"
                }
            },
            "hosts": {
                "myhost1.mydomain.io": "157.240.20.34",
                "myhost2.mydomain.io": "157.240.20.35"
            },
            "skip_pull": false,
            "pull_image_cron_expression": "0 0 * * *"
        },
        "use_https": false,
        "verify_ssl": false,
        "username": null,
        "password": null,
        "authentication": "basic",
        "connect_timeout": 60,
        "read_timeout": 1800
    }

Note that due to Docker naming conventions, the ``_id`` of the microservice must start with a ASCII letter or number
character and the only non-letter or number characters allowed in the rest of the string are "_" and "-".

The microservice ``_id`` is exposed as domain names in the local network and is thus subject to domain name rules:
the maximal size of an id is 63 characters and the minimal size is 2 characters.

It should also contain only lower-case letters to avoid DNS lookup errors when used via by HTTP requests,
for example in a URL system or via its proxy API.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``docker.image``
     - String
     - The fully qualified name of a Docker image, e.g. ``sesam/file-share-service:latest`` or ``quay.io/someuser/someimage:1.2.3``.
     -
     - Yes

   * - ``docker.port``
     - Integer
     - The port on which to talk to the microservice. This should be one of the ports that the Docker container exposes.
     -
     - Yes

   * - ``docker.environment``
     - Dict<String,String|Object>
     - The environment variables that should be passed to the microservice's Docker container. Note that string
       literals are passed along to the docker container as-is, while other types of values are serialized to a string
       in JSON format.
     -
     -

   * - ``docker.username``
     - String
     - If the Docker images is located in a private repository, then the username must be specified here.
     -
     -

   * - ``docker.password``
     - String
     - If the Docker images is located in a private repository, then the password must be specified here.
     -
     -

   * - ``docker.memory``
     - Integer
     - The number of MB of RAM to allocate for the microservice.
     - ``128``
     -

   * - ``docker.cpu_quota``
     - Integer
     - The percentage of CPU resources the container is allowed to consume. *Use with extreme care* as you can easily
       starve other processes on the server for resources if you set this value incorrectly or suboptimally. See
       `the Docker documentation <https://docs.docker.com/engine/reference/run/#cpu-period-constraint>`_ for details).
       Note that the value is divided by 1000 with respects to the range in the Docker documentation. Also note that
       the value represents the *sum* of CPU resources used across *all cores*. If the container is allowed to use more
       than one CPU (by default it can use all of them) the number can exceed 100. I.e. for a 4 core CPU, 400 means
       use all resources on all CPU cores.
     - ``25``
     -

   * - ``docker.cpu_period``
     - Integer
     - The percentage of CPU time the OS scheduler is allowed use (see `the Docker documentation <https://docs.docker.com/engine/reference/run/#cpu-period-constraint>`_ for details).
       Note that the value is divided by 1000 with respects to the range in the Docker documentation. You should not
       normally change the default value.
     - ``100``
     -

   * - ``docker.cpuset_cpus``
     - String
     - A string expression representing the CPU cores the container is allowed to use, see ``docker.cpu_quota``.
       The default (``null`` value) means the container can use all cores. A value of ``"0,4"`` means use core 0 and
       4. A value of ``"0-4"`` means use cores 0 through 4. A value of ``"0,6-8"`` means use core 0 and 6 through 8.
     - ``null``
     -

       .. _microservices_system_docker_hosts:
   * - ``docker.hosts``
     - Dict<String,String>
     - A mapping between domain names/hostnames and IP adresses. These custom hostnames will be resolvable inside the microservice container.
     - ``{}``
     -

   * - ``docker.skip_pull``
     - Boolean
     - If set to true then the system will will never try to pull a new version of the docker image. If this is
       set to false (the default), the system will attempt to pull a new version of the docker image every time
       the microservice docker container is restarted (for instance when a new config has been specified).
     - ``false``
     -

   * - ``docker.pull_image_cron_expression``
     - String
     - A cron expression that indicates when the system will attempt to pull a new version of the docker image.
       If a newer version of the docker image is pulled, the microservice docker container will restart.
     - ``null``
     -

   * - ``use_https``
     - Boolean
     - If set to true then the system will use the ``https`` protocol to communicate with the microservice.
     - ``false``
     -

   * - ``verify_ssl``
     - Boolean
     - Indicate to the client if it should attempt to verify the SSL certificate when communicating with the
       microservice over SSL/TLS.
     - ``false``
     -

   * - ``username``
     - String
     - The username to use when authenticating with the microservice. Note that you also have to specify
       authentication protocol in ``authentication`` and ``password`` for this property to have any effect.
     -
     -

   * - ``password``
     - String
     - The password to use if ``username`` and ``authentication`` is set. It is mandatory if ``username`` is provided.
     -
     - Yes*

   * - ``authentication``
     - String
     - What kind of authentication protocol to use. Note that authentication is opt-in only and the default is no
       authentication. No authentication set means means any ``username`` or ``password`` set will be ignored.
       Allowed values is either "basic" or "digest".
     -
     -

   * - ``connect_timeout``
     - Integer
     - Number of seconds to wait for connecting to the microservice before timing out. A value of ``null`` means
       wait indefinitely.
     - ``60``
     -

   * - ``read_timeout``
     - Integer
     - Number of seconds to wait for the microservice to respond to a request before timing out. A value of ``null``
       means wait indefinitely.
     - ``1800``
     -

Microservice APIs
^^^^^^^^^^^^^^^^^

The Microservice system exposes several API endpoints that can be used to access or gather information about the running
service:

* `Logs endpoint <./api.html#get--systems-system_id-logs>`_ - exposes the service's logs
* `Status endpoint <./api.html#get--systems-system_id-status>`_ - runtime information about the provisioned service
* `Reload endpoint <./api.html#post--systems-system_id-reload>`_ - pull new docker image and reload the microservice
* `Proxy endpoint <./api.html#get--systems-system_id-proxy--path-relative_path->`_ - proxy for the microservice URL through the node API

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-http-server",
        "name": "My microservice",
        "type": "system:microservice",
        "docker": {
            "image": "myrepo/myimage:1.0",
            "port": 4444,
            "environment": {
               "USE_PORT": "4444"
            }
        }
    }

.. _pump_section:

Pumps
=====

Pumps are responsible for "pumping" data through the :ref:`pipe <pipe_section>` by reading :doc:`entities <entitymodel>`
from a :ref:`source <source_section>` and writing them into a :ref:`sink <sink_section>`. The pump is also responsible
for retrying failed writes of entities and logging its activity. It can also write ultimately failed entities to a "dead letter"
dataset for manual inspection. Pumps log their :doc:`execution history <pump-execution>` in a internal dataset with
the id "system:pump_execution:<pipe_id>". See the chapter on :doc:`the pump execution dataset <pump-execution>` for more
details about the contents of this dataset.

Prototype
---------

::

    {
        "comment": "This is a comment",
        "schedule_interval": 30,
        "cron_expression": "* * * * *",
        "rescan_run_count": 10,
        "rescan_cron_expression": "* * * * *",
        "partial_rescan_run_count": 5,
        "partial_rescan_delta": 3600,
        "run_at_startup": false,
        "max_read_retries": 0,
        "read_retry_delay": 0,
        "write_retry_delay": 0,
        "max_retries_per_entity": 5,
        "max_consecutive_write_errors": 1,
        "max_write_errors_in_retry_dataset": 0,
        "fallback_to_single_entities_on_batch_fail": true,
        "dead_letter_dataset": "some-dataset-id",
        "track_dead_letters": false,
        "mode": "scheduled",
        "log_events_noop_runs": false,
        "log_events_noop_runs_changes_only": true,
        "notification_granularity": 99999999999
    }

Properties
----------

Note: A pump configuration needs to have either a ``schedule_interval`` *or* a
``cron_expression`` property to govern when the pump should be run. They are mutually exclusive with the
``cron_expression`` taking precedence if both are present. If neither property is set, the ``schedule_interval``
will be set to a default value. For pipes with a :ref:`dataset sink <dataset_sink>` *and* a
:ref:`dataset source <dataset_source>` the default will be 30 seconds +/- 1.5 seconds. For all other pipes, the default
will be 900 seconds +/- 45 seconds. It is good practice to always set the ``cron_expression`` property
on pipes that reads from or writes to external systems.

If you are unfamiliar with `cron expressions <https://en.wikipedia.org/wiki/Cron>`_, you can read more of how
they are formatted in the :doc:`Cron Expressions <cron-expressions>` document.


.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 1

   * - Property
     - Type
     - Description
     - Default
     -
      .. _pump_param_schedule_interval:

   * - ``comment``
     - String or list of strings
     - A human readable comment on the pump (optional).
     -
     -

   * - ``schedule_interval``
     - Number
     - The number of seconds between runs. It is mutually exclusive with the ``cron_expression`` property.
     - (see the note above)
     -
      .. _pump_param_cron_expression:

   * - ``cron_expression``
     - String
     - A cron expression that indicates when the pump should run.
       It is mutually exclusive with the ``schedule_interval`` property.
     -
     -

   * - ``rescan_run_count``
     - Integer(>=1)
     - How many times the pump should run before scheduling a complete rescan of the source of the pipe that the pump
       is part of. It is mutually exclusive with the ``rescan_cron_expression`` property.
     -
     -

   * - ``rescan_cron_expression``
     - String
     - A cron expression that indicates when the pump should schedule a full rescan of the source of the pipe the pump
       is part of. It is mutually exclusive with the ``rescan_run_count`` property.
     -
     -

   * - ``partial_rescan_run_count``
     - Integer(>=1)
     - How many times the pump should run before scheduling a partial rescan of the
       source of the pipe that the pump is part of. Any complete rescans will take
       precedence if they both apply. If this property is specified then the
       ``partial_rescan_delta`` must also be specified.
     -
     -

   * - ``partial_rescan_delta``
     - Integer(>=1)
     - This specifies the delta to perform a partial rescan of.

       If the since value is an integer the value is substracted.

       Example: If the since value is ``12637`` and the delta value is ``100``, then
       the since value will be shifted to ``12537``.

       If the since value is a timestamp then the value in seconds is substracted.

       Example: If the since value is
       ``"~t2018-04-27T15:46:40Z"`` and the delta value is 3600, then the
       since value will be shifted one hour back to ``"~t2018-04-27T14:46:40Z"``.
     -
     -

   * - ``run_at_startup``
     - Boolean
     - A flag that indicates if the pump should run when Sesam starts up, in addition to the normal schedule
       specified by the ``schedule_interval`` or ``cron_expression`` properties.
     - false
     -


   * - ``use_dead_letter_dataset``
     - Boolean
     - Deprecated. Use the ``dead_letter_dataset`` property instead. This is a flag used to indicate whether to write
       any entities that fail retries to a special "dead letter" dataset. This can only happen if
       ``max_write_errors_in_retry_dataset`` is non-zero and ``max_retries_per_entity`` for
       the particular entity has been exceeded. Note that unspecified dead letter datasets for a pipe has the special
       id pattern ``system:dead-letter:pipe-id``. Only users with the authorization to see the pipe configuration can
       access this dataset.
     -
     -

   * - ``dead_letter_dataset``
     - String
     - This is string that indicates which dataset to write any entities that fail retries if
       ``max_write_errors_in_retry_dataset`` is non-zero and ``max_retries_per_entity`` for the particular entity has
       been exceeded. Only users with the authorization to see the pipe configuration will have access to this dataset.
       The dataset indicated must be unique per pipe.
     -
     -

   * - ``track_dead_letters``
     - Boolean
     - A flag that indicates if the pump should delete any previously "dead letter" entities if a later version of it
       is successfully written to the sink. It is only active if the ``use_dead_letter_dataset`` property is set and
       retries are active. Note that enabling this option wil incur a performance cost because all successfully
       written entities must be looked up in the execution log to determine if it has been previously marked as "dead".
     - false
     -

   * - ``max_read_retries``
     - Integer
     - A counter that indicates to the pump how many times it should retry when failing to read a entity from a source.
       The default (0) means that it should not retry but log an error immediately when encountering read errors.
       See also the ``read_retry_delay`` property.
     - 0
     -

   * - ``read_retry_delay``
     - Number
     - How many seconds to wait before retrying after a read error (i.e. only if ``max_read_retries`` is non-zero).
       The default value is 0 which will retry immediately. If the reason for the read error is non-transient,
       the number of retries set by ``max_read_retries`` will be exhausted quickly - in this case, set this property to
       match the expected interval.
     - 0
     -

   * - ``write_retry_delay``
     - Number
     - How many seconds to wait before retrying after a write error (i.e. only if ``max_consecutive_write_errors`` is
       larger than 1).
       The default value is 0 which will retry immediately. If the reason for the write error is non-transient,
       the number of retries set by ``max_consecutive_write_errors`` will be exhausted quickly - in this case, set this
       property to match the expected interval.
     - 0
     -

   * - ``max_retries_per_entity``
     - Integer
     - A counter that indicates to the pump how many times it should retry a failing entity when writing to a sink before
       giving up on it, which in case it can optionally write it to the dataset referenced in ``dead_letter_dataset``
       (if specified).
     - 5
     -

   * - ``max_consecutive_write_errors``
     - Integer
     - A counter that indicates to the pump how many consecutive write errors it tolerates before terminating the
       current run. The default (1) means it will terminate after the first write error it encounters.
       See also the ``write_retry_delay`` property.
     - 1
     -

   * - ``max_write_errors_in_retry_dataset``
     - Integer
     - A counter that indicates to the pump how many write errors it accepts in its execution history dataset. If the number of
       retryable and not "dead" failed entities in the dataset exceeds this number, the pump will refuse to
       write any more failed entities to the execution dataset and terminate, even if the ``max_retries_per_entity`` or
       ``max_retries_per_entity`` is not reached at that point. This purpose of this property is to limit the size of the
       pump execution dataset in the case where a target system is unreachable (or misconfigured). The default value (0) effectively
       disables retries for write errors.
     - 0
     -

   * - ``fallback_to_single_entities_on_batch_fail``
     - Boolean
     - A flag that controls if the pipes should attempt to process a single entity at a time if a batch
       write operation fails. This can be useful to turn off if the cost of processing a single entity at a time
       is prohibitively high. This single-entity-at-a-time fallback is on by default (``true``).
     - true
     -

   * - ``mode``
     - String
     - The mode of operation. Valid options are "``scheduled``" (the default), "``manual``" and
       "``off``".

       Pumps in ``scheduled`` mode will follow the configured schedule and the scheduler can be
       enabled and disabled at runtime.

       Pumps in ``manual`` mode will not be scheduled and can only be operated manually through
       the Service API.

       Pumps in ``off`` mode cannot be started at all.
     - "scheduled"
     -

   * - ``log_events_noop_runs``
     - Boolean
     - A flag that controls if a "noop" ("no-operation") pipe run should be logged in the pipe execution log or not. The default
       value ``false`` means that runs that results in no processed or changed entities (the semantic depends on the type of sink)
       will never be logged. See also the ``log_events_noop_runs_changes_only`` property which controls if the source or
       the sink decides if a run is considered a "noop" or not. Note that any errors or retries will always imply logging
       to the execution dataset.
     - false
     -

   * - ``log_events_noop_runs_changes_only``
     - Boolean
     - A flag that controls what kind of metric is used to determine if a pipe run was a "noop" ("no-operation") run or not.
       The default setting ``true`` means that a run is considered a "noop" run if the sink reported that no entities
       was changed, even if the source produced entities. If it is set to ``false`` then all runs which yielded no
       new entities from the source is considered a "noop" run. Note that any errors or retries will always imply logging
       to the execution dataset.
     - true
     -

   * - ``notification_granularity``
     - int
     - This property lets the pipe "override" the ``log_events_noop_runs`` property and force the pipe to log a run
       at regular intervals, even if it was a "noop" run. The value is in seconds. The default value
       is ``999999999999999`` and means "never". A value of 900 means always log a pipe run if the last logged
       "completed" event is older than 15 minutes). Note that any errors or retries will always imply logging to the
       execution dataset.
     - true
     -


Example configuration
---------------------

The outermost object would be your :ref:`pipe <pipe_section>` configuration, which is omitted here for brevity:

A scheduled pump running every 30 seconds, no retries or dead letter dataset:

::

    {
        "pump": {
           "schedule_interval": 30
       }
    }

A cron pump running every day at midnight with max 5 retries, maximum 100 retries in the execution log and a dead letter
dataset. Also max ten consecutive write failures allowed:

::

    {
        "pump": {
           "cron_expression": "0 0 * * *",
           "max_retries_per_entity": 5,
           "max_consecutive_write_errors": 10,
           "max_write_errors_in_retry_dataset": 100,
           "dead_letter_dataset": "mypipe-dead-letters"
       }
    }

A scheduled pump running every 30 seconds but do a full rescan of the source every full hour. No retries or dead letter
datasets:

::

    {
        "pump": {
           "schedule_interval": 30,
           "rescan_cron_expression": "0 * * * *"
       }
    }

A scheduled pump running every 5 minutes from 14:00 and ending at 14:55, AND fire every 5 minutes starting at
18:00 and ending at 18:55, every day. No retries or dead letter datasets:

::

    {
        "pump": {
           "cron_expression": "0/5 14,18 * * ?"
       }
    }
