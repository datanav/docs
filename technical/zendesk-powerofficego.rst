=================================
Zendesk to PowerOfficeGo Dataflow
=================================

Generated: 2023-10-10 20:55:48

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to PowerOfficeGo Employees
----------------------------------------
Every Zendesk Users will be synchronized with a PowerOfficeGo Employees.

Once a link between a Zendesk Users and a PowerOfficeGo Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a PowerOfficeGo Employees:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOfficeGo Employees Property
     - PowerOfficeGo Data Type
   * - created_at
     - EmployeeCreatedDateTimeOffset
     - "string"
   * - created_at
     - employeeCreatedDateTimeOffset
     - "string"
   * - organization_id
     - DepartmentId
     - "string"

