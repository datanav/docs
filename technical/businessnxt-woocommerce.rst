====================================
Business Nxt to WooCommerce Dataflow
====================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Order to WooCommerce Order
---------------------------------------
Every Business Nxt Order will be synchronized with a WooCommerce Order.

Once a link between a Business Nxt Order and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Order and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Business Nxt Order Property
     - WooCommerce Order Property
     - WooCommerce Data Type
   * - totalDiscountAmountInCurrency
     - discount_total
     - "string"


Business Nxt Product to WooCommerce Product
-------------------------------------------
Every Business Nxt Product will be synchronized with a WooCommerce Product.

Once a link between a Business Nxt Product and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Product and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Business Nxt Product Property
     - WooCommerce Product Property
     - WooCommerce Data Type
   * - priceQuantity
     - sale_price
     - "string"

