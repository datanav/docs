=================================
Wave Financial to Trello Dataflow
=================================

Generated: 2024-09-05 12:09:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to  Members
--------------------------------
Every Wave Customer person will be synchronized with a  Members.

Once a link between a Wave Customer person and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Members:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Members Property
     -  Data Type
   * - email
     - email
     - "string"
   * - name
     - fullName
     - "string"


Wave Customer to  Organizations
-------------------------------
Every Wave Customer will be synchronized with a  Organizations.

Once a link between a Wave Customer and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Organizations Property
     -  Data Type
   * - internalNotes
     - desc
     - "string"
   * - name
     - name
     - "string"
   * - website
     - website
     - "string"

