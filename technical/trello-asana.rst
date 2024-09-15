========================
Trello to Asana Dataflow
========================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Cards to Asana Tasks
---------------------------
Every Trello Cards will be synchronized with a Asana Tasks.

Once a link between a Trello Cards and a Asana Tasks is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Cards and a Asana Tasks:

.. list-table::
   :header-rows: 1

   * - Trello Cards Property
     - Asana Tasks Property
     - Asana Data Type
   * - due
     - due_on
     - "string"
   * - dueComplete
     - completed_at
     - "string"
   * - name
     - name
     - "string"
   * - start
     - start_at
     - "string"


Trello Organizations to Asana Workspaces
----------------------------------------
Every Trello Organizations will be synchronized with a Asana Workspaces.

Once a link between a Trello Organizations and a Asana Workspaces is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a Asana Workspaces:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - Asana Workspaces Property
     - Asana Data Type
   * - name
     - name
     - "string"
   * - website
     - email_domains
     - "string"

