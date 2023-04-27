======================
The Connector Contract
======================

This document describes the output of connectors and the input to connectors. The output is the dataset that the collector writes to when synchronizing entities from the system. The input is the desired state of the system and the input to the connector to make it so.


.. _connector_contract_output:

Output of the connector
=======================

The dataset must use the following naming convention: SYSTEM-DATATYPE-collect, e.g. ``foo-person-collect``.

Connector should expose the data as close to the original API as possible. If any properties are added by the connector that are not in the API, they should be prefixed with ``sesam_``, e.g. ``sesam_saleId`` so that we know which data has been added by the connector.

Properties
----------

.. list-table::
   :widths: 20, 20, 50, 10
   :header-rows: 1

   * - Property
     - Datatype
     - Description
     - Required
   * - ``$origin``
     - Opaque
     - The value of the ``$origin`` property is opaque and is managed by the model mapping, but in general it encapsulates what entities from other systems caused the entity to be created in this system. The ``$origin`` property is retrieved from the ``$origin`` property in the share sink dataset by joining the entity's system primary key with the ``$generated_id`` property.
     - No
   * - ``$last-modified``
     - Datetime
     - This is a timestamp that tells when the entity was last modified in the system. The property is optional, but it is best to collect this information from the system or as close to the system as possible.
     - No

Example: existing entity in system
----------------------------------

::

   {
     "_id": "0",
     "id": 0,
     "key": "a",
     "value": 10,
     "$last-modified": "~t2023-01-30T12:00:01Z"
   }


Example: an entity that has previously been inserted by Sesam
-------------------------------------------------------------

::

   {
     "_id": "0",
     "id": 0,
     "key": "a",
     "value": 10,
     "$origin": "~:bar-person:123",
     "$last-modified": "~t2023-01-30T12:00:01Z"
   }


The input to the connector
==========================

The dataset must use the following naming convention: SYSTEM-DATATYPE-transform, e.g. `foo-person-transform`.

The dataset represents the desired state of the target system. The connector will make sure that the system reflects the desired state. Entities in the dataset should have the same structure as the output of the connector. Namespaces have been removed from the properties, but not from the `_id` property value. The properties have the same names, data types and structure as in the collect dataset.


If the source entity consists of one or more entities from the system, then it must be split into an entity for each of the entities. The ``_id`` property must use the system specific enriched ``_id``, e.g. if `foo-person:123` (it must be namespaced) and `foo:person:124` has been merged then one entity must be output for each of them.

If the source entity consists of no entities from the target system, then then output one entity. The ``_id`` property must be copied as-is from the source entity. This ``_id`` that will be treated as the *origin* of the inserted entity.

Properties
----------

.. list-table::
   :widths: 20, 20, 50, 10
   :header-rows: 1

   * - Property
     - Datatype
     - Description
     - Required
   * - ``$ids``
     - List<NI>
     - The property must contain ``_id`` and all other ids that may have been emitted as an ``_id`` for this object.
     - Required during insert. Optional for updated and deletes.
   * - ``$based_on``
     - Dict<String,Any>
     - The entity must contain the ``$based_on`` property, which should be a dict with property value pairs for all system raw properties that should be written back to the system. The ``$based_on`` property should be a subset of the properties from the connector output dataset as it should include the property values that was collected for this particular version of the entity. The property will be used to check if there has been modifications made to the entity in the target system after it was collected. The property can be used for preventing lost writes and avoiding unneccesary updates.
     - Required during insert. Optional for updated and deletes.
   * - ``$replaced``
     - Boolean
     - If set to true then it is not a real delete, but rather the entity got a new ``_id``. This property is produced by the merge source.
     - Optional for deletes. Disallowed for update and insert.
   * - ``$origin``
     - Opaque
     - The share pipe will just pass through the ``$origin`` property to its sink entity. It is an error if the operation is an insert and the property is missing. See the description of ``$origin`` in the section :ref:`Output of the connector <connector_contract_output>` above for more information on how it is used.
     - Optional if the entity originated in this particular system.

Example: insert
---------------

This entity does not have a system primary key, i.e. the ``id`` property, and will result in an insert into the system.

::

    {
      "_id": "bar-person:1",
      "_deleted": false,
      "$ids": [
        "~:bar-person:1"
      ],
      "key": "a",
      "value": 10
    }

Example: $replaced=true
-----------------------

The entity with this ``_id`` has been merged into another entity. The ``$replaced`` property and the ``_delete`` property was created by an upstream merge source and this must be communicated downstream to the dataset.

::

    {
      "_id": "bar-person:1",
      "_deleted": true,
      "$replaced": true
    }

Example: update
---------------

The properties in ``$based_on`` is different from the properties on the entity, so the entity will be updated in the system accordingly.

::

    {
      "_id": "foo-person:0",
      "_deleted": false,
      "$based_on": [
        "id": 0,
        "key": "a",
        "value": 10
      ],
      "id": 0,
      "key": "a",
      "value": 20
    }

Example: delete
---------------

The entity has been marked as deleted and will therefore be deleted in the system.

::

    {
      "_id": "foo-person:0",
      "_deleted": true
    }

Injected variables
==================

Any strings on the form ``{{@ foo @}}`` in the non-expanded connector configuration represent Jinja variables that are
injected into the configuration by a tool such as `sesam-py <https://github.com/sesam-community/sesam-py>`_.
With some exceptions, most of the variables that support this must be
listed in a connector's manifest to be made available. Some of these variables are always available and do not need to
be specified anywhere, such as ``datatype``.

The table below lists the supported variables.

Overview
--------

.. list-table::
   :widths: 20, 10
   :header-rows: 1

   * - Variable
     - Type
   * - :ref:`account_id<authentication_variables>`
     - String
   * - :ref:`base_url<connector_config_variables>`
     - String
   * - :ref:`connected_ts<authentication_variables>`
     - String
   * - :ref:`<connector>_webhook_dataset<webhook_variables>`
     - String
   * - :ref:`datatype<datatype_variables>`
     - String
   * - :ref:`is_fullsync<authentication_variables>`
     - Boolean
   * - :ref:`parent<datatype_variables>`
     - String
   * - :ref:`service_url<service_api_variables>`
     - String
   * - :ref:`system<system_variables>`
     - String
   * - :ref:`token_url<connector_config_variables>`
     - String

.. _authentication_variables:

Authentication-specific variables
---------------------------------

The values for these variables are retrieved from the output of the :ref:`Consumer portal<consumer-portal-authentication>`
for a given tenant.

The ``account_id`` Jinja variable can be used to inject the ID of the account that a tenant has connected to a system
with in the Consumer portal.

The ``connected_ts`` Jinja variable injects the timestamp for when an entity type/datatype has been enabled in the
Consumer portal.

The ``is_fullsync`` Jinja variable (EXPERIMENTAL) injects a boolean depending on whether a datatype has set
``fullsync`` to ``true`` or ``false`` by the user.

.. _system_variables:

System-specific variables
-------------------------

The ``system`` Jinja variable is always available and injects the name of the system (for example "hubspot", "wave" ...)

.. _datatype_variables:

Datatype-specific variables
---------------------------

The ``datatype`` Jinja variable is available for any configuration that belongs to a datatype and injects the name
of the datatype. Datatypes in the manifest can also be set to use specific properties:

The ``parent`` Jinja variable is replaced with the value of the ``parent`` property set for a datatype.

.. _connector_config_variables:

Properties from connector configuration
---------------------------------------

Properties from a provided connector configuration can also be injected.

The ``token_url`` Jinja variable injects the URL of an endpoint that grants an OAuth2 access token.

The ``base_url`` Jinja variable injects the base URL of the API for the system.

.. _service_api_variables:

Service API access
------------------

Setting ``requires_service_api_access`` to ``true`` in the manifest signals that any occurrences of the ``service_url``
Jinja variable should be replaced with "$ENV(service_url)", and a JWT granting access to the service API is added as a
secret to the connector's system. The secret can then be used in the config with ``$SECRET(service_jwt)``.

.. _webhook_variables:

Webhooks
--------

Setting ``use_webhook_secret`` to ``true`` in the manifest signals that a secret intended for validating incoming
requests to a receiver endpoint should be added to the system. The write permissions on all receiver endpoints that end
with `-event` in this connector will also be set to ``group:Anonymous``. This is meant to be used with the ``validation_expression`` in the
:ref:`HTTP endpoint source <http_endpoint_source>`.

Setting ``<connector>_webhook_dataset`` under ``additional_parameters`` in the manifest signals that any occurrences of
the ``<connector>_webhook_dataset`` Jinja variable should be replaced with "$ENV(<connector>_webhook_dataset)".


.. _other_parameters:

Other parameters
----------------

Any parameter and its value can be specified under the ``parameters`` section of a datatype in the manifest, replacing
any occurrence of that parameter in the configuration with the given value. For example, we can have a datatype
``contact`` that has this configuration in the manifest:

::

  {
    "datatypes": {
      "contact": {
        ...
        "parameters": {
          "foo": "bar"
        }
      }
    }
  }

This indicates that all occurrences of ``{{@ foo @}}`` in the ``contact`` template should be replaced with ``bar``.
Boolean values are also supported.


.. _injected_configuration:

Injected configuration
======================

In addition to injecting Jinja-type variables directly into the configuration (see the above section), certain
properties in the expanded pipe configurations can be set with the connector configuration and the pipe metadata.

Overview
--------

.. list-table::
   :widths: 20, 10
   :header-rows: 1

   * - Property
     - Type
   * - :ref:`supports_since<injected_pump_properties>`
     - String
   * - :ref:`sync_frequency<injected_pump_properties>`
     - String


.. _injected_pump_properties:

Pump properties
------------------------------------------

Setting ``metadata.supports_since`` on a pipe template will modify the pump's ``schedule_interval`` (if it is a collect
pipe). By default, collect pipes run at a schedule of every 300 seconds. If ``metadata.supports_since`` is set to
``true``, the pump will be set to run every 10 seconds instead.

Setting ``datatypes.<datatype>.sync_frequency`` to ``"slow"`` on a given datatype in the manifest will set the pump of
the collect pipe to run only once per day at midnight.
