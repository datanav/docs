==================================
YouTrack to PowerOfficeGo Dataflow
==================================

Generated: 2023-11-10 13:04:36

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to PowerOfficeGo Contactperson
---------------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a PowerOfficeGo Contactperson must be established.

A YouTrack Users will merge with a PowerOfficeGo Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOfficeGo Contactperson Property
   * - 
     - emailAddress

Once a link between a YouTrack Users and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - profile.email
     - emailAddress
     - "string"

