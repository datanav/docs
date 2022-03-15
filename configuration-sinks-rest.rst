
.. _rest_sink:

REST sink
---------

This is a data sink that can communicate with a REST service using HTTP requests.

Note that the shape of the entities piped to this sink must conform to certain criteria, see the
:ref:`notes <rest_expected_rest_entity_shape>` later in the section.

The pipe's :ref:`batch_size <pipe_batching>` defaults to 1 when this sink-type is being used.

Prototype
^^^^^^^^^

::

    {
        "type": "rest",
        "system" : "rest-system",
        "operation": "the-default-operation",
        "rate_limiting_retries": 3,
        "rate_limiting_delay": 60,
        "properties": {
           "the-default": "properties"
        },
        "payload": {
           "the-default": "payload"
        }
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
     - The id of the :ref:`REST system <rest_system>` to use.
     -
     - Yes

   * - ``operation``
     - String
     - The default id of the operation to use if not present in the entity.
     -
     -

   * - ``properties``
     - Object
     - The properties mapping to use if not present in the entity. Note that if both are present the properties in
       the entity takes precendence.
     -
     -

   * - ``payload``
     - Object, string or array
     - The default value to use as payload if not present in the entity.
     -
     -

.. _rest_expected_rest_entity_shape:

Expected entity shape
^^^^^^^^^^^^^^^^^^^^^

The entities must be transformed into a particular form before being piped to the RESTsink. The general form
expected is:

::

  {
    "_id": "1",
    "properties": {
        "foo": "bar",
        "zoo": 1,
        "baz": [1,2,3]
    },
    "operation": "some-named-operation",
    "payload": "<some>string-value</some>"
  }

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req


   * - ``properties``
     - Object
     - Any non-payload properties you need should go into the toplevel child entity ``properties``. You can then address
       these properties in the Jinja templates for operation ``url`` properties using the "{{ properties.key_name }}" syntax.
     -
     -

   * - ``operation``
     - String
     - The contents of this property must refer to one of the named ``operations`` registered with the sink's :ref:`REST system <rest_system>`.
       Note that if no default value is defined in the sink configuration, this property is required.
     -
     -

   * - ``payload``
     - String or Object
     - The payload for the operation specified. It can be a string or an object. You can also omit it, in which case
       the empty string will be used instead (for example for "DELETE" methods). All string payloads will be encoded
       as UTF-8.
     -
     -

   * - ``rate_limiting_retries``
     - Integer
     - If set and the REST service returns a HTTP 429 error code, the request will be retried the number of times
       indicated. The time between retries can be adjusted by setting ``rate_limiting_delay``.
     -
     -

   * - ``rate_limiting_delay``
     - Integer
     - If ``rate_limiting_retries`` is set on either the sink or on the REST system, and a retry is triggered
       the time to wait before retrying can be set by this value. If specified on both the system and sink,
       the sink value takes precedence.
     - 1
     -

Example entities:

String as payload:

::

  {
    "_id": "1",
    "properties": {
        "foo": "bar",
        "zoo": 1,
        "baz": [1,2,3]
    },
    "operation": "some-named-operation",
    "payload": "<some>string-value</some>"
  }

Object as payload (set operation ``payload-type`` to "json", "json-transit" or "form"  in the :ref:`REST system <rest_system>` the sink uses):

::

  {
    "_id": "2",
    "properties": {
        "foo": "bar",
        "zoo": 1,
        "baz": [1,2,3]
    },
    "operation": "some-other-operation",
    "payload": {
        "payload": "property",
        "child": {
          "foo": "bar"
        }
    }
  }

Multi-part form request if ``payload-type`` is "form", otherwise use "json" or "json-transit" for this type of entity:

::

  {
    "_id": "3",
    "operation": "some-third-operation",
    "payload": [
      {
        "foo": "bar"
      },
      {
        "zoo": "foo"
      }
    ]
  }

Example configuration
^^^^^^^^^^^^^^^^^^^^^

See the :ref:`REST system example <rest_system_example>` section for how to configure the operations we refer to in
these examples:

::

    {
        "type" : "pipe",
        "sink" : {
            "type" : "rest",
            "system" : "our-rest-service",
            "operation": "update-woman",
            "properties": {
                "sex": "F"
            },
            "payload": {
              "id": "unknown",
              "collection_name": "study-group-1"
            }
        }
    }

Example input entities:

::

    [
        {
            "_id": "john",
            "operation": "update-man",
            "properties": {
                "id": "john",
                "age": 21,
                "sex": "M"
            },
            "payload": "<man id=\"john\">john</man>"
        },
        {
            "_id": "mary",
            "properties": {
                "id": "mary",
                "age": 23,
                "collection_name": "study-group-2"
            },
            "payload": {
              "id": "mary",
              "age": 23
            }
        },
        {
            "_id": "bob",
            "operation": "delete-man",
            "properties": {
                "collection_name": "study-group-1"
            }
        }
    ]

