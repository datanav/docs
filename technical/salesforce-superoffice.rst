==================================
Salesforce to Superoffice Dataflow
==================================

Generated: 2024-08-23 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Superoffice Person
----------------------------------------
Every Salesforce Contact will be synchronized with a Superoffice Person.

Once a link between a Salesforce Contact and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - Birthdate
     - BirthDate
     - N/A
   * - Email
     - Emails.Value
     - "string"
   * - FirstName
     - Firstname
     - "string"
   * - HomePhone
     - OfficePhones.Value
     - "string"
   * - HomePhone
     - PrivatePhones.Value
     - "string"
   * - LastName
     - Lastname
     - "string"
   * - MobilePhone
     - MobilePhones.Value
     - "string"
   * - Phone
     - OfficePhones.Value
     - "string"

