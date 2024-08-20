============================
HubSpot to Youtrack Dataflow
============================

Generated: 2024-08-20 00:13:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Youtrack Users
---------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Youtrack Users must be established.

A HubSpot Contact will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Youtrack Users Property
   * - properties.email
     - profile.email.email

Once a link between a HubSpot Contact and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - properties.email
     - profile.email
     - "string"
   * - properties.email
     - profile.email.email
     - "string"
   * - properties.work_email
     - profile.email.email
     - "string"


HubSpot Ticket to Youtrack Issues
---------------------------------
Every HubSpot Ticket will be synchronized with a Youtrack Issues.

Once a link between a HubSpot Ticket and a Youtrack Issues is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a Youtrack Issues:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     - Youtrack Issues Property
     - Youtrack Data Type
   * - properties.hubspot_owner_id
     - reporter.id
     - "string"


HubSpot User to Youtrack Users
------------------------------
Every HubSpot User will be synchronized with a Youtrack Users.

Once a link between a HubSpot User and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - email
     - profile.email.email
     - "string"

