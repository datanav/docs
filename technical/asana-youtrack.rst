==========================
Asana to YouTrack Dataflow
==========================

Generated: 2023-11-08 13:18:36

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to YouTrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Projects to YouTrack Organizationroles
--------------------------------------------
Every Asana Projects will be synchronized with a YouTrack Organizationroles.

Once a link between a Asana Projects and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type
   * - due_on
     - id
     - "string"
   * - members.gid
     - role.immutable
     - "string"


Asana Tasks to YouTrack Organizationroles
-----------------------------------------
Every Asana Tasks will be synchronized with a YouTrack Organizationroles.

Once a link between a Asana Tasks and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Tasks and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Asana Tasks Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type
   * - due_on
     - id
     - "string"

