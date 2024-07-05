========================
YouTrack to Wix Dataflow
========================

Generated: 2024-07-05 00:00:00

Introduction
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
   * - profile.email.email
     - primaryInfo.email

Once a link between a YouTrack Users and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Wix Contacts Property
     - Wix Data Type
   * - name
     - info.name.first
     - "string"
   * - name
     - info.name.last
     - "string"
   * - profile.email
     - primaryInfo.email
     - "string"
   * - profile.email.email
     - primaryInfo.email
     - "string"

