==================================
Asana to Business Central Dataflow
==================================

Generated: 2024-09-11 11:41:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to BusinessCentral Companies
----------------------------------------
Every Asana Teams will be synchronized with a BusinessCentral Companies.

Once a link between a Asana Teams and a BusinessCentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a BusinessCentral Companies:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - BusinessCentral Companies Property
     - BusinessCentral Data Type


Asana Workspaces to BusinessCentral Companies
---------------------------------------------
Every Asana Workspaces will be synchronized with a BusinessCentral Companies.

Once a link between a Asana Workspaces and a BusinessCentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a BusinessCentral Companies:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - BusinessCentral Companies Property
     - BusinessCentral Data Type


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

