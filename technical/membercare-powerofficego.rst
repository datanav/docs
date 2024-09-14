=====================================
MemberCare to PowerOffice GO Dataflow
=====================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Invoices to PowerOffice GO Salesorderlines
-----------------------------------------------------
Every MemberCare Invoices will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a MemberCare Invoices and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type
   * - invoiceItems.quantity
     - Quantity
     - N/A
   * - invoiceItems.unitPrice
     - ProductUnitPrice
     - N/A

