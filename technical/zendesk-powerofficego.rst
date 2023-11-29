====================
Zendesk to  Dataflow
====================

Generated: 2023-11-29 23:37:14

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to  Contactperson
-------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a  Contactperson must be established.

A Zendesk Users will merge with a  Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Contactperson Property
   * - email
     - emailAddress

Once a link between a Zendesk Users and a  Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a  Contactperson:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Contactperson Property
     -  Data Type
   * - email
     - emailAddress
     - "string"
   * - organization_id
     - partyId
     - "integer"


Zendesk Organizations to PowerOfficeGo Customers person
-------------------------------------------------------
Before any synchronization can take place, a link between a Zendesk Organizations and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Zendesk Organizations if it is connected to a Zendesk Users that is synchronized into PowerOfficeGo.

Once a link between a Zendesk Organizations and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type


Zendesk Organizations to PowerOfficeGo Customers
------------------------------------------------
Before any synchronization can take place, a link between a Zendesk Organizations and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Zendesk Organizations if it is connected to a Zendesk Users that is synchronized into PowerOfficeGo.

Once a link between a Zendesk Organizations and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - name
     - Name
     - "string"
   * - url
     - WebsiteUrl
     - "string"


Zendesk Users to  Employees
---------------------------
When a Zendesk User is of type Agent, it  will be synchronized with a  Employees.

Once a link between a Zendesk Users and a  Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a  Employees:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Employees Property
     -  Data Type
   * - created_at
     - EmployeeCreatedDateTimeOffset
     - "string"
   * - created_at
     - employeeCreatedDateTimeOffset
     - "string"
   * - organization_id
     - DepartmentId (Dependant on having wd:Q703534 in JobTitle)
     - "string"
   * - role
     - MailAddress.countryCode
     - "string"

