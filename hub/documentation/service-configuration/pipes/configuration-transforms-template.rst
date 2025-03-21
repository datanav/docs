.. _template_transform:

Template transform
==================

The template transform comes with a bundle of pre-defined transform templates. These are meant to be used for specific use-cases. At this time the following named templates are available:

- :ref:`transform-collect-rest <template_transform_collect_rest>`
- :ref:`transform-defaults-rest <template_transform_defaults_rest>`
- :ref:`transform-share-rest <template_transform_share_rest>`

The common configuration options are:

Prototype
---------

::

   {
       "type": "template",
       "properties": {
           "some-property": "some-value"
       },
       "template": "template-name"
   }

Properties
----------

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``template``
     - String | Object
     - The name of the template, i.e. ``transform-collect-rest``, ``transform-defaults-rest`` or ``transform-share-rest``. For development purposes one can also include the template body in this property to override the built-in version.
     -
     - Yes

   * - ``properties``
     - Object
     - A dictionary of properties that are passed to the template. The actual properties that each template takes will vary. See the template specific documentation below.
     -
     - Yes

.. _template_transform_collect_rest:

transform-collect-rest
----------------------

This template transform is used in a collect pipe to retrieve the ``$origin`` property from the share pipes sink dataset. It will do this by hop-ing to the share sink dataset by joining the primary key with the ``$generated_id`` property.

The configuration options for this template are:

Prototype
~~~~~~~~~

::

   {
       "type": "template",
       "properties": {
           "rest_system": "hubspot-139567314",
           "operation_lookup": "deal-lookup",
           "operation_lookup_properties": {
           },
           "original_property": "_original",
           "primary_key": "id",
           "share_dataset": "hubspot-139567314-hubspot-deal-share"
       },
       "template": "transform-collect-rest"
   }

Template properties
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``rest_system``
     - String
     - The id of the :ref:`REST system <rest_system>` to use.
     -
     - Yes

   * - ``primary_key``
     - String | List<String>
     - The names of the properties that hold the primary key of the entity.
     -
     - Yes

   * - ``share_dataset``
     - String
     - The name of the corresponding share dataset. The template will hop to the share dataset to retrieve the ``$origin`` property.
     -
     - Yes

   * - ``operation_lookup``
     - String
     - The id of the REST system operation to use for lookups. This operation is used to apply the :doc:`source with parameterized input pattern <../../data-synchronization/source-with-parameterized-input-pattern>`.
     -
     - Yes

   * - ``operation_lookup_properties``
     - Object
     - The properties to pass to the lookup operation.
     -
     - No

   * - ``original_property``
     - String
     - Used to get access to the original source entity as was before the lookup operation. If you set this property to e.g. ``_original`` then the original source entity will be available in that property after the transform template.
     -
     - No

   * - ``operation_lookup_delete``
     - String
     - The id of the REST system operation to use for lookups of deletes. Requires the ``rest_system`` property. This property takes precedence over ``operation_lookup``, so the two cannot be used at the same time. This operation is used to do lookups of deleted entities to verify that they are actually non-existent in the system. If the entity does exist, then the ``_deleted`` property will be rewritten to be ``false``.
     -
     - Yes

   * - ``operation_lookup_delete_properties``
     - Object
     - The properties to pass to the lookup of deletes operation.
     -
     - No


.. _template_transform_defaults_rest:

transform-defaults-rest
-----------------------

This template transform is used when you want to merge the source entity's properties with the response body from a default values lookup REST operation. The source entity's properties takes precedence.

The configuration options for this template are:

Prototype
~~~~~~~~~

::

   {
       "type": "template",
       "properties": {
           "rest_system": "hubspot-139567314",
           "operation": "deal-lookup",
           "operation_properties": {
           },
           "primary_key": "id"
       },
       "template": "transform-defaults-rest"
   }

Template properties
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``rest_system``
     - String
     - The id of the :ref:`REST system <rest_system>` to use.
     -
     - Yes

   * - ``primary_key``
     - String | List<String>
     - The names of the properties that hold the primary key of the entity.
     -
     - Yes

   * - ``operation``
     - String
     - The name of the operation to use to retrieve the default values.
     -
     - No

   * - ``operation_properties``
     - Object
     - The properties to pass to the default values operation.
     -
     - No


.. _template_transform_share_rest:

transform-share-rest
----------------------

This template transform is used in a share pipe to perform CRUD operations against a REST system. It will perform an optimistic locking check to avoid overwriting changes that happened after the data was read from the system.

.. NOTE::

   If the source entity contains ``"$unsafe_skip_optimistic_locking": true`` then the entity will still be updated even if the comparison yields the result ``modified-in-system``. This is a mechanism to skip optimistic locking and it is primarily meant for use-cases when the data needs repairing. Use it with care.

The configuration options for this template are:

Prototype
~~~~~~~~~

::

   {
       "type": "template",
       "properties": {
           "rest_system": "hubspot-139567314",
           "operation_lookup": "lookup-deal",
           "operation_lookup_properties": {
           },
           "original_property": "_original",
           "primary_key": "id",
           "share_dataset": "hubspot-139567314-hubspot-deal-share"
       },
       "template": "transform-collect-rest"
   }

Template properties
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``rest_system``
     - String
     - The id of the :ref:`REST system <rest_system>` to use.
     -
     - Yes

   * - ``primary_key``
     - String | List<String>
     - The names of the properties that hold the primary key of the entity.
     -
     - Yes

   * - ``primary_key_insert``
     - String | List<String>
     - The names of the properties that hold the primary key of the entity. Use this property if the to-be inserted entity has a different primary key than in the other operations.
     -
     - No

   * - ``is_natural_key``
     - Boolean
     - If ``true`` then the primary key is a natural key. This means that the primary key is a natural part of the entity and is not being generated by the server-side on insert.
     - ``false``
     - No

   * - ``share_dataset``
     - String
     - The name of the corresponding share dataset. The template will hop to the share dataset to retrieve the ``$origin`` property.
     -
     - Yes

   * - ``payload_property``
     - String
     - Specifies the name of the property that should be used for the request payload (update or insert). This is used when you need to use a custom property for the payload.
     - ``payload``
     - No

   * - ``operation_lookup``
     - String
     - The name of the lookup operation.
     - ``lookup``
     - No

   * - ``operation_insert``
     - String
     - The name of the insert operation.
     - ``insert``
     - No

   * - ``operation_update``
     - String
     - The name of the update operation.
     - ``update``
     - No

   * - ``operation_delete``
     - String
     - The name of the delete operation.
     - ``delete``
     - No

   * - ``operation_lookup_properties``
     - Object
     - The properties to pass to the lookup operation.
     -
     - No

   * - ``operation_insert_properties``
     - Object
     - The properties to pass to the insert operation.
     -
     - No

   * - ``operation_update_properties``
     - Object
     - The properties to pass to the update operation.
     -
     - No

   * - ``operation_delete_properties``
     - Object
     - The properties to pass to the delete operation.
     -
     - No

   * - ``lookup_allowed_status_codes``
     - String
     - Override the default value for the ``allowed_status_codes`` for the lookup operation. Restricting the status codes will make the pipe fail for the excluded status codes.
     - ``100-599``
     - No

   * - ``insert_allowed_status_codes``
     - String
     - Override the default value for the ``allowed_status_codes`` for the insert operation. Restricting the status codes will make the pipe fail for the excluded status codes.
     - ``100-599``
     - No

   * - ``update_allowed_status_codes``
     - String
     - Override the default value for the ``allowed_status_codes`` for the update operation. Restricting the status codes will make the pipe fail for the excluded status codes.
     - ``100-599``
     - No

   * - ``delete_allowed_status_codes``
     - String
     - Override the default value for the ``allowed_status_codes`` for the delete operation. Restricting the status codes will make the pipe fail for the excluded status codes.
     - ``100-599``
     - No

   * - ``rules``
     - Object
     - A dictionary of DTL named rules. This can be used to implement the ``lookup_rewrite``, ``lookup_rewrite_based_on`` and ``lookup_rewrite_update`` named rules, which when defined will be used to rewrite the lookup response body. The ``lookup_rewrite`` named rule is used as a fallback if ``lookup_rewrite_based_on`` or ``lookup_rewrite_update`` is not specified. ``lookup_rewrite_based_on`` is used to rewrite the lookup response before it is used to create the ``$based_on_lookup`` value. ``lookup_rewrite_update`` is used to rewrite the lookup response before using it for client side patching  (see ``client_side_patching``).
     -
     - No

   * - ``rewrite_rules_payload``
     - Object
     - A dictionary of DTL named rules. This can be used to implement the ``rewrite_update_payload`` and ``rewrite_insert_payload`` named rules, which when defined will be used to rewrite the update and insert request payloads. The rule is passed the ``_S.`` entity and the original source entity can be found in ``_S.$source``. These rules take precedence over the ``$payload`` property. It can also include other named rules referenced directly or indirectly by the base rules. The rule should return a dict with the new payload inside the ``$payload`` property.
     
       It can also be used to implement the ``rewrite_update_payload_after_patch`` named rule which will rewrite the update payload after client-side patching is performed. The rule is passed an entity which contains the client-side patched payload in ``_S._payload``. The original source entity can be found in ``_R._S.$source``. 
     -
     - No

   * - ``rewrite_rules_lookup``
     - Object
     - A dictionary of DTL named rules. This can be used to implement the ``rewrite_lookup`` named rule, which when defined will be used to rewrite the lookup response body. It can also include other named rules referenced directly or indirectly by the base rule. The rule is passed the ``_S.`` entity returned from the lookup.
     -
     - No

   * - ``rewrite_rules_mutation``
     - Object
     - A dictionary of DTL named rules. This can be used to implement the ``rewrite_update``, ``rewrite_insert`` and ``rewrite_delete`` named rules, which when defined will be used to rewrite the update, insert and delete responses. It can also include other named rules referenced directly or indirectly by the base rules. The rule is passed the ``_S.`` entity returned from the mutation (i.e. update, insert or delete).
     -
     - No

   * - ``client_side_patching``
     - Boolean
     - If set to ``true`` then the update payload will be built from the result of the lookup operation and then patched with the actual payload. The use-case for this is when the REST operation does not support patching, but instead requires a complete payload to be sent.
     - ``false``
     - No

Special entity properties
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10

   * - Property
     - Type
     - Description
     - Req

   * - ``$payload``
     - Object
     - If you want to customize the request payload for the update and insert REST operations then put the customized request payload value into the ``$payload`` property.
     - No
