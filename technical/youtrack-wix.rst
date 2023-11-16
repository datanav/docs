========================
YouTrack to Wix Dataflow
========================

Generated: 2023-11-16 13:18:48

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to Wix Contacts
------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a Wix Contacts must be established.

A YouTrack Users will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Wix Contacts Property
   * - 
     - primaryInfo.email
   * - profile.email
     - primaryInfo.email

Once a link between a YouTrack Users and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Wix Contacts Property
     - Wix Data Type
   * - profile.email
     - primaryInfo.email
     - "string"


YouTrack Users to Wix Members
-----------------------------
Before any synchronization can take place, a link between a YouTrack Users and a Wix Members must be established.

A YouTrack Users will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Wix Members Property
   * - 
     - loginEmail
   * - profile.email
     - loginEmail

Once a link between a YouTrack Users and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Wix Members:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Wix Members Property
     - Wix Data Type
   * - profile.email
     - loginEmail
     - "string"

