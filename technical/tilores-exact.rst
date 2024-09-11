================================
Tilores to Exact Online Dataflow
================================

Generated: 2024-09-11 11:39:33

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tilores to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tilores Human to ExactOnline Contacts
-------------------------------------
Every Tilores Human will be synchronized with a ExactOnline Contacts.

Once a link between a Tilores Human and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tilores Human and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - Tilores Human Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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

