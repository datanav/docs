=================================
Chargebee to Woocommerce Dataflow
=================================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Woocommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Item to Woocommerce Product
-------------------------------------
Every Chargebee Item will be synchronized with a Woocommerce Product.

Once a link between a Chargebee Item and a Woocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Woocommerce Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Woocommerce Product Property
     - Woocommerce Data Type


Chargebee Order to Woocommerce Order
------------------------------------
Every Chargebee Order will be synchronized with a Woocommerce Order.

Once a link between a Chargebee Order and a Woocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Woocommerce Order:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Woocommerce Order Property
     - Woocommerce Data Type
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

