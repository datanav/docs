============================
Zendesk to Youtrack Dataflow
============================

Generated: 2024-07-02 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to Youtrack Groups
----------------------------------------
Every Zendesk Organizations will be synchronized with a Youtrack Groups.

Once a link between a Zendesk Organizations and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - Youtrack Groups Property
     - Youtrack Data Type
   * - name
     - name
     - "string"


Zendesk Ticketcomments to Youtrack Hubprojects
----------------------------------------------
Every Zendesk Ticketcomments will be synchronized with a Youtrack Hubprojects.

Once a link between a Zendesk Ticketcomments and a Youtrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Ticketcomments and a Youtrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - Zendesk Ticketcomments Property
     - Youtrack Hubprojects Property
     - Youtrack Data Type


Zendesk Tickets to Youtrack Hubprojects
---------------------------------------
Every Zendesk Tickets will be synchronized with a Youtrack Hubprojects.

Once a link between a Zendesk Tickets and a Youtrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a Youtrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     - Youtrack Hubprojects Property
     - Youtrack Data Type


Zendesk Tickets to Youtrack Issues
----------------------------------
Every Zendesk Tickets will be synchronized with a Youtrack Issues.

Once a link between a Zendesk Tickets and a Youtrack Issues is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Tickets and a Youtrack Issues:

.. list-table::
   :header-rows: 1

   * - Zendesk Tickets Property
     - Youtrack Issues Property
     - Youtrack Data Type
   * - requester_id
     - reporter.id
     - "string"


Zendesk Users to Youtrack Users
-------------------------------
When a Zendesk User is of type Agent, it  will be synchronized with a Youtrack Users.

If a matching Youtrack Users already exists, the Zendesk Users will be merged with the existing one.
If no matching Youtrack Users is found, a new Youtrack Users will be created.

A Zendesk Users will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Youtrack Users Property
   * - email
     - profile.email.email

Once a link between a Zendesk Users and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - email
     - profile.email
     - "string"
   * - email
     - profile.email.email
     - "string"
   * - name
     - name
     - "string"

