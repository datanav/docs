==================
Asana to  Dataflow
==================

Generated: 2024-09-05 11:02:22

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to  Boards
-------------------------
Every Asana Projects will be synchronized with a  Boards.

Once a link between a Asana Projects and a  Boards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a  Boards:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     -  Boards Property
     -  Data Type
   * - name
     - name
     - "string"


Asana Tasks to  Boards
----------------------
Every Asana Tasks will be synchronized with a  Boards.

Once a link between a Asana Tasks and a  Boards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a  Boards:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     -  Boards Property
     -  Data Type
   * - name
     - name
     - "string"


Asana Teams to  Organizations
-----------------------------
Every Asana Teams will be synchronized with a  Organizations.

Once a link between a Asana Teams and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     -  Organizations Property
     -  Data Type
   * - description
     - desc
     - "string"
   * - name
     - name
     - "string"
   * - permalink_url
     - website
     - "string"


Asana Tasks to  Cards
---------------------
Every Asana Tasks will be synchronized with a  Cards.

Once a link between a Asana Tasks and a  Cards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a  Cards:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     -  Cards Property
     -  Data Type
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


Asana Users to  Actions
-----------------------
Every Asana Users will be synchronized with a  Actions.

Once a link between a Asana Users and a  Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a  Actions:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     -  Actions Property
     -  Data Type


Asana Users to  Members
-----------------------
Every Asana Users will be synchronized with a  Members.

Once a link between a Asana Users and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a  Members:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     -  Members Property
     -  Data Type
   * - email
     - email
     - "string"
   * - name
     - fullName
     - "string"


Asana Workspaces to  Organizations
----------------------------------
Every Asana Workspaces will be synchronized with a  Organizations.

Once a link between a Asana Workspaces and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     -  Organizations Property
     -  Data Type
   * - email_domains
     - website
     - "string"
   * - name
     - name
     - "string"

