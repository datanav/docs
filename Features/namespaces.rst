.. _concepts-namespaces:

Namespaces
==========

:ref:`Namespaces <best-practice-namespace>` are inspired by The Resource Description Framework `(RDF) <https://www.w3.org/RDF/>`_. You'll see them in terms of namespaced identifiers - also called NIs. A NI is a special datatype defined in the :doc:`entity data model <../entitymodel>`. In essence they are a string consisting of two parts, the namespace and the identifier. ``"~:global-person:john-doe"`` is an example. The ``~:`` is the type part that tells you that it is a namespaced identifier. ``global-person`` in this case is the namespace and ``john-doe`` is the identifier.

Properties can also have namespaces, but here the ``~:`` part is not used. ``global-person:fullname`` is an example of such a namespaced property. Namespaced properties are essential when :ref:`merging <concepts-merging>` to avoid naming collisions and to maintain provenance of the properties.

A namespaced identifier (NI) is a unique reference to an abstract thing. In Sesam, a NI is not a globally unique identifier, but it is a unique identifier inside one specific Sesam datahub. There are mechanisms in place for collapsing and expanding namespaced identifiers to globally unique identifiers on import and export.

Namespaced identifiers and properties with namespaces will automatically expand to fully qualified Uniform Resource Identifiers (URIs) when exporting to RDF. URIs in RDF are similarly collapsed into namespaced identifiers and properties with namespaces on import. They can also be expanded and collapsed using DTL.

Sesam can `utilize RDF <https://docs.sesam.io/rdf-support.html?highlight=rdf#>`_ for input, transformation or producing data for external consumption.


How to use
----------

Namespaces can be used by :ref:`entity identifiers <id_field>`, entity property names and the :ref:`namespaced identifier datatype <ni_data_type>`. A namespaced identifier consists of two parts; a namespace and an identifier. The namespace part can consist of any character, including colons. The identifier part can consist of any character except colons (``:``).

Example of an entity with namespaces:

.. code-block:: json


  {
    "_id": "user:123",
    "user:username": "erica",
    "user:first_name": "Erica",
    "user:manager": "~:user:101"
  }

Namespaced identifiers can be enabled by setting the ``namespaced_identifiers`` property to ``true`` in the pipe configuration (see below) or the service metadata. The former enables it for just the one pipe. The latter enables it for all pipes - except for those pipes that have explicitly disabled it.

.. NOTE::

   Some of the DTL functions are namespace aware and they will behave slightly differently when namespaces are enabled. See the section on :ref:`namespaces <namespace_aware_functions>` in the DTL reference guide for more details.

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

   * - ``namespaced_identifiers``
     - Boolean
     - Flag used to enable namespaced identifers support on the pipe. The default value is read from the service metadata. If not specified in the service metadata then the default value is ``false``.
     - Service metadata default
     -

   * - ``namespaces.identity``
     - String
     - The namespace used for identifiers. The default value is the pipe's id.
     - ``pipe.id``
     -

   * - ``namespaces.property``
     - String
     - The namespace used for properties. The default value is the pipe's id.
     - ``pipe.id``
     -

   * - ``add_namespaces``
     - Boolean
     - If ``true`` then the current identity namespace will be added to ``_id`` and the current property namespace will be added to all properties. The namespaces are added before the first transform. This property is normally only specified on inbound pipes.

       If ``namespaced_identifiers`` is enabled in the service metadata then the source default value is used. The following sources has a default value of ``true``: :ref:`csv <csv_source>`, :ref:`ldap <ldap_source>`, :ref:`sql <sql_source>`, :ref:`embedded <embedded_source>`, :ref:`http_endpoint <http_endpoint_source>`, and :ref:`json <json_source>`.
     - Source default
     -

   * - ``remove_namespaces``
     - Boolean
     - If ``true`` then namespaces will be removed from ``_id``, properties and namespaced identifier values. The namespaces are removed after the last transform. This property is normally only specified on outbound pipes.

       If ``namespaced_identifiers`` is enabled in the service metadata then the sink default value is used. The following sinks has a default value of ``true``:  :ref:`csv_endpoint <csv_endpoint_sink>`, :ref:`elasticsearch <elasticsearch_sink>`, :ref:`mail <mail_sink>`, :ref:`rest <rest_sink>`, :ref:`sms <sms_sink>`, :ref:`solr <solr_sink>`, :ref:`sql <sql_sink>`, :ref:`http_endpoint <http_endpoint_sink>`, and :ref:`json <json_sink>`.
     - Sink default
     -