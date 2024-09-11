===================================
PowerOfficeGO to CRMOffice Dataflow
===================================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


PowerOfficeGO Contactperson to CRMOffice Contacts
-------------------------------------------------
Every PowerOfficeGO Contactperson will be synchronized with a CRMOffice Contacts.

Once a link between a PowerOfficeGO Contactperson and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - firstName
     - givenName
     - "string"
   * - lastName
     - familyName
     - "string"
   * - phoneNumber
     - directPhone
     - "string"


PowerOfficeGO Suppliers person to CRMOffice Contacts
----------------------------------------------------
Every PowerOfficeGO Suppliers person will be synchronized with a CRMOffice Contacts.

Once a link between a PowerOfficeGO Suppliers person and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Suppliers person and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Suppliers person Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - FirstName
     - givenName
     - "string"
   * - LastName
     - familyName
     - "string"
   * - PhoneNumber
     - directPhone
     - "string"

