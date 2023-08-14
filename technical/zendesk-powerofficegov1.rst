===================================
Zendesk to PowerOfficeGov1 Dataflow
===================================

Generated: 2023-08-14 08:49:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to PowerOfficeGov1. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to PowerOfficeGov1 Person
---------------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a PowerOfficeGov1 Person must be established.

A Zendesk Users will merge with a PowerOfficeGov1 Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOfficeGov1 Person Property
   * - email
     - Emails.Value

Once a link between a Zendesk Users and a PowerOfficeGov1 Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a PowerOfficeGov1 Person:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOfficeGov1 Person Property
     - PowerOfficeGov1 Data Type


Zendesk Organisations to PowerOfficeGov1 Organisations
------------------------------------------------------
Considering changing this to be a Customer instead, it  will be synchronized with a PowerOfficeGov1 Organisations.

Once a link between a Zendesk Organisations and a PowerOfficeGov1 Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organisations and a PowerOfficeGov1 Organisations:

.. list-table::
   :header-rows: 1

   * - Zendesk Organisations Property
     - PowerOfficeGov1 Organisations Property
     - PowerOfficeGov1 Data Type


Zendesk Ticketcomments to PowerOfficeGov1 Ticketcomments
--------------------------------------------------------
Every Zendesk Ticketcomments will be synchronized with a PowerOfficeGov1 Ticketcomments.

Once a link between a Zendesk Ticketcomments and a PowerOfficeGov1 Ticketcomments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Ticketcomments and a PowerOfficeGov1 Ticketcomments:

.. list-table::
   :header-rows: 1

   * - Zendesk Ticketcomments Property
     - PowerOfficeGov1 Ticketcomments Property
     - PowerOfficeGov1 Data Type


Zendesk Tickets to PowerOfficeGov1 Tickets
------------------------------------------
Every Zendesk Tickets will be synchronized with a PowerOfficeGov1 Tickets.

Once a link between a Zendesk Tickets and a PowerOfficeGov1 Tickets is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a PowerOfficeGov1 Tickets:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     - PowerOfficeGov1 Tickets Property
     - PowerOfficeGov1 Data Type


Zendesk Users to PowerOfficeGov1 Employee
-----------------------------------------
Every Zendesk Users will be synchronized with a PowerOfficeGov1 Employee.

If a matching PowerOfficeGov1 Employee already exists, the Zendesk Users will be merged with the existing one.
If no matching PowerOfficeGov1 Employee is found, a new PowerOfficeGov1 Employee will be created.

A Zendesk Users will merge with a PowerOfficeGov1 Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOfficeGov1 Employee Property
   * - email
     - email

Once a link between a Zendesk Users and a PowerOfficeGov1 Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a PowerOfficeGov1 Employee:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - PowerOfficeGov1 Employee Property
     - PowerOfficeGov1 Data Type

