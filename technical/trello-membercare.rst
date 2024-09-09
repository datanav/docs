=============================
Trello to Membercare Dataflow
=============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Members to Membercare Persons
------------------------------------
Every Trello Members will be synchronized with a Membercare Persons.

Once a link between a Trello Members and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Members and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Trello Members Property
     - Membercare Persons Property
     - Membercare Data Type
   * - fullName
     - name
     - "string"


Trello Organizations to Membercare Companies
--------------------------------------------
Every Trello Organizations will be synchronized with a Membercare Companies.

Once a link between a Trello Organizations and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - Membercare Companies Property
     - Membercare Data Type
   * - name
     - companyName
     - "string"
   * - website
     - url
     - "string"

