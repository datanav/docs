==================================
YouTrack to PowerOfficeGO Dataflow
==================================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to PowerOfficeGO Contactperson
---------------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a PowerOfficeGO Contactperson must be established.

A YouTrack Users will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOfficeGO Contactperson Property
   * - profile.email.email
     - emailAddress

Once a link between a YouTrack Users and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
   * - profile.email
     - emailAddress
     - "string"
   * - profile.email.email
     - emailAddress
     - "string"


YouTrack Users to PowerOfficeGO Customers person
------------------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a PowerOfficeGO Customers person must be established.

A YouTrack Users will merge with a PowerOfficeGO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOfficeGO Customers person Property
   * - profile.email.email
     - EmailAddress

Once a link between a YouTrack Users and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type

