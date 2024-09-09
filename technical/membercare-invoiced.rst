===============================
Membercare to Invoiced Dataflow
===============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Invoices to Invoiced Lineitem
----------------------------------------
Every Membercare Invoices will be synchronized with a Invoiced Lineitem.

Once a link between a Membercare Invoices and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Invoiced Lineitem Property
     - Invoiced Data Type
   * - invoiceItems.description
     - items.description
     - "string"
   * - invoiceItems.quantity
     - items.quantity
     - "string"
   * - invoiceItems.unitPrice
     - items.amount
     - "string"

