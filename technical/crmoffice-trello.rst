============================
Crmoffice to Trello Dataflow
============================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Crmoffice to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Crmoffice Contacts to Trello Members
------------------------------------
Every Crmoffice Contacts will be synchronized with a Trello Members.

Once a link between a Crmoffice Contacts and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Contacts and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Crmoffice Contacts Property
     - Trello Members Property
     - Trello Data Type


Crmoffice Activities to Trello Actions
--------------------------------------
Every Crmoffice Activities will be synchronized with a Trello Actions.

Once a link between a Crmoffice Activities and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Activities and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - Crmoffice Activities Property
     - Trello Actions Property
     - Trello Data Type
   * - ownerId
     - memberCreator.id
     - "string"
   * - startsAt
     - date
     - "string"

