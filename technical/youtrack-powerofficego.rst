===================================
YouTrack to PowerOffice GO Dataflow
===================================

Generated: 2024-09-12 00:00:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to PowerOffice GO Contactperson
----------------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a PowerOffice GO Contactperson must be established.

A YouTrack Users will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOffice GO Contactperson Property
   * - profile.email.email
     - emailAddress

Once a link between a YouTrack Users and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - profile.email
     - emailAddress
     - "string"
   * - profile.email.email
     - emailAddress
     - "string"


YouTrack Users to PowerOffice GO Customers person
-------------------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a PowerOffice GO Customers person must be established.

A YouTrack Users will merge with a PowerOffice GO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOffice GO Customers person Property
   * - profile.email.email
     - EmailAddress

Once a link between a YouTrack Users and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type

