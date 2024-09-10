======================
Tripletex to  Dataflow
======================

Generated: 2024-09-10 13:23:48

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to  Customer
-------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a  Customer.

Once a link between a Tripletex Customer and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Customer Property
     -  Data Type
   * - deliveryAddress.addressLine1
     - StreetAddress1
     - "string"
   * - deliveryAddress.addressLine2
     - StreetAddress2
     - "string"
   * - deliveryAddress.city
     - City
     - "string"
   * - deliveryAddress.postalCode
     - ZipCode
     - "string"
   * - name
     - Name
     - "string"
   * - phoneNumberMobile
     - Phone
     - "string"
   * - physicalAddress.addressLine1
     - StreetAddress1
     - "string"
   * - physicalAddress.addressLine2
     - StreetAddress2
     - "string"
   * - physicalAddress.city
     - City
     - "string"
   * - physicalAddress.postalCode
     - ZipCode
     - "string"
   * - postalAddress.addressLine1
     - StreetAddress1
     - "string"
   * - postalAddress.addressLine2
     - StreetAddress2
     - "string"
   * - postalAddress.city
     - City
     - "string"
   * - postalAddress.postalCode
     - ZipCode
     - "string"
   * - website
     - Website
     - "string"

