=======================================
MemberCare to Business Central Dataflow
=======================================

Generated: 2024-09-13 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Companies to Business Central Companies
--------------------------------------------------
Every MemberCare Companies will be synchronized with a Business Central Companies.

Once a link between a MemberCare Companies and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - Business Central Companies Property
     - Business Central Data Type


MemberCare Organizations to Business Central Companies
------------------------------------------------------
Every MemberCare Organizations will be synchronized with a Business Central Companies.

Once a link between a MemberCare Organizations and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - Business Central Companies Property
     - Business Central Data Type


MemberCare Invoices to Business Central Salesorderlines
-------------------------------------------------------
Every MemberCare Invoices will be synchronized with a Business Central Salesorderlines.

Once a link between a MemberCare Invoices and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
   * - invoiceItems.quantity
     - quantity
     - N/A
   * - invoiceItems.unitPrice
     - unitPrice
     - "float"

