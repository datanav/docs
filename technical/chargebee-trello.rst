============================
Chargebee to Trello Dataflow
============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to Trello Members
------------------------------------
Every Chargebee Customer will be synchronized with a Trello Members.

Once a link between a Chargebee Customer and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Trello Members Property
     - Trello Data Type
   * - email
     - email
     - "string"


Chargebee Business_entity to Trello Organizations
-------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Trello Organizations.

Once a link between a Chargebee Business_entity and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Trello Organizations Property
     - Trello Data Type
   * - name
     - name
     - "string"

