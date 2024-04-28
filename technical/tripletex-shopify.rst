======================
Tripletex to  Dataflow
======================

Generated: 2024-04-28 00:00:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer person to  Customer
--------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a  Customer.

Once a link between a Tripletex Customer person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     -  Customer Property
     -  Data Type
   * - deliveryAddress.addressLine1
     - addresses.address1
     - "string"
   * - deliveryAddress.addressLine2
     - addresses.address2
     - "string"
   * - deliveryAddress.city
     - addresses.city
     - "string"
   * - deliveryAddress.country.id
     - addresses.country
     - "string"
   * - deliveryAddress.postalCode
     - addresses.zip
     - "string"
   * - email
     - email
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - physicalAddress.addressLine1
     - addresses.address1
     - "string"
   * - physicalAddress.addressLine2
     - addresses.address2
     - "string"
   * - physicalAddress.city
     - addresses.city
     - "string"
   * - physicalAddress.country.id
     - addresses.country
     - "string"
   * - physicalAddress.postalCode
     - addresses.zip
     - "string"
   * - postalAddress.addressLine1
     - addresses.address1
     - "string"
   * - postalAddress.addressLine2
     - addresses.address2
     - "string"
   * - postalAddress.city
     - addresses.city
     - "string"
   * - postalAddress.country.id
     - addresses.country
     - "string"
   * - postalAddress.postalCode
     - addresses.zip
     - "string"

