==============================
Freshteam to YouTrack Dataflow
==============================

Generated: 2023-11-29 14:44:43

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to YouTrack Groups
---------------------------------------
Every Freshteam Department will be synchronized with a YouTrack Groups.

Once a link between a Freshteam Department and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"

