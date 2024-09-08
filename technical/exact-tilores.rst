=========================
Exact to Tilores Dataflow
=========================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Contacts to Tilores Human
-------------------------------
Every Exact Contacts will be synchronized with a Tilores Human.

Once a link between a Exact Contacts and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - Tilores Human Property
     - Tilores Data Type
   * - BirthDate
     - dateOfBirth
     - "string"
   * - City
     - city
     - "string"


Exact Employees to Tilores Human
--------------------------------
Every Exact Employees will be synchronized with a Tilores Human.

Once a link between a Exact Employees and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
     - Tilores Human Property
     - Tilores Data Type
   * - BirthDate
     - dateOfBirth
     - "string"
   * - City
     - city
     - "string"
   * - ID
     - id
     - "string"
   * - Postcode
     - postalCode
     - "string"

