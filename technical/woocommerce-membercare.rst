==================================
WooCommerce to MemberCare Dataflow
==================================

Generated: 2024-09-11 07:46:45

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to Membercare Invoices
----------------------------------------
Every WooCommerce Order will be synchronized with a Membercare Invoices.

Once a link between a WooCommerce Order and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - line_items.price
     - invoiceItems.unitPrice
     - "string"
   * - line_items.quantity
     - invoiceItems.quantity
     - "string"


WooCommerce Product to Membercare Products
------------------------------------------
Every WooCommerce Product will be synchronized with a Membercare Products.

Once a link between a WooCommerce Product and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Membercare Products Property
     - Membercare Data Type
   * - name
     - name
     - "string"

