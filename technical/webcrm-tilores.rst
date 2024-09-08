==========================
Webcrm to Tilores Dataflow
==========================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Persons to Tilores Human
-------------------------------
Every Webcrm Persons will be synchronized with a Tilores Human.

Once a link between a Webcrm Persons and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     - Tilores Human Property
     - Tilores Data Type
   * - PersonFirstName
     - firstName
     - "string"
   * - PersonLastName
     - lastName
     - "string"
   * - document_number
     - dateOfBirth
     - "string"


Webcrm Users to Tilores Human
-----------------------------
Every Webcrm Users will be synchronized with a Tilores Human.

Once a link between a Webcrm Users and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Users and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Webcrm Users Property
     - Tilores Human Property
     - Tilores Data Type

