==================================
Trello to BusinessCentral Dataflow
==================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Organizations to Business Companies
------------------------------------------
Every Trello Organizations will be synchronized with a Business Companies.

Once a link between a Trello Organizations and a Business Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a Business Companies:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - Business Companies Property
     - Business Data Type


Trello Members to BusinessCentral Employees
-------------------------------------------
Every Trello Members will be synchronized with a BusinessCentral Employees.

Once a link between a Trello Members and a BusinessCentral Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Members and a BusinessCentral Employees:

.. list-table::
   :header-rows: 1

   * - Trello Members Property
     - BusinessCentral Employees Property
     - BusinessCentral Data Type
   * - email
     - personalEmail
     - "string"
   * - fullName
     - displayName
     - "string"

