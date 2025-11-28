.. _kafka_sink:

Kafka sink
--------------

The Kafka sink produces data to a Kafka topic.

Entities sent to this sink will use the ``"key"``, ``"value"``, ``"headers"``, ``"key_schema"`` and ``"value_schema"`` properties to produce the messages sent to the Kafka topic. The latter two properties are only relevant if the ``"confluent_schema_json"`` serializer is used. The properties ``"key"`` and ``"value"`` are mandatory. The ``"headers"`` property is optional, but it must be an object with string keys and string or bytes values if present.

The properties used matches the properties emitted by the :ref:`Kafka source <kafka_source>`. This means that it should be possible to consume a topic and produce to a new topic in a pipe with no DTL.

The sink will flush to Kafka after every batch.

.. NOTE::

   The sink does not do client-side schema valiation at this time. We might add this in a future release.

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

   * - ``strategy``
     - String
     - Name of the strategy to use for the message. Allowed values are ``"key-value"`` and ``"value"``. The ``"key-value"`` will use the ``key`` property as the message key and ``value`` property as the message value. The ``"value"`` strategy will use the sink entity as the message value and the ``_id`` property as the message key.
     - ``"key-value"``
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
