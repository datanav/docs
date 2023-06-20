===============================
SuperOffice to Zendesk Dataflow
===============================

Generated: 2023-06-20 08:37:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Ticket to Zendesk Tickets
-------------------------------------
Every SuperOffice Ticket will be synchronized with a Zendesk Tickets.

Once a link between a SuperOffice Ticket and a Zendesk Tickets is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ticket and a Zendesk Tickets:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ticket Property
     - Zendesk Tickets Property
     - Zendesk Data Type
   * - OwnedBy.AssociateId
     - requester_id
     - "string"
   * - Person.PersonId
     - assignee_id
     - "string"
   * - TimeToReply
     - due_at
     - "string"
   * - Title
     - subject
     - "string"

