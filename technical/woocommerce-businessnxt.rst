========================
Woocommerce to  Dataflow
========================

Generated: 2024-09-03 08:16:57

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Order to  Currency
------------------------------
Every Woocommerce Order will be synchronized with a  Currency.

Once a link between a Woocommerce Order and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a  Currency:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     -  Currency Property
     -  Data Type
   * - billing.country
     - isoCode
     - "string"
   * - shipping.country
     - isoCode
     - "string"


Woocommerce Order to  Order
---------------------------
Every Woocommerce Order will be synchronized with a  Order.

Once a link between a Woocommerce Order and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a  Order:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     -  Order Property
     -  Data Type
   * - discount_total
     - totalDiscountAmountInCurrency
     - "string"


Woocommerce Order to  Orderline
-------------------------------
Every Woocommerce Order will be synchronized with a  Orderline.

Once a link between a Woocommerce Order and a  Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a  Orderline:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     -  Orderline Property
     -  Data Type
   * - id
     - orderNo
     - "string"


Woocommerce Product to  Product
-------------------------------
Every Woocommerce Product will be synchronized with a  Product.

Once a link between a Woocommerce Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     -  Product Property
     -  Data Type
   * - sale_price
     - priceQuantity
     - "string"

