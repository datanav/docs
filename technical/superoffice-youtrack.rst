================================
SuperOffice to YouTrack Dataflow
================================

Generated: 2023-11-08 13:22:29

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to YouTrack Workitems
-----------------------------------------
Every SuperOffice Contact will be synchronized with a YouTrack Workitems.

Once a link between a SuperOffice Contact and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - YouTrack Workitems Property
     - YouTrack Data Type


SuperOffice Project to YouTrack Projects
----------------------------------------
Every SuperOffice Project will be synchronized with a YouTrack Projects.

Once a link between a SuperOffice Project and a YouTrack Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Project and a YouTrack Projects:

.. list-table::
   :header-rows: 1

   * - SuperOffice Project Property
     - YouTrack Projects Property
     - YouTrack Data Type
   * - Associate.AssociateId
     - owner.gid
     - "string"
   * - EndDate
     - due_on
     - "string"
   * - Name
     - name
     - "string"
   * - NextMilestoneDate
     - start_on
     - "string"

