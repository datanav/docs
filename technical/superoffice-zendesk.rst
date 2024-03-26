========================
SuperOffice to  Dataflow
========================

Generated: 2024-03-26 00:00:02

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to  Users
----------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a  Users must be established.

A new  Users will be created from a SuperOffice Person if it is connected to a SuperOffice Ticket that is synchronized into .

A SuperOffice Person will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Users Property
   * - Emails.Value
     - email

Once a link between a SuperOffice Person and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Users Property
     -  Data Type
   * - Contact.ContactId
     - organization_id
     - "string"
   * - Emails.Value
     - email
     - "string"
   * - PrivatePhones.Value
     - phone
     - "string"


SuperOffice Contact to  Organizations
-------------------------------------
Every SuperOffice Contact will be synchronized with a  Organizations.

Once a link between a SuperOffice Contact and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Organizations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Organizations Property
     -  Data Type
   * - Name
     - name
     - "string"


SuperOffice Ticket to  Tickets
------------------------------
Every SuperOffice Ticket will be synchronized with a  Tickets.

Once a link between a SuperOffice Ticket and a  Tickets is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ticket and a  Tickets:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ticket Property
     -  Tickets Property
     -  Data Type
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


SuperOffice User to  Users
--------------------------
Every SuperOffice User will be synchronized with a  Users.

If a matching  Users already exists, the SuperOffice User will be merged with the existing one.
If no matching  Users is found, a new  Users will be created.

A SuperOffice User will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Users Property
   * - personEmail
     - email

Once a link between a SuperOffice User and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a  Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Users Property
     -  Data Type
   * - contactId
     - organization_id
     - "string"
   * - personEmail
     - email
     - "string"

