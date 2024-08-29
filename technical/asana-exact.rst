==================
Asana to  Dataflow
==================

Generated: 2024-08-29 13:09:07

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to  Accounts
------------------------
Every Asana Teams will be synchronized with a  Accounts.

Once a link between a Asana Teams and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     -  Accounts Property
     -  Data Type
   * - name
     - Name
     - "string"
   * - permalink_url
     - Website
     - "string"


Asana Workspaces to  Accounts
-----------------------------
Every Asana Workspaces will be synchronized with a  Accounts.

Once a link between a Asana Workspaces and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     -  Accounts Property
     -  Data Type
   * - email_domains
     - Website
     - "string"
   * - name
     - Name
     - "string"


Asana Users to  Employees
-------------------------
Every Asana Users will be synchronized with a  Employees.

Once a link between a Asana Users and a  Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a  Employees:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     -  Employees Property
     -  Data Type
   * - email
     - Email
     - "string"

