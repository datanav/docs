.. _http_endpoint_source:

HTTP endpoint source
--------------------

This is a special data source that registers an `HTTP <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_
receiver endpoint that one can post entities to. Entities posted here will be written to the pipe's sink.

A pipe that references the ``HTTP endpoint`` source will not pump any
entities, in practice this means that a pump is not configured for the
pipe; the only way for entities to flow through the pipe is by posting
them to the HTTP endpoint.

It exposes two URLs:

.. list-table::
   :header-rows: 1
   :widths: 50, 60

   * - URL
     - Description

   * - ``http://localhost:9042/api/receivers/mypipe/entities``
     - JSON Push endpoint

   * - ``http://localhost:9042/api/receivers/mypipe/sdshare-push-receiver``
     - SDShare Push receiver endpoint

JSON Push protocol
^^^^^^^^^^^^^^^^^^

The JSON Push protocol is described in additional detail in the
:doc:`JSON Push Protocol <../../../json-push>` document. The serialisation of
entities as `JSON <https://en.wikipedia.org/wiki/JSON>`_ is described in more detail :ref:`here
<entity-data-model>`. Both individual entities and lists of entities can be
posted. This endpoint is compatible with :ref:`The JSON push sink
<json_sink>`.

The JSON Push endpoint supports `HTTP POST <https://en.wikipedia.org/wiki/POST_(HTTP)>`_ of
both a single JSON object and a list of JSON objects. The HTTP request's ``content-type``
`header <https://en.wikipedia.org/wiki/List_of_HTTP_header_fields>`_ element must be set to ``application/json`` in this case.

SDShare Push protocol
^^^^^^^^^^^^^^^^^^^^^

The SDShare Push protocol is described `here
<https://github.com/SesamResearch/sdshare-push/blob/master/spec.md>`__.

The SDShare Push endpoint supports receiving `RDF <https://www.w3.org/TR/2004/REC-rdf-primer-20040210/>`_
in `N-Triples <https://www.w3.org/TR/2014/REC-n-triples-20140225/>`_ form. In this case the URL
parameters have to include at least one ``resource`` parameter describing which resources the
N-Triples payload contains statements about. If you include a ``resource`` parameter that there
are no statements about in the N-Triples body, an empty entity is generated with its ``_deleted``
flag set to ``true``. Note that the ``graph`` parameter of the protocol is ignored - the destination
of the entities generated from the N-Triples payload must be configured in the pipe's ``sink``
section. This type of HTTP request expects the ``content-type`` to be ``application/n-triples`` or
``text/plain``. See the :doc:`../../../rdf-support` document for more detail on working with RDF in Sesam.


Prototype
^^^^^^^^^

::

    {
        "type": "http_endpoint"
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

   * - ``auto_populate_dataset``
     - Boolean
     - If true (the default) the sink dataset will be marked as populated initially. This property can only be
       specified if the sink is of type ``dataset``.
     - ``true``
     - No

   * - ``do_float_as_decimal``
     - Boolean
     - If true (the default) numbers with a decimal point will be stored as the ``Decimal`` datatype. If false,
       numbers a decimal point will be stored as the ``float`` datatype. See the :ref:`entity data model <entity_data_types>`
       for more information about the difference between the two datatypes.
     - ``true``
     - No

   * - ``do_float_as_int``
     - Boolean
     - If true (the default) numbers where all the digits after the decimal point is zero will be stored as the
       ``Integer`` datatype.
     - ``true``
     - No

   * - ``trace``
     - Boolean or Object
     - This can be set to ``true`` to write ``pump-started`` and ``pump-completed`` (or ``pump-failed``) events to
       the execution log dataset whenever the http_endpoint source receives a request. The "pump-completed"/"pump-failed"
       events will contain the request-headers and the first few bytes of the request-body. If you need more fine-grained
       control of the logging, you can set ``trace`` to be an object and set the ``trace.log_request_headers`` and/or
       ``trace.log_request_body_maxsize`` sub-properties.
     - ``false``
     - No

   * - ``trace.log_request_headers``
     - Boolean
     - If the ``trace`` property is an object this sub-property specifies if the request headers will
       be logged in the ``pump-completed``/``pump-completed`` events in the execution-log.
     - ``true``
     - No

   * - ``trace.log_secret_redacted_bytes``
     - Integer
     - If the ``trace`` property is an object this property specifies how many bytes of the ``Authorization`` request
       header that should be redacted in the ``pump-completed``/``pump-completed`` events in the execution-log. The
       purpose of this setting is to redact enough of the ``Authorization`` header to render it safe to log, but to
       potentially leave some of the header for debugging purposes.
       A value of ``-1`` means to redact all bytes in the header.
     - 600
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

   * - ``validation_expression``
     - String
     - This property allows custom request validation for receiver endpoints. This is particularly useful when clients cannot use JWT tokens for authentication. The string must be a `Jinja template <https://jinja.palletsprojects.com/en/3.1.x/templates/#tests>`_. The Jinja template is rendered for each incoming request. If it renders as an empty string then the request is accepted, otherwise the rendered string will be reported as an error in the response. The context allows using the ``secret`` function to access values of secrets. The named variables ``url``, ``request_params`` and ``request_headers`` are available to the template.  Example: ``"{{ '' if request_headers['X-Sesam-Authorization'] == secret('webhook_secret') else 'Invalid authorization header value' }}"``.

       .. NOTE::

          It is assumed that the receiver pipe has granted the ``write_data`` permission granted to the role ``group:Anonymous`` if JWT tokens are not to be used for authentication.
     -
     - No


Completeness
^^^^^^^^^^^^

When entities are posted to the HTTP endpoint source, the :ref:`completeness <completeness_feature>` value of the sink dataset will by default be set to the current time. But it is also possible to explicitly specify the completeness value by adding a 'X-Dataset-Completeness' header in the POST-request. This value must be a positive integer. It is recommended to use microseconds since the epoch, since this is what Sesam does by default.  Example::

    curl -H "X-Dataset-Completeness: 1633934725921188" ...


Continuation support
^^^^^^^^^^^^^^^^^^^^

See the section on :ref:`continuation support <continuation_support>` for more information.

.. list-table::
   :header-rows: 1
   :widths: 10, 80

   * - Property
     - Value

   * - ``supports_since``
     - ``false`` (Fixed)

   * - ``is_since_comparable``
     - ``true`` (Fixed)

   * - ``is_chronological``
     - ``false`` (Fixed)



Example configuration
^^^^^^^^^^^^^^^^^^^^^

The pipe configuration given below will expose the
``my-entities`` receiver endpoint and write any data it receives
into the ``my-entities`` dataset:

::

    {
        "_id": "my-entities",
        "type": "pipe",
        "source": {
            "type": "http_endpoint"
        }
    }
