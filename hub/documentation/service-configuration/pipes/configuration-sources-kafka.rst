.. _kafka_source:

Kafka source
-----------------

The Kafka source consumes data from a Kafka topic. The consumer does not use a consumer group, but instead stores the offset in the pipe, and it does not commit the consumer offset back to Kafka.

The entities emitted from this source has the properties ``"offset"``, ``"partition"``, ``"timestamp"``, ``"key"``, ``"key_schema"``, ``"value"`` and ``"value_schema"``. If key deserialization fails and ``"strict"`` is ``false`` then the entity will also have an ``"invalid_key"`` property. Similarly if value deserialization fails and ``"strict"`` is ``false`` then the entity will also have an ``"invalid_value"`` property.

.. NOTE::


   The ``"_id"`` property will be added to the entities if the key is deserialized successfully and it is not null or bytes. If the ``"_id"`` property cannot be constructed then a pipe transform must add it before writing the entities to the dataset sink. 

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

   * - ``strict``
     - Boolean
     - If the key or value cannot be deserialized then the pipe will fail if ``"strict"`` is ``true``. If ``false`` then pipe won't fail, but an invalid key will be stored in the ``"invalid_key"`` property and an invalid value will stored in the ``"invalid_value`` property. Note that if key serialization fails then the resulting entity won't have an ``"_id"`` property, so that must be dealt with in the pipe.
     - ``true``
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
