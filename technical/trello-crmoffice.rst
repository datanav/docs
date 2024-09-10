============================
Trello to Crmoffice Dataflow
============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Boards to Crmoffice Activities
-------------------------------------
Every Trello Boards will be synchronized with a Crmoffice Activities.

Once a link between a Trello Boards and a Crmoffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Boards and a Crmoffice Activities:

.. list-table::
   :header-rows: 1

   * - Trello Boards Property
     - Crmoffice Activities Property
     - Crmoffice Data Type
   * - name
     - subject
     - "string"


Trello Cards to Crmoffice Activities
------------------------------------
Every Trello Cards will be synchronized with a Crmoffice Activities.

Once a link between a Trello Cards and a Crmoffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Cards and a Crmoffice Activities:

.. list-table::
   :header-rows: 1

   * - Trello Cards Property
     - Crmoffice Activities Property
     - Crmoffice Data Type
   * - name
     - subject
     - "string"


Trello Lists to Crmoffice Activities
------------------------------------
Every Trello Lists will be synchronized with a Crmoffice Activities.

Once a link between a Trello Lists and a Crmoffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Lists and a Crmoffice Activities:

.. list-table::
   :header-rows: 1

   * - Trello Lists Property
     - Crmoffice Activities Property
     - Crmoffice Data Type
   * - name
     - subject
     - "string"


Trello Members to Crmoffice Contacts
------------------------------------
Every Trello Members will be synchronized with a Crmoffice Contacts.

Once a link between a Trello Members and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Members and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Trello Members Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type


Trello Actions to Crmoffice Activities
--------------------------------------
Every Trello Actions will be synchronized with a Crmoffice Activities.

Once a link between a Trello Actions and a Crmoffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Actions and a Crmoffice Activities:

.. list-table::
   :header-rows: 1

   * - Trello Actions Property
     - Crmoffice Activities Property
     - Crmoffice Data Type
   * - date
     - startsAt
     - "string"
   * - memberCreator.id
     - ownerId
     - "string"

