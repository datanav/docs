==================================
WooCommerce to MemberCare Dataflow
==================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Order to MemberCare Invoices
----------------------------------------
Every WooCommerce Order will be synchronized with a MemberCare Invoices.

Once a link between a WooCommerce Order and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - line_items.price
     - invoiceItems.unitPrice
     - "string"
   * - line_items.quantity
     - invoiceItems.quantity
     - "string"


WooCommerce Product to MemberCare Products
------------------------------------------
Every WooCommerce Product will be synchronized with a MemberCare Products.

Once a link between a WooCommerce Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - name
     - name
     - "string"

