=======================
Wave to Trello Dataflow
=======================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to Trello Members
--------------------------------------
Every Wave Customer person will be synchronized with a Trello Members.

Once a link between a Wave Customer person and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Trello Members Property
     - Trello Data Type
   * - email
     - email
     - "string"
   * - name
     - fullName
     - "string"


Wave Customer to Trello Organizations
-------------------------------------
Every Wave Customer will be synchronized with a Trello Organizations.

Once a link between a Wave Customer and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Trello Organizations Property
     - Trello Data Type
   * - internalNotes
     - desc
     - "string"
   * - name
     - name
     - "string"
   * - website
     - website
     - "string"

