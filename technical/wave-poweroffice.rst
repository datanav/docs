======================================
Wave Financial to PowerOffice Dataflow
======================================

Generated: 2023-06-23 10:01:04

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to PowerOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to PowerOffice Customer
-------------------------------------
Every Wave Customer will be synchronized with a PowerOffice Customer.

Once a link between a Wave Customer and a PowerOffice Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice Customer Property
     - PowerOffice Data Type
   * - address.addressLine1
     - streetAddresses.address1
     - "string"
   * - address.addressLine2
     - streetAddresses.address2
     - "string"
   * - address.city
     - streetAddresses.city
     - "string"
   * - address.country.code
     - streetAddresses.countryCode
     - "string"
   * - address.postalCode
     - streetAddresses.zipCode
     - "string"
   * - id
     - id
     - "string"
   * - modifiedAt
     - LastChanged
     - "string"
   * - name
     - LegalName
     - "string"
   * - phone
     - PhoneNumber
     - "string"
   * - website
     - WebsiteUrl
     - "string"


Wave Vendor to PowerOffice Customer
-----------------------------------
Every Wave Vendor will be synchronized with a PowerOffice Customer.

Once a link between a Wave Vendor and a PowerOffice Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a PowerOffice Customer:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - PowerOffice Customer Property
     - PowerOffice Data Type
   * - address.addressLine1
     - streetAddresses.address1
     - "string"
   * - address.addressLine2
     - streetAddresses.address2
     - "string"
   * - address.city
     - streetAddresses.city
     - "string"
   * - address.country.code
     - streetAddresses.countryCode
     - "string"
   * - address.postalCode
     - streetAddresses.zipCode
     - "string"
   * - id
     - id
     - "string"
   * - modifiedAt
     - LastChanged
     - "string"
   * - name
     - LegalName
     - "string"
   * - phone
     - PhoneNumber
     - "string"
   * - website
     - WebsiteUrl
     - "string"

