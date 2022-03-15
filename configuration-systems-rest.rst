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
       place of its ``%s`` placeholder marker to get the final URL to use for the operation.
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
     - String
     - A enumeration of "json", "json-transit" and "form", that denotes how to treat the ``payload`` property of the
       entity (see the :ref:`expected entity shape <rest_expected_rest_entity_shape>` section of the :ref:`REST sink <rest_sink>` for details). If you
       specify "json", the payload contents will serialized to JSON (without transit encoding). If you specify "json-transit"
       you will get a transit-encoded JSON document. If "form" is used, the contents will be used to construct a
       HTML FORM for the request. In this case, if the property contains a list, the request will use a multi-part form.
       If ``payload-type`` is omitted, the contents of the ``payload`` property will be assumed to be a string.
     -
     -

   * - ``properties``
     - Object
     - The properties mapping used as default values for the emitted entitites. Note that if both are present the
       properties in the emitted entity takes precendence. Also note that this property can be defined in the
       :ref:`REST source <rest_source>`, :ref:`REST transform <rest_transform>` and :ref:`REST sink <rest_sink>`
       configuration as well. The configuration in pipes will take precendence if both are defined.
     -
     -

   * - ``payload``
     - Object, string or array
     - The value to use as payload for the operation. Note that if both are present the
       properties in the processed entity takes precendence. Also note that this property can be defined
       in the :ref:`REST source <rest_source>`, :ref:`REST transform <rest_transform>` and :ref:`REST sink <rest_sink>`
       configuration as well. The configuration in pipes will take precendence if both are defined.
     -
     -

   * - ``response_property``
     - String
     - The name of the property to put the response in when emitting entities. Note that this property can be defined
       in the :ref:`REST source <rest_source>` and :ref:`REST transform <rest_transform>` configuration as well.
       The configuration in pipes will take precendence if both are defined.
     -
     -

   * - ``payload_property``
     - String
     - The JSON response sub-property to use as the source of the emitted entities. Note that this property can be
       defined in the :ref:`REST source <rest_source>` and :ref:`REST transform <rest_transform>` configuration as
       well. It will be ignored by the :ref:`REST sink <rest_sink>`. The configuration in pipes will take precendence
       if both are defined.
     -
     -

   * - ``next_page_link``
     - String
     - The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the source
       or transform response properties and header values available to the templating context bound to the ``body``
       and ``headers`` variables respectively. It is used to extract the next URL to perform the operation on for
       pagination support. This property will be ignored by the :ref:`REST sink <rest_sink>`.
     -
     -

   * - ``id_expression``
     - String
     - The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the entities
       properties available to the templating context. It can be used to add ``_id`` properties to the emitted
       entities if missing from the source system. Note that this property can be defined in the
       :ref:`REST source <rest_source>` configuration and :ref:`REST transform <rest_transform>` as well. It will be
       ignored by the :ref:`REST sink <rest_sink>`. The configuration in pipes will take precendence if both are defined.
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
       ignored by the :ref:`REST sink <rest_sink>`. The configuration in pipes will take precendence if both are defined.
     -
     -

   * - ``since_property_name``
     - String
     - The name of the property to relay continuation information. This is only relevant if ``since_support`` as been
       set to ``true`` in the source. See ``since_property_location`` and ``updated_property`` as well. Note that this
       property can be defined in the :ref:`REST source <rest_source>` configuration as well. It will be ignored by the
       :ref:`REST transform <rest_transform>` and :ref:`REST sink <rest_sink>`. The configuration in pipes will take
       precendence if both are defined.
     - ``"since"``
     -

   * - ``since_property_location``
     - String
     - A enumeration of "query" and "header". The location property to relay continuation information.
       This is only relevant if ``since_support`` as been set to ``true``. See ``since_property_name`` and
       ``updated_property`` as well. Note that this property can be defined in the :ref:`REST source <rest_source>`
       configuration as well. It will be ignored by the :ref:`REST transform <rest_transform>` and
       :ref:`REST sink <rest_sink>`. The configuration in pipes will take precendence if both are defined.
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
                "url" : "men/{{ properties.collection_name }}/men",
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
           }
        }
    }

