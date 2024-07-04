===============================
Tilores to Superoffice Dataflow
===============================

Generated: 2024-07-04 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tilores to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tilores Human to Superoffice Person
-----------------------------------
Every Tilores Human will be synchronized with a Superoffice Person.

Once a link between a Tilores Human and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tilores Human and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Tilores Human Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - dateOfBirth
     - BirthDate
     - N/A
   * - email
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"
   * - lastName
     - Lastname
     - "string"

