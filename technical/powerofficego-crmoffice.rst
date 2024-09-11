===================================
PowerOfficeGO to CRMOffice Dataflow
===================================

Generated: 2024-09-11 09:03:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice Customers person to CRMOffice Contacts
--------------------------------------------------
Every PowerOffice Customers person will be synchronized with a CRMOffice Contacts.

Once a link between a PowerOffice Customers person and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers person and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
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


PowerOffice Employees to CRMOffice Contacts
-------------------------------------------
Every PowerOffice Employees will be synchronized with a CRMOffice Contacts.

Once a link between a PowerOffice Employees and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Employees and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOffice Employees Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - FirstName
     - givenName
     - "string"
   * - LastName
     - familyName
     - "string"
   * - PhoneNumber
     - mobilePhone
     - "string"


PowerOfficeGO Product to CRMOffice Companies
--------------------------------------------
Every PowerOfficeGO Product will be synchronized with a CRMOffice Companies.

Once a link between a PowerOfficeGO Product and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Product and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Product Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


PowerOfficeGO Projects to CRMOffice Activities
----------------------------------------------
Every PowerOfficeGO Projects will be synchronized with a CRMOffice Activities.

Once a link between a PowerOfficeGO Projects and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Projects and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Projects Property
     - CRMOffice Activities Property
     - CRMOffice Data Type
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


PowerOfficeGO Projectactivity to CRMOffice Activities
-----------------------------------------------------
Every PowerOfficeGO Projectactivity will be synchronized with a CRMOffice Activities.

Once a link between a PowerOfficeGO Projectactivity and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Projectactivity and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Projectactivity Property
     - CRMOffice Activities Property
     - CRMOffice Data Type


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

