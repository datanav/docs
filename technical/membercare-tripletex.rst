================================
MemberCare to Tripletex Dataflow
================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Countries to Tripletex Country
-----------------------------------------
Every MemberCare Countries will be synchronized with a Tripletex Country.

Once a link between a MemberCare Countries and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Countries and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - MemberCare Countries Property
     - Tripletex Country Property
     - Tripletex Data Type


MemberCare Invoices to Tripletex Invoice
----------------------------------------
Every MemberCare Invoices will be synchronized with a Tripletex Invoice.

Once a link between a MemberCare Invoices and a Tripletex Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Tripletex Invoice:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - Tripletex Invoice Property
     - Tripletex Data Type


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

