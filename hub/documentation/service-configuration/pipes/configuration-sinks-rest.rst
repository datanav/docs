
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
     - A mapping to use for properties not available in the entity. Note that if the ``properties`` object is also
       present in the entity, it will take precedence and the ``properties`` object in the sink configuration will
       be ignored. See the :ref:`"Expected entity shape" <rest_system>` section for more details.
     -
     -

   * - ``payload``
     - Object, string or array
     - The value to use as payload for the operation if not present in the entity. Note that this property can be
       defined in the specified ``operation`` section of the :ref:`REST system <rest_system>` as well. If
       the ``payload`` exists in the entity, then the one in the entity will take
       precedence over any ``payload`` defined on sink or system operation (in that order).
       This property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the named
       variables ``properties``, ``url``, ``request_params``, ``entity`` and ``headers`` available to the template.
     -
     -

   * - ``trace``
     - Boolean or Object
     - This can be set to ``true`` to log the http requests and responses the REST sink sends and receives. This
       information will be added to a "trace" property in the ``pump-completed`` and  ``pump-failed`` events in
       the pipe execution log.
       By default the http headers and the first few bytes of the body is logged. If you need more fine-grained
       control of the logging, you can set ``trace`` to be an object and set the various ``trace.log_*``
       sub-properties (see below for a description of each sub-property).
     - ``false``
     - No

   * - ``trace.log_request_headers``
     - Boolean
     - If the ``trace`` property is an object this sub-property specifies if the request headers will
       be logged in the ``pump-completed``/``pump-completed`` events in the execution-log.
     - ``true``
     - No

   * - ``trace.log_request_body_maxsize``
     - Integer
     - If the ``trace`` property is an object this property specifies how many bytes of the request body should be
       logged in the ``pump-completed``/``pump-completed`` events in the execution-log.
     - 100
     - No

   * - ``trace.log_response_headers``
     - Boolean
     - If the ``trace`` property is an object this sub-property specifies if the response headers will
       be logged in the ``pump-completed``/``pump-completed`` events in the execution-log.
     - ``true``
     - No

   * - ``trace.log_response_body_maxsize``
     - Integer
     - If the ``trace`` property is an object this property specifies how many bytes of the response body should be
       logged in the ``pump-completed``/``pump-completed`` events in the execution-log.
     - 100
     - No

   * - ``trace.log_secret_redacted_bytes``
     - Integer
     - If the ``trace`` property is an object this property specifies how many bytes of each ``$SECRET`` will
       be redacted in the ``pump-completed``/``pump-completed`` events in the execution-log. The
       purpose of this setting is to redact enough of the secrets to render them safe to log, but to
       potentially leave some of the sectret for debugging purposes.
       A value of ``-1`` means to redact all bytes of the secrets. Note that the redaction is only a best-effort
       attempt to prevent secrets from ending up in the logs, there may be cases where secrets leak through in any
       case, so it is best to always check that what ends up being logged looks ok.
     - 600
     - No

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
       these properties in the Jinja templates for the operation using a "{{ properties.key_name }}" syntax. Note that
       if the ``properties`` object is not present in the entity, the ``properties`` property on the sink configuration
       will be used instead (if it is set).
     -
     -

   * - ``operation``
     - String
     - The contents of this property must refer to one of the named ``operations`` registered with the sink's :ref:`REST system <rest_system>`.
       Note that if no default value is defined in the sink configuration, this property is required.
     -
     -

   * - ``operations``
     - Object
     - An object containing the registered operations allowed for the ``operation`` specified. See the
       :ref:`Operation properties <rest_operations>`  section for details. Note that you can also define an
       ``operations`` property on the :ref:`REST system <rest_system>`. If present both places then the sink
       version will take precedence. You need to specify an ``operations`` section  in at least one of them.
       If multiple pipes use the same operation configuration you should consider storing
       it on the system so they can be reused. Note that secrets are only allowed in the ``operations`` property
       defined on the system.
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

If the ``payload-type`` is "form" or "multipart-form" the request will encode the contents as a HTML form submission
with either a ``application/x-www-form-urlencoded`` or ``multipart/form`` Content-Type, respectively.
The form variables and corresponding values should be given as a dictionary of variable-name/variable-value pairs as
the contents of ``payload``:

::

  {
    "_id": "3",
    "operation": "form-or-multi-part-form-operation",
    "payload": {
        "form-variable": "form-value",
        "other-form-variable": "other-form-value"
      }
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

