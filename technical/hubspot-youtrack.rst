====================
HubSpot to  Dataflow
====================

Generated: 2023-11-30 00:10:08

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
     - profile.email.email

Once a link between a HubSpot Contact and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Users:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Users Property
     -  Data Type
   * - properties.email
     - profile.email
     - "string"
   * - properties.email
     - profile.email.email
     - "string"
   * - properties.work_email
     - profile.email.email
     - "string"


HubSpot Ticket to  Issues
-------------------------
Every HubSpot Ticket will be synchronized with a  Issues.

Once a link between a HubSpot Ticket and a  Issues is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a  Issues:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     -  Issues Property
     -  Data Type
   * - properties.hubspot_owner_id
     - reporter.id
     - "string"


HubSpot User to  Users
----------------------
Every HubSpot User will be synchronized with a  Users.

Once a link between a HubSpot User and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a  Users:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     -  Users Property
     -  Data Type
   * - email
     - profile.email.email
     - "string"

