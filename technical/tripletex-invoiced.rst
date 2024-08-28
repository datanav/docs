======================
Tripletex to  Dataflow
======================

Generated: 2024-08-28 07:51:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to  Customers company
----------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a  Customers company.

Once a link between a Tripletex Customer and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Customers company Property
     -  Data Type
   * - deliveryAddress.addressLine1
     - address1
     - "string"
   * - deliveryAddress.addressLine2
     - address2
     - "string"
   * - deliveryAddress.city
     - city
     - "string"
   * - deliveryAddress.country.id
     - country
     - "string"
   * - deliveryAddress.postalCode
     - postal_code
     - "string"
   * - id
     - id
     - "string"
   * - physicalAddress.addressLine1
     - address1
     - "string"
   * - physicalAddress.addressLine2
     - address2
     - "string"
   * - physicalAddress.city
     - city
     - "string"
   * - physicalAddress.country.id
     - country
     - "string"
   * - physicalAddress.postalCode
     - postal_code
     - "string"
   * - postalAddress.addressLine1
     - address1
     - "string"
   * - postalAddress.addressLine2
     - address2
     - "string"
   * - postalAddress.city
     - city
     - "string"
   * - postalAddress.country.id
     - country
     - "string"
   * - postalAddress.postalCode
     - postal_code
     - "string"


Tripletex Customer person to  Customers person
----------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a  Customers person.

Once a link between a Tripletex Customer person and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     -  Customers person Property
     -  Data Type
   * - deliveryAddress.addressLine1
     - address1
     - "string"
   * - deliveryAddress.addressLine2
     - address2
     - "string"
   * - deliveryAddress.city
     - city
     - "string"
   * - deliveryAddress.country.id
     - country
     - "string"
   * - deliveryAddress.postalCode
     - postal_code
     - "string"
   * - physicalAddress.addressLine1
     - address1
     - "string"
   * - physicalAddress.addressLine2
     - address2
     - "string"
   * - physicalAddress.city
     - city
     - "string"
   * - physicalAddress.country.id
     - country
     - "string"
   * - physicalAddress.postalCode
     - postal_code
     - "string"
   * - postalAddress.addressLine1
     - address1
     - "string"
   * - postalAddress.addressLine2
     - address2
     - "string"
   * - postalAddress.city
     - city
     - "string"
   * - postalAddress.country.id
     - country
     - "string"
   * - postalAddress.postalCode
     - postal_code
     - "string"

