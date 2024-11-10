============================
Trello to Freshteam Dataflow
============================

Generated: 2024-11-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Members to Freshteam Employee
------------------------------------
Every Trello Members will be synchronized with a Freshteam Employee.

Once a link between a Trello Members and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Members and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Trello Members Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - email
     - official_email
     - "string"
   * - email
     - personal_email
     - "string"

