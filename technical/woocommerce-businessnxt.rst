===================================
WooCommerce to BusinessNxt Dataflow
===================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to BusinessNxt Currency
-----------------------------------------
Every WooCommerce Order will be synchronized with a BusinessNxt Currency.

Once a link between a WooCommerce Order and a BusinessNxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a BusinessNxt Currency:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - BusinessNxt Currency Property
     - BusinessNxt Data Type
   * - billing.country
     - isoCode
     - "string"
   * - shipping.country
     - isoCode
     - "string"


WooCommerce Order to BusinessNxt Order
--------------------------------------
Every WooCommerce Order will be synchronized with a BusinessNxt Order.

Once a link between a WooCommerce Order and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type
   * - discount_total
     - totalDiscountAmountInCurrency
     - "string"


WooCommerce Order to BusinessNxt Orderline
------------------------------------------
Every WooCommerce Order will be synchronized with a BusinessNxt Orderline.

Once a link between a WooCommerce Order and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type
   * - id
     - orderNo
     - "string"


WooCommerce Product to BusinessNxt Product
------------------------------------------
Every WooCommerce Product will be synchronized with a BusinessNxt Product.

Once a link between a WooCommerce Product and a BusinessNxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a BusinessNxt Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - BusinessNxt Product Property
     - BusinessNxt Data Type
   * - sale_price
     - priceQuantity
     - "string"

