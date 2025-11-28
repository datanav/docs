.. _kafka_system:

The Kafka system
----------------

This system can be used to read and write data from `Apache Kafka <https://kafka.apache.org>`_ as well as `Azure Event Hubs for Apache Kafka <https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-for-kafka-ecosystem-overview>`_.

Prototype
^^^^^^^^^

.. code-block:: json

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:kafka",
        "bootstrap_servers": "somehost:9092,otherhost:9092",
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

   * - ``bootstrap_servers``
     - String
     - Comma separated list of bootstrap servers with hostname and port. For Azure Event Hubs this should be set to ``<fqdn>:9093``.
     -
     - Yes

   * - ``sasl_username``
     - String
     - Username to use when authenticating against a SASL enabled Kafka cluster. If username is set, authentication will be performed.
       For Azure Event Hubs this property must be set to ``$ConnectionString`` and the connection string should be passed as the
       password.
     -
     - No

   * - ``sasl_password``
     - String
     - Password to use when authenticating against a SASL enabled Kafka cluster. For Azure Event Hubs this should be set to ``Endpoint=sb://[...]``.
     -
     - No

   * - ``registry_url``
     - String
     - The URL of the schema registry endpoint.
     -
     - No

   * - ``registry_username``
     - String
     - The username to use when authenticating against the schema registry.
     -
     - Required when ``registry_url`` is specified.

   * - ``registry_password``
     - String
     - The password to use when authenticating against the schema registry.
     -
     - Required when ``registry_url`` is specified.

