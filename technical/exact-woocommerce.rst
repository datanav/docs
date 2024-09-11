===================================
ExactOnline to WooCommerce Dataflow
===================================

Generated: 2024-09-11 08:35:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Items to WooCommerce Product
----------------------------------
Every Exact Items will be synchronized with a WooCommerce Product.

Once a link between a Exact Items and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - WooCommerce Product Property
     - WooCommerce Data Type


Exact Salesorders to WooCommerce Order
--------------------------------------
Every Exact Salesorders will be synchronized with a WooCommerce Order.

Once a link between a Exact Salesorders and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - WooCommerce Order Property
     - WooCommerce Data Type
   * - Currency
     - currency
     - "string"
   * - Discount
     - discount_total
     - "string"

