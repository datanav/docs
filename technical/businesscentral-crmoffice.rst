=====================================
BusinessCentral to CRMOffice Dataflow
=====================================

Generated: 2024-09-11 08:35:29

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


Business Contacts person to CRMOffice Contacts
----------------------------------------------
Every Business Contacts person will be synchronized with a CRMOffice Contacts.

Once a link between a Business Contacts person and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - mobilePhoneNumber
     - mobilePhone
     - "string"
   * - phoneNumber
     - directPhone
     - "string"


Business Customers company to CRMOffice Companies
-------------------------------------------------
Every Business Customers company will be synchronized with a CRMOffice Companies.

Once a link between a Business Customers company and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers company and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - Business Customers company Property
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

