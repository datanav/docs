==================================
Exact Online to Freshteam Dataflow
==================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Online Departments to Freshteam Department
------------------------------------------------
Every Exact Online Departments will be synchronized with a Freshteam Department.

Once a link between a Exact Online Departments and a Freshteam Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Departments and a Freshteam Department:

.. list-table::
   :header-rows: 1

   * - Exact Online Departments Property
     - Freshteam Department Property
     - Freshteam Data Type


Exact Online Employees to Freshteam Employee
--------------------------------------------
Every Exact Online Employees will be synchronized with a Freshteam Employee.

Once a link between a Exact Online Employees and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Employees and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Exact Online Employees Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - BirthDate
     - date_of_birth
     - "string"

