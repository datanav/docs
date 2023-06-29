=======================
Asana to Asana Dataflow
=======================

Generated: 2023-06-29 21:30:38

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Tasks to Asana Projects
-----------------------------
Every Asana Tasks will be synchronized with a Asana Projects.

Once a link between a Asana Tasks and a Asana Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a Asana Projects:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     - Asana Projects Property
     - Asana Data Type
   * - completed_at
     - completed_at
     - "string"
   * - created_at
     - created_at
     - "string"
   * - due_on
     - due_date
     - "string"
   * - workspace.gid
     - workspace.gid
     - "string"

