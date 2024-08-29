=======================
Salesforce to  Dataflow
=======================

Generated: 2024-08-29 11:00:44

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Organization to  Accounts
------------------------------------
Every Salesforce Organization will be synchronized with a  Accounts.

Once a link between a Salesforce Organization and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     -  Accounts Property
     -  Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"


Salesforce Contact to  Contacts
-------------------------------
Every Salesforce Contact will be synchronized with a  Contacts.

Once a link between a Salesforce Contact and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     -  Contacts Property
     -  Data Type
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
   * - Phone
     - Phone
     - "string"


Salesforce Organization to  Addresses
-------------------------------------
Every Salesforce Organization will be synchronized with a  Addresses.

Once a link between a Salesforce Organization and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a  Addresses:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     -  Addresses Property
     -  Data Type
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"

