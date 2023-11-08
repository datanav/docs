================================
YouTrack to SuperOffice Dataflow
================================

Generated: 2023-11-08 14:21:27

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Usergroups to SuperOffice Contact
------------------------------------------
Every YouTrack Usergroups will be synchronized with a SuperOffice Contact.

Once a link between a YouTrack Usergroups and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - SuperOffice Contact Property
     - SuperOffice Data Type


YouTrack Workitems to SuperOffice Contact
-----------------------------------------
Every YouTrack Workitems will be synchronized with a SuperOffice Contact.

Once a link between a YouTrack Workitems and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workitems and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - YouTrack Workitems Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - updated
     - Name
     - "string"

