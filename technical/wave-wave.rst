=====================
Wave to Wave Dataflow
=====================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to Wave Customer person
--------------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a Wave Customer person must be established.

A Wave Customer person will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Wave Customer person Property
   * - email
     - email

Once a link between a Wave Customer person and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Wave Customer person Property
     - Wave Data Type
   * - address.addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - address.addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - address.city
     - shippingDetails.address.city
     - "string"
   * - address.country.code
     - shippingDetails.address.country.code
     - "string"
   * - address.postalCode
     - shippingDetails.address.postalCode
     - "string"
   * - address.province.code
     - shippingDetails.address.province.code
     - "string"
   * - shippingDetails.address.addressLine1
     - address.addressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - address.addressLine2
     - "string"
   * - shippingDetails.address.city
     - address.city
     - "string"
   * - shippingDetails.address.country.code
     - address.country.code
     - "string"
   * - shippingDetails.address.postalCode
     - address.postalCode
     - "string"
   * - shippingDetails.address.province.code
     - address.province.code
     - "string"
   * - shippingDetails.phone
     - phone
     - "string"


Wave Customer to Wave Customer person
-------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Wave Customer person must be established.

A new Wave Customer person will be created from a Wave Customer if it is connected to a Wave Vendor, Invoice, Business, or Customer that is synchronized into Wave.

A Wave Customer will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wave Customer person Property
   * - email
     - email

Once a link between a Wave Customer and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wave Customer person Property
     - Wave Data Type
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.city
     - shippingDetails.address.city
     - "string"
   * - address.country.code
     - address.country.code
     - "string"
   * - address.country.code
     - address.countryCode
     - "string"
   * - address.country.code
     - shippingDetails.address.country.code
     - "string"
   * - address.countryCode
     - address.country.code
     - "string"
   * - address.countryCode
     - address.countryCode
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - shippingDetails.address.postalCode
     - "string"
   * - address.province.code
     - address.province.code
     - "string"
   * - address.province.code
     - shippingDetails.address.province.code
     - "string"
   * - shippingDetails.address.addressLine1
     - address.addressLine1
     - "string"
   * - shippingDetails.address.addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - address.addressLine2
     - "string"
   * - shippingDetails.address.addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - shippingDetails.address.city
     - address.city
     - "string"
   * - shippingDetails.address.city
     - shippingDetails.address.city
     - "string"
   * - shippingDetails.address.country.code
     - address.country.code
     - "string"
   * - shippingDetails.address.country.code
     - address.countryCode
     - "string"
   * - shippingDetails.address.country.code
     - shippingDetails.address.country.code
     - "string"
   * - shippingDetails.address.postalCode
     - address.postalCode
     - "string"
   * - shippingDetails.address.postalCode
     - shippingDetails.address.postalCode
     - "string"
   * - shippingDetails.address.province.code
     - address.province.code
     - "string"
   * - shippingDetails.address.province.code
     - shippingDetails.address.province.code
     - "string"


Wave Vendor to Wave Customer person
-----------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Wave Customer person must be established.

A new Wave Customer person will be created from a Wave Vendor if it is connected to a Wave Vendor, Invoice, Business, or Customer that is synchronized into Wave.

A Wave Vendor will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Wave Customer person Property
   * - email
     - email

Once a link between a Wave Vendor and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Wave Customer person Property
     - Wave Data Type
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.city
     - shippingDetails.address.city
     - "string"
   * - address.country.code
     - address.country.code
     - "string"
   * - address.country.code
     - shippingDetails.address.country.code
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - shippingDetails.address.postalCode
     - "string"
   * - address.province.code
     - address.province.code
     - "string"
   * - address.province.code
     - shippingDetails.address.province.code
     - "string"


Wave Financial Vendor to Wave Customer
--------------------------------------
Before any synchronization can take place, a link between a Wave Financial Vendor and a Wave Customer must be established.

A new Wave Customer will be created from a Wave Financial Vendor if it is connected to a Wave Financial Wave-vendor, Wave-invoice, Wave-business, or Wave-customer that is synchronized into Wave.

Once a link between a Wave Financial Vendor and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Financial Vendor and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Wave Financial Vendor Property
     - Wave Customer Property
     - Wave Data Type
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.city
     - shippingDetails.address.city
     - "string"
   * - address.country.code
     - address.country.code
     - "string"
   * - address.country.code
     - shippingDetails.address.country.code
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - shippingDetails.address.postalCode
     - "string"
   * - address.province.code
     - address.province.code
     - "string"
   * - address.province.code
     - shippingDetails.address.province.code
     - "string"
   * - email
     - email
     - "string"
   * - fax
     - fax
     - "string"
   * - firstName
     - firstName
     - "string"
   * - internalNotes
     - id
     - "string"
   * - internalNotes
     - internalNotes
     - "string"
   * - lastName
     - lastName
     - "string"
   * - mobile
     - mobile
     - "string"
   * - name
     - name
     - N/A
   * - tollFree
     - tollFree
     - "string"
   * - website
     - website
     - "string"

