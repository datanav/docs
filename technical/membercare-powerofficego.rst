====================================
MemberCare to PowerOfficeGO Dataflow
====================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Invoices to PowerOfficeGO Salesorderlines
----------------------------------------------------
Every MemberCare Invoices will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a MemberCare Invoices and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type
   * - invoiceItems.quantity
     - Quantity
     - N/A
   * - invoiceItems.unitPrice
     - ProductUnitPrice
     - N/A

