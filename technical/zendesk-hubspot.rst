===========================
Zendesk to HubSpot Dataflow
===========================

Generated: 2023-06-20 09:00:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organisations to HubSpot Company
----------------------------------------
Every Zendesk Organisations will be synchronized with a HubSpot Company.

Once a link between a Zendesk Organisations and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organisations and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Zendesk Organisations Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - name
     - properties.name
     - "string"
   * - url
     - properties.website
     - "string"


Zendesk Tickets to HubSpot Ticket
---------------------------------
Every Zendesk Tickets will be synchronized with a HubSpot Ticket.

Once a link between a Zendesk Tickets and a HubSpot Ticket is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a HubSpot Ticket:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     - HubSpot Ticket Property
     - HubSpot Data Type
   * - requester_id
     - properties.hubspot_owner_id
     - "string"
   * - subject
     - properties.subject
     - "string"

