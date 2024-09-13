===============================
MemberCare to Invoiced Dataflow
===============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Invoices to Invoiced Lineitem
----------------------------------------
Every MemberCare Invoices will be synchronized with a Invoiced Lineitem.

Once a link between a MemberCare Invoices and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
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

