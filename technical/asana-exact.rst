=======================
Asana to Exact Dataflow
=======================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to Exact Accounts
-----------------------------
Every Asana Teams will be synchronized with a Exact Accounts.

Once a link between a Asana Teams and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - Exact Accounts Property
     - Exact Data Type
   * - name
     - Name
     - "string"
   * - permalink_url
     - Website
     - "string"


Asana Workspaces to Exact Accounts
----------------------------------
Every Asana Workspaces will be synchronized with a Exact Accounts.

Once a link between a Asana Workspaces and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - Exact Accounts Property
     - Exact Data Type
   * - email_domains
     - Website
     - "string"
   * - name
     - Name
     - "string"


Asana Users to Exact Employees
------------------------------
Every Asana Users will be synchronized with a Exact Employees.

Once a link between a Asana Users and a Exact Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a Exact Employees:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - Exact Employees Property
     - Exact Data Type
   * - email
     - Email
     - "string"

