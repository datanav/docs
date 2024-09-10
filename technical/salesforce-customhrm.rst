================================
Salesforce to Customhrm Dataflow
================================

Generated: 2024-09-10 14:22:33

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Customhrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce User to Customhrm Employee
-------------------------------------
Every Salesforce User will be synchronized with a Customhrm Employee.

Once a link between a Salesforce User and a Customhrm Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Customhrm Employee:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Customhrm Employee Property
     - Customhrm Data Type

