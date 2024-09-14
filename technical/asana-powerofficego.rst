================================
Asana to PowerOffice GO Dataflow
================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to PowerOffice GO Projects
-----------------------------------------
Every Asana Projects will be synchronized with a PowerOffice GO Projects.

Once a link between a Asana Projects and a PowerOffice GO Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a PowerOffice GO Projects:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - PowerOffice GO Projects Property
     - PowerOffice GO Data Type
   * - name
     - Name
     - "string"
   * - owner.gid
     - ProjectManagerEmployeeId
     - "integer"


Asana Users to PowerOffice GO Employees
---------------------------------------
Every Asana Users will be synchronized with a PowerOffice GO Employees.

Once a link between a Asana Users and a PowerOffice GO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a PowerOffice GO Employees:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - PowerOffice GO Employees Property
     - PowerOffice GO Data Type
   * - name
     - FirstName
     - "string"
   * - name
     - firstName
     - "string"
   * - workspaces.gid
     - DepartmentId
     - "string"

