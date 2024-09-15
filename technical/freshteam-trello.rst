============================
Freshteam to Trello Dataflow
============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to Trello Organizations
--------------------------------------------
Every Freshteam Department will be synchronized with a Trello Organizations.

Once a link between a Freshteam Department and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Trello Organizations Property
     - Trello Data Type
   * - name
     - name
     - "string"


Freshteam Employee to Trello Members
------------------------------------
Every Freshteam Employee will be synchronized with a Trello Members.

Once a link between a Freshteam Employee and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Trello Members Property
     - Trello Data Type
   * - personal_email
     - email
     - "string"

