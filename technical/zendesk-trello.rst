==========================
Zendesk to Trello Dataflow
==========================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to Trello Organizations
---------------------------------------------
Every Zendesk Organizations will be synchronized with a Trello Organizations.

Once a link between a Zendesk Organizations and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Trello Organizations Property
     - Trello Data Type
   * - name
     - name
     - "string"


Zendesk Ticketcomments to Trello Actions
----------------------------------------
Every Zendesk Ticketcomments will be synchronized with a Trello Actions.

Once a link between a Zendesk Ticketcomments and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Ticketcomments and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - Zendesk Ticketcomments Property
     - Trello Actions Property
     - Trello Data Type


Zendesk Tickets to Trello Actions
---------------------------------
Every Zendesk Tickets will be synchronized with a Trello Actions.

Once a link between a Zendesk Tickets and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     - Trello Actions Property
     - Trello Data Type
   * - requester_id
     - memberCreator.id
     - "string"


Zendesk Users to Trello Members
-------------------------------
Every Zendesk Users will be synchronized with a Trello Members.

Once a link between a Zendesk Users and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Trello Members Property
     - Trello Data Type
   * - email
     - email
     - "string"
   * - name
     - fullName
     - "string"

