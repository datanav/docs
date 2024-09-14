====================================
WooCommerce to Business Nxt Dataflow
====================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to Business Nxt Currency
------------------------------------------
Every WooCommerce Order will be synchronized with a Business Nxt Currency.

Once a link between a WooCommerce Order and a Business Nxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Business Nxt Currency:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Business Nxt Currency Property
     - Business Nxt Data Type
   * - billing.country
     - isoCode
     - "string"
   * - shipping.country
     - isoCode
     - "string"


WooCommerce Order to Business Nxt Order
---------------------------------------
Every WooCommerce Order will be synchronized with a Business Nxt Order.

Once a link between a WooCommerce Order and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - discount_total
     - totalDiscountAmountInCurrency
     - "string"


WooCommerce Order to Business Nxt Orderline
-------------------------------------------
Every WooCommerce Order will be synchronized with a Business Nxt Orderline.

Once a link between a WooCommerce Order and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type
   * - id
     - orderNo
     - "string"


WooCommerce Product to Business Nxt Product
-------------------------------------------
Every WooCommerce Product will be synchronized with a Business Nxt Product.

Once a link between a WooCommerce Product and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Business Nxt Product Property
     - Business Nxt Data Type
   * - sale_price
     - priceQuantity
     - "string"

