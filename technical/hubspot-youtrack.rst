============================
HubSpot to YouTrack Dataflow
============================

Generated: 2023-11-08 13:21:41

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to YouTrack Workitems
-------------------------------------
Every HubSpot Company will be synchronized with a YouTrack Workitems.

Once a link between a HubSpot Company and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - properties.description
     - date
     - "string"
   * - properties.name
     - updated
     - "string"


HubSpot Ticket to YouTrack Organizationroles
--------------------------------------------
Every HubSpot Ticket will be synchronized with a YouTrack Organizationroles.

Once a link between a HubSpot Ticket and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type

