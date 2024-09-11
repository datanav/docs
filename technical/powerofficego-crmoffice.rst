===================================
PowerOfficeGO to CRMOffice Dataflow
===================================

Generated: 2024-09-11 08:49:20

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


PowerOffice Product to CRMOffice Companies
------------------------------------------
Every PowerOffice Product will be synchronized with a CRMOffice Companies.

Once a link between a PowerOffice Product and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Product and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - PowerOffice Product Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


PowerOffice Projects to CRMOffice Activities
--------------------------------------------
Every PowerOffice Projects will be synchronized with a CRMOffice Activities.

Once a link between a PowerOffice Projects and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Projects and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - PowerOffice Projects Property
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

