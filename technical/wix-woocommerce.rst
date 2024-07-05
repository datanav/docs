====================
Wix.com to  Dataflow
====================

Generated: 2024-07-05 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Orders to  Orders
-------------------------
Every Wix.com Orders will be synchronized with a  Orders.

Once a link between a Wix.com Orders and a  Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Orders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Orders Property
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


Wix.com Products to  Products
-----------------------------
Every Wix.com Products will be synchronized with a  Products.

Once a link between a Wix.com Products and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Products:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Products Property
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

