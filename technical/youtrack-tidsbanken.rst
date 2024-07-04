===============================
YouTrack to Tidsbanken Dataflow
===============================

Generated: 2024-07-04 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from YouTrack to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

YouTrack Users to Tidsbanken Ansatt
-----------------------------------
Before any synchronization can take place, a link between a YouTrack Users and a Tidsbanken Ansatt must be established.

A YouTrack Users will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Tidsbanken Ansatt Property
   * - profile.email.email
     - Epost

Once a link between a YouTrack Users and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a YouTrack Users and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - YouTrack Users Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - name
     - Etternavn
     - "string"
   * - name
     - Fornavn
     - "string"
   * - name
     - Navn
     - "string"
   * - profile.email.email
     - Epost
     - "string"

