==========================
YouTrack to Asana Dataflow
==========================

Generated: 2023-11-08 14:43:36

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Projects to Asana Projects
-----------------------------------
Before any synchronization can take place, a link between a YouTrack Projects and a Asana Projects must be established.

A new Asana Projects will be created from a YouTrack Projects if it is connected to a YouTrack Tasks, or Workitems that is synchronized into Asana.

Once a link between a YouTrack Projects and a Asana Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projects and a Asana Projects:

.. list-table::
   :header-rows: 1

   * - YouTrack Projects Property
     - Asana Projects Property
     - Asana Data Type


YouTrack Tasks to Asana Tasks
-----------------------------
Before any synchronization can take place, a link between a YouTrack Tasks and a Asana Tasks must be established.

A new Asana Tasks will be created from a YouTrack Tasks if it is connected to a YouTrack Tasks, or Workitems that is synchronized into Asana.

Once a link between a YouTrack Tasks and a Asana Tasks is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Tasks and a Asana Tasks:

.. list-table::
   :header-rows: 1

   * - YouTrack Tasks Property
     - Asana Tasks Property
     - Asana Data Type


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

