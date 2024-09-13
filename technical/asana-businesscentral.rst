==================================
Asana to Business Central Dataflow
==================================

Generated: 2024-09-13 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to Business Central Companies
-----------------------------------------
Every Asana Teams will be synchronized with a Business Central Companies.

Once a link between a Asana Teams and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - Business Central Companies Property
     - Business Central Data Type


Asana Workspaces to Business Central Companies
----------------------------------------------
Every Asana Workspaces will be synchronized with a Business Central Companies.

Once a link between a Asana Workspaces and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - Business Central Companies Property
     - Business Central Data Type


Asana Users to Business Central Employees
-----------------------------------------
Every Asana Users will be synchronized with a Business Central Employees.

Once a link between a Asana Users and a Business Central Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a Business Central Employees:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - Business Central Employees Property
     - Business Central Data Type
   * - email
     - email
     - "string"
   * - email
     - personalEmail
     - "string"
   * - name
     - displayName
     - "string"
   * - name
     - givenName
     - "string"
   * - name
     - surname
     - "string"
   * - workspaces.gid
     - jobTitle
     - "string"

