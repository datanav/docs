.. _metrics-api:

Metrics API
===========

If the ``Monitoring and metrics`` product is enabled on the Sesam subscription, then the ``/api/metrics`` endpoint is available. This API endpoint exposes `Prometheus <https://prometheus.io/>`_ compatible
metrics.

Note that you need a JWT token with ``Admin`` role to be able to scrape the endpoint.

Example:

::

   curl -s -H "Authorization: bearer $JWT" "$SESAM_API_URL/metrics"


See the :doc:`Metrics <../metrics>` documentation for more information about the metrics exposed.