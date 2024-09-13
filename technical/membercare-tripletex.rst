================================
MemberCare to Tripletex Dataflow
================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Invoices to Tripletex Orderline
------------------------------------------
Every MemberCare Invoices will be synchronized with a Tripletex Orderline.

Once a link between a MemberCare Invoices and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - invoiceItems.description
     - description
     - "string"
   * - invoiceItems.quantity
     - count
     - N/A
   * - invoiceItems.unitPrice
     - unitPriceExcludingVatCurrency
     - "float"

