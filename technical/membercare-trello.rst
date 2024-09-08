=============================
Membercare to Trello Dataflow
=============================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Organizations to Trello Organizations
------------------------------------------------
Every Membercare Organizations will be synchronized with a Trello Organizations.

Once a link between a Membercare Organizations and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Organizations and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Membercare Organizations Property
     - Trello Organizations Property
     - Trello Data Type
   * - name
     - name
     - "string"


Membercare Persons to Trello Members
------------------------------------
Every Membercare Persons will be synchronized with a Trello Members.

Once a link between a Membercare Persons and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Persons and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Membercare Persons Property
     - Trello Members Property
     - Trello Data Type
   * - name
     - fullName
     - "string"


Membercare Companies to Trello Organizations
--------------------------------------------
Every Membercare Companies will be synchronized with a Trello Organizations.

Once a link between a Membercare Companies and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Trello Organizations Property
     - Trello Data Type
   * - companyName
     - name
     - "string"
   * - url
     - website
     - "string"

