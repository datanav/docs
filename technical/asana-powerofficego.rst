===============================
Asana to Powerofficego Dataflow
===============================

Generated: 2024-03-26 14:14:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to  Projects
---------------------------
Every Asana Projects will be synchronized with a  Projects.

Once a link between a Asana Projects and a  Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a  Projects:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     -  Projects Property
     -  Data Type
   * - name
     - Name
     - "string"
   * - owner.gid
     - ProjectManagerEmployeeId
     - "integer"


Asana Users to  Employees
-------------------------
Every Asana Users will be synchronized with a  Employees.

Once a link between a Asana Users and a  Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a  Employees:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     -  Employees Property
     -  Data Type
   * - name
     - FirstName
     - "string"
   * - name
     - firstName
     - "string"
   * - workspaces.gid
     - DepartmentId
     - "string"

