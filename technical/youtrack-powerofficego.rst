===================================
YouTrack to PowerOffice GO Dataflow
===================================

Generated: 2024-09-11 07:52:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to PowerOffice Contactperson
-------------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a PowerOffice Contactperson must be established.

A YouTrack Users will merge with a PowerOffice Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOffice Contactperson Property
   * - profile.email.email
     - emailAddress

Once a link between a YouTrack Users and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
   * - profile.email
     - emailAddress
     - "string"
   * - profile.email.email
     - emailAddress
     - "string"


YouTrack Users to PowerOffice Customers person
----------------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a PowerOffice Customers person must be established.

A YouTrack Users will merge with a PowerOffice Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOffice Customers person Property
   * - profile.email.email
     - EmailAddress

Once a link between a YouTrack Users and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type

