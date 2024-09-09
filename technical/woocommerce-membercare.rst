==================================
Woocommerce to Membercare Dataflow
==================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Order to Membercare Invoices
----------------------------------------
Every Woocommerce Order will be synchronized with a Membercare Invoices.

Once a link between a Woocommerce Order and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - line_items.price
     - invoiceItems.unitPrice
     - "string"
   * - line_items.quantity
     - invoiceItems.quantity
     - "string"


Woocommerce Product to Membercare Products
------------------------------------------
Every Woocommerce Product will be synchronized with a Membercare Products.

Once a link between a Woocommerce Product and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Membercare Products Property
     - Membercare Data Type
   * - name
     - name
     - "string"

