==========================
Trello to Zendesk Dataflow
==========================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Trello to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Trello Organizations to Zendesk Organizations
---------------------------------------------
Every Trello Organizations will be synchronized with a Zendesk Organizations.

Once a link between a Trello Organizations and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Trello Organizations and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - Trello Organizations Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - name
     - name
     - "string"

