============================
YouTrack to Tilores Dataflow
============================

Generated: 2024-09-13 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to Tilores Human
-------------------------------
Every YouTrack Users will be synchronized with a Tilores Human.

Once a link between a YouTrack Users and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Tilores Human Property
     - Tilores Data Type
   * - profile.email
     - email
     - "string"
   * - profile.email.email
     - email
     - "string"

