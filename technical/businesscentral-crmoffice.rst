=====================================
BusinessCentral to CRMOffice Dataflow
=====================================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers person to Crmoffice Contacts
------------------------------------------------------
Every Businesscentral Customers person will be synchronized with a Crmoffice Contacts.

Once a link between a Businesscentral Customers person and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - phoneNumber
     - directPhone
     - "string"


Businesscentral Employees to Crmoffice Contacts
-----------------------------------------------
Every Businesscentral Employees will be synchronized with a Crmoffice Contacts.

Once a link between a Businesscentral Employees and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
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


Businesscentral Items to Crmoffice Companies
--------------------------------------------
Every Businesscentral Items will be synchronized with a Crmoffice Companies.

Once a link between a Businesscentral Items and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Crmoffice Companies Property
     - Crmoffice Data Type


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

