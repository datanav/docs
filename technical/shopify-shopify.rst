===========================
Shopify to Shopify Dataflow
===========================

Generated: 2024-06-25 00:00:01

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


Shopify Product to Shopify Inventoryitem
----------------------------------------
Every Shopify Product will be synchronized with a Shopify Inventoryitem.

If a matching Shopify Inventoryitem already exists, the Shopify Product will be merged with the existing one.
If no matching Shopify Inventoryitem is found, a new Shopify Inventoryitem will be created.

A Shopify Product will merge with a Shopify Inventoryitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Shopify Inventoryitem Property
   * - variants.inventory_item_id
     - id

Once a link between a Shopify Product and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Shopify Inventoryitem Property
     - Shopify Data Type


Shopify Product to Shopify Product
----------------------------------
Before any synchronization can take place, a link between a Shopify Product and a Shopify Product must be established.

A Shopify Product will merge with a Shopify Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Shopify Product Property
   * - variants.inventory_item_id
     - variants.inventory_item_id

Once a link between a Shopify Product and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Shopify Product Property
     - Shopify Data Type

