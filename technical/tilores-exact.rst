================================
Tilores to Exact Online Dataflow
================================

Generated: 2024-09-11 12:17:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tilores to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tilores Human to Exact Online Contacts
--------------------------------------
Every Tilores Human will be synchronized with a Exact Online Contacts.

Once a link between a Tilores Human and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tilores Human and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Tilores Human Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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

