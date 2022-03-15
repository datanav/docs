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
:doc:`JSON Push Protocol <json-push>` document. The serialisation of
entities as `JSON <https://en.wikipedia.org/wiki/JSON>`_ is described in more detail :doc:`here
<entitymodel>`. Both individual entities and lists of entities can be
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
``text/plain``. See the :doc:`rdf-support` document for more detail on working with RDF in Sesam.


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


Completeness
^^^^^^^^^^^^

When entities are posted to the HTTP endpoint source, the :ref:`completeness <completeness>` value of the sink dataset will by default be set to the current time. But it is also possible to explicitly specify the completeness value by adding a 'X-Dataset-Completeness' header in the POST-request. This value must be a positive integer. It is recommended to use microseconds since the epoch, since this is what Sesam does by default.  Example::

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



