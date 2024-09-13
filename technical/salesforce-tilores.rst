==============================
Salesforce to Tilores Dataflow
==============================

Generated: 2024-09-13 00:00:22

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
   * - ID
     - id
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


Salesforce Customer to Tilores Human
------------------------------------
Every Salesforce Customer will be synchronized with a Tilores Human.

Once a link between a Salesforce Customer and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Tilores Human Property
     - Tilores Data Type


Salesforce Seller to Tilores Human
----------------------------------
Every Salesforce Seller will be synchronized with a Tilores Human.

Once a link between a Salesforce Seller and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Seller and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Salesforce Seller Property
     - Tilores Human Property
     - Tilores Data Type


Salesforce User to Tilores Human
--------------------------------
Every Salesforce User will be synchronized with a Tilores Human.

Once a link between a Salesforce User and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Tilores Human Property
     - Tilores Data Type
   * - City
     - city
     - "string"
   * - Email
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - ID
     - id
     - "string"
   * - LastName
     - lastName
     - "string"
   * - PostalCode
     - postalCode
     - "string"

