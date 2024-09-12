==================================
PowerOffice GO to Zendesk Dataflow
==================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to Zendesk Users
---------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Zendesk Users must be established.

A PowerOffice GO Contactperson will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Zendesk Users Property
   * - emailAddress
     - email

Once a link between a PowerOffice GO Contactperson and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - emailAddress
     - email
     - "string"
   * - partyId
     - organization_id
     - "string"


PowerOffice GO Customers person to Zendesk Users
------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers person and a Zendesk Users must be established.

A PowerOffice GO Customers person will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Zendesk Users Property
   * - EmailAddress
     - email

Once a link between a PowerOffice GO Customers person and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - EmailAddress
     - email
     - "string"
   * - IsPerson
     - role
     - "string"


PowerOffice GO Customers to Zendesk Organizations
-------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Zendesk Organizations.

Once a link between a PowerOffice GO Customers and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - Name
     - name
     - "string"


PowerOffice GO Departments to Zendesk Organizations
---------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a Zendesk Organizations.

Once a link between a PowerOffice GO Departments and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - Name
     - name
     - "string"

