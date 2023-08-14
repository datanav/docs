=====================================
Freshteam to PowerOfficeGov1 Dataflow
=====================================

Generated: 2023-08-14 08:51:07

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to PowerOfficeGov1 Department
--------------------------------------------------
Every Freshteam Department will be synchronized with a PowerOfficeGov1 Department.

Once a link between a Freshteam Department and a PowerOfficeGov1 Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a PowerOfficeGov1 Department:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - PowerOfficeGov1 Department Property
     - PowerOfficeGov1 Data Type


Freshteam Department to PowerOfficeGov1 Departments
---------------------------------------------------
Every Freshteam Department will be synchronized with a PowerOfficeGov1 Departments.

Once a link between a Freshteam Department and a PowerOfficeGov1 Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a PowerOfficeGov1 Departments:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - PowerOfficeGov1 Departments Property
     - PowerOfficeGov1 Data Type


Freshteam Employee to PowerOfficeGov1 Employee
----------------------------------------------
Every Freshteam Employee will be synchronized with a PowerOfficeGov1 Employee.

If a matching PowerOfficeGov1 Employee already exists, the Freshteam Employee will be merged with the existing one.
If no matching PowerOfficeGov1 Employee is found, a new PowerOfficeGov1 Employee will be created.

A Freshteam Employee will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - PowerOfficeGov1 Employee Property
   * - employee_id
     - employeeNumber

Once a link between a Freshteam Employee and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type
   * - communication_address.communication_city
     - MailAddress.City
     - "string"

