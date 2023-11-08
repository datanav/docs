==============================
Freshteam to YouTrack Dataflow
==============================

Generated: 2023-11-08 14:19:28

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to YouTrack Usergroups
-------------------------------------------
Every Freshteam Department will be synchronized with a YouTrack Usergroups.

Once a link between a Freshteam Department and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - YouTrack Usergroups Property
     - YouTrack Data Type


Freshteam Department to YouTrack Workitems
------------------------------------------
Every Freshteam Department will be synchronized with a YouTrack Workitems.

Once a link between a Freshteam Department and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - name
     - updated
     - "string"

