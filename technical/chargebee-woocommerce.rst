=================================
Chargebee to WooCommerce Dataflow
=================================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Item to WooCommerce Product
-------------------------------------
Every Chargebee Item will be synchronized with a WooCommerce Product.

Once a link between a Chargebee Item and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - WooCommerce Product Property
     - WooCommerce Data Type


Chargebee Order to WooCommerce Order
------------------------------------
Every Chargebee Order will be synchronized with a WooCommerce Order.

Once a link between a Chargebee Order and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - WooCommerce Order Property
     - WooCommerce Data Type
   * - currency_code
     - currency
     - "string"
   * - customer_id
     - customer_id
     - "string"
   * - order_line_items.amount
     - line_items.quantity
     - "string"
   * - order_line_items.unit_price
     - line_items.price
     - "string"

