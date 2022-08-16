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
The following *JSON* snippet shows the general form of a pipe definition.

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
        },
        "metadata": {
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
is usually 100, but this may vary depending on the source- and
sink-type used in the pipe. The :ref:`REST sink <rest_sink>` will
for instance make the default batch_size 1.

Note that the sink may have its own ``batch_size`` property. This is
useful if the pipe has transforms that produce more entities than the
number of entities taken as input.

.. _pipe_properties:

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

   * - ``type``
     - String
     - The type of the component, for pipes the only allowed value is "pipe"
     -
     - Yes

   * - ``name``
     - String
     - A human readable name of the component.
     -
     -

   * - ``description``
     - String or list of strings
     - A human readable description of the component.
     -
     -

   * - ``comment``
     - String or list of strings
     - A human readable comment on the component.
     -
     -

   * - ``batch_size``
     - Integer(>=1)
     - The number of source entities to consume before writing to the sink. The batch size
       can be used to buffer up entities so that they can be written together to the sink in
       one go. The sink must support batch for the bulking to happen. This may increase the
       throughput of the pipe, at the cost of extra memory usage. If the batch fails,
       then entities will be retried individually.
     - usually 100, but varies with other pipe settings.
     -

   * - ``checkpoint_interval``
     - Integer(>=1)
     - Specifies how often the pipe offset is saved. It says how many batches
       must be processed before the pipe offset is saved the next time. Note that the pipe
       offset is always saved at the end of the sync if it changed.

       The default value is 10000/``batch_size`` = 100, i.e. the
       checkpoint happens every 100 batches. The exception is if ``batch_size`` is 1, in which case the
       default value of ``checkpoint_interval`` is also set to 1.
     - 100 (1 if batch_size=1)
     -

   * - ``disable_set_last_seen``
     - Boolean
     - If this flag is set to ``true``, it will no longer be possible to reset or set the 'last seen' parameter for this
       pipe. The primary use case for this property is when you need to protect the pipe from accidental resets.
     - ``false``
     -

       .. _pipe_settings_enable_background_rescan:

   * - ``enable_background_rescan``
     - Boolean
     - When set to true, enables running :ref:`pipe rescans <pipe_rescans>` in the background for this pipe.
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

   * - ``infer_pipe_entity_types``
     - Boolean
     - :ref:`Schema inferencing <schema-inferencing>` is enabled for
       all pipes by default. Setting this property to false will
       disable schema inferencing for this pipe.
     - ``true``
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

       If ``namespaced_identifiers`` is enabled in the service metadata then the sink default value is used. The following sinks has a default value of ``true``:  :ref:`csv_endpoint <csv_endpoint_sink>`, :ref:`elasticsearch <elasticsearch_sink>`, :ref:`mail <mail_sink>`, :ref:`rest <rest_sink>`, :ref:`sms <sms_sink>`, :ref:`solr <solr_sink>`, :ref:`sql <sql_sink>`, :ref:`http_endpoint <http_endpoint_sink>`, and :ref:`json <json_sink>`.
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
       in. Uses the minimum value of ``1.0`` by default, meaning that compaction will always
       run when new entities are written to the dataset.
     - ``1.0``
     - No

   * - ``compaction.compaction_interval``
     - Float
     - Specifies the sink compaction interval. If this value is zero, sink compaction will run every time
       the pipe runs. If it is larger than zero, sink compaction will only run if at least
       ``compaction_interval`` seconds has passed since the last sink compaction. The use-case for this setting is
       to prevent a pipe that run often from constantly trying to compact the sink-dataset.
     - ``0``
     - No



.. _circuit_breakers_section:

Circuit breakers
----------------

A circuit breaker is a safety mechanism that one can enable on the
:ref:`dataset sink <dataset_sink>`. The circuit breaker will trip if
the number of entities written to a dataset in a pipe run exceeds a
certain configurable limit.

Note that a circuit breaker is only activated if the sink dataset is
populated. In practice this means that the pipe must have ran to
completion at least once. This is to avoid tripping it on the initial
sync.

A tripped circuit breaker will prevent the pipe from running.
It can either be rolled back or committed. Rolling it back
will delete any entities that were written in the pipe run before the
circuit breaker was tripped. Committing it will expose the uncommitted
entities. Both operations resets the circuit breaker so that pipe can
run again.

Compaction will not be performed on datasets with a tripped circuit
breaker. It is also not possible to repost entities to these datasets.

You can rollback or commit the circuit breaker on the dataset page in
the :doc:`Management Studio <management-studio>`, or use the
`service API <api.html#post--datasets-dataset_id>`_.

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

When a pipe completes a successful run the sink dataset will inherit the smallest completeness timestamp value of the source datasets and the related datasets. Inbound pipes will use the current time as the completeness timestamp value (the :ref:`http_endpoint <http_endpoint_source>` can optionally get the completeness value from a request header). This mechanism has been introduced so that a pipe can hold off processing source entities that are more recent than the source dataset's completeness timestamp value. The propagation of these timestamp values is done automatically. Individual datasets can be excluded from completeness timestamp calculation via the ``exclude_completeness`` property on the pipe.  One can enable the completeness filtering feature on a pipe by setting the ``completeness`` property on the :ref:`dataset source <dataset_source>` to ``true``.

.. WARNING::

   Completeness is implicitly incompatible with full rescans as they do not necessarily expose all the latest entities. This means that if deletion tracking is performed by the pipe that has completeness set to ``true`` then the non-covered entity ids will get deleted from the sink dataset. This may or may not be a problem depending on the use-case. Deletion tracking is only performed by pipes with ``dataset`` sinks currently. Set ``deletion_tracking`` to ``false`` on the ``dataset`` sink if you do not want deletion tracking to be performed.

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

       .. _exclude_completeness:
   * - ``exclude_completeness``
     - List<String>
     - A list of dataset ids that should not contribute to the completeness timestamp value. Any
       dataset listed in this property will be ignored when calculating the dataset sink
       completeness timestamp value.

       .. NOTE::

         If all datasets are excluded a new completeness timestamp value will be generated in this pipe.
     - ``[]``
     - No

        .. _include_completeness:
   * - ``include_completeness``
     - List<String>
     - A list of dataset ids that *should* contribute to the completeness timestamp value. All
       datasets listed in this property will be used when calculating the dataset sink
       completeness timestamp value. If this property is not specified, it defaults to a list of all the datasets in the
       pipe's source and transforms, with the exception of datasets that are also specified in ``exclude_completeness``.

       .. NOTE::

         If both ``exclude_completeness`` and ``include_completeness`` specify the same dataset id,
         ``exclude_completeness`` will take priority so that the dataset does not contribute to the sink
         completeness value.
     -
     - No

.. _pipe_metadata:
.. _pipe_metadata_durable:

Metadata
--------

Pipe metadata can be used to annotate a pipe in various user-defined ways. Some keys (documented below) are
reserved for internal use, but otherwise the users are free to add their own metadata settings.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10

   * - Property
     - Type
     - Description
     - Default

   * - ``metadata.durable``
     - Boolean
     - When set to true, this pipe will store its state and data on a high-durability disk. This makes the pipe more
       resilient to data-loss, but will also incur an additional cost, see :ref:`Durable Data <durable-data>`
       for more details.
     - ``false``


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
