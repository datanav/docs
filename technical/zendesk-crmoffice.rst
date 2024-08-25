====================
Zendesk to  Dataflow
====================

Generated: 2024-08-25 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Ticketcomments to  Activities
-------------------------------------
Every Zendesk Ticketcomments will be synchronized with a  Activities.

Once a link between a Zendesk Ticketcomments and a  Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Ticketcomments and a  Activities:

.. list-table::
   :header-rows: 1

   * - Zendesk Ticketcomments Property
     -  Activities Property
     -  Data Type


Zendesk Tickets to  Activities
------------------------------
Every Zendesk Tickets will be synchronized with a  Activities.

Once a link between a Zendesk Tickets and a  Activities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a  Activities:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     -  Activities Property
     -  Data Type
   * - requester_id
     - ownerId
     - "string"
   * - subject
     - subject
     - "string"


Zendesk Users to  Contacts
--------------------------
Every Zendesk Users will be synchronized with a  Contacts.

Once a link between a Zendesk Users and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Contacts Property
     -  Data Type
   * - organization_id
     - company.id
     - "string"

