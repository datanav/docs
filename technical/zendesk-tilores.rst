===========================
Zendesk to Tilores Dataflow
===========================

Generated: 2024-06-30 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Users to Tilores Human
------------------------------
Every Zendesk Users will be synchronized with a Tilores Human.

Once a link between a Zendesk Users and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - Tilores Human Property
     - Tilores Data Type
   * - email
     - email
     - "string"

