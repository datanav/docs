===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-04-28 00:00:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to  Customer
---------------------------------
Every Wave Customer person will be synchronized with a  Customer.

Once a link between a Wave Customer person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Customer Property
     -  Data Type
   * - address.addressLine1
     - addresses.address1
     - "string"
   * - address.addressLine2
     - addresses.address2
     - "string"
   * - address.city
     - addresses.city
     - "string"
   * - address.country.code
     - addresses.country
     - "string"
   * - address.postalCode
     - addresses.zip
     - "string"
   * - address.province.code
     - addresses.province_code
     - "string"
   * - email
     - email
     - "string"
   * - phone
     - phone
     - "string"
   * - shippingDetails.address.addressLine1
     - addresses.address1
     - "string"
   * - shippingDetails.address.addressLine2
     - addresses.address2
     - "string"
   * - shippingDetails.address.city
     - addresses.city
     - "string"
   * - shippingDetails.address.country.code
     - addresses.country
     - "string"
   * - shippingDetails.address.postalCode
     - addresses.zip
     - "string"
   * - shippingDetails.address.province.code
     - addresses.province_code
     - "string"
   * - shippingDetails.phone
     - phone
     - "string"

