======================================
Businesscentral to Salesforce Dataflow
======================================

Generated: 2024-08-26 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to Salesforce Organization
----------------------------------------------------
Every Businesscentral Companies will be synchronized with a Salesforce Organization.

Once a link between a Businesscentral Companies and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     - Salesforce Organization Property
     - Salesforce Data Type


Businesscentral Contacts person to Salesforce Contact
-----------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Salesforce Contact.

Once a link between a Businesscentral Contacts person and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Salesforce Contact Property
     - Salesforce Data Type
   * - city
     - MailingCity
     - "string"
   * - email
     - Email
     - "string"
   * - id
     - Id
     - "string"
   * - mobilePhoneNumber
     - MobilePhone
     - "string"
   * - phoneNumber
     - HomePhone
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - postalCode
     - MailingPostalCode
     - "string"


Businesscentral Customers company to Salesforce Organization
------------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Salesforce Organization.

Once a link between a Businesscentral Customers company and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - city
     - City
     - "string"
   * - country
     - Country
     - "string"
   * - displayName
     - Name	
     - "string"
   * - phoneNumber
     - Phone	
     - "string"
   * - postalCode
     - PostalCode	
     - "string"


Businesscentral Items to Salesforce Product2
--------------------------------------------
Every Businesscentral Items will be synchronized with a Salesforce Product2.

Once a link between a Businesscentral Items and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - displayName
     - Name	
     - "string"

