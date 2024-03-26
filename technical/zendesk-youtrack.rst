============================
Zendesk to Youtrack Dataflow
============================

Generated: 2024-03-26 14:14:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to  Groups
--------------------------------
Every Zendesk Organizations will be synchronized with a  Groups.

Once a link between a Zendesk Organizations and a  Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a  Groups:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     -  Groups Property
     -  Data Type
   * - name
     - name
     - "string"


Zendesk Ticketcomments to  Hubprojects
--------------------------------------
Every Zendesk Ticketcomments will be synchronized with a  Hubprojects.

Once a link between a Zendesk Ticketcomments and a  Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Ticketcomments and a  Hubprojects:

.. list-table::
   :header-rows: 1

   * - Zendesk Ticketcomments Property
     -  Hubprojects Property
     -  Data Type


Zendesk Tickets to  Hubprojects
-------------------------------
Every Zendesk Tickets will be synchronized with a  Hubprojects.

Once a link between a Zendesk Tickets and a  Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a  Hubprojects:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     -  Hubprojects Property
     -  Data Type


Zendesk Tickets to  Issues
--------------------------
Every Zendesk Tickets will be synchronized with a  Issues.

Once a link between a Zendesk Tickets and a  Issues is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a  Issues:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     -  Issues Property
     -  Data Type
   * - requester_id
     - reporter.id
     - "string"


Zendesk Users to  Users
-----------------------
When a Zendesk User is of type Agent, it  will be synchronized with a  Users.

If a matching  Users already exists, the Zendesk Users will be merged with the existing one.
If no matching  Users is found, a new  Users will be created.

A Zendesk Users will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Users Property
   * - email
     - profile.email.email

Once a link between a Zendesk Users and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a  Users:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Users Property
     -  Data Type
   * - email
     - profile.email
     - "string"
   * - email
     - profile.email.email
     - "string"
   * - name
     - name
     - "string"

