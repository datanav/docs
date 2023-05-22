=============================
Tripletex to Tilores Dataflow
=============================

Generated: 2023-05-22 22:07:15

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Tilores Human
----------------------------------
Every Tripletex Contact will be synchronized with a Tilores Human.

Once a link between a Tripletex Contact and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Tilores Human Property
     - Tilores Data Type
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"


Tripletex Employee to Tilores Human
-----------------------------------
Every Tripletex Employee will be synchronized with a Tilores Human.

Once a link between a Tripletex Employee and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Tilores Human Property
     - Tilores Data Type
   * - address.changes
     - city
     - "string"
   * - address.id
     - postalCode
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - lastName
     - "string"

