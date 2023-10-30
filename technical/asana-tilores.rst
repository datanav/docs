=========================
Asana to Tilores Dataflow
=========================

Generated: 2023-10-30 16:23:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Users to Tilores Human
----------------------------
Every Asana Users will be synchronized with a Tilores Human.

Once a link between a Asana Users and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - Tilores Human Property
     - Tilores Data Type
   * - email
     - email
     - "string"
   * - name
     - firstName
     - "string"

