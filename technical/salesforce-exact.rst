=======================
Salesforce to  Dataflow
=======================

Generated: 2024-08-29 10:35:42

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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

