===========================
Shopify to Tilores Dataflow
===========================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Tilores Human
---------------------------------
Every Shopify Customer will be synchronized with a Tilores Human.

Once a link between a Shopify Customer and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Tilores Human Property
     - Tilores Data Type
   * - addresses.city
     - city
     - "string"
   * - addresses.zip
     - postalCode
     - "string"
   * - default_address.city
     - city
     - "string"
   * - default_address.zip
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

