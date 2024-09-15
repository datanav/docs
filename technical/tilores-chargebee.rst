=============================
Tilores to Chargebee Dataflow
=============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tilores to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tilores Human to Chargebee Customer
-----------------------------------
Every Tilores Human will be synchronized with a Chargebee Customer.

Once a link between a Tilores Human and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tilores Human and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Tilores Human Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - email
     - email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"

