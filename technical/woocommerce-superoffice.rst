===================================
Woocommerce to Superoffice Dataflow
===================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Order to Superoffice Quotealternative
-------------------------------------------------
Before any synchronization can take place, a link between a Woocommerce Order and a Superoffice Quotealternative must be established.

A new Superoffice Quotealternative will be created from a Woocommerce Order if it is connected to a Woocommerce Order that is synchronized into Superoffice.

Once a link between a Woocommerce Order and a Superoffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Superoffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Superoffice Quotealternative Property
     - Superoffice Data Type
   * - discount_total
     - DiscountPercent
     - "integer"


Woocommerce Order to Superoffice Quoteline
------------------------------------------
Every Woocommerce Order will be synchronized with a Superoffice Quoteline.

Once a link between a Woocommerce Order and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Superoffice Quoteline Property
     - Superoffice Data Type
   * - id
     - QuoteAlternativeId
     - "integer"
   * - line_items.name
     - Name
     - "string"
   * - line_items.price
     - UnitListPrice
     - N/A
   * - line_items.quantity
     - Quantity
     - N/A


Woocommerce Product to Superoffice Product
------------------------------------------
Every Woocommerce Product will be synchronized with a Superoffice Product.

Once a link between a Woocommerce Product and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Superoffice Product Property
     - Superoffice Data Type
   * - name
     - Name
     - "string"
   * - price
     - UnitCost
     - "string"
   * - sale_price
     - UnitListPrice
     - N/A

