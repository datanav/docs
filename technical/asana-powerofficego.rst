===============================
Asana to Powerofficego Dataflow
===============================

Generated: 2024-07-05 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to Powerofficego Projects
----------------------------------------
Every Asana Projects will be synchronized with a Powerofficego Projects.

Once a link between a Asana Projects and a Powerofficego Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a Powerofficego Projects:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - Powerofficego Projects Property
     - Powerofficego Data Type
   * - name
     - Name
     - "string"
   * - owner.gid
     - ProjectManagerEmployeeId
     - "integer"


Asana Users to Powerofficego Employees
--------------------------------------
Every Asana Users will be synchronized with a Powerofficego Employees.

Once a link between a Asana Users and a Powerofficego Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a Powerofficego Employees:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - Powerofficego Employees Property
     - Powerofficego Data Type
   * - name
     - FirstName
     - "string"
   * - name
     - firstName
     - "string"
   * - workspaces.gid
     - DepartmentId
     - "string"

