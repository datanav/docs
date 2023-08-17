==================================
Wave Financial to HubSpot Dataflow
==================================

Generated: 2023-08-17 08:57:39

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
   * - address.postalCode
     - properties.zip
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
   * - address.postalCode
     - properties.zip
     - "string"
   * - id
     - id
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
   * - shippingDetails.phone
     - properties.phone
     - "string"
   * - website
     - properties.website
     - "string"


Wave Vendor to HubSpot Company
------------------------------
Every Wave Vendor will be synchronized with a HubSpot Company.

Once a link between a Wave Vendor and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
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
   * - address.postalCode
     - properties.zip
     - "string"
   * - id
     - id
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

