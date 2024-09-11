=================================
ExactOnline to Freshteam Dataflow
=================================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Departments to Freshteam Department
-----------------------------------------------
Every ExactOnline Departments will be synchronized with a Freshteam Department.

Once a link between a ExactOnline Departments and a Freshteam Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Departments and a Freshteam Department:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - Freshteam Department Property
     - Freshteam Data Type


ExactOnline Employees to Freshteam Employee
-------------------------------------------
Every ExactOnline Employees will be synchronized with a Freshteam Employee.

Once a link between a ExactOnline Employees and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Employees and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - ExactOnline Employees Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - BirthDate
     - date_of_birth
     - "string"

