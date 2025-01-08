.. _rest_system:

REST system
-----------

The REST system represents a REST service (i.e. a web server) serving
`HTTP requests <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_ from a base url using the REST
vocabulary of GET, PUT, POST, PATCH, OPTIONS and HEAD.

It is used by the :ref:`REST sink <rest_sink>`.

It supports the ``HTTP`` and ``HTTPS`` protocols. It provides session handling, connection pooling and authentication
services to sources and sinks which need to communicate with a HTTP server.

The REST system is an extension of the URL system, so all configuration properties of the :ref:`URL system <url_system>`
apply. We'll only cover the REST system specific properties in this section.

Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-system",
        "name": "Name of system",
        "type": "system:rest",
        "url_pattern": "http://host:port/path/%s",
        "verify_ssl": false,
        "custom_ca_pem_chain": "-----BEGIN CERTIFICATE-----\nMIIGYTCCB[...]\n-----END CERTIFICATE-----\n",
        "username": null,
        "password": null,
        "authentication": "basic",
        "jwt_token": null,
        "connect_timeout": 60,
        "read_timeout": 1800,
        "rate_limiting_retries": 3,
        "rate_limiting_delay": 60,
        "json_content_types": ["application/jsonish"]
        "headers": {
            "MY_HEADER": "some-value",
            "MY_OTHER_HEADER": "$ENV(key-for-other-value)",
            "MY_SECRET_HEADER": "$SECRET(secret-key)"
        },
        "operations": {
            "get-operation": {
                "url" : "/a/service/that/supports/get/{{ _id }}",
                "method": "GET",
                "next_page_link": {{ body.pagination.next }},
                "next_page_termination_strategy": ["next-page-link-empty", "same-next-page-request", "same-response"]
                "id_expression": {{ id }},
                "updated_expression": {{ updated }},
                "payload_property": "result",
                "response_property": "response",
                "since_property_name": "updated",
                "since_property_location": "query|header|manual"
            },
            "delete-operation": {
                "url" : "/a/service/that/supports/delete/{{ _id }}",
                "method": "DELETE",
                "rate_limiting_retries": 3,
                "rate_limiting_delay": 60
            },
            "put-operation": {
                "url" : "/some/service/that/supports/put",
                "method": "PUT",
                "headers": {
                    "Content-type": "application/json"
                },
                "payload-type": "json"
            },
            "post-operation": {
                "url" : "/some/service/that/supports/post",
                "method": "POST",
                "payload-type": "form"
            },
            "patch-operation": {
                "url" : "/some/service/that/supports/patch",
                "headers": {
                    "Content-type": "application/xml"
                },
                "method": "PATCH"
            }
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

   * - ``<any url system property>``
     -
     - The REST system extends the URL system, so any property from the URL system can be applied.
     -
     -

   * - ``headers``
     - Dict<String,String>
     - A optional set of header values to set as defaults in the requests made using the REST system. Both keys and values must
       evaluate to strings. Note that any "Authorization" header provided in this object is automatically overwritten
       when using the ``jwt_token`` property. Note that the keys in this mapping can be overridden in the ``operations``
       section but cannot be discarded.
     -
     -

   * - ``operations``
     - Object
     - An object containing the registered operations allowed for the REST service. See the :ref:`Operation properties <rest_operations>` section for details.
       Note that you can also define an ``operations`` property on the :ref:`REST source <rest_source>`, :ref:`REST sink <rest_sink>`
       and :ref:`REST transform <rest_transform>` as well. The latter will take precedence if present both places.
       You need to specify an ``operations`` section in at least one of them.
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
     - If ``rate_limiting_retries`` is set on either the transform or on the REST system, and a retry is triggered
       the time to wait before retrying can be set by this value. If specified on both the toplevel system and in
       the operation definition, the operation value takes precedence.
     - 1
     -

   * - ``json_content_types``
     - Array of strings
     - This property can be used to supply the REST source and transform a list of response "content-type" strings
       that represent valid JSON content that should be parsed as such. The content-type "application/json" is always
       included.
     - ["application/json"]
     -

   * - ``custom_auth``
     - Object
     - An optional set of parameters that instruct the system on how to fetch an access token for authentication towards
       an external system.
       The ``get_token_operation`` is required and must point to an operation in the ``operations`` section that is
       configured to fetch an access token.
       The ``access_token_property`` is also required, and it must be set to the name of the property inside the
       expected response from the above operation that contains the access token. The retrieved access token is available
       in the Jinja2 environment and can be used with ``{{ access_token }}``.
       For systems that use refresh tokens, the ``initial_refresh_token`` should be set. Some systems may also supply
       a new refresh token in the same response that provides the access token. In that case, the
       ``refresh_token_property`` should also be set, and it should point to the name of the property that is
       expected to contain the refresh token. The current refresh token is available in the Jinja2 environment as
       ``{{ refresh_token }}``.
       Other props that need documentation: ``expires_at_expression``, ``expires_in_expression``, ``refresh_window``
       Also, document the new Jinja properties access_token and refresh_token, and that support for converting to bytes, b64encode/decode, datetime injection has been added (Tripletex example config)
       See (new section somewhere) for example configurations.
     -
     -


.. _rest_operations:

Operation properties
^^^^^^^^^^^^^^^^^^^^

You can register as many named "operations" as you like with the system (even using the same type of "method").
A operation configuration looks like:

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req


   * - ``url``
     - String
     - A URL or URL part. The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the entities properties
       available to the templating context. The expanded string is then substituted into the system's ``url_pattern`` property in
       place of its ``%s`` placeholder marker to get the final URL to use for the operation. If used with the
       :ref:`REST source <rest_source>`, the variables ``since``, ``entity`` (only for :ref:`REST transforms <rest_transform>` and
       :ref:`REST sinks <rest_sink>`), ``properties`` are available to this template. For the :ref:`REST transforms <rest_transform>` and
       :ref:`REST sources <rest_sink>` that support pagination some additional parameters are also available: ``previous_body``,
       ``previous_request_headers``, ``previous_params`` and ``previous_headers`` (response headers).
       Note that if you use the ``since`` variable (or a variable matching the ``since_property_name``) in this template
       the ``since_property_location`` property will be ignored for the operation (it implies a ``"query"`` value).
     -
     - Yes

   * - ``method``
     - String
     - A enumeration of ``"GET"``, ``"POST"``, ``"PUT"``, ``"DELETE"``, ``"PATCH"``, ``"OPTIONS"`` and ``"HEAD"``
       (note: case sensitive) that represents the HTTP operation that the operation should execute on the ``url`` specified.
     -
     - Yes

   * - ``headers``
     - Dict<String,String>
     - An optional object that contain key-value mappings for the HTTP request header. Entries in this dictionary
       will override any default ``headers`` property defined on the system (see previous section). The property
       supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the named variables
       ``url``, ``params``, ``entity`` (only for :ref:`REST transforms <rest_transform>` and
       :ref:`REST sinks <rest_sink>`), ``since`` (only for :ref:`REST sources <rest_source>`) and ``properties``
       available to the template. If the operation supports paging then ``previous_body``,
       ``previous_request_headers``, ``previous_params`` and ``previous_headers`` (response headers) are available
       for all page requests except the first. In addition ``page`` (integer, starting at 0) and ``is_first_page``
       (a boolean flag) are available for all requests in paged operations. Tip: use the Jinja "is defined" syntax for
       these variables to set default values for the first page.
     -
     -

   * - ``params``
     - Objects
     - An optional object that contain key-value mappings for any HTTP parameters. The property supports the
       ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the named variables
       ``url``, ``entity`` (only for :ref:`REST transforms <rest_transform>` and :ref:`REST sinks <rest_sink>`),
       ``since`` (only for :ref:`REST sources <rest_source>`) and ``properties`` available to the template. If
       the operation supports paging then ``previous_body``, ``previous_request_headers``, ``previous_params``
       and ``previous_headers`` (response headers) are available for all page requests except the first.
       In addition ``page`` (integer, starting at 0) and ``is_first_page`` (a boolean flag) are available for all
       requests in paged operations. Tip: use the Jinja "is defined" syntax for these variables to set default values
       for the first page.
     -
     -

   * - ``payload-type``
     - Enum<String>
     - A enumeration of "text", "json", "json-transit", "form" and "multipart-form", that denotes how to treat the
       ``payload`` property of the entity (see the :ref:`expected entity shape <rest_expected_rest_entity_shape>`
       section of the :ref:`REST sink <rest_sink>` for details). The various enumerations in combination with the
       ``payload`` type will set the appropriate ``Content-Type`` in the request headers, if it isn't set explicitly in
       the ``headers`` property of the operation. If you specify ``"json"``, the payload contents will serialized to JSON
       (without transit encoding). If you specify ``"json-transit"`` you will get a transit-encoded JSON document.
       Both of the JSON variants will result in the ``Content-Type`` ``"application/json"``. If ``"form"`` or
       ``"multipart-form"`` is used, the contents will be used to construct a HTML FORM for the request. The
       ``Content-Type`` will be ``"application/x-www-form-urlencoded"`` or ``"multipart/form"`` respectively. In this
       case, the form variables and corresponding values should be given as a single dictionary of
       variable-name/variable-value pairs. The values in the form will be transit encoded before the request is issued.
       The ``"text"`` payload type will use ``"text/plain"`` if the ``payload`` is not of type ``bytes`` or
       `"application/octet-stream"`` if it is. All ``payload`` types other than ``string`` or ``bytes`` will be
       serialized to a JSON encoded string.
     - ``"json"``
     -

   * - ``properties``
     - Object
     - The properties mapping used as default values for the emitted entities. Note that if both are present the
       properties in the emitted entity takes precedence. Also note that this property can be defined in the
       :ref:`REST source <rest_source>`, :ref:`REST transform <rest_transform>` and :ref:`REST sink <rest_sink>`
       configuration as well. The configuration in pipes will take precedence if both are defined.
     -
     -

   * - ``payload``
     - Object, string or array
     - The value to use as payload for the operation. Note that this property can be defined in the :ref:`REST source <rest_source>`,
       :ref:`REST transform <rest_transform>` and :ref:`REST sink <rest_sink>` configuration as well, but only the
       ``payload`` property on operations can refer to secrets. It can also be defined on the entities for the
       :ref:`REST transform <rest_transform>` and :ref:`REST sink <rest_sink>`. If this property is defined multiple places
       then the order of precedence is 1) entity, 2) sink/source/transform and 3) operation. This property supports the
       ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the named variables
       ``properties``, ``url``, ``request_params``, ``entity`` (only for :ref:`REST transforms <rest_transform>` and
       :ref:`REST sinks <rest_sink>`), ``since`` (only for :ref:`REST sources <rest_source>`) and ``headers`` available
       to the template. If the operation supports paging then ``previous_body``, ``previous_request_headers``,
       ``previous_params`` and ``previous_headers`` (response headers) are available for all page requests except the
       first. In addition ``page`` (integer, starting at 0) and ``is_first_page`` (a boolean flag) are available for all
       requests in paged operations. Tip: use the Jinja "is defined" syntax for these variables to set default values
       for the first page. For the :ref:`REST source <rest_source>` the variable ``since`` is also available.
     -
     -

   * - ``response_property``
     - String
     - The name of the property to put the response in when emitting entities. Note that this property can be defined
       in the :ref:`REST source <rest_source>` and :ref:`REST transform <rest_transform>` configuration as well.
       The configuration in pipes will take precedence if both are defined.
     -
     -

   * - ``response_headers_property``
     - String
     - The name of the property to put the response headers in when emitting entities. Note that this property can be
       defined in the :ref:`REST source <rest_source>` and :ref:`REST transform <rest_transform>` configuration as well.
       The configuration in pipes will take precedence if both are defined.
     -
     -

   * - ``response_status_property``
     - String
     - The name of the property to put the response status code in when emitting entities. Note that this property can be
       defined in the :ref:`REST source <rest_source>` and :ref:`REST transform <rest_transform>` configuration as well.
       The configuration in pipes will take precedence if both are defined.
     -
     -

   * - ``payload_property``
     - String
     - The JSON response sub-property to use as the source of the emitted entities. Note that this property can be
       defined in the :ref:`REST source <rest_source>` and :ref:`REST transform <rest_transform>` configuration as
       well. It will be ignored by the :ref:`REST sink <rest_sink>`. The configuration in pipes will take precedence
       if both are defined.
     -
     -

   * - ``next_page_link``
     - String
     - The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with several named variables
       values available to the template: ``body``, ``url``, ``request_params``, ``request_headers`, ``properties``, ``since``
       (only for :ref:`REST sources <rest_source>`), ``entity``, ``source_entity`` (only for
       :ref:`REST transforms <rest_transform>`)  and ``response_headers``. Additionally, ``previous_body``,
       ``previous_request_headers``, ``previous_params`` and ``previous_headers`` (response headers)
       is available for all page requests except the first. In addition ``page`` (integer, starting at 0) and
       ``is_first_page`` (a boolean flag) are available for all requests in paged operations. Tip: use Jinja's
       `"is defined" <https://jinja.palletsprojects.com/en/3.1.x/templates/#tests>`_ tests for these variables
       to set default values for the first page.  This property is used to extract the next URL to perform the
       operation on for pagination support. This property will be ignored by the :ref:`REST sink <rest_sink>`. See
       ``next_page_termination_strategy`` for how to control the termination of a paginated response.
     -
     -

   * - ``next_page_termination_strategy`` (experimental)
     - Enum<String> or array of Enum<String>
     - Enumeration of ``"empty-result"``, ``"same-next-page-link"``, ``"next-page-link-empty"``, ``"same-next-page-request"``,
       ``"same-response"`` and ``"not-full-page"``.
       The values indicate how to determine when a paginated response is finished. ``"empty-result"`` will terminate pagination
       when the result evaluates to missing or empty (or if the response body is empty). ``"same-next-page-link"``
       terminates if the computed ``next_page_link`` value matches the previous one and ``"next-page-link-empty"`` will
       terminate if this template evaluates to null or an empty string. ``"same-next-page-request"`` terminates paging if
       the component detects that request to issue is identical to the previous request (i.e. the headers, url, parameters and
       payload to use are all the same). ``"same-response"`` terminates paging if the response is equal to the previous one.
       ``"not-full-page"`` terminates paging if the last response contained less entities than the specified ``page_size``.
       Note that ``page_size`` *must* be set if this strategy is used.
       The default is ``"next-page-link-empty"``, ``"same-next-page-request"`` and ``"same-response"``.
       Note that these strategies can be combined in an array if the source system pagination sequence can
       terminate in multiple ways.
     - ``["next-page-link-empty", "same-next-page-request", "same-response"]``
     -

   * - ``page_size``
     - Integer
     - An integer indicating the number of entities contained in a paged response. This property must be set if the
       ``"not-full-page"`` next page termination strategy is used. Note that this property does *not* enable paging
       on its own, and is intended to be used in other properties that support the ``Jinja`` template
       (https://palletsprojects.com/p/jinja/) syntax. When the ``page_size`` is set, the value will substitute any
       instances of ``{{ page_size }}`` in the operation configuration.
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

       .. NOTE::

          This operation property can only be used with the :ref:`REST transform <rest_transform>`.

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

       .. NOTE::

          This operation property can only be used with the :ref:`REST transform <rest_transform>`.

       .. WARNING::

          Any response with status codes listed here will be discarded with no traces to be found, making it next to
          impossible to audit the pipe.

     -
     -

   * - ``id_expression``
     - String
     - The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the entities
       properties available to the templating context. It can be used to add ``_id`` properties to the emitted
       entities if missing from the source system. Note that this property can be defined in the
       :ref:`REST source <rest_source>` configuration and :ref:`REST transform <rest_transform>` as well. It will be
       ignored by the :ref:`REST sink <rest_sink>`. The configuration in pipes will take precedence if both are defined.
       The bound parameters available to this template are ``body``, ``url``, ``request_params``, ``properties``, ``since``
       (only for :ref:`REST sources <rest_source>`), ``entity``, ``source_entity`` (only for
       :ref:`REST transforms <rest_transform>`) and ``headers``. If the operation supports paging then ``previous_body``,
       ``previous_request_headers``, ``previous_params`` and ``previous_headers`` (response headers) are available for
       all page requests except the first. In addition ``page`` (integer, starting at 0) and ``is_first_page``
       (a boolean flag) are available for all requests in paged operations. Tip: use Jinja's
       `"is defined" <https://jinja.palletsprojects.com/en/3.1.x/templates/#tests>`_ tests for these
       variables to set default values for the first page.
     -
     -

   * - ``updated_expression``
     - String
     - The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the entities
       properties available to the templating context. It can be used to add ``_updated`` properties to the emitted
       entities if missing from the source system (for continuation support). For REST sources, this is only relevant if
       ``since_support`` as been set to ``true`` in the source. See the ``since_property_name`` and ``since_property_location``
       configuration properties as well. Note that this property can be defined in the
       :ref:`REST source <rest_source>` and :ref:`REST transform <rest_transform>` configuration as well. It will be
       ignored by the :ref:`REST sink <rest_sink>`. The configuration in pipes will take precedence if both are defined.
       The template supports the same named parameters as the ``id_expression``.  If the operation supports paging then
       ``previous_body``, ``previous_request_headers``, ``previous_params`` and ``previous_headers`` (response headers)
       are available for all page requests except the first. In addition ``page`` (integer, starting at 0) and
       ``is_first_page`` (a boolean flag) are available for all requests in paged operations.
       Tip: use Jinja's `"is defined" <https://jinja.palletsprojects.com/en/3.1.x/templates/#tests>`_ tests for these
       variables to set default values for the first page.
     -
     -

   * - ``error_expression``
     - String
     - The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with various
       bound parameters available to the templating context. It can be used to detect error conditions in responses
       from systems that doesn't properly use HTTP status codes to reflect failed operations. If the expression
       evaluates to a non-empty string, the source or transform will throw an exception and the pipe will fail.
       The rendered result is included in the error message. Note that this property is only relevant for the
       :ref:`REST source <rest_source>` and :ref:`REST transform <rest_transform>`. It will be
       ignored by the :ref:`REST sink <rest_sink>`. It is only evaluated when ``payload_property`` is set and the
       response content-type is recognized as JSON. For the :ref:`REST transforms <rest_transform>` the
       ``replace_entity`` property must be ``false`` (which is the default). The bound parameters available to this
       template are ``body``, ``url``, ``request_params``, ``properties``, ``since`` (only for :ref:`REST sources <rest_source>`),
       ``entity``, ``source_entity`` (these two only for
       :ref:`REST transforms <rest_transform>`) and ``headers``. If the operation supports paging then ``previous_body``,
       ``previous_request_headers``, ``previous_params`` and ``previous_headers`` (response headers) are available for
       all page requests except the first. In addition ``page`` (integer, starting at 0) and ``is_first_page``
       (a boolean flag) are available for all requests in paged operations. Tip: use Jinja's
       `"is defined" <https://jinja.palletsprojects.com/en/3.1.x/templates/#tests>`_ tests for these
       variables to set default values for the first page.
     -
     -

   * - ``since_property_name``
     - String
     - The name of the property to relay continuation information. This is only relevant if ``since_support`` as been
       set to ``true`` in the source. See ``since_property_location`` and ``updated_expression`` as well. Note that this
       property can be defined in the :ref:`REST source <rest_source>` configuration as well. It will be ignored by the
       :ref:`REST transform <rest_transform>` and :ref:`REST sink <rest_sink>`. The configuration in pipes will take
       precedence if both are defined. Note that if you use the ``since`` variable in the ``url`` template property
       the ``since_property_location`` and ``since_property_name`` configuration properties will be ignored for the
       operation.  Also note that if ``since_property_location`` is set to ``"manual"`` this property will be ignored.
     - ``"since"``
     -

   * - ``since_property_location``
     - String
     - A enumeration of ``"query"``, ``"header"`` and ``"manual``". This property is used to indicate where in the
       request to relay continuation information. This is only relevant if ``since_support`` as been set to ``true``.
       If you set it to `"manual"` the :ref:`REST source <rest_source>` will not attempt to provide any continuation
       parameters automatically. See ``since_property_name`` and ``updated_expression`` as well. Note that this property
       can be defined in the :ref:`REST source <rest_source>` configuration as well. It will be ignored by the
       :ref:`REST transform <rest_transform>` and :ref:`REST sink <rest_sink>`. The configuration in pipes will take
       precedence if both are defined.  Also note that if you use the ``since`` variable (or a variable matching the
       ``since_property_name``) in the ``url`` template, this property will be ignored for the operation (it implies
       a ``"query"`` value).
     - ``"query"``
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
       the time to wait before retrying can be set by this value. If specified on both the toplevel system and in the
       operation definition, the operation value takes precedence.
     - 1
     -

Notes on Jinja templates
^^^^^^^^^^^^^^^^^^^^^^^^

(experimental)
The ``payload``,  ``headers`` and ``params`` operation configuration properties are objects where the properties can be
templated using Jinja (both the key and the values) with various dynamically bound parameters. This makes it possible to construct
these request parameters dynamically. You can also control whether a particular property is included in the final
object by injecting a special marker constant ``"sesam:markskip"`` using conditional logic. If this marker is present in the
rendered template, then the property is omitted from its parent object. Note that you can use this marker in both keys and values.

An example:


::

    {
        "_id": "our-rest-service",
        "name": "Our REST service",
        "url_pattern": "http://our.domain.com/api/%s",
        "type": "system:rest",
        "operations": {
            "post-operation": {
                "url" : "{{ properties.url }}/some-path",
                "method": "POST",
                "payload-type": "json",
                "payload": {
                   "key": "value",
                   "conditional_key": "{% if entity.conditional_property is defined %}{{ entity.conditional_property }}{% else %}sesam:markskip{% endif %}",
                   "some_other_key{% if entity.other_conditional_property is not defined %}sesam:markskip{% endif %}": "other_value"
                }
            }
        ..


(experimental)
You can use the special marker ``"sesam:markjson"`` to construct JSON objects, lists or single values from a templated string in the ``payload``,  ``headers`` and ``params`` operation configuration properties. It can be used to cast Jinja templated strings to JSON data types or construct objects or lists with conditional Jinja logic.

An example:

::

    {
        "_id": "our-rest-service",
        "name": "Our REST service",
        "url_pattern": "http://our.domain.com/api/%s",
        "type": "system:rest",
        "operations": {
            "post-operation": {
                "url" : "{{ properties.url }}/some-path",
                "method": "POST",
                "payload-type": "json",
                "payload": {
                   "key": "{{ properties.integer_property }}system:markjson",
                   "some_other_key": "[{{ properties.arg1, \"literal value \"}}]sesam:markjson"
                }
            }
        ..



Result payload object:


::

    ..
    "payload": {
        "key": 10,
        "some_other_key": [1.2, \"literal value \"]
    }
    ..



.. _rest_system_example:

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-rest-service",
        "name": "Our REST service",
        "url_pattern": "http://our.domain.com/api/%s",
        "type": "system:rest",
        "operations": {
            "get-men": {
                "url" : "men/{{ properties.collection_name }}/men/{{ since }}",
                "method": "GET"
            },
            "get-man": {
                "url" : "men/{{ properties.collection_name }}/{{ _id }}",
                "method": "GET"
            },
            "get-woman": {
                "url" : "women/{{ properties.collection_name }}/{{ _id }}",
                "method": "GET"
            },
           "delete-man": {
               "url" : "men/{{ properties.collection_name }}/{{ _id }}",
               "method": "DELETE"
           },
           "delete-woman": {
               "url" : "women/{{ properties.collection_name }}/{{ _id }}",
               "method": "DELETE"
           },
           "update-man": {
               "url" : "men/{{ properties.collection_name }}/",
               "method": "POST",
               "headers": {
                   "Content-type": "application/xml"
               }
           },
           "update-woman": {
               "url" : "women/{{ properties.collection_name }}/",
               "method": "POST",
               "headers": {
                   "Content-type": "application/json"
               },
               "payload-type": "json"
           },
           "form-operation": {
               "url" : "men/{{ properties.collection_name }}/submit-form",
               "method": "POST",
               "payload-type": "form"
           },
           "multipart-form-operation": {
               "url" : "men/{{ properties.collection_name }}/submit-multipart-form",
               "method": "POST",
               "payload-type": "multipart-form"
           }
        }
    }
