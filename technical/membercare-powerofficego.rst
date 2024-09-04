====================================
Membercare to Powerofficego Dataflow
====================================

Generated: 2024-09-04 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Invoices to Powerofficego Salesorderlines
----------------------------------------------------
Every Membercare Invoices will be synchronized with a Powerofficego Salesorderlines.

Once a link between a Membercare Invoices and a Powerofficego Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Powerofficego Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Powerofficego Salesorderlines Property
     - Powerofficego Data Type
   * - invoiceItems.quantity
     - Quantity
     - N/A
   * - invoiceItems.unitPrice
     - ProductUnitPrice
     - N/A


Membercare Organizations to Powerofficego Departments
-----------------------------------------------------
Every Membercare Organizations will be synchronized with a Powerofficego Departments.

Once a link between a Membercare Organizations and a Powerofficego Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Organizations and a Powerofficego Departments:

.. list-table::
   :header-rows: 1

   * - Membercare Organizations Property
     - Powerofficego Departments Property
     - Powerofficego Data Type

