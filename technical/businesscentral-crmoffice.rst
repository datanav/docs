======================================
Business Central to CRMOffice Dataflow
======================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessCentral Customers person to CRMOffice Contacts
------------------------------------------------------
Every BusinessCentral Customers person will be synchronized with a CRMOffice Contacts.

Once a link between a BusinessCentral Customers person and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers person and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers person Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - phoneNumber
     - directPhone
     - "string"


BusinessCentral Employees to CRMOffice Contacts
-----------------------------------------------
Every BusinessCentral Employees will be synchronized with a CRMOffice Contacts.

Once a link between a BusinessCentral Employees and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Employees and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Employees Property
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


BusinessCentral Items to CRMOffice Companies
--------------------------------------------
Every BusinessCentral Items will be synchronized with a CRMOffice Companies.

Once a link between a BusinessCentral Items and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Items and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


BusinessCentral Contacts person to CRMOffice Contacts
-----------------------------------------------------
Every BusinessCentral Contacts person will be synchronized with a CRMOffice Contacts.

Once a link between a BusinessCentral Contacts person and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - mobilePhoneNumber
     - mobilePhone
     - "string"
   * - phoneNumber
     - directPhone
     - "string"


BusinessCentral Customers company to CRMOffice Companies
--------------------------------------------------------
Every BusinessCentral Customers company will be synchronized with a CRMOffice Companies.

Once a link between a BusinessCentral Customers company and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers company and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers company Property
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

