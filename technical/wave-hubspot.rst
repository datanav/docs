========================
Wave to HubSpot Dataflow
========================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to HubSpot Contact
--------------------------------
Before any synchronization can take place, a link between a Wave Customer and a HubSpot Contact must be established.

A Wave Customer will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - HubSpot Contact Property
   * - email
     - properties.email

Once a link between a Wave Customer and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - HubSpot Contact Property
     - HubSpot Data Type
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


Wave Customer person to HubSpot Contact
---------------------------------------
Every Wave Customer person will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the Wave Customer person will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A Wave Customer person will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - HubSpot Contact Property
   * - email
     - properties.email

Once a link between a Wave Customer person and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - HubSpot Contact Property
     - HubSpot Data Type
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


Wave Vendor to HubSpot Contact
------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a HubSpot Contact must be established.

A Wave Vendor will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - HubSpot Contact Property
   * - email
     - properties.email

Once a link between a Wave Vendor and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - HubSpot Contact Property
     - HubSpot Data Type
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


Wave Customer to HubSpot Company
--------------------------------
Every Wave Customer will be synchronized with a HubSpot Company.

Once a link between a Wave Customer and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - HubSpot Company Property
     - HubSpot Data Type
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


Wave Invoice to HubSpot Lineitem
--------------------------------
Every Wave Invoice will be synchronized with a HubSpot Lineitem.

Once a link between a Wave Invoice and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - HubSpot Lineitem Property
     - HubSpot Data Type
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


Wave Product to HubSpot Product
-------------------------------
Every Wave Product will be synchronized with a HubSpot Product.

Once a link between a Wave Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - description
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - unitPrice
     - properties.price
     - "string"


Wave User to HubSpot User
-------------------------
Every Wave User will be synchronized with a HubSpot User.

Once a link between a Wave User and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave User and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - Wave User Property
     - HubSpot User Property
     - HubSpot Data Type

