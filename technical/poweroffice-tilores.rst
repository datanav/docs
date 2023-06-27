===============================
Poweroffice to Tilores Dataflow
===============================

Generated: 2023-06-27 11:29:58

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Poweroffice to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Poweroffice Contactperson to Tilores Human
------------------------------------------
Every Poweroffice Contactperson will be synchronized with a Tilores Human.

Once a link between a Poweroffice Contactperson and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Contactperson and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Poweroffice Contactperson Property
     - Tilores Human Property
     - Tilores Data Type
   * - address1
     - street
     - "string"
   * - address2
     - street
     - "string"
   * - city
     - city
     - "string"
   * - dateOfBirth
     - dateOfBirth
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
   * - zipCode
     - postalCode
     - "string"

