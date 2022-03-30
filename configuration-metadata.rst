.. _service_metadata_section:


Service metadata
----------------


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
         "use_signalling_internally": true,
         "default_compaction_type": "sink",
         "symmetric_namespace_collapse": false
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
       The default setting of this property is ``true`` which means signalling is turned on for all :ref:`dataset-type sources <dataset_source>` in the
       installation. You can turn this feature on or off individually by setting the ``supports_signalling`` flag on the
       :ref:`dataset source <dataset_source>` (including variants like
       :ref:`merge <merge_source>`, :ref:`union datasets <union_datasets_source>` and
       :ref:`merge datasets <merge_datasets_source>` sources). Note that signalling support is "best-effort" only; signals are not persisted so
       delivery is not guaranteed. For this reason, pipes in such flows should always have scheduled interval as a "backup".
       Also note that if the scheduled interval on a pipe is less than 2 minutes or if the scheduling is cron based or the schedule interval
       is equal or greater than an hour (3600 seconds), signalling will be disabled for the pipe source (if it's only set globally).
       However, if you set ``supports_signalling`` explicitly on the pipe source it will be turned on regardless of the pump schedule.
     - ``true``
     -

       .. _service_metadata_global_defaults_compaction_settings:

   * - ``global_defaults.default_compaction_type``
     - Enum<String>
     - Specifies the default compaction type. It can be set to ``"background"`` or ``"sink"``. Background compaction
       will run once every 24 hours. Sink compaction will normally run every time the pipe runs, but this can be
       tweaked with the ``global_defaults.compaction_interval`` setting.
     - ``"sink"``
     -

   * - ``global_defaults.compaction_interval``
     - Float
     - Specifies the default sink compaction interval. If this value is zero, sink compaction will run every time
       the pipe runs. If it is larger than zero, sink compaction will only run if at least
       ``compaction_interval`` seconds has passed since the last sink compaction. The use-case for this setting is
       to prevent pipes that run often from constantly trying to compact the sink-dataset.
     - ``0``
     -

   * - ``global_defaults.compaction_keep_versions``
     - Integer
     - The number of unique versions of an entity to keep around.
       The value must be greater than or equal to ``0``. If set to ``0`` then a time
       threshold must be set explicitly.

       .. WARNING::

          A value less than ``2`` means that dependency tracking is best effort only,
          and it will not be able to find all reprocessable entities. Do full or partial
          rescans as a counter measure.

     -
     -

   * - ``global_defaults.compaction_time_threshold_hours``
     - Integer
     - Specifies the threshold for how old entities must be before they are considered
       for compaction. This property is usually used when you want to keep entities
       around for a certain time.
     -
     -

   * - ``global_defaults.compaction_time_threshold_hours_pump``
     - Integer
     - Same as ``compaction_time_threshold_hours``, but applies to the pipe's pump
       execution dataset. Pump execution datasets are always trimmed by time.
     -
     -

   * - ``global_defaults.compaction_growth_threshold``
     - Float
     - The growth factor required for the automatically scheduled compaction to kick
       in. A value of ``1.1`` mean that there must have been 10% new offsets written to
       the dataset since the last compaction. ``1.0`` is the minimum value allowed.
     -
     -

   * - ``global_defaults.max_entity_bytes_size``
     - Integer
     - Defines the maximum size in bytes of an individual entity as it is stored in a dataset.
     - ``104857600`` (100MB)
     -

   * - ``global_defaults.use_config_circuit_breaker``
     - Boolean
     - When set to true, activates the circuit breaker for uploading configuration to the node. When activated, any changes to the node configuration that would result in the deletion of more than 10% of the existing components will not go through (this is the case only when the number of deleted components is also more than 10).
     - False
     -

       .. _service_metadata_global_defaults_enable_background_rescan:

   * - ``global_defaults.enable_background_rescan``
     - Boolean
     - When set to true, enables running :ref:`pipe rescans <pipe_rescans>` in the background for all applicable pipes.
     - False
     -

       .. _service_metadata_global_defaults_eager_load_microservices:

   * - ``global_defaults.eager_load_microservices``
     - Boolean
     - When set to false, Sesam can hold off starting up microservices which aren't connected to any pipes. Set to true to force all microservices to start up regardless.
     - True
     -

       .. _service_metadata_global_defaults_symmetric_namespace_collapse:

   * - ``global_defaults.symmetric_namespace_collapse``
     - Boolean
     - When set to true, the expand and collapse features will be symmetrical, i.e. data containing namespaced identifiers read into Sesam will map to the same thing
       on the way out of Sesam. Note that setting this option to ``true`` as assumed by the DTL ``ni-collapse`` and ``ni-expand`` DTL functions
       will also alter the URI/NI collapse and expand behaviour of the RDF and SPARQL source and sink.
     - False
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
