==============================
Salesforce to Tilores Dataflow
==============================

Generated: 2024-08-23 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Tilores Human
-----------------------------------
Every Salesforce Contact will be synchronized with a Tilores Human.

Once a link between a Salesforce Contact and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Tilores Human Property
     - Tilores Data Type
   * - Birthdate
     - dateOfBirth
     - "string"
   * - Email
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - Id
     - id
     - "string"
   * - LastName
     - lastName
     - "string"
   * - MailingCity
     - city
     - "string"
   * - MailingPostalCode
     - postalCode
     - "string"
   * - MailingStreet
     - street
     - "string"
   * - Phone
     - phoneNumber
     - "string"

