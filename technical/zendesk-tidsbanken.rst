==============================
Zendesk to Tidsbanken Dataflow
==============================

Generated: 2024-07-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to Tidsbanken Ansatt
----------------------------------
Before any synchronization can take place, a link between a Zendesk Users and a Tidsbanken Ansatt must be established.

A Zendesk Users will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Tidsbanken Ansatt Property
   * - email
     - Epost

Once a link between a Zendesk Users and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - name
     - Navn
     - "string"
   * - phone
     - TlfPrivat
     - "string"

