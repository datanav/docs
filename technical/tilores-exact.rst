====================
Tilores to  Dataflow
====================

Generated: 2024-08-29 10:36:42

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tilores to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tilores Human to  Contacts
--------------------------
Every Tilores Human will be synchronized with a  Contacts.

Once a link between a Tilores Human and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tilores Human and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Tilores Human Property
     -  Contacts Property
     -  Data Type
   * - city
     - City
     - "string"
   * - dateOfBirth
     - BirthDate
     - "string"
   * - email
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"

