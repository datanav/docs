======================================
Business Central to CRMOffice Dataflow
======================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Customers person to CRMOffice Contacts
-------------------------------------------------------
Every Business Central Customers person will be synchronized with a CRMOffice Contacts.

Once a link between a Business Central Customers person and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - phoneNumber
     - directPhone
     - "string"


Business Central Employees to CRMOffice Contacts
------------------------------------------------
Every Business Central Employees will be synchronized with a CRMOffice Contacts.

Once a link between a Business Central Employees and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - givenName
     - givenName
     - "string"
   * - mobilePhone
     - mobilePhone
     - "string"
   * - phoneNumber
     - directPhone
     - "string"
   * - surname
     - familyName
     - "string"


Business Central Items to CRMOffice Companies
---------------------------------------------
Every Business Central Items will be synchronized with a CRMOffice Companies.

Once a link between a Business Central Items and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


Business Central Contacts person to CRMOffice Contacts
------------------------------------------------------
Every Business Central Contacts person will be synchronized with a CRMOffice Contacts.

Once a link between a Business Central Contacts person and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - mobilePhoneNumber
     - mobilePhone
     - "string"
   * - phoneNumber
     - directPhone
     - "string"


Business Central Customers company to CRMOffice Companies
---------------------------------------------------------
Every Business Central Customers company will be synchronized with a CRMOffice Companies.

Once a link between a Business Central Customers company and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - CRMOffice Companies Property
     - CRMOffice Data Type
   * - city
     - postAddress.postalArea
     - "string"
   * - country
     - postAddress.country
     - "string"
   * - country
     - visitAddress.country
     - "string"
   * - postalCode
     - postAddress.postCode
     - "string"

