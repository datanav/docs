=========================
YouTrack to Wave Dataflow
=========================

Generated: 2024-10-01 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to Wave Customer
-------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a Wave Customer must be established.

A YouTrack Users will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Wave Customer Property
   * - profile.email.email
     - email

Once a link between a YouTrack Users and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Wave Customer Property
     - Wave Data Type
   * - name
     - name
     - N/A

