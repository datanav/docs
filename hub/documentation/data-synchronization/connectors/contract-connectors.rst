======================
The Connector Contract
======================

This document describes the output of connectors and the input to connectors. The output is the dataset that the collector writes to when synchronizing entities from the system. The input is the desired state of the system and the input to the connector to make it so.


.. _connector_contract_output:

Output of the connector
=======================

The dataset must use the following naming convention: SYSTEM-DATATYPE-collect, e.g. ``foo-person-collect``.


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
   * - ``$last-updated``
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
