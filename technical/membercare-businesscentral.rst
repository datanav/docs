======================================
MemberCare to BusinessCentral Dataflow
======================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Companies to Businesscentral Companies
-------------------------------------------------
Every MemberCare Companies will be synchronized with a Businesscentral Companies.

Once a link between a MemberCare Companies and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


MemberCare Organizations to Businesscentral Companies
-----------------------------------------------------
Every MemberCare Organizations will be synchronized with a Businesscentral Companies.

Once a link between a MemberCare Organizations and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


MemberCare Invoices to BusinessCentral Salesorderlines
------------------------------------------------------
Every MemberCare Invoices will be synchronized with a BusinessCentral Salesorderlines.

Once a link between a MemberCare Invoices and a BusinessCentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a BusinessCentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - BusinessCentral Salesorderlines Property
     - BusinessCentral Data Type
   * - invoiceItems.quantity
     - quantity
     - N/A
   * - invoiceItems.unitPrice
     - unitPrice
     - "float"

