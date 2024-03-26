=====================
YouTrack to  Dataflow
=====================

Generated: 2024-03-26 13:42:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to  Human
------------------------
Every YouTrack Users will be synchronized with a  Human.

Once a link between a YouTrack Users and a  Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a  Human:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     -  Human Property
     -  Data Type
   * - profile.email
     - email
     - "string"
   * - profile.email.email
     - email
     - "string"

