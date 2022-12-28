
.. _rest_source:

REST source
-----------

This is a data source that can communicate with a REST service that produce JSON output using HTTP requests.
The REST source supports both pagination as part of the response body or pagination in the form of header properties
after the `RFC 5988 specifcation <https://tools.ietf.org/html/rfc5988>`_ . It optionally supports continuation both as
a query parameter or as header property.

Note that by default the REST source will only attempt to parse responses with content-type "application/json", if
the REST API provides other types of valid JSON, you can specify which in the ``json_content_types`` property of
the associated :ref:`REST system <rest_system>`.

Responses which aren't recognised as JSON will make the REST source emit "empty" entities with a property containing
the raw response body and - optionally - the content-type of the response for further processing with DTL and/or
HTTP or REST transform(s).

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
        "rate_limiting_retries": 3,
        "rate_limiting_delay": 60,
        "response_property": "the-property-name-to-put-the-response-in",
        "response_include_content_type": false,
        "payload_property": "the-property-the-response-resides-in",
        "id_expression": "{{ jinja_expression_for_the_id.property }}",
        "updated_expression": "{{ jinja_expression_for_the_updated_property }}",
        "since_property_name": "name-of-since-property",
        "since_property_location": "where-to-put-since-param"
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
     - The id of the operation to use.
     -
     - Yes

   * - ``properties``
     - Object
     - The properties mapping used as default values for the emitted entities. Note that if both are present the
       properties in the emitted entity takes precedence. Also note that this property can be defined in the specified
       ``operation`` section of the :ref:`REST system <rest_system>` as well. The source configuration will take
       precedence if defined.
     -
     -

   * - ``payload``
     - Object, string or array
     - The value to use as payload for the operation. Note that this property can be defined in the specified
       ``operation`` section of the :ref:`REST system <rest_system>` as well. Note that if the payload is an
       object (dictionary) and the system operation also defines a ``payload`` of the same type, then these will be
       merged before being used in the operation. In the merge operation, payload property values from the source take
       precedence over properties defined on the system. Also note that if the data type of the source
       ``payload`` and operation ``payload`` differ, then the source payload will take precedence and the
       operations payload will be ignored. This property supports the
       ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the named parameters
       ``properties``, ``url``, ``request_params``, ``since`` and ``headers`` available to the template.  If the
       operation supports paging then ``previous_body`` and ``previous_headers`` is available for all page requests
       except the first. Tip: use the Jinja "is defined" syntax for these variables to set default values for the
       first page.
     -
     -

   * - ``response_property``
     - String
     - The name of the property to put the response in when emitting entities. Note that this property can be defined
       in the specified ``operation`` section of the :ref:`REST system <rest_system>` as well. The source configuration
       will take precedence if defined.
     -
     -

   * - ``response_include_content_type``
     - Boolean
     - This property controls if the output entity should include the Content-Type of the response in a
       ``content-type`` property.

     - ``false``
     -

   * - ``payload_property``
     - String
     - The JSON response sub-property to use as the source of the emitted entities. Note that this property can be
       defined in the specified ``operation`` section of the :ref:`REST system <rest_system>` as well. The source
       configuration will take precedence if defined. This property can express a "path" into the response using a dot
       as path separator, i.e. ``foo.bar``. Note that a if a "non-path" version of the property can be found in the
       response body it will take precedence over any property found by traversing the path using the dot notation.
     -
     -

   * - ``id_expression``
     - String
     - The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the entities
       properties available to the templating context. It can be used to add ``_id`` properties to the emitted entities
       if missing from the source system. Note that this property can be defined
       in the specified ``operation`` section of the :ref:`REST system <rest_system>` as well. The source configuration
       will take precedence if defined. The bound parameters available to this template are ``body``, ``url``,
       ``requests_params``, ``properties``, ``since`` and ``headers``. All entity properties are also available as named
       variables. If the operation supports paging then ``previous_body`` and ``previous_headers`` is available for all
       page requests except the first. Tip: use the Jinja "is defined" syntax for these variables to set default values
       for the first page.
     -
     -

   * - ``updated_expression``
     - String
     - The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the entities
       properties available to the templating context. It can be used to add ``_updated`` properties to the emitted
       entities if missing from the source system (for continuation support). This is only relevant if
       ``since_support`` as been set to ``true`` in the source. Note that this property can be defined in the
       :ref:`REST system <rest_system>` operations configuration as well. The configuration in the source will take
       precedence if both are defined. The template supports the same named parameters as the ``id_expression``.
       If the operation supports paging then ``previous_body`` and ``previous_headers`` is available for all
       page requests except the first. Tip: use the Jinja "is defined" syntax for these variables to set default values
       for the first page.
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
     - If ``rate_limiting_retries`` is set on either the source or on the REST system, and a retry is triggered
       the time to wait before retrying can be set by this value. If specified on both the system and source,
       the source value takes precedence.
     - 1
     -

   * - ``if_source_empty``
     - Enum<String>
     - Determines the behaviour of the pipe when the REST source does not return any entities. Normally, any previously synced
       entities will be deleted even if the pipe does not receive any entities from its source.
       If set to ``"fail"``, the pipe will automatically fail if the source returns no entities. This means that any
       previous entities in the pipe's dataset are not deleted.
       If set to ``"accept"``, the pipe will *not* fail and any previously synced entities will be deleted.

       The global default ``global_defaults.if_source_empty`` can be set for all pipes in the
       :ref:`service metadata <service_metadata_section>`.
     - ``"accept"``
     -


Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``supports_since``
     - Boolean
     -
     - ``false``
     -

   * - ``is_since_comparable``
     - Boolean
     -
     - ``true``
     -

   * - ``is_chronological``
     - Boolean
     -
     - ``false``
     -

   * - ``updated_expression``
     - String
     - The property supports the ``Jinja`` template (https://palletsprojects.com/p/jinja/) syntax with the entities
       properties available to the templating context. It can be used to add ``_updated`` properties to the emitted
       entities if missing from the source system (for continuation support). This is only relevant if
       ``supports_since`` as been set to ``true``. See the ``since_property_name`` and ``since_property_location``
       configuration properties as well. Note that this property can alternatively be defined in the specified
       ``operation`` section of the :ref:`REST system <rest_system>`. The source configuration will take precedence
       if defined. The bound parameters available to this template are ``body``, ``headers``
       and ``properties``. All entity properties are also available as named variables.
     -
     -

   * - ``since_property_name``
     - String
     - The name of the property to relay continuation information. This is only relevant if ``supports_since`` as been
       set to ``true``. See ``since_property_location`` and ``updated_expression`` as well. Note that this
       property can alternatively be defined in the specified ``operation`` section of the
       :ref:`REST system <rest_system>`. The source configuration will take precedence if defined. Note that if you
       use the ``since`` variable in the ``url`` template property in the system operation configuration, the
       ``since_property_location`` and ``since_property_name`` configuration properties will be ignored for this
       operation.
     -
     -

   * - ``since_property_location``
     - String
     - A enumeration of "query" and "header". The location property to relay continuation information.
       This is only relevant if ``supports_since`` as been set to ``true``. See ``since_property_name`` and
       ``updated_expression`` as well. Note that this property can alternatively be defined in the specified ``operation``
       section of the :ref:`REST system <rest_system>`. The source configuration will take precedence if defined.
       Note that if you use the ``since`` variable in the ``url`` template property in the system operation
       configuration, the ``since_property_location`` and ``since_property_name`` configuration properties will be
       ignored for this operation.
     -
     -

   * - ``initial_since_value``
     - String or integer
     - If set, the source will use this value as the "since" value if the pipe offset has not been set yet (or
       the pipe has been reset). It should be used when you don't want the source to fetch all available data when
       the pipe is initially run or has been reset. Note that this value is only used if the source has been configured
       with continuation support.
     -
     -


.. _rest_source_examples:

Example configuration
^^^^^^^^^^^^^^^^^^^^^

See the :ref:`REST system example <rest_system_example>` section for how to configure the operations we refer to in
these examples:

Example response entities:

::

    [
        {
            "_id": "john",
            "name": "John",
            "age": 21,
            "sex": "M"
        },
        {
            "_id": "bob",
            "name": "Bob",
            "age": 44,
            "sex": "M"
        }
    ]


Configuration for REST source:

::

    {
        "type" : "pipe",
        "source" : {
            "type" : "rest",
            "system" : "our-rest-service",
            "operation": "get-men"
        }
    }


Example response entities:

::

    {
        "result": [
            {
                "_id": "john",
                "name": "John",
                "age": 21,
                "sex": "M"
            },
            {
                "_id": "bob",
                "name": "Bob",
                "age": 44,
                "sex": "M"
            }
        ]
    }


Configuration for REST source:

::

    {
        "type" : "pipe",
        "source" : {
            "type" : "rest",
            "system" : "our-rest-service",
            "operation": "get-men",
            "payload_property": "result"
        }
    }


Example response entities:

::

    [
        {
            "id": "john",
            "seq": 0,
            "name": "John",
            "age": 21,
            "sex": "M"
        },
        {
            "id": "bob",
            "seq": 1,
            "name": "Bob",
            "age": 44,
            "sex": "M"
        }
    ]


Configuration for REST source:

::

    {
        "type" : "pipe",
        "source" : {
            "type" : "rest",
            "system" : "our-rest-service",
            "operation": "get-men"
            "id_expression" : "{{ id }}"
            "updated_expression" : "{{ seq }}",
            "supports_since": true,
            "is_chronological": true,
            "is_since_comparable": true
        }
    }

Example response entities:

::

    {
        "result": [
            {
                "_id": "john",
                "name": "John",
                "age": 21,
                "sex": "M"
            },
            {
                "_id": "bob",
                "name": "Bob",
                "age": 44,
                "sex": "M"
            }
        ],
        "pagination": {
            "next": "?page=3",
            "prev": "?page=1"
        }
    }


Configuration for REST system:

In this case we add a Jinja template to extract the pagination link so we can parse all pages of the response:

::

    {
        "_id": "our-rest-service",
        "name": "Our REST service",
        "url_pattern": "http://our.domain.com/api/%s",
        "type": "system:rest",
        "operations": {
            "get-men": {
                "url" : "men/{{ properties.collection_name }}/",
                "next_page_link": "{{ body.pagination.next }}"
                "method": "GET"
            }
    }


Configuration for REST source is the same as previously:

::

    {
        "type" : "pipe",
        "source" : {
            "type" : "rest",
            "system" : "our-rest-service",
            "operation": "get-men",
            "payload_property": "result"
        }
    }

Example response from a service that supports pagination in the header as per the `RFC 5988 specifcation <https://tools.ietf.org/html/rfc5988>`_ .

::

    Headers:

    Content-Type: application/json
    Link: <?page=1>; rel="prev", <?page=3>; rel="next"

    [
        {
            "_id": "john",
            "name": "John",
            "age": 21,
            "sex": "M"
        },
        {
            "_id": "bob",
            "name": "Bob",
            "age": 44,
            "sex": "M"
        }
    ]


In this case we add a Jinja template to extract the pagination link from the reponse header so we can parse
all pages of the response:

::

    {
        "_id": "our-rest-service",
        "name": "Our REST service",
        "url_pattern": "http://our.domain.com/api/%s",
        "type": "system:rest",
        "operations": {
            "get-men": {
                "url" : "men/{{ properties.collection_name }}/",
                "next_page_link": "{{ headers.Link.next }}"
                "method": "GET"
            }
    }

Configuration for REST source is unchanged:

::

    {
        "type" : "pipe",
        "source" : {
            "type" : "rest",
            "system" : "our-rest-service",
            "operation": "get-men"
        }
    }



