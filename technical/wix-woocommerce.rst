====================
Wix.com to  Dataflow
====================

Generated: 2024-09-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Orders to  Order
------------------------
Every Wix.com Orders will be synchronized with a  Order.

Once a link between a Wix.com Orders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Order:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Order Property
     -  Data Type
   * - buyerInfo.id
     - customer_id
     - "string"
   * - currency
     - currency
     - "string"
   * - lineItems.name
     - line_items.name
     - "string"
   * - lineItems.price
     - line_items.price
     - "string"
   * - lineItems.quantity
     - line_items.quantity
     - "string"


Wix.com Products to  Product
----------------------------
Every Wix.com Products will be synchronized with a  Product.

Once a link between a Wix.com Products and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Product Property
     -  Data Type
   * - costAndProfitData.itemCost
     - price
     - "string"
   * - costRange.maxValue
     - price
     - "string"
   * - name
     - name
     - "string"
   * - priceData.price
     - sale_price
     - "string"
   * - sku
     - sku
     - "string"

