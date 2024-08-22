===========================
Shopify to Shopify Dataflow
===========================

Generated: 2024-08-22 13:09:45

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Inventoryitem to Shopify Inventoryitem
----------------------------------------------
Before any synchronization can take place, a link between a Shopify Inventoryitem and a Shopify Inventoryitem must be established.

A Shopify Inventoryitem will merge with a Shopify Inventoryitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Shopify Inventoryitem Property
   * - id
     - id
   * - sku
     - sku

Once a link between a Shopify Inventoryitem and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Shopify Inventoryitem Property
     - Shopify Data Type


Shopify Inventoryitem to Shopify Product
----------------------------------------
Before any synchronization can take place, a link between a Shopify Inventoryitem and a Shopify Product must be established.

A Shopify Inventoryitem will merge with a Shopify Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Shopify Product Property
   * - sku
     - variants.sku
   * - id
     - variants.inventory_item_id

Once a link between a Shopify Inventoryitem and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Shopify Product Property
     - Shopify Data Type
   * - id
     - variants.inventory_item_id
     - "string"
   * - sku
     - variants.sku
     - "string"


Shopify Inventoryitem to Shopify Product variant
------------------------------------------------
Before any synchronization can take place, a link between a Shopify Inventoryitem and a Shopify Product variant must be established.

A Shopify Inventoryitem will merge with a Shopify Product variant if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Shopify Product variant Property
   * - id
     - variants.inventory_item_id

Once a link between a Shopify Inventoryitem and a Shopify Product variant is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Shopify Product variant:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Shopify Product variant Property
     - Shopify Data Type
   * - sku
     - variants.sku
     - "string"


Shopify Product to Shopify Inventoryitem
----------------------------------------
Before any synchronization can take place, a link between a Shopify Product and a Shopify Inventoryitem must be established.

A Shopify Product will merge with a Shopify Inventoryitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Shopify Inventoryitem Property
   * - variants.sku
     - sku
   * - variants.inventory_item_id
     - id

Once a link between a Shopify Product and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Shopify Inventoryitem Property
     - Shopify Data Type
   * - variants.sku
     - sku
     - "string"


Shopify Product to Shopify Product
----------------------------------
Before any synchronization can take place, a link between a Shopify Product and a Shopify Product must be established.

A Shopify Product will merge with a Shopify Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Shopify Product Property
   * - variants.sku
     - variants.sku
   * - variants.inventory_item_id
     - variants.inventory_item_id

Once a link between a Shopify Product and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Shopify Product Property
     - Shopify Data Type
   * - title
     - variants.title
     - "string"
   * - variants.title
     - title
     - "string"


Shopify Product variant to Shopify Inventoryitem
------------------------------------------------
Before any synchronization can take place, a link between a Shopify Product variant and a Shopify Inventoryitem must be established.

A Shopify Product variant will merge with a Shopify Inventoryitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Product variant Property
     - Shopify Inventoryitem Property
   * - variants.inventory_item_id
     - id

Once a link between a Shopify Product variant and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product variant and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Shopify Product variant Property
     - Shopify Inventoryitem Property
     - Shopify Data Type
   * - variants.sku
     - sku
     - "string"


Shopify Product variant to Shopify Product variant
--------------------------------------------------
Before any synchronization can take place, a link between a Shopify Product variant and a Shopify Product variant must be established.

A Shopify Product variant will merge with a Shopify Product variant if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Product variant Property
     - Shopify Product variant Property
   * - variants.inventory_item_id
     - variants.inventory_item_id

Once a link between a Shopify Product variant and a Shopify Product variant is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product variant and a Shopify Product variant:

.. list-table::
   :header-rows: 1

   * - Shopify Product variant Property
     - Shopify Product variant Property
     - Shopify Data Type

