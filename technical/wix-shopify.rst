===========================
Wix.com to Shopify Dataflow
===========================

Generated: 2024-07-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Products to Shopify Inventoryitem
-----------------------------------------
Every Wix.com Products will be synchronized with a Shopify Inventoryitem.

Once a link between a Wix.com Products and a Shopify Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Shopify Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Shopify Inventoryitem Property
     - Shopify Data Type
   * - costAndProfitData.itemCost
     - cost
     - "string"
   * - costRange.maxValue
     - cost
     - "string"
   * - sku
     - sku
     - "string"


Wix.com Orders to Shopify Order
-------------------------------
Every Wix.com Orders will be synchronized with a Shopify Order.

Once a link between a Wix.com Orders and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Shopify Order Property
     - Shopify Data Type
   * - buyerInfo.id
     - customer.id
     - "string"
   * - currency
     - currency
     - "string"
   * - lineItems.name
     - line_items.title
     - "string"
   * - lineItems.price
     - line_items.price
     - "string"
   * - lineItems.quantity
     - line_items.quantity
     - "string"
   * - totals.total
     - current_total_price
     - "string"
   * - totals.total
     - total_price
     - "string"


Wix.com Products to Shopify Product
-----------------------------------
Every Wix.com Products will be synchronized with a Shopify Product.

Once a link between a Wix.com Products and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Shopify Product Property
     - Shopify Data Type
   * - name
     - variants.title
     - "string"
   * - priceData.price
     - variants.price
     - "string"

