=============================
MemberCare to Trello Dataflow
=============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Organizations to Trello Organizations
------------------------------------------------
Every MemberCare Organizations will be synchronized with a Trello Organizations.

Once a link between a MemberCare Organizations and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - Trello Organizations Property
     - Trello Data Type
   * - name
     - name
     - "string"


MemberCare Persons to Trello Members
------------------------------------
Every MemberCare Persons will be synchronized with a Trello Members.

Once a link between a MemberCare Persons and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Persons and a Trello Members:

.. list-table::
   :header-rows: 1

   * - MemberCare Persons Property
     - Trello Members Property
     - Trello Data Type
   * - name
     - fullName
     - "string"


MemberCare Companies to Trello Organizations
--------------------------------------------
Every MemberCare Companies will be synchronized with a Trello Organizations.

Once a link between a MemberCare Companies and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - Trello Organizations Property
     - Trello Data Type
   * - companyName
     - name
     - "string"
   * - url
     - website
     - "string"

