=============================
Tripletex to Tilores Dataflow
=============================

Generated: 2023-06-27 11:30:28

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

