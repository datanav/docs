============================
YouTrack to HubSpot Dataflow
============================

Generated: 2023-11-08 14:20:32

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Usergroups to HubSpot Company
--------------------------------------
Every YouTrack Usergroups will be synchronized with a HubSpot Company.

Once a link between a YouTrack Usergroups and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - HubSpot Company Property
     - HubSpot Data Type


YouTrack Workitems to HubSpot Company
-------------------------------------
Every YouTrack Workitems will be synchronized with a HubSpot Company.

Once a link between a YouTrack Workitems and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Workitems and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - YouTrack Workitems Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - date
     - properties.description
     - "string"
   * - updated
     - properties.name
     - "string"

