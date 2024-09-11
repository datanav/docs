===============================
Asana to PowerOfficeGO Dataflow
===============================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to PowerOfficeGOPowerOffice GOPowerofficego Projects
-------------------------------------------------------------------
Every Asana Projects will be synchronized with a PowerOfficeGOPowerOffice GOPowerofficego Projects.

Once a link between a Asana Projects and a PowerOfficeGOPowerOffice GOPowerofficego Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a PowerOfficeGOPowerOffice GOPowerofficego Projects:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - PowerOfficeGOPowerOffice GOPowerofficego Projects Property
     - PowerOfficeGOPowerOffice GOPowerofficego Data Type
   * - name
     - Name
     - "string"
   * - owner.gid
     - ProjectManagerEmployeeId
     - "integer"


Asana Users to PowerOfficeGO Employees
--------------------------------------
Every Asana Users will be synchronized with a PowerOfficeGO Employees.

Once a link between a Asana Users and a PowerOfficeGO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a PowerOfficeGO Employees:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - PowerOfficeGO Employees Property
     - PowerOfficeGO Data Type
   * - name
     - FirstName
     - "string"
   * - name
     - firstName
     - "string"
   * - workspaces.gid
     - DepartmentId
     - "string"

