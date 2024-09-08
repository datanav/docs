==============================
Tilores to Membercare Dataflow
==============================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tilores to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tilores Human to Membercare Persons
-----------------------------------
Every Tilores Human will be synchronized with a Membercare Persons.

Once a link between a Tilores Human and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tilores Human and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Tilores Human Property
     - Membercare Persons Property
     - Membercare Data Type
   * - dateOfBirth
     - birthDate
     - "string"
   * - firstName
     - firstname
     - "string"
   * - lastName
     - lastname
     - "string"

