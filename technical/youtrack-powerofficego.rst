==================================
YouTrack to Powerofficego Dataflow
==================================

Generated: 2024-06-30 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to Powerofficego Contactperson
---------------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a Powerofficego Contactperson must be established.

A YouTrack Users will merge with a Powerofficego Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Powerofficego Contactperson Property
   * - profile.email.email
     - emailAddress

Once a link between a YouTrack Users and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
   * - profile.email
     - emailAddress
     - "string"
   * - profile.email.email
     - emailAddress
     - "string"


YouTrack Users to Powerofficego Customers person
------------------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a Powerofficego Customers person must be established.

A YouTrack Users will merge with a Powerofficego Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Powerofficego Customers person Property
   * - profile.email.email
     - EmailAddress

Once a link between a YouTrack Users and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type

