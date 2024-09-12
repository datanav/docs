=============================
Trello to Tidsbanken Dataflow
=============================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Members to Tidsbanken Ansatt
-----------------------------------
Every Trello Members will be synchronized with a Tidsbanken Ansatt.

Once a link between a Trello Members and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Members and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Trello Members Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - fullName
     - Navn
     - "string"

