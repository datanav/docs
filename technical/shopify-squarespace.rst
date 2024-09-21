====================
Shopify to  Dataflow
====================

Generated: 2024-09-21 00:00:05

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Inventoryitem to  Inventory
-----------------------------------
Every Shopify Inventoryitem will be synchronized with a  Inventory.

Once a link between a Shopify Inventoryitem and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     -  Inventory Property
     -  Data Type
   * - sku
     - sku
     - "string"


Shopify Product to  Inventory
-----------------------------
Every Shopify Product will be synchronized with a  Inventory.

Once a link between a Shopify Product and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     -  Inventory Property
     -  Data Type


Shopify Sesamproduct to  Inventory
----------------------------------
Every Shopify Sesamproduct will be synchronized with a  Inventory.

Once a link between a Shopify Sesamproduct and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     -  Inventory Property
     -  Data Type
   * - variants.inventory_quantity
     - quantity
     - "string"
   * - variants.sku
     - sku
     - "string"
   * - variants.title
     - descriptor
     - "string"


Shopify Order to  Order
-----------------------
Every Shopify Order will be synchronized with a  Order.

Once a link between a Shopify Order and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a  Order:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     -  Order Property
     -  Data Type


Shopify Sesamproduct to  Inventory
----------------------------------
Every Shopify Sesamproduct will be synchronized with a  Inventory.

Once a link between a Shopify Sesamproduct and a  Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a  Inventory:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     -  Inventory Property
     -  Data Type

