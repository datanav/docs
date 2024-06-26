==================================
Wave Financial to Tilores Dataflow
==================================

Generated: 2024-06-26 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to Tilores Human
-------------------------------------
Every Wave Customer person will be synchronized with a Tilores Human.

Once a link between a Wave Customer person and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Tilores Human Property
     - Tilores Data Type
   * - address.city
     - city
     - "string"
   * - address.postalCode
     - postalCode
     - "string"
   * - email
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - lastName
     - "string"
   * - shippingDetails.address.city
     - city
     - "string"
   * - shippingDetails.address.postalCode
     - postalCode
     - "string"

