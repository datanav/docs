.. _metrics-api:

:badge:`Paid feature,badge-info badge-pill`

Metrics and monitoring
======================

If the ``Monitoring and metrics`` product is enabled on the Sesam subscription, then the ``/api/metrics`` endpoint is available. This API endpoint exposes `Prometheus <https://prometheus.io/>`_ compatible
metrics.

.. note::
   You need a JWT token with ``Admin`` role to be able to scrape the endpoint.

Example:

.. code-block:: python

   curl -s -H "Authorization: bearer $JWT" "$SESAM_API_URL/metrics"


See the :doc:`Metrics <../metrics>` documentation for more information about the metrics exposed.

How to enable
-------------

Metrics and monitoring is now available for all subscriptions with clustered architecture. This is how you can activate the new feature:

- Login to the `Sesam portal <https://portal.sesam.io />`_

- Select the subscription you want to use

- Navigate to Subscription on the left menu

- Click on Products tab

- Click on “Enable Metrics and monitoring”

If your subscription is not yet on a clustered architecture please take contact with support to start the migration.