.. _metrics-api:
.. _metrics_api:

:badge:`Paid feature,badge-info badge-pill`

======================
Metrics and monitoring
======================

Enabling the metrics and monitoring feature will give you access to a set of tools that help you monitor your subscription. This bundle includes features like custom notifications, insights, and the metrics API.

How to enable
=============

Metrics and monitoring is now available for all subscriptions with clustered architecture. This is how you can activate the new feature:

- Login to the `Sesam portal <https://portal.sesam.io />`_

- Select the subscription you want to use

- Navigate to Subscription on the left menu

- Click on Products tab

- Click on “Enable Metrics and monitoring”


Pricing
=======

Follow the steps above to check how this feature affect your monthly price. 

Metrics API
===========

This feature will make the ``/api/metrics`` endpoint available. This API endpoint exposes `Prometheus <https://prometheus.io/>`_ compatible
metrics. 

After enabling the feature, you will need to set up a prometheus database, then you can use tools, like Grafana, to create your own dashboards.

.. note::
   You need a JWT token with ``Admin`` role to be able to scrape the endpoint.

Example:

.. code-block:: python

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
     - Is the circuit-breaker tripped? 1.0 if tripped, otherwise 0.0.


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


Monitoring
==========

Monitoring allows you to see pipe insights and set up custom pipe notifications.

Insights
--------

After enabling metrics and monitoring, you can enable insights in the pipe you want to monitor. You will then have access to charts that show how many entities, errors and latencies there have been for the current pipe during the last 30 days.

To enable insights on a specific pipe:

- Navigate to the pipe you want to monitor
- Find the Insight tab
- Enable insights

.. important::
   Monitoring data collection will start only after you enable insights in a specific pipe.

Notifications
-------------

Add notification rules to pipes and get alerts when those rules are triggered. You can get notification alerts either in the user-interface or by email.

To see how to use custom notifications, please visit the :doc:`notification documentation <notifications-feature>`.
