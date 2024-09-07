=============================
Zendesk to Crmoffice Dataflow
=============================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Ticketcomments to Crmoffice Activities
----------------------------------------------
Every Zendesk Ticketcomments will be synchronized with a Crmoffice Activities.

Once a link between a Zendesk Ticketcomments and a Crmoffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Ticketcomments and a Crmoffice Activities:

.. list-table::
   :header-rows: 1

   * - Zendesk Ticketcomments Property
     - Crmoffice Activities Property
     - Crmoffice Data Type


Zendesk Tickets to Crmoffice Activities
---------------------------------------
Every Zendesk Tickets will be synchronized with a Crmoffice Activities.

Once a link between a Zendesk Tickets and a Crmoffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a Crmoffice Activities:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     - Crmoffice Activities Property
     - Crmoffice Data Type
   * - requester_id
     - ownerId
     - "string"
   * - subject
     - subject
     - "string"


Zendesk Users to Crmoffice Contacts
-----------------------------------
Every Zendesk Users will be synchronized with a Crmoffice Contacts.

Once a link between a Zendesk Users and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - organization_id
     - company.id
     - "string"

