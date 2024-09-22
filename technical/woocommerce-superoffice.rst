===================================
WooCommerce to SuperOffice Dataflow
===================================

Generated: 2024-09-22 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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

