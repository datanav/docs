===========================
Shopify to Shopify Dataflow
===========================

Generated: 2024-07-04 07:06:12

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


Shopify Variant to Shopify Variant
----------------------------------
Before any synchronization can take place, a link between a Shopify Variant and a Shopify Variant must be established.

A Shopify Variant will merge with a Shopify Variant if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Variant Property
     - Shopify Variant Property
   * - 
     - 
   * - product_id
     - product_id

Once a link between a Shopify Variant and a Shopify Variant is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Variant and a Shopify Variant:

.. list-table::
   :header-rows: 1

   * - Shopify Variant Property
     - Shopify Variant Property
     - Shopify Data Type


Shopify Product to Shopify Inventoryitem
----------------------------------------
Every Shopify Product will be synchronized with a Shopify Inventoryitem.

Once a link between a Shopify Product and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Shopify Inventoryitem Property
     - Shopify Data Type


Shopify Variant to Shopify Inventoryitem
----------------------------------------
Every Shopify Variant will be synchronized with a Shopify Inventoryitem.

Once a link between a Shopify Variant and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Variant and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Shopify Variant Property
     - Shopify Inventoryitem Property
     - Shopify Data Type
   * - sku
     - sku
     - "string"

