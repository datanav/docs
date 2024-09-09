=============================
Exact to Woocommerce Dataflow
=============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Woocommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Items to Woocommerce Product
----------------------------------
Every Exact Items will be synchronized with a Woocommerce Product.

Once a link between a Exact Items and a Woocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Woocommerce Product:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Woocommerce Product Property
     - Woocommerce Data Type


Exact Salesorders to Woocommerce Order
--------------------------------------
Every Exact Salesorders will be synchronized with a Woocommerce Order.

Once a link between a Exact Salesorders and a Woocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Woocommerce Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Woocommerce Order Property
     - Woocommerce Data Type
   * - Currency
     - currency
     - "string"
   * - Discount
     - discount_total
     - "string"

