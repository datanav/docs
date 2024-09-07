===================================
Businessnxt to Woocommerce Dataflow
===================================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Woocommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Order to Woocommerce Order
--------------------------------------
Every Businessnxt Order will be synchronized with a Woocommerce Order.

Once a link between a Businessnxt Order and a Woocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Order and a Woocommerce Order:

.. list-table::
   :header-rows: 1

   * - Businessnxt Order Property
     - Woocommerce Order Property
     - Woocommerce Data Type
   * - totalDiscountAmountInCurrency
     - discount_total
     - "string"


Businessnxt Product to Woocommerce Product
------------------------------------------
Every Businessnxt Product will be synchronized with a Woocommerce Product.

Once a link between a Businessnxt Product and a Woocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a Woocommerce Product:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
     - Woocommerce Product Property
     - Woocommerce Data Type
   * - priceQuantity
     - sale_price
     - "string"

