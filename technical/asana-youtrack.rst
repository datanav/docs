==========================
Asana to YouTrack Dataflow
==========================

Generated: 2023-11-08 13:13:50

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to YouTrack Projects
-----------------------------------
Every Asana Projects will be synchronized with a YouTrack Projects.

Once a link between a Asana Projects and a YouTrack Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a YouTrack Projects:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - YouTrack Projects Property
     - YouTrack Data Type
   * - completed
     - completed
     - "string"
   * - completed
     - current_status.gid
     - "string"
   * - completed
     - current_status.title
     - "string"
   * - completed_at
     - completed_at
     - "string"
   * - completed_by.gid
     - completed_by.gid
     - "string"
   * - current_status.gid
     - completed
     - "string"
   * - current_status.gid
     - current_status.gid
     - "string"
   * - current_status.text
     - current_status.text
     - "string"
   * - current_status.title
     - completed
     - "string"
   * - current_status.title
     - current_status.title
     - "string"
   * - due_on
     - due_on
     - "string"
   * - members.gid
     - members.gid
     - "string"
   * - name
     - name
     - "string"
   * - owner.gid
     - owner.gid
     - "string"
   * - start_on
     - start_on
     - "string"
   * - team.gid
     - team.gid
     - "string"
   * - workspace.gid
     - workspace.gid
     - "string"


Asana Tasks to YouTrack Tasks
-----------------------------
Every Asana Tasks will be synchronized with a YouTrack Tasks.

Once a link between a Asana Tasks and a YouTrack Tasks is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a YouTrack Tasks:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     - YouTrack Tasks Property
     - YouTrack Data Type
   * - assignee.gid
     - assignee.gid
     - "string"
   * - completed
     - completed
     - "string"
   * - completed_at
     - completed_at
     - "string"
   * - due_on
     - due_on
     - "string"
   * - name
     - name
     - "string"
   * - parent
     - parent
     - "string"
   * - projects.gid
     - projects.gid
     - "string"
   * - start_at
     - start_at
     - "string"
   * - workspace.gid
     - workspace.gid
     - "string"

