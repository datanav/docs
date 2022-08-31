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

.. code-block:: python


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

.. _pipe_metadata:

Example configuration
---------------------

The following example shows a pipe definition that exposes data from HubSpot's REST API through the endpoint **companies**, and feeds it into a sink that writes the data into a dataset with the same ``_id`` as the pipe.

.. code-block:: json
  
    {
      "_id": "hubspot-company-collect",
      "type": "pipe",
      "source": {
        "type": "rest",
        "system": "hubspot",
        "id_expression": "{{ id }}",
        "operation": "get",
        "payload_property": "results",
        "properties": {
          "url": "companies"
        }
      },
      "add_namespaces": false,
      "namespaced_identifiers": false
    }

Pipe Features
-------------

The following are available features that can be activate and/or changed on any pipe in Sesam. 


.. list-table::
   :header-rows: 1
   :widths: 10, 60

   * - Feature
     - Description

   * - ``Compaction``
     - :ref:`Compaction <compaction-feature>` decides how and when old entities should re removed from datasets.

   * - ``Circuit breakers``
     - :ref:`Circuit breakers <circuit-breakers>` prevent pipes from running if the number of changed entities is too large.

   * - ``Automatic reprocessing``
     - :ref:`Automatic reprocessing <automatic-reprocessing>` automatically resets a pipe when it is out of sync with its input data.

   * - ``Completeness``
     - :ref:`Completeness <completeness-feature>` lets pipes hold of processing of data until upstream dependencies are processed.

   * - ``Namespaces``
     - :ref:`Namespaces <namespaces-feature>` allows tracking of property origins in Sesam.

   * - ``Durable data``
     - :ref:`Durable data <durable-data>` allows additional data storage to minimize likelihood of dataloss.