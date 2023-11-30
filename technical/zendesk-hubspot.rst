====================
Zendesk to  Dataflow
====================

Generated: 2023-11-30 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to  Contact
-------------------------
Every Zendesk Users will be synchronized with a  Contact.

If a matching  Contact already exists, the Zendesk Users will be merged with the existing one.
If no matching  Contact is found, a new  Contact will be created.

A Zendesk Users will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Contact Property
   * - email
     - properties.email

Once a link between a Zendesk Users and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a  Contact:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Contact Property
     -  Data Type
   * - email
     - properties.email
     - "string"
   * - role
     - properties.country
     - "string"


Zendesk Organizations to  Company
---------------------------------
Every Zendesk Organizations will be synchronized with a  Company.

Once a link between a Zendesk Organizations and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a  Company:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     -  Company Property
     -  Data Type
   * - name
     - properties.name
     - "string"
   * - url
     - properties.website
     - "string"


Zendesk Tickets to  Ticket
--------------------------
Every Zendesk Tickets will be synchronized with a  Ticket.

Once a link between a Zendesk Tickets and a  Ticket is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a  Ticket:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     -  Ticket Property
     -  Data Type
   * - requester_id
     - properties.hubspot_owner_id
     - "string"
   * - subject
     - properties.subject
     - "string"

