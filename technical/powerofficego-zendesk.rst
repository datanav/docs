=================================
Powerofficego to Zendesk Dataflow
=================================

Generated: 2023-10-10 20:55:48

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to Zendesk Users
--------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Zendesk Users.

Once a link between a Powerofficego Contactperson and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - partyId
     - organization_id
     - "string"


Powerofficego Customers to Zendesk Organisations
------------------------------------------------
Every Powerofficego Customers will be synchronized with a Zendesk Organisations.

Once a link between a Powerofficego Customers and a Zendesk Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Zendesk Organisations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Zendesk Organisations Property
     - Zendesk Data Type
   * - Name
     - name
     - "string"
   * - WebsiteUrl
     - url
     - "string"


Powerofficego Departments to Zendesk Organisations
--------------------------------------------------
Every Powerofficego Departments will be synchronized with a Zendesk Organisations.

Once a link between a Powerofficego Departments and a Zendesk Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Zendesk Organisations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Zendesk Organisations Property
     - Zendesk Data Type
   * - Name
     - name
     - "string"


Powerofficego Suppliers to Zendesk Organisations
------------------------------------------------
Every Powerofficego Suppliers will be synchronized with a Zendesk Organisations.

Once a link between a Powerofficego Suppliers and a Zendesk Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a Zendesk Organisations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - Zendesk Organisations Property
     - Zendesk Data Type
   * - LegalName
     - name
     - "string"
   * - WebsiteUrl
     - url
     - "string"


Powerofficego Employees to Zendesk Users
----------------------------------------
Every Powerofficego Employees will be synchronized with a Zendesk Users.

Once a link between a Powerofficego Employees and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - DepartmentId
     - organization_id
     - "string"

