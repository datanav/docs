======================================
Membercare to Businesscentral Dataflow
======================================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companies to Businesscentral Companies
-------------------------------------------------
Every Membercare Companies will be synchronized with a Businesscentral Companies.

Once a link between a Membercare Companies and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Membercare Organizations to Businesscentral Companies
-----------------------------------------------------
Every Membercare Organizations will be synchronized with a Businesscentral Companies.

Once a link between a Membercare Organizations and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Organizations and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Membercare Organizations Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Membercare Invoices to Businesscentral Salesorderlines
------------------------------------------------------
Every Membercare Invoices will be synchronized with a Businesscentral Salesorderlines.

Once a link between a Membercare Invoices and a Businesscentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Businesscentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Businesscentral Salesorderlines Property
     - Businesscentral Data Type
   * - invoiceItems.quantity
     - quantity
     - N/A
   * - invoiceItems.unitPrice
     - unitPrice
     - "float"

