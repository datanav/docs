================================
Exact Online to Tilores Dataflow
================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Online Contacts to Tilores Human
--------------------------------------
Every Exact Online Contacts will be synchronized with a Tilores Human.

Once a link between a Exact Online Contacts and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Contacts and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Exact Online Contacts Property
     - Tilores Human Property
     - Tilores Data Type
   * - BirthDate
     - dateOfBirth
     - "string"
   * - City
     - city
     - "string"


Exact Online Employees to Tilores Human
---------------------------------------
Every Exact Online Employees will be synchronized with a Tilores Human.

Once a link between a Exact Online Employees and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Employees and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Exact Online Employees Property
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

