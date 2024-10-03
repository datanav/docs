===========================
Wix.com to Shopify Dataflow
===========================

Generated: 2024-10-03 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
     - "integer"
   * - totals.total
     - current_total_price
     - "string"
   * - totals.total
     - total_price
     - "string"


Wix.com Products to Shopify Sesamproduct
----------------------------------------
Every Wix.com Products will be synchronized with a Shopify Sesamproduct.

Once a link between a Wix.com Products and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - name
     - title
     - "string"
   * - priceData.price
     - sesam_priceExclVAT
     - "string"
   * - sku
     - variants.sku
     - "string"

