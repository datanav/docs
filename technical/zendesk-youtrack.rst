============================
Zendesk to YouTrack Dataflow
============================

Generated: 2023-11-10 13:02:58

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to YouTrack Groups
----------------------------------------
Every Zendesk Organizations will be synchronized with a YouTrack Groups.

Once a link between a Zendesk Organizations and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


Zendesk Organizations to YouTrack Usergroups
--------------------------------------------
Every Zendesk Organizations will be synchronized with a YouTrack Usergroups.

Once a link between a Zendesk Organizations and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - name
     - name
     - "string"


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


Zendesk Ticketcomments to YouTrack Hubprojects
----------------------------------------------
Every Zendesk Ticketcomments will be synchronized with a YouTrack Hubprojects.

Once a link between a Zendesk Ticketcomments and a YouTrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Ticketcomments and a YouTrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - Zendesk Ticketcomments Property
     - YouTrack Hubprojects Property
     - YouTrack Data Type


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


Zendesk Ticketcomments to YouTrack Usergroups
---------------------------------------------
Every Zendesk Ticketcomments will be synchronized with a YouTrack Usergroups.

Once a link between a Zendesk Ticketcomments and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Ticketcomments and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Zendesk Ticketcomments Property
     - YouTrack Usergroups Property
     - YouTrack Data Type


Zendesk Tickets to YouTrack Hubprojects
---------------------------------------
Every Zendesk Tickets will be synchronized with a YouTrack Hubprojects.

Once a link between a Zendesk Tickets and a YouTrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a YouTrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     - YouTrack Hubprojects Property
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


Zendesk Tickets to YouTrack Usergroups
--------------------------------------
Every Zendesk Tickets will be synchronized with a YouTrack Usergroups.

Once a link between a Zendesk Tickets and a YouTrack Usergroups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a YouTrack Usergroups:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     - YouTrack Usergroups Property
     - YouTrack Data Type
   * - due_at
     - name
     - "string"
   * - subject
     - users.id
     - "string"


Zendesk Users to YouTrack Users
-------------------------------
Every Zendesk Users will be synchronized with a YouTrack Users.

Once a link between a Zendesk Users and a YouTrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a YouTrack Users:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - YouTrack Users Property
     - YouTrack Data Type
   * - email
     - profile.email
     - "string"

