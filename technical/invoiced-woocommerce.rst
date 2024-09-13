================================
Invoiced to WooCommerce Dataflow
================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Invoices to WooCommerce Order
--------------------------------------
Every Invoiced Invoices will be synchronized with a WooCommerce Order.

Once a link between a Invoiced Invoices and a WooCommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a WooCommerce Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - WooCommerce Order Property
     - WooCommerce Data Type
   * - currency
     - currency
     - "string"
   * - customer
     - customer_id
     - "string"
   * - discounts
     - discount_total
     - "string"


Invoiced Items to WooCommerce Product
-------------------------------------
Every Invoiced Items will be synchronized with a WooCommerce Product.

Once a link between a Invoiced Items and a WooCommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a WooCommerce Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - WooCommerce Product Property
     - WooCommerce Data Type
   * - name
     - name
     - "string"
   * - unit_cost
     - price
     - "string"

