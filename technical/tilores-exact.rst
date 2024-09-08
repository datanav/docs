=========================
Tilores to Exact Dataflow
=========================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tilores to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tilores Human to Exact Contacts
-------------------------------
Every Tilores Human will be synchronized with a Exact Contacts.

Once a link between a Tilores Human and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tilores Human and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Tilores Human Property
     - Exact Contacts Property
     - Exact Data Type
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

