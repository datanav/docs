=============================
Tripletex to Tilores Dataflow
=============================

Generated: 2024-03-26 14:24:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to  Human
---------------------------
Every Tripletex Contact will be synchronized with a  Human.

Once a link between a Tripletex Contact and a  Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Human:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Human Property
     -  Data Type
   * - email
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - phoneNumberMobileCountry.id
     - phoneNumber
     - "string"


Tripletex Employee to  Human
----------------------------
Every Tripletex Employee will be synchronized with a  Human.

Once a link between a Tripletex Employee and a  Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Human:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Human Property
     -  Data Type
   * - address.city
     - city
     - "string"
   * - address.postalCode
     - postalCode
     - "string"
   * - dateOfBirth
     - dateOfBirth
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

