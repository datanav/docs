=================================
Zendesk to PowerOfficeGo Dataflow
=================================

Generated: 2023-10-20 08:12:38

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to PowerOfficeGo Contactperson
--------------------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a PowerOfficeGo Contactperson must be established.

A Zendesk Users will merge with a PowerOfficeGo Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOfficeGo Contactperson Property
   * - email
     - emailAddress

Once a link between a Zendesk Users and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type


Zendesk Organisations to PowerOfficeGo Departments
--------------------------------------------------
Before any synchronization can take place, a link between a Zendesk Organisations and a PowerOfficeGo Departments must be established.

A new PowerOfficeGo Departments will be created from a Zendesk Organisations if it is connected to a Zendesk Users that is synchronized into PowerOfficeGo.

Once a link between a Zendesk Organisations and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organisations and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - Zendesk Organisations Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type
   * - created_at
     - CreatedDateTimeOffset
     - "string"
   * - name
     - Name
     - "string"


Zendesk Users to PowerOfficeGo Employees
----------------------------------------
When a Zendesk User is of type Agent, it  will be synchronized with a PowerOfficeGo Employees.

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
   * - role
     - MailAddress.countryCode
     - "string"

