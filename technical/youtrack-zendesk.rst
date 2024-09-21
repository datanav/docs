============================
YouTrack to Zendesk Dataflow
============================

Generated: 2024-09-21 00:01:13

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to Zendesk Users
-------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a Zendesk Users must be established.

A YouTrack Users will merge with a Zendesk Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Zendesk Users Property
   * - profile.email.email
     - email

Once a link between a YouTrack Users and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Zendesk Users Property
     - Zendesk Data Type
   * - name
     - name
     - "string"
   * - profile.email.email
     - email
     - "string"


YouTrack Groups to Zendesk Organizations
----------------------------------------
Every YouTrack Groups will be synchronized with a Zendesk Organizations.

Once a link between a YouTrack Groups and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Groups and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - YouTrack Groups Property
     - Zendesk Organizations Property
     - Zendesk Data Type


YouTrack Organizations to Zendesk Organizations
-----------------------------------------------
Every YouTrack Organizations will be synchronized with a Zendesk Organizations.

Once a link between a YouTrack Organizations and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Organizations and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - YouTrack Organizations Property
     - Zendesk Organizations Property
     - Zendesk Data Type


YouTrack Usergroups to Zendesk Organizations
--------------------------------------------
Every YouTrack Usergroups will be synchronized with a Zendesk Organizations.

Once a link between a YouTrack Usergroups and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Usergroups and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - YouTrack Usergroups Property
     - Zendesk Organizations Property
     - Zendesk Data Type


YouTrack Issues to Zendesk Tickets
----------------------------------
Every YouTrack Issues will be synchronized with a Zendesk Tickets.

Once a link between a YouTrack Issues and a Zendesk Tickets is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Issues and a Zendesk Tickets:

.. list-table::
   :header-rows: 1

   * - YouTrack Issues Property
     - Zendesk Tickets Property
     - Zendesk Data Type
   * - reporter.id
     - requester_id
     - "string"


YouTrack Users to Zendesk Users
-------------------------------
Every YouTrack Users will be synchronized with a Zendesk Users.

Once a link between a YouTrack Users and a Zendesk Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Zendesk Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Zendesk Users Property
     - Zendesk Data Type

