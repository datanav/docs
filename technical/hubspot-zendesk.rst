===========================
HubSpot to Zendesk Dataflow
===========================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Zendesk Users
--------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Zendesk Users must be established.

A HubSpot Contact will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Zendesk Users Property
   * - properties.email
     - email

Once a link between a HubSpot Contact and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - properties.email
     - email
     - "string"


HubSpot Company to Zendesk Organizations
----------------------------------------
Every HubSpot Company will be synchronized with a Zendesk Organizations.

Once a link between a HubSpot Company and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - properties.country
     - tags
     - "string"
   * - properties.industry
     - tags
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.type
     - tags
     - "string"
   * - properties.website
     - url
     - "string"


HubSpot Ticket to Zendesk Tickets
---------------------------------
Every HubSpot Ticket will be synchronized with a Zendesk Tickets.

Once a link between a HubSpot Ticket and a Zendesk Tickets is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a Zendesk Tickets:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     - Zendesk Tickets Property
     - Zendesk Data Type
   * - properties.hubspot_owner_id
     - requester_id
     - "string"
   * - properties.subject
     - subject
     - "string"


HubSpot User to Zendesk Users
-----------------------------
Every HubSpot User will be synchronized with a Zendesk Users.

Once a link between a HubSpot User and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Zendesk Users Property
     - Zendesk Data Type

