=================================
PowerOfficeGO to Zendesk Dataflow
=================================

Generated: 2024-09-11 08:35:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice Contactperson to Zendesk Users
------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Contactperson and a Zendesk Users must be established.

A PowerOffice Contactperson will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - Zendesk Users Property
   * - emailAddress
     - email

Once a link between a PowerOffice Contactperson and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - emailAddress
     - email
     - "string"
   * - partyId
     - organization_id
     - "string"


PowerOffice Customers person to Zendesk Users
---------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Customers person and a Zendesk Users must be established.

A PowerOffice Customers person will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - Zendesk Users Property
   * - EmailAddress
     - email

Once a link between a PowerOffice Customers person and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers person and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - EmailAddress
     - email
     - "string"
   * - IsPerson
     - role
     - "string"


Powerofficego Customers to Zendesk Organizations
------------------------------------------------
Every Powerofficego Customers will be synchronized with a Zendesk Organizations.

Once a link between a Powerofficego Customers and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - Name
     - name
     - "string"


Powerofficego Departments to Zendesk Organizations
--------------------------------------------------
Every Powerofficego Departments will be synchronized with a Zendesk Organizations.

Once a link between a Powerofficego Departments and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - Name
     - name
     - "string"

