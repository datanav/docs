==============================
Tilores to MemberCare Dataflow
==============================

Generated: 2024-11-11 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tilores to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tilores Human to MemberCare Persons
-----------------------------------
Every Tilores Human will be synchronized with a MemberCare Persons.

Once a link between a Tilores Human and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tilores Human and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Tilores Human Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - dateOfBirth
     - birthDate
     - "string"
   * - firstName
     - firstname
     - "string"
   * - lastName
     - lastname
     - "string"

