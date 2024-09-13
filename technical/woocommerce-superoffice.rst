===================================
WooCommerce to SuperOffice Dataflow
===================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to SuperOffice Quotealternative
-------------------------------------------------
Before any synchronization can take place, a link between a WooCommerce Order and a SuperOffice Quotealternative must be established.

A new SuperOffice Quotealternative will be created from a WooCommerce Order if it is connected to a WooCommerce Order that is synchronized into SuperOffice.

Once a link between a WooCommerce Order and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - discount_total
     - DiscountPercent
     - "integer"


WooCommerce Order to SuperOffice Quoteline
------------------------------------------
Every WooCommerce Order will be synchronized with a SuperOffice Quoteline.

Once a link between a WooCommerce Order and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
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


WooCommerce Product to SuperOffice Product
------------------------------------------
Every WooCommerce Product will be synchronized with a SuperOffice Product.

Once a link between a WooCommerce Product and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"
   * - price
     - UnitCost
     - "string"
   * - sale_price
     - UnitListPrice
     - N/A

