========================
Asana to Trello Dataflow
========================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to Trello Actions
--------------------------------
Every Asana Projects will be synchronized with a Trello Actions.

Once a link between a Asana Projects and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - Trello Actions Property
     - Trello Data Type
   * - owner.gid
     - memberCreator.id
     - "string"


Asana Tasks to Trello Actions
-----------------------------
Every Asana Tasks will be synchronized with a Trello Actions.

Once a link between a Asana Tasks and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     - Trello Actions Property
     - Trello Data Type


Asana Teams to Trello Organizations
-----------------------------------
Every Asana Teams will be synchronized with a Trello Organizations.

Once a link between a Asana Teams and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - Trello Organizations Property
     - Trello Data Type
   * - description
     - desc
     - "string"
   * - name
     - name
     - "string"
   * - permalink_url
     - website
     - "string"


Asana Tasks to Trello Cards
---------------------------
Every Asana Tasks will be synchronized with a Trello Cards.

Once a link between a Asana Tasks and a Trello Cards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a Trello Cards:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     - Trello Cards Property
     - Trello Data Type
   * - completed_at
     - dueComplete
     - "string"
   * - due_on
     - due
     - "string"
   * - name
     - closed
     - "string"
   * - name
     - desc
     - "string"
   * - name
     - descData
     - "string"
   * - name
     - idMemberCreator
     - "string"
   * - name
     - idOrganization
     - "string"
   * - name
     - invited
     - "string"
   * - name
     - limits
     - "string"
   * - name
     - memberships
     - "string"
   * - name
     - name
     - "string"
   * - start_at
     - start
     - "string"


Asana Users to Trello Members
-----------------------------
Every Asana Users will be synchronized with a Trello Members.

Once a link between a Asana Users and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - Trello Members Property
     - Trello Data Type
   * - email
     - email
     - "string"
   * - name
     - fullName
     - "string"


Asana Workspaces to Trello Organizations
----------------------------------------
Every Asana Workspaces will be synchronized with a Trello Organizations.

Once a link between a Asana Workspaces and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - Trello Organizations Property
     - Trello Data Type
   * - email_domains
     - website
     - "string"
   * - name
     - name
     - "string"

