=====================
YouTrack to  Dataflow
=====================

Generated: 2023-11-29 23:37:14

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to  Users
------------------------
Before any synchronization can take place, a link between a YouTrack Users and a  Users must be established.

A YouTrack Users will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Users Property
   * - profile.email.email
     - email

Once a link between a YouTrack Users and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a  Users:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Users Property
     -  Data Type
   * - profile.email
     - email
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
   * - name
     - name
     - "string"


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
   * - name
     - name
     - "string"


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
   * - name
     - name
     - "string"


YouTrack Issues to  Tickets
---------------------------
Every YouTrack Issues will be synchronized with a  Tickets.

Once a link between a YouTrack Issues and a  Tickets is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Issues and a  Tickets:

.. list-table::
   :header-rows: 1

   * - YouTrack Issues Property
     -  Tickets Property
     -  Data Type
   * - reporter.id
     - requester_id
     - "string"

