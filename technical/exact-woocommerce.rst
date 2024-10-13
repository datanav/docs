====================================
Exact Online to WooCommerce Dataflow
====================================

Generated: 2024-10-13 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Online Items to WooCommerce Product
-----------------------------------------
Every Exact Online Items will be synchronized with a WooCommerce Product.

Once a link between a Exact Online Items and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Items and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Exact Online Items Property
     - WooCommerce Product Property
     - WooCommerce Data Type


Exact Online Salesorders to WooCommerce Order
---------------------------------------------
Every Exact Online Salesorders will be synchronized with a WooCommerce Order.

Once a link between a Exact Online Salesorders and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorders and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorders Property
     - WooCommerce Order Property
     - WooCommerce Data Type
   * - Currency
     - currency
     - "string"
   * - Discount
     - discount_total
     - "string"

