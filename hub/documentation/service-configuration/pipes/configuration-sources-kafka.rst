.. _kafka_source:

Kafka source
-----------------

The Kafka source consumes data from a Kafka topic. The consumer stores the offset in the pipe, and does not commit the consumer offset back to Kafka.

The entities emitted from this source has offset, partition, timestamp, value and key as properties. Message keys in Kafka can be any bytes, but the source will try to utf-8 decode the key and add that as the ``_id`` property.

Prototype
^^^^^^^^^

::

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
     - The topic to consume from.
     -
     - Yes

   * - ``partitions``
     - List<Integer>
     - Manual assignment of partitions if only a subset of the topic is to be consumed by this pipe. In Azure Event Hubs this property
       has to be set for assignment to work for now.
     - <All>
     - No (Yes for Event Hubs)

   * - ``seek_to_beginning``
     - Boolean
     - If the consumer should start from the beginning of the topic or only consume new messages. This only applies to the first run,
       subsequent runs will continue where it left off unless the pipe is reset.
     - ``true``
     -

   * - ``key_deserializer``
     - String
     - Name of the deserializer to use for the key. Allowed values are ``"bytes"``, ``"string"``, ``"json"``, ``"confluent_schema_json"``.
     - ``"string"``
     -

   * - ``value_deserializer``
     - String
     - Name of the deserializer to use for the value. Allowed values are ``"bytes"``, ``"string"``, ``"json"``, ``"confluent_schema_json"``.
     - ``"json"``
     -

   * - ``consumer_timeout_ms``
     - Integer
     - The pipe will consume all available messages from the topic. Once all messages has been consumed it will wait for this period of
       time until it will complete. Note that for topics that receives new messages more often than this interval the pipe will never
       complete.
     - 10000
     -

Example configuration
^^^^^^^^^^^^^^^^^^^^^

The outermost object would be your :ref:`pipe <pipe_section>`
configuration, which is omitted here for brevity.

::

    {
        "source": {
            "type": "kafka",
            "system": "my-kafka",
            "topic": "foo",
            "consumer_timeout_ms": 10000,
            "partitions": [0, 1],
            "key_deserializer": "string",
            "value_deserializer": "json"
        },
    }
