=====================
Wave to Wave Dataflow
=====================

Generated: 2024-09-24 13:16:04

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Wave Customer
------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Wave Customer must be established.

A Wave Customer will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wave Customer Property
   * - email
     - email

Once a link between a Wave Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wave Customer Property
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


Wave Customer to Wave Customer
------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Wave Customer must be established.

A new Wave Customer will be created from a Wave Customer if it is connected to a Wave Vendor, Invoice, Business, Customer, or Customer-person that is synchronized into Wave.

A Wave Customer will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wave Customer Property
   * - email
     - email

Once a link between a Wave Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wave Customer Property
     - Wave Data Type


Wave Vendor to Wave Customer
----------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Wave Customer must be established.

A new Wave Customer will be created from a Wave Vendor if it is connected to a Wave Vendor, Invoice, Business, Customer, or Customer-person that is synchronized into Wave.

A Wave Vendor will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Wave Customer Property
   * - email
     - email

Once a link between a Wave Vendor and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
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


Wave Customer (organisation data) to Wave Customer
--------------------------------------------------
Every Wave Customer (organisation data) will be synchronized with a Wave Customer.

Once a link between a Wave Customer (organisation data) and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer (organisation data) and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer (organisation data) Property
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
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - mobile
     - mobile
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


Wave Customer to Wave Customer (human data)
-------------------------------------------
Every Wave Customer will be synchronized with a Wave Customer (human data).

Once a link between a Wave Customer and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wave Customer (human data) Property
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

