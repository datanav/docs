=================================
Woocommerce to Customerp Dataflow
=================================

Generated: 2024-09-10 14:20:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Customerp. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Order to Customerp Order
------------------------------------
Every Woocommerce Order will be synchronized with a Customerp Order.

Once a link between a Woocommerce Order and a Customerp Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Customerp Order:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Customerp Order Property
     - Customerp Data Type


Woocommerce Product to Customerp Product
----------------------------------------
Every Woocommerce Product will be synchronized with a Customerp Product.

Once a link between a Woocommerce Product and a Customerp Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Customerp Product:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Customerp Product Property
     - Customerp Data Type

