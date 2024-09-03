===================================
Powerofficego to Crmoffice Dataflow
===================================

Generated: 2024-09-03 09:00:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers person to  Contacts
-------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Contacts.

Once a link between a Powerofficego Customers person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Contacts Property
     -  Data Type
   * - FirstName
     - givenName
     - "string"
   * - LastName
     - familyName
     - "string"
   * - PhoneNumber
     - directPhone
     - "string"


Powerofficego Employees to  Contacts
------------------------------------
Every Powerofficego Employees will be synchronized with a  Contacts.

Once a link between a Powerofficego Employees and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     -  Contacts Property
     -  Data Type
   * - FirstName
     - givenName
     - "string"
   * - LastName
     - familyName
     - "string"
   * - PhoneNumber
     - mobilePhone
     - "string"


Powerofficego Product to  Companies
-----------------------------------
Every Powerofficego Product will be synchronized with a  Companies.

Once a link between a Powerofficego Product and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a  Companies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     -  Companies Property
     -  Data Type


Powerofficego Projects to  Activities
-------------------------------------
Every Powerofficego Projects will be synchronized with a  Activities.

Once a link between a Powerofficego Projects and a  Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Projects and a  Activities:

.. list-table::
   :header-rows: 1

   * - Powerofficego Projects Property
     -  Activities Property
     -  Data Type
   * - Name
     - subject
     - "string"
   * - ProjectManagerEmployeeId
     - ownerId
     - "string"
   * - StartDate
     - startsAt
     - "string"


Powerofficego Contactperson to  Contacts
----------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Contacts.

Once a link between a Powerofficego Contactperson and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Contacts Property
     -  Data Type
   * - firstName
     - givenName
     - "string"
   * - lastName
     - familyName
     - "string"
   * - phoneNumber
     - directPhone
     - "string"


Powerofficego Suppliers person to  Contacts
-------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a  Contacts.

Once a link between a Powerofficego Suppliers person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     -  Contacts Property
     -  Data Type
   * - FirstName
     - givenName
     - "string"
   * - LastName
     - familyName
     - "string"
   * - PhoneNumber
     - directPhone
     - "string"

