===========================
Shopify to Shopify Dataflow
===========================

Generated: 2024-09-15 00:00:00

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


Shopify Inventoryitem to Shopify Sesamproduct
---------------------------------------------
Before any synchronization can take place, a link between a Shopify Inventoryitem and a Shopify Sesamproduct must be established.

A Shopify Inventoryitem will merge with a Shopify Sesamproduct if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Shopify Sesamproduct Property
   * - sku
     - variants.sku
   * - id
     - variants.inventory_item_id

Once a link between a Shopify Inventoryitem and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Inventoryitem and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Shopify Inventoryitem Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - sku
     - variants..sku
     - "string"
   * - sku
     - variants.sku
     - "string"


Shopify Sesamproduct to Shopify Inventoryitem
---------------------------------------------
Before any synchronization can take place, a link between a Shopify Sesamproduct and a Shopify Inventoryitem must be established.

A Shopify Sesamproduct will merge with a Shopify Inventoryitem if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Shopify Inventoryitem Property
   * - variants.sku
     - sku
   * - variants.inventory_item_id
     - id

Once a link between a Shopify Sesamproduct and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Shopify Inventoryitem Property
     - Shopify Data Type
   * - variants..sku
     - sku
     - "string"
   * - variants.sku
     - sku
     - "string"


Shopify Sesamproduct to Shopify Sesamproduct
--------------------------------------------
Before any synchronization can take place, a link between a Shopify Sesamproduct and a Shopify Sesamproduct must be established.

A Shopify Sesamproduct will merge with a Shopify Sesamproduct if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Shopify Sesamproduct Property
   * - variants.sku
     - variants.sku
   * - variants.inventory_item_id
     - variants.inventory_item_id

Once a link between a Shopify Sesamproduct and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - Shopify Sesamproduct Property
     - Shopify Data Type

