===========================
Zendesk to Zendesk Dataflow
===========================

Generated: 2023-10-05 06:14:44

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Tickets to Zendesk Ticketcomments
-----------------------------------------
Every Zendesk Tickets will be synchronized with a Zendesk Ticketcomments.

Once a link between a Zendesk Tickets and a Zendesk Ticketcomments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a Zendesk Ticketcomments:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     - Zendesk Ticketcomments Property
     - Zendesk Data Type

