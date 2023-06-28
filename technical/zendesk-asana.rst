=========================
Zendesk to Asana Dataflow
=========================

Generated: 2023-06-28 17:49:32

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Asana. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organisations to Asana Workspaces
-----------------------------------------
Before any synchronization can take place, a link between a Zendesk Organisations and a Asana Workspaces must be established.

A new Asana Workspaces will be created from a Zendesk Organisations if it is connected to a Zendesk Tickets that is synchronized into Asana.

Once a link between a Zendesk Organisations and a Asana Workspaces is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organisations and a Asana Workspaces:

.. list-table::
   :header-rows: 1

   * - Zendesk Organisations Property
     - Asana Workspaces Property
     - Asana Data Type


Zendesk Organisations to Asana Teams
------------------------------------
Every Zendesk Organisations will be synchronized with a Asana Teams.

Once a link between a Zendesk Organisations and a Asana Teams is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organisations and a Asana Teams:

.. list-table::
   :header-rows: 1

   * - Zendesk Organisations Property
     - Asana Teams Property
     - Asana Data Type
   * - name
     - member_invite_management_access_level
     - "string"


Zendesk Tickets to Asana Projects
---------------------------------
Every Zendesk Tickets will be synchronized with a Asana Projects.

Once a link between a Zendesk Tickets and a Asana Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a Asana Projects:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     - Asana Projects Property
     - Asana Data Type
   * - created_at
     - created_at
     - "string"
   * - due_at
     - due_date
     - "string"
   * - organization_id
     - workspace.gid
     - "string"
   * - requester_id
     - owner.gid
     - "string"


Zendesk Users to Asana Users
----------------------------
Every Zendesk Users will be synchronized with a Asana Users.

Once a link between a Zendesk Users and a Asana Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Asana Users:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Asana Users Property
     - Asana Data Type

