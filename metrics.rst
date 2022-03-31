Metrics
=======

If the ``Monitoring and metrics`` product is enabled on the Sesam
subscription, then the ``/api/metrics`` endpoint is available. This
API endpoint exposes `Prometheus <https://prometheus.io/>`_ compatible
metrics. The metrics are described below.

Note that you need a JWT token with ``Admin`` role to be able to
scrape the endpoint.

Example:

::

   curl -s -H "Authorization: bearer $JWT" "$SESAM_API_URL/metrics"


Service metrics
---------------

.. list-table::
   :header-rows: 1
   :widths: 30, 10, 60

   * - Metric
     - Type
     - Description

   * - ``sesam_health``
     - Enum<healthy|unhealthy|unknown>
     - Is the Sesam API up?

   * - ``sesam_backup_health``
     - Enum<healthy|unhealthy|unknown>
     - Are there any failed backups?


Pipe metrics
------------

.. list-table::
   :header-rows: 1
   :widths: 30, 10, 60

   * - Metric
     - Type
     - Description

   * - ``sesam_pipe_queue_source``
     - Gauge
     - Number of source entities in the pipe queue

   * - ``sesam_pipe_queue_tracking``
     - Gauge
     - Number of untracked entities in the pipe queue

   * - ``sesam_pipe_queue_replicas``
     - Gauge
     - Number of entities in the pipe's replica queues

   * - ``sesam_pipe_sink_dataset_count_index_exists``
     - Gauge
     - Number of non-deleted entity ids in the sink dataset

   * - ``sesam_pipe_sink_dataset_count_index_deleted``
     - Gauge
     - Number of deleted entity ids in the sink dataset

   * - ``sesam_pipe_sink_dataset_count_log_exists``
     - Gauge
     - Number of non-deleted entities in the sink dataset log

   * - ``sesam_pipe_sink_dataset_count_log_deleted``
     - Gauge
     - Number of deleted entities in the sink dataset log

   * - ``sesam_pipe_dead_letter_dataset_count_index_exists``
     - Gauge
     - Number of non-deleted entity ids in the dead-letter dataset

   * - ``sesam_pipe_dead_letter_dataset_count_index_deleted``
     - Gauge
     - Number of deleted entity ids in the dead-letter dataset

   * - ``sesam_pipe_dead_letter_dataset_count_log_exists``
     - Gauge
     - Number of non-deleted entities in the dead-letter dataset log

   * - ``sesam_pipe_dead_letter_dataset_count_log_deleted``
     - Gauge
     - Number of deleted entities in the dead-letter dataset log

   * - ``sesam_pipe_circuit_breaker_tripped``
     - Gauge
     - Is the circuit-breaker tripped? 1.0 if tripped otherwise 0.0.


Pump metrics
------------

.. list-table::
   :header-rows: 1
   :widths: 30, 10, 60

   * - Metric
     - Type
     - Description

   * - ``sesam_pump_started``
     - Counter
     - The number of pump-started events. Note: no-op runs are not counted currently.

   * - ``sesam_pump_completed``
     - Counter
     - The number of pump-completed events. Note: no-op runs are not counted currently.

   * - ``sesam_pump_failed``
     - Counter
     - The number of pump-failed events.

   * - ``sesam_pump_entities_changes``
     - Counter
     - The number of entities changed

   * - ``sesam_pump_entities_seen``
     - Counter
     - The number of entities seen

   * - ``sesam_pump_entities_compacted``
     - Counter
     - The number of entities compacted away

   * - ``sesam_pump_entities_deletion_tracked``
     - Counter
     - The number of entities deletion tracked
