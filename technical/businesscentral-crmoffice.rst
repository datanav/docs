=====================================
BusinessCentral to CRMOffice Dataflow
=====================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Customers person to CRMOffice Contacts
-----------------------------------------------
Every Business Customers person will be synchronized with a CRMOffice Contacts.

Once a link between a Business Customers person and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers person and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Business Customers person Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - phoneNumber
     - directPhone
     - "string"


Business Employees to CRMOffice Contacts
----------------------------------------
Every Business Employees will be synchronized with a CRMOffice Contacts.

Once a link between a Business Employees and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Employees and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Business Employees Property
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


Business Items to CRMOffice Companies
-------------------------------------
Every Business Items will be synchronized with a CRMOffice Companies.

Once a link between a Business Items and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Items and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - Business Items Property
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

