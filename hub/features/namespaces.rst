.. _namespaces-feature:

:badge:`Free feature,badge-success badge-pill`

Namespaces
==========

Namespaces in Sesam are inspired by the Resource Description Framework `(RDF) <https://www.w3.org/RDF/>`_ where namespaces are URL references that allows us to reuse names from different sources without loosing context. In Sesam namespaces are used to determine the origin of attributes, which is essential for master data management in :ref:`global pipes <whatis-global>`. Inside global pipes we often wish to merge entities with other similar entities, such as person data from a CRM system and the equivalent person data from an HR system. Sesam prefixes namespaces to each attribute name in order to merge data from multiple sources without losing context. Namespaces in Sesam are also essential for :ref:`late schema binding <transform-late-schema-binding>` where we map global models to target models.

With some exceptions, attributes will always inherit the pipe name where the attribute was first created as its namespace, i.e. an attribute ``x`` created in pipe ``y`` will use the namespace ``y:``, becoming ``y:x``. 

See examples below.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Pipe name
     - Attribute from source
     - Attribute with namespace
   * - hubspot-person
     - name
     - hubspot-person:name
   * - visma-person
     - name
     - visma-person:name
   * - hubspot-company
     - company_name
     - hubspot-company:company_name  
   * - visma-company
     - company_name
     - visma-company:company_name

How to enable
-------------

**Enable on specific pipes:**
Namespaces can be enabled on specific pipes by setting the required property/properties in the pipe configuration (see properties below). 

**Enable globally in a subscription:**
You can enable namespaces in the service metadata for all the pipes in your subscription. This can be overridden at the pipe level. 

.. important::

   Some of the DTL functions are namespace aware and they will behave slightly differently when namespaces are enabled. See the section on :ref:`Namespace aware functions <namespace_aware_functions>` for more details.

Properties
^^^^^^^^^^
.. _namespaces_feature_add_namespaces:

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
     - Flag used to enable sink default values for ``add_namespaces`` and ``remove_namespaces``. If not specified in the service metadata then the default value is ``false``.
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