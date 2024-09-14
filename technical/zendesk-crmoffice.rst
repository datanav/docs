=============================
Zendesk to CRMOffice Dataflow
=============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Ticketcomments to CRMOffice Activities
----------------------------------------------
Every Zendesk Ticketcomments will be synchronized with a CRMOffice Activities.

Once a link between a Zendesk Ticketcomments and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Ticketcomments and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - Zendesk Ticketcomments Property
     - CRMOffice Activities Property
     - CRMOffice Data Type


Zendesk Tickets to CRMOffice Activities
---------------------------------------
Every Zendesk Tickets will be synchronized with a CRMOffice Activities.

Once a link between a Zendesk Tickets and a CRMOffice Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a CRMOffice Activities:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     - CRMOffice Activities Property
     - CRMOffice Data Type
   * - requester_id
     - ownerId
     - "string"
   * - subject
     - subject
     - "string"


Zendesk Users to CRMOffice Contacts
-----------------------------------
Every Zendesk Users will be synchronized with a CRMOffice Contacts.

Once a link between a Zendesk Users and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - organization_id
     - company.id
     - "string"

