.. _rest_system:

REST system
-----------

The REST system represents a REST service (i.e. a web server) serving
`HTTP requests <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_ from a base url using the REST
vocabulary of GET, PUT, POST and PATCH.

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
        "operations": {
            "get-operation": {
                "url" : "/a/service/that/supports/get/{{ _id }}",
                "method": "GET",
                "next_page_link": {{ body.pagination.next }},
                "next_page_termination_strategy": "next-page-link-empty",
                "id_expression": {{ id }},
                "updated_expression": {{ updated }},
                "payload_property": "result",
                "response_property": "response",
                "since_property_name": "updated",
                "since_property_location": "query|header"
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

   * - ``operations``
     - Object
     - An object containing the registered operations allowed for the REST service. See the next section for details.
       At least one operation need to be registered for the system.
     -
     - Yes

   * - ``rate_limiting_retries``
     - Integer
     - If set and the REST service returns a HTTP 429 error code, the request will be retried the number of times
       indicated. The time between retries can be adjusted by setting ``rate_limiting_delay``.
     -
     -

   * - ``rate_limiting_delay``
     - Integer
     - If ``rate_limiting_retries`` is set on either the transform or on the REST system, and a retry is triggered
       the time to wait before retrying can be set by this value. If specified on both the toplevel system and in the,
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
       :ref:`REST source <rest_source>`, the variables ``since`` and ``properties`` are available to this template. 
       Note that if you use the ``since`` variable in this template the ``since_property_location`` and 
       ``since_property_name`` configuration properties will be ignored for the operation.
     -
     - Yes

   * - ``method``
     - String
     - A enumeration of "GET", "POST", "PUT", "DELETE" and "PATCH" (note: case sensitive) that represents the HTTP operation
       that the operation should execute on the ``url`` specified.
     -
     - Yes

   * - ``headers``
     - Dict<String,String>
     - An optional object that contain key-value mappings for the HTTP request header. Entries in this dictionary
       will override any default ``headers`` property defined on the system (see previous section).
     -
     -

   * - ``params``
     - Objects
     - An optional object that contain key-value mappings for any HTTP parameters.
     -
     -

   * - ``payload-type``
     - Enum<String>
     - A enumeration of "json", "json-transit", "form" and "multipart-form", that denotes how to treat the ``payload`` property of the
       entity (see the :ref:`expected entity shape <rest_expected_rest_entity_shape>` section of the :ref:`REST sink <rest_sink>` for details). If you
       specify "json", the payload contents will serialized to JSON (without transit encoding). If you specify "json-transit"
       you will get a transit-encoded JSON document. If "form" or "multipart-form" is used, the contents will be used to construct a
       HTML FORM for the request. The Content-Type of the request will be ``application/x-www-form-urlencoded`` or ``multipart/form``
       respectively. In this case, the form variables and corresponding values should be given as a single dictionary of
       variable-name/variable-value pairs. The values in the form will be transit encoded before the request is issued.
       If ``payload-type`` is omitted, the contents of the ``payload`` property will be assumed to be a string.
     -
     -

   * - ``properties``
     - Object
     - The properties mapping used as default values for the emitted entitites. Note that if both are present the
       properties in the emitted entity takes precedence. Also note that this property can be defined in the
       :ref:`REST source <rest_source>`, :ref:`REST transform <rest_transform>` and :ref:`REST sink <rest_sink>`
       configuration as well. The configuration in pipes will take precedence if both are defined.
     -
     -

   * - ``payload``
     - Object, string or array
     - The value to use as payload for the operation. Note that if the payload is an object (dictionary) and the
       pipe also defines a payload of the same type, then these will be merged before being used in the operation.
       In the merge operation, payload property values from the pipe take precedence over properties defined on the
       system. Note that this property can be defined in the :ref:`REST source <rest_source>`,
       :ref:`REST transform <rest_transform>` and :ref:`REST sink <rest_sink>` configuration as well, but only the
       ``payload`` property on operations can refer to secrets. Also note that if the data type of the pipe
       ``payload`` and operation ``payload`` differ, then the pipe payload will take precedence and the
       operations payload will be ignored.
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
     - The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with several named parameters
       values available to the template: ``body``, ``url``, ``requests_params``, ``properties``, ``since``
       (only for :ref:`REST sources <rest_source>`) and ``headers``. It is used to extract the next URL to perform the
       operation on for pagination support. This property will be ignored by the :ref:`REST sink <rest_sink>`. See
       ``next_page_termination_strategy`` for how to control the termination of a paginated response.
     -
     -

   * - ``next_page_termination_strategy``
     - Enum<String> or array of Enum<String>
     - Enumeration of ``"empty-result"``, ``"same-next-page-link"`` and ``"next-page-link-empty"``. The values
       indicate how to determine when a paginated response is finished. ``"empty-result"`` will terminate pagination
       when the result evaluates to missing or empty (or if the response body is empty). ``"same-next-page-link"``
       terminates if the computed ``next_page_link`` value matches the current one and ``"next-page-link-empty"`` will
       terminate if this template evaluates to null or an empty string. The ``"next-page-link-empty"`` is the default
       strategy. Note that these strategies can be combined in an array if the source system pagination sequence can
       terminate in multiple ways.
     - ``"next-page-link-empty"``
     -

   * - ``id_expression``
     - String
     - The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the entities
       properties available to the templating context. It can be used to add ``_id`` properties to the emitted
       entities if missing from the source system. Note that this property can be defined in the
       :ref:`REST source <rest_source>` configuration and :ref:`REST transform <rest_transform>` as well. It will be
       ignored by the :ref:`REST sink <rest_sink>`. The configuration in pipes will take precedence if both are defined.
       The bound parameters available to this template are ``body``, ``url``, ``requests_params``, ``properties``, ``since``
       (only for :ref:`REST sources <rest_source>`) and ``headers``. All current entity
       properties are also available as named variables.
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
       The template supports the same named parameters as the ``id_expression``.
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
       operation.
     - ``"since"``
     -

   * - ``since_property_location``
     - String
     - A enumeration of "query" and "header". The location property to relay continuation information.
       This is only relevant if ``since_support`` as been set to ``true``. See ``since_property_name`` and
       ``updated_expression`` as well. Note that this property can be defined in the :ref:`REST source <rest_source>`
       configuration as well. It will be ignored by the :ref:`REST transform <rest_transform>` and
       :ref:`REST sink <rest_sink>`. The configuration in pipes will take precedence if both are defined.
       Note that if you use the ``since`` variable in the ``url`` template property
       the ``since_property_location`` and ``since_property_name`` configuration properties will be ignored for the
       operation.
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
       the time to wait before retrying can be set by this value. If specified on both the toplevel system and in the,
       the operation definition, the operation value takes precedence.
     - 1
     -

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

