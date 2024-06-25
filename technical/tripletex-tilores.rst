=============================
Tripletex to Tilores Dataflow
=============================

Generated: 2024-06-25 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Tilores Human
----------------------------------
Every Tripletex Contact will be synchronized with a Tilores Human.

Once a link between a Tripletex Contact and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Tilores Human Property
     - Tilores Data Type
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


Tripletex Customer person to Tilores Human
------------------------------------------
Every Tripletex Customer person will be synchronized with a Tilores Human.

Once a link between a Tripletex Customer person and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Tilores Human Property
     - Tilores Data Type
   * - deliveryAddress.city
     - city
     - "string"
   * - deliveryAddress.postalCode
     - postalCode
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - physicalAddress.city
     - city
     - "string"
   * - physicalAddress.postalCode
     - postalCode
     - "string"
   * - postalAddress.city
     - city
     - "string"
   * - postalAddress.postalCode
     - postalCode
     - "string"


Tripletex Employee to Tilores Human
-----------------------------------
Every Tripletex Employee will be synchronized with a Tilores Human.

Once a link between a Tripletex Employee and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Tilores Human Property
     - Tilores Data Type
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

