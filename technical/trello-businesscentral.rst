==================================
Trello to Businesscentral Dataflow
==================================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Organizations to Businesscentral Companies
-------------------------------------------------
Every Trello Organizations will be synchronized with a Businesscentral Companies.

Once a link between a Trello Organizations and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Trello Members to Businesscentral Employees
-------------------------------------------
Every Trello Members will be synchronized with a Businesscentral Employees.

Once a link between a Trello Members and a Businesscentral Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Members and a Businesscentral Employees:

.. list-table::
   :header-rows: 1

   * - Trello Members Property
     - Businesscentral Employees Property
     - Businesscentral Data Type
   * - email
     - personalEmail
     - "string"
   * - fullName
     - displayName
     - "string"

