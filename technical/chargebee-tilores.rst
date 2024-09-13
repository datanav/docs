=============================
Chargebee to Tilores Dataflow
=============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to Tilores Human
-----------------------------------
Every Chargebee Customer will be synchronized with a Tilores Human.

Once a link between a Chargebee Customer and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Tilores Human Property
     - Tilores Data Type
   * - billing_address.city
     - city
     - "string"
   * - billing_address.zip
     - postalCode
     - "string"
   * - email
     - email
     - "string"
   * - first_name
     - firstName
     - "string"
   * - id
     - id
     - "string"
   * - last_name
     - lastName
     - "string"

