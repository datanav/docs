==============================
YouTrack to Freshteam Dataflow
==============================

Generated: 2023-11-10 13:08:37

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to Freshteam Employee
------------------------------------
Every YouTrack Users will be synchronized with a Freshteam Employee.

Once a link between a YouTrack Users and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - profile.email
     - personal_email
     - "string"

