====================================
Business Central to Tilores Dataflow
====================================

Generated: 2024-09-30 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Contacts (human data) to Tilores Human
-------------------------------------------------------
Every Business Central Contacts (human data) will be synchronized with a Tilores Human.

Once a link between a Business Central Contacts (human data) and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts (human data) and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts (human data) Property
     - Tilores Human Property
     - Tilores Data Type
   * - city
     - city
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - postalCode
     - postalCode
     - "string"


Business Central Customers (human data) to Tilores Human
--------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Tilores Human.

Once a link between a Business Central Customers (human data) and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - Tilores Human Property
     - Tilores Data Type
   * - city
     - city
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - postalCode
     - postalCode
     - "string"


Business Central Employees to Tilores Human
-------------------------------------------
Every Business Central Employees will be synchronized with a Tilores Human.

Once a link between a Business Central Employees and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - Tilores Human Property
     - Tilores Data Type
   * - birthDate
     - dateOfBirth
     - "string"
   * - city
     - city
     - "string"
   * - givenName
     - firstName
     - "string"
   * - id
     - id
     - "string"
   * - personalEmail
     - email
     - "string"
   * - postalCode
     - postalCode
     - "string"
   * - surname
     - lastName
     - "string"

