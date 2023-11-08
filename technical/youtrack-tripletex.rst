==============================
YouTrack to Tripletex Dataflow
==============================

Generated: 2023-11-08 13:14:31

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Projectroles to Tripletex Project
------------------------------------------
Every YouTrack Projectroles will be synchronized with a Tripletex Project.

Once a link between a YouTrack Projectroles and a Tripletex Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projectroles and a Tripletex Project:

.. list-table::
   :header-rows: 1

   * - YouTrack Projectroles Property
     - Tripletex Project Property
     - Tripletex Data Type


YouTrack Projects to Tripletex Project
--------------------------------------
Every YouTrack Projects will be synchronized with a Tripletex Project.

Once a link between a YouTrack Projects and a Tripletex Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Projects and a Tripletex Project:

.. list-table::
   :header-rows: 1

   * - YouTrack Projects Property
     - Tripletex Project Property
     - Tripletex Data Type
   * - due_on
     - endDate
     - "datetime-format","%Y-%m-%d","_."]
   * - name
     - name
     - "string"
   * - owner.gid
     - projectManager.id
     - "integer"
   * - start_on
     - startDate
     - "datetime-format","%Y-%m-%d","_."]

