====================
Zendesk to  Dataflow
====================

Generated: 2024-09-05 12:06:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to  Organizations
---------------------------------------
Every Zendesk Organizations will be synchronized with a  Organizations.

Once a link between a Zendesk Organizations and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     -  Organizations Property
     -  Data Type
   * - name
     - name
     - "string"


Zendesk Ticketcomments to  Actions
----------------------------------
Every Zendesk Ticketcomments will be synchronized with a  Actions.

Once a link between a Zendesk Ticketcomments and a  Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Ticketcomments and a  Actions:

.. list-table::
   :header-rows: 1

   * - Zendesk Ticketcomments Property
     -  Actions Property
     -  Data Type


Zendesk Ticketcomments to  Boards
---------------------------------
Every Zendesk Ticketcomments will be synchronized with a  Boards.

Once a link between a Zendesk Ticketcomments and a  Boards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Ticketcomments and a  Boards:

.. list-table::
   :header-rows: 1

   * - Zendesk Ticketcomments Property
     -  Boards Property
     -  Data Type


Zendesk Tickets to  Actions
---------------------------
Every Zendesk Tickets will be synchronized with a  Actions.

Once a link between a Zendesk Tickets and a  Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a  Actions:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     -  Actions Property
     -  Data Type


Zendesk Tickets to  Boards
--------------------------
Every Zendesk Tickets will be synchronized with a  Boards.

Once a link between a Zendesk Tickets and a  Boards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a  Boards:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     -  Boards Property
     -  Data Type
   * - subject
     - name
     - "string"


Zendesk Users to  Members
-------------------------
Every Zendesk Users will be synchronized with a  Members.

Once a link between a Zendesk Users and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a  Members:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Members Property
     -  Data Type
   * - email
     - email
     - "string"
   * - name
     - fullName
     - "string"

