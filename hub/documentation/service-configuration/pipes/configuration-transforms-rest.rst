.. _REST_transform:

REST transform
--------------

This transform can communicate with a REST service using HTTP requests.

Note that by default the REST transform will only attempt to parse responses with content-type "application/json", if
the REST API provides other types of valid JSON, you can specify which in the ``json_content_types`` property of
the associated :ref:`REST system <rest_system>`.

Responses which aren't recognised as JSON will make the REST transform emit entities with a property containing
the raw response body and - optionally - the content-type of the response for further processing with DTL and/or
HTTP or REST transform(s).

Note that the shape of the entities piped to this transform must conform to certain criteria, see the
:ref:`notes <rest_transform_expected_rest_entity_shape>` later in the section.

Also note that, in contrast to the REST sink, the REST transform also supports the GET operation.

Prototype
^^^^^^^^^

::

    {
        "type": "rest",
        "system" : "rest-system",
        "operation": "the-default-operation",
        "properties": {
           "the-default": "properties"
        },
        "payload": {
           "the-default": "payload"
        },
        "trigger_on": {
            "key":"_trigger",
            "value": "some-value*"
        },
        "rate_limiting_retries": 3,
        "rate_limiting_delay": 60,
        "response_property": "the-property-name-to-put-the-response-in",
        "response_include_content_type": false,
        "payload_property": "the-property-the-response-resides-in",
        "id_expression": "{{ jinja_expression_for_the_id.property }}",
        "updated_expression": "{{ jinja_expression_for_the_updated_property }}",
        "ignored_status_codes": "404,444-450,501-599"
        "if_transform_empty": "allow"
    }

.. _REST_transform_properties:

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

   * - ``side_effects``
     - Boolean
     - Set to ``false`` if the transform does not have side-effects. A side-effect means that it causes changes to the system that it talks to. The intention of this property is to prevent inadvertent changes to the system by features like pipe preview. You can set this to ``false`` if you're sure your transform is free from side-effects or if you don't mind changes happening when previewing a pipe.
     - ``true``
     -

   * - ``response_property``
     - String
     - The name of the property to store the result returned from the REST service. Note that if the ``replace_entity``
       property is set to ``true`` and the service returns JSON data, this JSON data will be returned as entities. If
       the data type is not JSON, the result will be an empty entity with the same ``_id`` as the original with
       the ``response_property`` set to the contents of the request reponse body as a string. If ``replace_entity`` is
       set to ``false``, the ``response_property`` will be added to the original entity and set to the contents of the
       request response body as a string or a parsed JSON structure if that is the returned content type.

     - ``"response"``
     -

   * - ``response_headers_property``
     - String
     - The name of the property to put the response headers in when emitting entities. Note that this property can be
       defined in the :ref:`REST system <rest_system>` operation configuration as well. The configuration in the
       transform will take precedence if both are defined. Also note that this property will only be set if
       ``replace_entity`` is set to ``false``.
     -
     -

   * - ``response_status_property``
     - String
     - The name of the property to put the response status code in when emitting entities. Note that this property can be
       defined in the :ref:`REST system <rest_system>` operation configuration as well. The configuration in the transform
       will take precedence if both are defined. Also note that this property will only be set if
       ``replace_entity`` is set to ``false``.
     -
     -

   * - ``replace_entity``
     - Boolean
     - This property controls if the entity should be replaced with the JSON contents of the response or if the
       original entity should be kept. See the ``response_property`` for more detail on how this works. The default
       is to keep the original entity and add a ``response`` property holding the result of the REST operation.
       Note that this property should normally not be altered, it's primarily intended for backwards compatibility with
       ported :ref:`HTTP transforms <http_transform>`. When set to ``true`` the ``id_expression``,
       ``updated_expression`` and ``error_expression`` expressions are not evaluated and the response is passed through
       directly in the form returned by the system operation (assumed to be a JSON object or list of objects).
     - ``false``
     -

   * - ``response_include_content_type``
     - Boolean
     - This property controls if the output entity should include the Content-Type of the response in a
       ``content-type`` property. Note that this property is ignored if ``replace_entity`` is set to ``true`` and
       the response is JSON.

     - ``false``
     -

   * - ``operation``
     - String
     - The default id of the operation to use if not present in the entity.
     -
     -

   * - ``operations``
     - Object
     - An object containing the properties used for the ``operation`` specified in the transform configuration or
       in the entity. See the :ref:`Operation properties <rest_operations>` section for details. Note that you can also
       define an ``operations`` property on the :ref:`REST system <rest_system>`. If present in multiple places then the
       transform version will take precedence. You need to specify an ``operations`` section in at least one of them.
       If multiple pipes use the same operation configuration you should consider storing
       it on the system so they can be reused. Note that secrets are only allowed in the ``operations`` property
       defined on the :ref:`REST system <rest_system>`.
     -
     -

   * - ``properties``
     - Object
     - Any non-payload properties you need can be specified in the ``properties`` property. You can then address
       these in the Jinja templates for the operation or source using a "{{ properties.key_name }}" syntax.
       Note that if a ``properties`` object is present in the entity, the ``properties`` object in the transform
       configuration will be ignored.
     -
     -

   * - ``trigger_on`` (experimental)
     - Object
     - A dictionary with two properties: ``"key"`` (optional, defaults to ``"_trigger"``) and ``"value"``. The ``"key"``
       should point to a property in the entity (it supports path notation) and ``"value"`` should contain a value that
       this property should have to be passed into the transform. The ``"value"`` supports wildcards ("*") for substring
       matching. If the ``"key"`` doesn't exist or the ``"value"`` does not match the corresponding value in the entity,
       the entity will be passed through without being transformed. Note that this property is experimental and may
       be changed or removed.
     -
     -

   * - ``payload``
     - Object, string or array
     - The value to use as payload for the operation if not present in the entity. Note that this property can be
       defined in the specified ``operation`` section of the :ref:`REST system <rest_system>` as well. If
       the ``payload`` exists in the entity, then the one in the entity will take
       precedence over any ``payload`` defined on transform or system operation (in that order). This property
       supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the named variables
       ``properties``, ``url``, ``request_params``, ``entity`` and ``headers`` available to the template.
       If the operation supports paging then ``previous_body``, ``previous_request_headers``, ``previous_params``
       and ``previous_headers`` (response headers) are available for all page requests except the
       first. In addition ``page`` (integer, starting at 0) and ``is_first_page`` (a boolean flag) are available for all
       requests in paged operations. Tip: use Jinja's
       `"is defined" <https://jinja.palletsprojects.com/en/3.1.x/templates/#tests>`_ tests for these variables to set
       default values for the first page.
     -
     -

   * - ``payload_property``
     - String
     - The JSON response sub-property to use as the source of the emitted entities. Note that this property can be
       defined in the specified ``operation`` section of the :ref:`REST system <rest_system>` as well. The transform
       configuration will take precedence if defined. This property can express a "path" into the response using a dot
       as path separator, i.e. ``foo.bar``. Note that a if a "non-path" version of the property can be found in the
       response body it will take precedence over any property found by traversing the path using the dot notation.
     -
     -

   * - ``id_expression``
     - String
     - The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the entities
       properties available to the templating context. It can be used to add ``_id`` properties to the emitted entities
       if missing from the transform response. Note that this property can be defined
       in the specified ``operation`` section of the :ref:`REST system <rest_system>` as well. The transform configuration
       will take precedence if defined.  The bound parameters available to this template are ``body``, ``url``,
       ``request_params``, ``properties``, ``entity``, ``source_entity`` and ``headers``. If the operation supports
       paging then ``previous_body``, ``previous_request_headers``, ``previous_params`` and ``previous_headers``
       (response headers) are available for all page requests except the first. In addition ``page`` (integer, starting
       at 0) and ``is_first_page`` (a boolean flag) are available for all requests in paged operations.
       Tip: use Jinja's `"is defined" <https://jinja.palletsprojects.com/en/3.1.x/templates/#tests>`_ tests for these
       variables to set default values for the first page.
     -
     -

   * - ``updated_expression``
     - String
     - The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the entities
       properties available to the templating context. It can be used to add ``_updated`` properties to the emitted
       entities if missing from the transform response. Note that this property can alternatively be defined in the
       specified ``operation`` section of the :ref:`REST system <rest_system>`. The transform configuration will take
       precedence if defined. This template supports the same named variables as ``id_expression``.
     -
     -

   * - ``allowed_status_codes``
     - String
     - An expression in the form of single values or value ranges of HTTP status codes that will be allowed to be passed
       through by the transform. The values are either comma separated integer values or a range of values with a hyphen separator
       (i.e. a single ``-`` character). The start and end of a range are inclusive, i.e. 200-299 includes both 200 and
       299. Whitespaces are not allowed in the expression. Note that ``200-299`` are the default status codes and any response
       status codes other than this will make the transform fail. See the complimentary ``ignored_status_codes``
       if you want to omit non-ok responses instead of them making the transform fail or passing them through. Also note
       that the ranges in ``ignored_status_codes`` cannot overlap with ``allowed_status_codes``.

       .. WARNING::

          If you allow other status codes than the default, *make sure* that these are dealt with downstream.

     - ``"200-299"``
     -

   * - ``ignored_status_codes``
     - String
     - An expression in the form of single values or value ranges of HTTP status codes that will be ignored by the
       transform. HTTP responses with status codes matching this list will result in the response being omitted from
       the result. The values are either comma separated integer values or a range of values with a hyphen separator
       (i.e. a single ``-`` character). The start and end of a range are inclusive, i.e. 400-403 includes both 400 and
       403. Whitespaces are not allowed in the expression. See the complimentary ``allowed_status_codes`` if you
       want to pass through any non-ok responses instead of skipping them. Also note that the ranges in
       ``ignored_status_codes`` cannot overlap with ``allowed_status_codes``.

       .. WARNING::

          Any response with status codes listed here will be discarded with no traces to be found, making it next to
          impossible to audit the pipe.

     -
     -

   * - ``if_transform_empty``
     - Enum<String>
     - Determines the behaviour of the pipe when the REST transform does not produce any entities. The default value is
       ``"accept"`` which means that any previously emitted entities might be deletion tracked if the pipe is doing a
       full run, and the sink is a dataset sink. If set to ``"fail"`` the pipe will instead fail if the transform
       unexpectedly produce no entities thus preventing potential deletion tracking downstream.
     - ``"accept"``
     -

   * - ``rate_limiting_retries``
     - Integer
     - If set and the REST service returns a HTTP 429 error code, the request will be retried the number of times
       indicated. The time between retries can be adjusted by setting ``rate_limiting_delay``.
     -
     -

   * - ``rate_limiting_delay``
     - Integer
     - If ``rate_limiting_retries`` is set on either the transform or on the REST system, and a retry is triggered
       the time to wait before retrying can be set by this value. If specified on both the system and transform,
       the transform value takes precedence.
     - 1
     -


   * - ``trace``
     - Boolean or Object
     - This can be set to ``true`` to log the http requests and responses the REST transform sends and receives. This
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
       potentially leave some of the secret for debugging purposes.
       A value of ``-1`` means to redact all bytes of the secrets. Note that the redaction is only a best-effort
       attempt to prevent secrets from ending up in the logs, there may be cases where secrets leak through in any
       case, so it is best to always check that what ends up being logged looks ok.
     - 600
     - No

.. _rest_transform_expected_rest_entity_shape:

Expected entity shape
^^^^^^^^^^^^^^^^^^^^^

The entities must be transformed into a particular form before being piped to the REST transform. The general form
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
     - The contents of this property must refer to one of the named ``operations`` registered with the transform's :ref:`REST system <rest_system>`.
       Note that if no default value is defined in the transform configuration, this property is required.
     -
     -

   * - ``payload``
     - String or Object
     - The payload for the operation specified. It can be a string or an object. You can also omit it, in which case
       the empty string will be used instead (for example for "DELETE" methods). All string payloads will be encoded
       as UTF-8.
     -
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

Object as payload (set operation ``payload-type`` to "json", "json-transit" or "form"  in the :ref:`REST system <rest_system>` the transform uses):

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
        "transform" : {
            "type" : "rest",
            "system" : "our-rest-service",
            "operation": "post-man",
            "properties": {
                 "collection_name": "study-group-2"
            }
        }
    }

Example input entities:

::

    [
      {
          "_id": "bob",
          "operation": "get-man",
          "properties": {
              "collection_name": "study-group-1"
          }
      }
    ]


Example output entities:

::

    [
      {
          "_id": "bob",
          "operation": "get-man",
          "properties": {
              "collection_name": "study-group-1"
          },
          "response": {
              "name": "Bob Maker"
              "email": "bob.maker@example.com"
          }
      }
    ]

Pagination support
^^^^^^^^^^^^^^^^^^

See the the :ref:`REST source examples <rest_source_examples>` for how to use pagination with the REST transform -
the configuration set up is the same as with the REST source.
