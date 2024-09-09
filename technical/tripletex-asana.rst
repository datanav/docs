===========================
Tripletex to Asana Dataflow
===========================

Generated: 2024-09-09 12:08:45

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Project to Asana Projects
-----------------------------------
Every Tripletex Project will be synchronized with a Asana Projects.

Once a link between a Tripletex Project and a Asana Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a Asana Projects:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - Asana Projects Property
     - Asana Data Type
   * - endDate
     - completed_at
     - "string"
   * - endDate
     - due_date
     - "string"
   * - endDate
     - due_on
     - "string"
   * - name
     - name
     - "string"
   * - projectManager.id
     - owner.gid
     - "string"
   * - startDate
     - start_on
     - "string"


Tripletex Task to Asana Tasks
-----------------------------
Every Tripletex Task will be synchronized with a Asana Tasks.

Once a link between a Tripletex Task and a Asana Tasks is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Task and a Asana Tasks:

.. list-table::
   :header-rows: 1

   * - Tripletex Task Property
     - Asana Tasks Property
     - Asana Data Type
   * - name
     - name
     - "string"
   * - sesam_projectid
     - projects.gid
     - "string"

