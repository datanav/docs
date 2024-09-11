=================================
PowerOfficeGO to Zendesk Dataflow
=================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOfficeGO Contactperson to Zendesk Users
--------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Contactperson and a Zendesk Users must be established.

A PowerOfficeGO Contactperson will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
     - Zendesk Users Property
   * - emailAddress
     - email

Once a link between a PowerOfficeGO Contactperson and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - emailAddress
     - email
     - "string"
   * - partyId
     - organization_id
     - "string"


PowerOfficeGO Customers person to Zendesk Users
-----------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Customers person and a Zendesk Users must be established.

A PowerOfficeGO Customers person will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - Zendesk Users Property
   * - EmailAddress
     - email

Once a link between a PowerOfficeGO Customers person and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers person and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - EmailAddress
     - email
     - "string"
   * - IsPerson
     - role
     - "string"


PowerOffice Customers to Zendesk Organizations
----------------------------------------------
Every PowerOffice Customers will be synchronized with a Zendesk Organizations.

Once a link between a PowerOffice Customers and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - Name
     - name
     - "string"


PowerOffice Departments to Zendesk Organizations
------------------------------------------------
Every PowerOffice Departments will be synchronized with a Zendesk Organizations.

Once a link between a PowerOffice Departments and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Departments and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - PowerOffice Departments Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - Name
     - name
     - "string"

