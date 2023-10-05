=====================================
Businesscentral to Tripletex Dataflow
=====================================

Generated: 2023-10-05 10:41:25

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Company to Tripletex Customer
---------------------------------------------
Every Businesscentral Company will be synchronized with a Tripletex Customer.

Once a link between a Businesscentral Company and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Company and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Company Property
     - Tripletex Customer Property
     - Tripletex Data Type


Businesscentral Contact company to Tripletex Customer
-----------------------------------------------------
Every Businesscentral Contact company will be synchronized with a Tripletex Customer.

Once a link between a Businesscentral Contact company and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contact company and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contact company Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - addressLine1
     - postalAddress.addressLine1
     - "string"
   * - addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - addressLine2
     - postalAddress.addressLine2
     - "string"
   * - city
     - deliveryAddress.city
     - "string"
   * - city
     - physicalAddress.city
     - "string"
   * - city
     - postalAddress.city
     - "string"
   * - country
     - deliveryAddress.country.id
     - "string"
   * - country
     - physicalAddress.country.id
     - "integer"
   * - country
     - postalAddress.country.id
     - "integer"
   * - id
     - id
     - "integer"
   * - postalCode
     - deliveryAddress.postalCode
     - "string"
   * - postalCode
     - physicalAddress.postalCode
     - "string"
   * - postalCode
     - postalAddress.postalCode
     - "string"

