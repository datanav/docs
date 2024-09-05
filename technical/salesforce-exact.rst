============================
Salesforce to Exact Dataflow
============================

Generated: 2024-09-05 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Organization to Exact Accounts
-----------------------------------------
Every Salesforce Organization will be synchronized with a Exact Accounts.

Once a link between a Salesforce Organization and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Exact Accounts Property
     - Exact Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"
   * - Name	
     - Name
     - "string"
   * - Phone	
     - Phone
     - "string"
   * - PostalCode	
     - Postcode
     - "string"


Salesforce Contact to Exact Contacts
------------------------------------
Every Salesforce Contact will be synchronized with a Exact Contacts.

Once a link between a Salesforce Contact and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Exact Contacts Property
     - Exact Data Type
   * - Birthdate
     - BirthDate
     - "string"
   * - Email
     - Email
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailingCity
     - City
     - "string"
   * - MailingCountry
     - Country
     - "string"
   * - MobilePhone
     - Mobile
     - "string"
   * - Name
     - FirstName
     - "string"
   * - Name
     - FullName
     - "string"
   * - Name
     - LastName
     - "string"
   * - Phone
     - Phone
     - "string"


Salesforce Organization to Exact Addresses
------------------------------------------
Every Salesforce Organization will be synchronized with a Exact Addresses.

Once a link between a Salesforce Organization and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Exact Addresses Property
     - Exact Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"


Salesforce Product2 to Exact Items
----------------------------------
Every Salesforce Product2 will be synchronized with a Exact Items.

Once a link between a Salesforce Product2 and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Exact Items Property
     - Exact Data Type

