=============================
Asana to ExactOnline Dataflow
=============================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to ExactOnline Accounts
-----------------------------------
Every Asana Teams will be synchronized with a ExactOnline Accounts.

Once a link between a Asana Teams and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
   * - name
     - Name
     - "string"
   * - permalink_url
     - Website
     - "string"


Asana Workspaces to ExactOnline Accounts
----------------------------------------
Every Asana Workspaces will be synchronized with a ExactOnline Accounts.

Once a link between a Asana Workspaces and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
   * - email_domains
     - Website
     - "string"
   * - name
     - Name
     - "string"


Asana Users to ExactOnline Employees
------------------------------------
Every Asana Users will be synchronized with a ExactOnline Employees.

Once a link between a Asana Users and a ExactOnline Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a ExactOnline Employees:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - ExactOnline Employees Property
     - ExactOnline Data Type
   * - email
     - Email
     - "string"

