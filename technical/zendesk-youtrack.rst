============================
Zendesk to YouTrack Dataflow
============================

Generated: 2023-11-08 13:27:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to YouTrack Workitems
-------------------------------------------
Every Zendesk Organizations will be synchronized with a YouTrack Workitems.

Once a link between a Zendesk Organizations and a YouTrack Workitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a YouTrack Workitems:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - YouTrack Workitems Property
     - YouTrack Data Type
   * - name
     - updated
     - "string"


Zendesk Ticketcomments to YouTrack Organizationroles
----------------------------------------------------
Every Zendesk Ticketcomments will be synchronized with a YouTrack Organizationroles.

Once a link between a Zendesk Ticketcomments and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Ticketcomments and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Zendesk Ticketcomments Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


Zendesk Tickets to YouTrack Organizationroles
---------------------------------------------
Every Zendesk Tickets will be synchronized with a YouTrack Organizationroles.

Once a link between a Zendesk Tickets and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type
   * - due_at
     - id
     - "string"

