===================================
SuperOffice to WooCommerce Dataflow
===================================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Product to WooCommerce Product
------------------------------------------
Every SuperOffice Product will be synchronized with a WooCommerce Product.

Once a link between a SuperOffice Product and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - WooCommerce Product Property
     - WooCommerce Data Type
   * - Name
     - name
     - "string"
   * - UnitCost
     - price
     - "string"
   * - UnitListPrice
     - sale_price
     - "string"

