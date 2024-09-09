===================================
Woocommerce to Businessnxt Dataflow
===================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Order to Businessnxt Currency
-----------------------------------------
Every Woocommerce Order will be synchronized with a Businessnxt Currency.

Once a link between a Woocommerce Order and a Businessnxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Businessnxt Currency:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Businessnxt Currency Property
     - Businessnxt Data Type
   * - billing.country
     - isoCode
     - "string"
   * - shipping.country
     - isoCode
     - "string"


Woocommerce Order to Businessnxt Order
--------------------------------------
Every Woocommerce Order will be synchronized with a Businessnxt Order.

Once a link between a Woocommerce Order and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - discount_total
     - totalDiscountAmountInCurrency
     - "string"


Woocommerce Order to Businessnxt Orderline
------------------------------------------
Every Woocommerce Order will be synchronized with a Businessnxt Orderline.

Once a link between a Woocommerce Order and a Businessnxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Businessnxt Orderline:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Businessnxt Orderline Property
     - Businessnxt Data Type
   * - id
     - orderNo
     - "string"


Woocommerce Product to Businessnxt Product
------------------------------------------
Every Woocommerce Product will be synchronized with a Businessnxt Product.

Once a link between a Woocommerce Product and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Businessnxt Product Property
     - Businessnxt Data Type
   * - sale_price
     - priceQuantity
     - "string"

