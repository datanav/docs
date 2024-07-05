=============================
SuperOffice to Asana Dataflow
=============================

Generated: 2024-07-05 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Ownercontactlink to Asana Teams
-------------------------------------------
Every SuperOffice Ownercontactlink will be synchronized with a Asana Teams.

Once a link between a SuperOffice Ownercontactlink and a Asana Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a Asana Teams:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - Asana Teams Property
     - Asana Data Type
   * - name
     - name
     - "string"


SuperOffice Project to Asana Projects
-------------------------------------
Every SuperOffice Project will be synchronized with a Asana Projects.

Once a link between a SuperOffice Project and a Asana Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Project and a Asana Projects:

.. list-table::
   :header-rows: 1

   * - SuperOffice Project Property
     - Asana Projects Property
     - Asana Data Type
   * - Associate.AssociateId
     - owner.gid
     - "string"
   * - CreatedDate
     - created_at
     - "string"
   * - EndDate
     - due_date
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

