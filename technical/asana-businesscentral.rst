=================================
Asana to Businesscentral Dataflow
=================================

Generated: 2024-07-04 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to Businesscentral Companies
----------------------------------------
Every Asana Teams will be synchronized with a Businesscentral Companies.

Once a link between a Asana Teams and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Asana Workspaces to Businesscentral Companies
---------------------------------------------
Every Asana Workspaces will be synchronized with a Businesscentral Companies.

Once a link between a Asana Workspaces and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Asana Users to Businesscentral Employees
----------------------------------------
Every Asana Users will be synchronized with a Businesscentral Employees.

Once a link between a Asana Users and a Businesscentral Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a Businesscentral Employees:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - Businesscentral Employees Property
     - Businesscentral Data Type
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

