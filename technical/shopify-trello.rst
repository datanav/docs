==========================
Shopify to Trello Dataflow
==========================

Generated: 2024-09-29 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Trello Members
----------------------------------
Every Shopify Customer will be synchronized with a Trello Members.

Once a link between a Shopify Customer and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Trello Members Property
     - Trello Data Type
   * - email
     - email
     - "string"

