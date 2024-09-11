===============================
Chargebee to CustomHRM Dataflow
===============================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to CustomHRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Business_entity to CustomHRM Department
-------------------------------------------------
Every Chargebee Business_entity will be synchronized with a CustomHRM Department.

Once a link between a Chargebee Business_entity and a CustomHRM Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a CustomHRM Department:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - CustomHRM Department Property
     - CustomHRM Data Type


Chargebee Customer to CustomHRM Employee
----------------------------------------
Every Chargebee Customer will be synchronized with a CustomHRM Employee.

Once a link between a Chargebee Customer and a CustomHRM Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a CustomHRM Employee:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - CustomHRM Employee Property
     - CustomHRM Data Type

