===============================
Tilores to SuperOffice Dataflow
===============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tilores to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tilores Human to SuperOffice Person
-----------------------------------
Every Tilores Human will be synchronized with a SuperOffice Person.

Once a link between a Tilores Human and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tilores Human and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Tilores Human Property
     - SuperOffice Person Property
     - SuperOffice Data Type
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

