=========================
YouTrack to Wave Dataflow
=========================

Generated: 2024-06-28 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to Wave Customer person
--------------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a Wave Customer person must be established.

A YouTrack Users will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Wave Customer person Property
   * - profile.email.email
     - email

Once a link between a YouTrack Users and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Wave Customer person Property
     - Wave Data Type
   * - name
     - name
     - N/A

