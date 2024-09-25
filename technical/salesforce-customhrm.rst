=================================
Salesforce to Custom HRM Dataflow
=================================

Generated: 2024-09-25 00:34:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Custom HRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce User to Custom HRM Employee
--------------------------------------
Every Salesforce User will be synchronized with a Custom HRM Employee.

Once a link between a Salesforce User and a Custom HRM Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Custom HRM Employee:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Custom HRM Employee Property
     - Custom HRM Data Type

