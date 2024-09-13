===================================
Trello to Business Central Dataflow
===================================

Generated: 2024-09-13 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Organizations to Business Central Companies
--------------------------------------------------
Every Trello Organizations will be synchronized with a Business Central Companies.

Once a link between a Trello Organizations and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - Business Central Companies Property
     - Business Central Data Type


Trello Members to Business Central Employees
--------------------------------------------
Every Trello Members will be synchronized with a Business Central Employees.

Once a link between a Trello Members and a Business Central Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Members and a Business Central Employees:

.. list-table::
   :header-rows: 1

   * - Trello Members Property
     - Business Central Employees Property
     - Business Central Data Type
   * - email
     - personalEmail
     - "string"
   * - fullName
     - displayName
     - "string"

