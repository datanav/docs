=============================
Freshteam to Tilores Dataflow
=============================

Generated: 2024-06-26 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Tilores Human
-----------------------------------
Every Freshteam Employee will be synchronized with a Tilores Human.

Once a link between a Freshteam Employee and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Tilores Human Property
     - Tilores Data Type
   * - address.city
     - city
     - "string"
   * - address.street
     - street
     - "string"
   * - address.zip_code
     - postalCode
     - "string"
   * - communication_address.communication_city
     - city
     - "string"
   * - communication_address.communication_street
     - street
     - "string"
   * - communication_address.communication_zip_code
     - postalCode
     - "string"
   * - date_of_birth
     - dateOfBirth
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
   * - personal_email
     - email
     - "string"

