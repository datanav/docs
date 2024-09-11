====================================
Exact Online to WooCommerce Dataflow
====================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Items to WooCommerce Product
----------------------------------------
Every ExactOnline Items will be synchronized with a WooCommerce Product.

Once a link between a ExactOnline Items and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Items and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - ExactOnline Items Property
     - WooCommerce Product Property
     - WooCommerce Data Type


ExactOnline Salesorders to WooCommerce Order
--------------------------------------------
Every ExactOnline Salesorders will be synchronized with a WooCommerce Order.

Once a link between a ExactOnline Salesorders and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorders and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorders Property
     - WooCommerce Order Property
     - WooCommerce Data Type
   * - Currency
     - currency
     - "string"
   * - Discount
     - discount_total
     - "string"

