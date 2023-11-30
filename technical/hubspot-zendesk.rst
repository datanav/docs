====================
HubSpot to  Dataflow
====================

Generated: 2023-11-30 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to  Users
-------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a  Users must be established.

A HubSpot Contact will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Users Property
   * - properties.email
     - email

Once a link between a HubSpot Contact and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Users:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Users Property
     -  Data Type
   * - properties.email
     - email
     - "string"


HubSpot Company to  Organizations
---------------------------------
Every HubSpot Company will be synchronized with a  Organizations.

Once a link between a HubSpot Company and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Organizations:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Organizations Property
     -  Data Type
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


HubSpot Ticket to  Tickets
--------------------------
Every HubSpot Ticket will be synchronized with a  Tickets.

Once a link between a HubSpot Ticket and a  Tickets is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a  Tickets:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     -  Tickets Property
     -  Data Type
   * - properties.hubspot_owner_id
     - requester_id
     - "string"
   * - properties.subject
     - subject
     - "string"

