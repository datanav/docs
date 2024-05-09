====================
Wix.com to  Dataflow
====================

Generated: 2024-05-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Products to  Inventoryitem
----------------------------------
Every Wix.com Products will be synchronized with a  Inventoryitem.

Once a link between a Wix.com Products and a  Inventoryitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Inventoryitem:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Inventoryitem Property
     -  Data Type
   * - costAndProfitData.itemCost
     - cost
     - "string"
   * - costRange.maxValue
     - cost
     - "string"


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
   * - name
     - variants.title
     - "string"
   * - priceData.price
     - variants.price
     - "string"

