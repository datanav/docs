===================================
Powerofficego to Crmoffice Dataflow
===================================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers person to Crmoffice Contacts
----------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Crmoffice Contacts.

Once a link between a Powerofficego Customers person and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - FirstName
     - givenName
     - "string"
   * - LastName
     - familyName
     - "string"
   * - PhoneNumber
     - directPhone
     - "string"


Powerofficego Employees to Crmoffice Contacts
---------------------------------------------
Every Powerofficego Employees will be synchronized with a Crmoffice Contacts.

Once a link between a Powerofficego Employees and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - FirstName
     - givenName
     - "string"
   * - LastName
     - familyName
     - "string"
   * - PhoneNumber
     - mobilePhone
     - "string"


Powerofficego Product to Crmoffice Companies
--------------------------------------------
Every Powerofficego Product will be synchronized with a Crmoffice Companies.

Once a link between a Powerofficego Product and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Crmoffice Companies Property
     - Crmoffice Data Type


Powerofficego Projects to Crmoffice Activities
----------------------------------------------
Every Powerofficego Projects will be synchronized with a Crmoffice Activities.

Once a link between a Powerofficego Projects and a Crmoffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Projects and a Crmoffice Activities:

.. list-table::
   :header-rows: 1

   * - Powerofficego Projects Property
     - Crmoffice Activities Property
     - Crmoffice Data Type
   * - Name
     - subject
     - "string"
   * - ProjectManagerEmployeeId
     - ownerId
     - "string"
   * - StartDate
     - startsAt
     - "string"


Powerofficego Contactperson to Crmoffice Contacts
-------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Crmoffice Contacts.

Once a link between a Powerofficego Contactperson and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - firstName
     - givenName
     - "string"
   * - lastName
     - familyName
     - "string"
   * - phoneNumber
     - directPhone
     - "string"


Powerofficego Suppliers person to Crmoffice Contacts
----------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Crmoffice Contacts.

Once a link between a Powerofficego Suppliers person and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - FirstName
     - givenName
     - "string"
   * - LastName
     - familyName
     - "string"
   * - PhoneNumber
     - directPhone
     - "string"

