===========================
Asana to Freshteam Dataflow
===========================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Users to Freshteam Employee
---------------------------------
Every Asana Users will be synchronized with a Freshteam Employee.

Once a link between a Asana Users and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - email
     - personal_email
     - "string"
   * - name
     - first_name
     - "string"

