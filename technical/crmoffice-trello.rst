============================
CRMOffice to Trello Dataflow
============================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Contacts to Trello Members
------------------------------------
Every CRMOffice Contacts will be synchronized with a Trello Members.

Once a link between a CRMOffice Contacts and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a Trello Members:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
     - Trello Members Property
     - Trello Data Type


CRMOffice Activities to Trello Actions
--------------------------------------
Every CRMOffice Activities will be synchronized with a Trello Actions.

Once a link between a CRMOffice Activities and a Trello Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Activities and a Trello Actions:

.. list-table::
   :header-rows: 1

   * - CRMOffice Activities Property
     - Trello Actions Property
     - Trello Data Type
   * - ownerId
     - memberCreator.id
     - "string"
   * - startsAt
     - date
     - "string"

