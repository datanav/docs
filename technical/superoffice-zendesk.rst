===============================
SuperOffice to Zendesk Dataflow
===============================

Generated: 2024-06-26 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to Zendesk Users
-----------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Zendesk Users must be established.

A new Zendesk Users will be created from a SuperOffice Person if it is connected to a SuperOffice Ticket that is synchronized into Zendesk.

A SuperOffice Person will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Zendesk Users Property
   * - Emails.Value
     - email

Once a link between a SuperOffice Person and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - Contact.ContactId
     - organization_id
     - "string"
   * - Emails.Value
     - email
     - "string"
   * - PrivatePhones.Value
     - phone
     - "string"


SuperOffice Contact to Zendesk Organizations
--------------------------------------------
Every SuperOffice Contact will be synchronized with a Zendesk Organizations.

Once a link between a SuperOffice Contact and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - Name
     - name
     - "string"


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


SuperOffice User to Zendesk Users
---------------------------------
Every SuperOffice User will be synchronized with a Zendesk Users.

If a matching Zendesk Users already exists, the SuperOffice User will be merged with the existing one.
If no matching Zendesk Users is found, a new Zendesk Users will be created.

A SuperOffice User will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Zendesk Users Property
   * - personEmail
     - email

Once a link between a SuperOffice User and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - contactId
     - organization_id
     - "string"
   * - personEmail
     - email
     - "string"

