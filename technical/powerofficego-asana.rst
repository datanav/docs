================================
PowerOffice GO to Asana Dataflow
================================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Projects to Asana Projects
-----------------------------------------
Every PowerOffice GO Projects will be synchronized with a Asana Projects.

Once a link between a PowerOffice GO Projects and a Asana Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projects and a Asana Projects:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projects Property
     - Asana Projects Property
     - Asana Data Type
   * - Name
     - name
     - "string"
   * - ProjectManagerEmployeeId
     - owner.gid
     - "string"

