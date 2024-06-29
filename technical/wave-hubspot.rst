==================================
Wave Financial to Hubspot Dataflow
==================================

Generated: 2024-06-29 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Hubspot Contact
--------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Hubspot Contact must be established.

A Wave Customer will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Hubspot Contact Property
   * - email
     - properties.email

Once a link between a Wave Customer and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - address.addressLine1
     - properties.address
     - "string"
   * - address.city
     - properties.city
     - "string"
   * - address.country.code
     - properties.country
     - "string"
   * - address.countryCode
     - properties.country
     - "string"
   * - address.postalCode
     - properties.zip
     - "string"
   * - address.province.code
     - properties.state
     - "string"
   * - address.province.name
     - properties.country
     - "string"
   * - address.province.name
     - properties.state
     - "string"
   * - email
     - properties.email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - properties.lastname
     - "string"
   * - mobile
     - properties.mobilephone
     - "string"
   * - phone
     - properties.phone
     - "string"
   * - shippingDetails.address.addressLine1
     - properties.address
     - "string"
   * - shippingDetails.address.city
     - properties.city
     - "string"
   * - shippingDetails.address.country.code
     - properties.country
     - "string"
   * - shippingDetails.address.postalCode
     - properties.zip
     - "string"
   * - shippingDetails.address.province.code
     - properties.state
     - "string"
   * - shippingDetails.address.province.name
     - properties.country
     - "string"
   * - shippingDetails.address.province.name
     - properties.state
     - "string"


Wave Customer person to Hubspot Contact
---------------------------------------
Every Wave Customer person will be synchronized with a Hubspot Contact.

If a matching Hubspot Contact already exists, the Wave Customer person will be merged with the existing one.
If no matching Hubspot Contact is found, a new Hubspot Contact will be created.

A Wave Customer person will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Hubspot Contact Property
   * - email
     - properties.email

Once a link between a Wave Customer person and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - address.addressLine1
     - properties.address
     - "string"
   * - address.city
     - properties.city
     - "string"
   * - address.country.code
     - properties.country
     - "string"
   * - address.countryCode
     - properties.country
     - "string"
   * - address.postalCode
     - properties.zip
     - "string"
   * - address.province.code
     - properties.state
     - "string"
   * - address.province.name
     - properties.country
     - "string"
   * - address.province.name
     - properties.state
     - "string"
   * - email
     - properties.email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - properties.lastname
     - "string"
   * - mobile
     - properties.mobilephone
     - "string"
   * - phone
     - properties.phone
     - "string"
   * - shippingDetails.address.addressLine1
     - properties.address
     - "string"
   * - shippingDetails.address.city
     - properties.city
     - "string"
   * - shippingDetails.address.country.code
     - properties.country
     - "string"
   * - shippingDetails.address.postalCode
     - properties.zip
     - "string"
   * - shippingDetails.address.province.code
     - properties.state
     - "string"
   * - shippingDetails.address.province.name
     - properties.country
     - "string"
   * - shippingDetails.address.province.name
     - properties.state
     - "string"
   * - shippingDetails.phone
     - properties.phone
     - "string"


Wave Vendor to Hubspot Contact
------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Hubspot Contact must be established.

A Wave Vendor will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Hubspot Contact Property
   * - email
     - properties.email

Once a link between a Wave Vendor and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - address.addressLine1
     - properties.address
     - "string"
   * - address.city
     - properties.city
     - "string"
   * - address.country.code
     - properties.country
     - "string"
   * - address.postalCode
     - properties.zip
     - "string"
   * - address.province.code
     - properties.state
     - "string"
   * - address.province.name
     - properties.country
     - "string"
   * - address.province.name
     - properties.state
     - "string"
   * - email
     - properties.email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - properties.lastname
     - "string"
   * - mobile
     - properties.mobilephone
     - "string"
   * - phone
     - properties.phone
     - "string"


Wave Customer to Hubspot Company
--------------------------------
Every Wave Customer will be synchronized with a Hubspot Company.

Once a link between a Wave Customer and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - address.addressLine1
     - properties.address
     - "string"
   * - address.addressLine2
     - properties.address2
     - "string"
   * - address.city
     - properties.city
     - "string"
   * - address.country.code
     - properties.country
     - "string"
   * - address.countryCode
     - properties.country
     - "string"
   * - address.postalCode
     - properties.zip
     - "string"
   * - address.province
     - properties.state
     - "string"
   * - address.province.code
     - properties.state
     - "string"
   * - address.province.name
     - properties.state
     - "string"
   * - id
     - id
     - "string"
   * - id
     - properties.description
     - "string"
   * - internalNotes
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - phone
     - properties.phone
     - "string"
   * - shippingDetails.address.addressLine1
     - properties.address
     - "string"
   * - shippingDetails.address.addressLine2
     - properties.address2
     - "string"
   * - shippingDetails.address.city
     - properties.city
     - "string"
   * - shippingDetails.address.country.code
     - properties.country
     - "string"
   * - shippingDetails.address.postalCode
     - properties.zip
     - "string"
   * - shippingDetails.address.province
     - properties.state
     - "string"
   * - shippingDetails.address.province.code
     - properties.state
     - "string"
   * - shippingDetails.address.province.name
     - properties.state
     - "string"
   * - shippingDetails.phone
     - properties.phone
     - "string"
   * - website
     - properties.website
     - "string"


Wave Invoice to Hubspot Lineitem
--------------------------------
Every Wave Invoice will be synchronized with a Hubspot Lineitem.

Once a link between a Wave Invoice and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Hubspot Lineitem Property
     - Hubspot Data Type
   * - items.description
     - properties.description
     - "string"
   * - items.description
     - properties.name
     - "string"
   * - items.price
     - properties.price
     - "string"
   * - items.product.id
     - properties.hs_product_id
     - "string"
   * - items.quantity
     - properties.quantity
     - N/A
   * - items.unitPrice
     - properties.price
     - "string"


Wave Product to Hubspot Product
-------------------------------
Every Wave Product will be synchronized with a Hubspot Product.

Once a link between a Wave Product and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Hubspot Product Property
     - Hubspot Data Type
   * - description
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - unitPrice
     - properties.price
     - "string"


Wave User to Hubspot User
-------------------------
Every Wave User will be synchronized with a Hubspot User.

Once a link between a Wave User and a Hubspot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave User and a Hubspot User:

.. list-table::
   :header-rows: 1

   * - Wave User Property
     - Hubspot User Property
     - Hubspot Data Type

