========================
Wave to HubSpot Dataflow
========================

Generated: 2024-09-22 00:00:00

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
   * - email
     - properties.email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - lastName
     - properties.lastname
     - "string"
   * - mobile
     - properties.mobilephone
     - "string"


Wave Customer (human data) to HubSpot Contact
---------------------------------------------
Every Wave Customer (human data) will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the Wave Customer (human data) will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A Wave Customer (human data) will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer (human data) Property
     - HubSpot Contact Property
   * - email
     - properties.email

Once a link between a Wave Customer (human data) and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer (human data) and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer (human data) Property
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
   * - address.province.code
     - properties.state
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
   * - shippingDetails.address.province.code
     - properties.state
     - "string"
   * - shippingDetails.phone
     - properties.phone
     - "string"
   * - website
     - properties.website
     - "string"


Wave Invoice to HubSpot Deal
----------------------------
Every Wave Invoice will be synchronized with a HubSpot Deal.

Once a link between a Wave Invoice and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - currency.code
     - properties.deal_currency_code
     - "string"
   * - memo
     - properties.description
     - "string"
   * - title
     - properties.dealname
     - "string"
   * - total.value
     - properties.amount
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


Wave Invoice to HubSpot Lineitemdealassociationtype
---------------------------------------------------
Every Wave Invoice will be synchronized with a HubSpot Lineitemdealassociationtype.

Once a link between a Wave Invoice and a HubSpot Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a HubSpot Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - HubSpot Lineitemdealassociationtype Property
     - HubSpot Data Type


Wave Invoice to HubSpot Lineitemquoteassociationtype
----------------------------------------------------
Every Wave Invoice will be synchronized with a HubSpot Lineitemquoteassociationtype.

Once a link between a Wave Invoice and a HubSpot Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a HubSpot Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - HubSpot Lineitemquoteassociationtype Property
     - HubSpot Data Type


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
   * - defaultEmail
     - email
     - "string"

