===================================
BusinessNxt to WooCommerce Dataflow
===================================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessNxt Order to WooCommerce Order
--------------------------------------
Every BusinessNxt Order will be synchronized with a WooCommerce Order.

Once a link between a BusinessNxt Order and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Order and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Order Property
     - WooCommerce Order Property
     - WooCommerce Data Type
   * - totalDiscountAmountInCurrency
     - discount_total
     - "string"


BusinessNxt Product to WooCommerce Product
------------------------------------------
Every BusinessNxt Product will be synchronized with a WooCommerce Product.

Once a link between a BusinessNxt Product and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Product and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Product Property
     - WooCommerce Product Property
     - WooCommerce Data Type
   * - priceQuantity
     - sale_price
     - "string"

