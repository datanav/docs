================================
Invoiced to Woocommerce Dataflow
================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Woocommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Invoices to Woocommerce Order
--------------------------------------
Every Invoiced Invoices will be synchronized with a Woocommerce Order.

Once a link between a Invoiced Invoices and a Woocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Woocommerce Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Woocommerce Order Property
     - Woocommerce Data Type
   * - currency
     - currency
     - "string"
   * - customer
     - customer_id
     - "string"
   * - discounts
     - discount_total
     - "string"


Invoiced Items to Woocommerce Product
-------------------------------------
Every Invoiced Items will be synchronized with a Woocommerce Product.

Once a link between a Invoiced Items and a Woocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Woocommerce Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Woocommerce Product Property
     - Woocommerce Data Type
   * - name
     - name
     - "string"
   * - unit_cost
     - price
     - "string"

