=========================
Trello to Trello Dataflow
=========================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Boards to Trello Actions
-------------------------------
Every Trello Boards will be synchronized with a Trello Actions.

Once a link between a Trello Boards and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Boards and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - Trello Boards Property
     - Trello Actions Property
     - Trello Data Type


Trello Cards to Trello Actions
------------------------------
Every Trello Cards will be synchronized with a Trello Actions.

Once a link between a Trello Cards and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Cards and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - Trello Cards Property
     - Trello Actions Property
     - Trello Data Type
   * - idBoard
     - data.board.id
     - "string"


Trello Lists to Trello Actions
------------------------------
Every Trello Lists will be synchronized with a Trello Actions.

Once a link between a Trello Lists and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Lists and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - Trello Lists Property
     - Trello Actions Property
     - Trello Data Type
   * - idBoard
     - data.board.id
     - "string"

