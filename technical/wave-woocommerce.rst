======================================
Wave Financial to Woocommerce Dataflow
======================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Woocommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Invoice to Woocommerce Order
---------------------------------
Every Wave Invoice will be synchronized with a Woocommerce Order.

Once a link between a Wave Invoice and a Woocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Woocommerce Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Woocommerce Order Property
     - Woocommerce Data Type
   * - currency.code
     - currency
     - "string"
   * - customer.id
     - customer_id
     - "string"
   * - items.price
     - line_items.price
     - "string"
   * - items.quantity
     - line_items.quantity
     - "string"


Wave Product to Woocommerce Product
-----------------------------------
Every Wave Product will be synchronized with a Woocommerce Product.

Once a link between a Wave Product and a Woocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Woocommerce Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Woocommerce Product Property
     - Woocommerce Data Type
   * - name
     - name
     - "string"
   * - unitPrice
     - sale_price
     - "string"

