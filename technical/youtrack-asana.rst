==========================
YouTrack to Asana Dataflow
==========================

Generated: 2023-11-08 13:16:41

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Teams to Asana Teams
-----------------------------
Before any synchronization can take place, a link between a YouTrack Teams and a Asana Teams must be established.

A new Asana Teams will be created from a YouTrack Teams if it is connected to a YouTrack Projects, or Projectroles that is synchronized into Asana.

Once a link between a YouTrack Teams and a Asana Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Teams and a Asana Teams:

.. list-table::
   :header-rows: 1

   * - YouTrack Teams Property
     - Asana Teams Property
     - Asana Data Type


YouTrack Workspaces to Asana Workspaces
---------------------------------------
Before any synchronization can take place, a link between a YouTrack Workspaces and a Asana Workspaces must be established.

A new Asana Workspaces will be created from a YouTrack Workspaces if it is connected to a YouTrack Tasks, Projects, Workitems, or Projectroles that is synchronized into Asana.

Once a link between a YouTrack Workspaces and a Asana Workspaces is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workspaces and a Asana Workspaces:

.. list-table::
   :header-rows: 1

   * - YouTrack Workspaces Property
     - Asana Workspaces Property
     - Asana Data Type


YouTrack Projectroles to Asana Projects
---------------------------------------
Every YouTrack Projectroles will be synchronized with a Asana Projects.

Once a link between a YouTrack Projectroles and a Asana Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a Asana Projects:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     - Asana Projects Property
     - Asana Data Type
   * - owner.type
     - workspace.gid
     - "string"


YouTrack Projects to Asana Projects
-----------------------------------
Every YouTrack Projects will be synchronized with a Asana Projects.

Once a link between a YouTrack Projects and a Asana Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projects and a Asana Projects:

.. list-table::
   :header-rows: 1

   * - YouTrack Projects Property
     - Asana Projects Property
     - Asana Data Type
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
   * - ringId
     - completed_at
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


YouTrack Tasks to Asana Tasks
-----------------------------
Every YouTrack Tasks will be synchronized with a Asana Tasks.

Once a link between a YouTrack Tasks and a Asana Tasks is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Tasks and a Asana Tasks:

.. list-table::
   :header-rows: 1

   * - YouTrack Tasks Property
     - Asana Tasks Property
     - Asana Data Type
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


YouTrack Workitems to Asana Tasks
---------------------------------
Every YouTrack Workitems will be synchronized with a Asana Tasks.

Once a link between a YouTrack Workitems and a Asana Tasks is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workitems and a Asana Tasks:

.. list-table::
   :header-rows: 1

   * - YouTrack Workitems Property
     - Asana Tasks Property
     - Asana Data Type
   * - attributes
     - workspace.gid
     - "string"
   * - attributes.value
     - workspace.gid
     - "string"

