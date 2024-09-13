============================
Wave to WooCommerce Dataflow
============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Invoice to WooCommerce Order
---------------------------------
Every Wave Invoice will be synchronized with a WooCommerce Order.

Once a link between a Wave Invoice and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - WooCommerce Order Property
     - WooCommerce Data Type
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


Wave Product to WooCommerce Product
-----------------------------------
Every Wave Product will be synchronized with a WooCommerce Product.

Once a link between a Wave Product and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - WooCommerce Product Property
     - WooCommerce Data Type
   * - name
     - name
     - "string"
   * - unitPrice
     - sale_price
     - "string"

