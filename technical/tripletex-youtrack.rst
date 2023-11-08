==============================
Tripletex to YouTrack Dataflow
==============================

Generated: 2023-11-08 13:13:50

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Project to YouTrack Projects
--------------------------------------
Every Tripletex Project will be synchronized with a YouTrack Projects.

Once a link between a Tripletex Project and a YouTrack Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a YouTrack Projects:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - YouTrack Projects Property
     - YouTrack Data Type
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

