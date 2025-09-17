.. _kafka_sink:

Kafka sink
--------------

The Kafka sink produces data to a Kafka topic.

Entities sent to this sink will use the ``"key"``, ``"value"``, ``"key_schema"`` and ``"value_schema"`` properties to produce the message sent to the Kafka topic. The latter two properties are only relevant if the ``"confluent_schema_json"`` serializer is used. ``"key"`` and``"value"`` are mandatory.

The properties used matches the properties emitted by the :ref:`Kafka source <kafka_source>`. This means that it should be possible to consume a topic and produce to a new topic in a pipe with no DTL.

The sink will flush to Kafka after every batch.

Prototype
^^^^^^^^^

.. code-block:: json

    {
        "type": "kafka",
        "system": "kafka-system-id",
        "topic": "some-topic"
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
     - The id of the :ref:`Kafka System <kafka_system>` component to use.
     -
     - Yes

   * - ``topic``
     - String
     - The topic to send to.
     -
     - Yes

   * - ``key_serializer``
     - String
     - Name of the serializer to use for the key. Allowed values are ``"bytes"``, ``"string"``, ``"json"``, ``"confluent_schema_json"``.
     - ``"string"``
     -

   * - ``value_serializer``
     - String
     - Name of the serializer to use for the value. Allowed values are ``"bytes"``, ``"string"``, ``"json"``, ``"confluent_schema_json"``.
     - ``"json"``
     -

   * - ``delivery_timeout_ms``
     - Integer
     - The time in milliseconds to await acknowledgement from the broker and the time allowed for retriable send failures.
     - ``120000``
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity.

.. code-block:: json

    {
        "sink": {
            "type": "kafka",
            "system": "my-kafka",
            "topic": "foo",
            "key_serializer": "string",
            "value_serializer": "json"
        },
    }
