===============================
SuperOffice to Tilores Dataflow
===============================

Generated: 2024-06-29 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to Tilores Human
-----------------------------------
Every SuperOffice Person will be synchronized with a Tilores Human.

Once a link between a SuperOffice Person and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tilores Human Property
     - Tilores Data Type
   * - Address.Postal.City
     - city
     - "string"
   * - Address.Postal.Zipcode
     - postalCode
     - "string"
   * - Address.Street.City
     - city
     - "string"
   * - Address.Street.Zipcode
     - postalCode
     - "string"
   * - BirthDate
     - dateOfBirth
     - "string"
   * - Emails.Value
     - email
     - "string"
   * - Firstname
     - firstName
     - "string"
   * - Lastname
     - lastName
     - "string"
   * - PersonId
     - id
     - "string"

