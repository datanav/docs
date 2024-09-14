==============================
MemberCare to Tilores Dataflow
==============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Persons to Tilores Human
-----------------------------------
Every MemberCare Persons will be synchronized with a Tilores Human.

Once a link between a MemberCare Persons and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Persons and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - MemberCare Persons Property
     - Tilores Human Property
     - Tilores Data Type
   * - addresses.id
     - id
     - "string"
   * - addresses.postalCode.city
     - city
     - "string"
   * - addresses.postalCode.zipCode
     - postalCode
     - "string"
   * - birthDate
     - dateOfBirth
     - "string"
   * - firstname
     - firstName
     - "string"
   * - lastname
     - lastName
     - "string"

