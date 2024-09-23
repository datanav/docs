==========================
Tripletex to Wave Dataflow
==========================

Generated: 2024-09-23 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Wave Customer
----------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Wave Customer must be established.

A new Wave Customer will be created from a Tripletex Contact if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into Wave.

A Tripletex Contact will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Wave Customer Property
   * - email
     - email

Once a link between a Tripletex Contact and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Wave Customer Property
     - Wave Data Type
   * - email
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - N/A
   * - phoneNumberMobile
     - mobile
     - "string"
   * - phoneNumberWork
     - phone
     - "string"


Tripletex Customer to Wave Customer
-----------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Wave Customer must be established.

A Tripletex Customer will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Wave Customer Property
   * - email
     - email

Once a link between a Tripletex Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Wave Customer Property
     - Wave Data Type
   * - deliveryAddress.addressLine1
     - address.addressLine1
     - "string"
   * - deliveryAddress.addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - address.addressLine2
     - "string"
   * - deliveryAddress.addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - deliveryAddress.city
     - address.city
     - "string"
   * - deliveryAddress.city
     - shippingDetails.address.city
     - "string"
   * - deliveryAddress.country.id
     - address.country.code
     - "string"
   * - deliveryAddress.country.id
     - shippingDetails.address.country.code
     - "string"
   * - deliveryAddress.postalCode
     - address.postalCode
     - "string"
   * - deliveryAddress.postalCode
     - shippingDetails.address.postalCode
     - "string"
   * - email
     - email
     - "string"
   * - name
     - name
     - N/A
   * - phoneNumber
     - phone
     - "string"
   * - phoneNumberMobile
     - mobile
     - "string"
   * - physicalAddress.addressLine1
     - address.addressLine1
     - "string"
   * - physicalAddress.addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - address.addressLine2
     - "string"
   * - physicalAddress.addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - physicalAddress.city
     - address.city
     - "string"
   * - physicalAddress.city
     - shippingDetails.address.city
     - "string"
   * - physicalAddress.country.id
     - address.country.code
     - "string"
   * - physicalAddress.country.id
     - shippingDetails.address.country.code
     - "string"
   * - physicalAddress.postalCode
     - address.postalCode
     - "string"
   * - physicalAddress.postalCode
     - shippingDetails.address.postalCode
     - "string"
   * - postalAddress.addressLine1
     - address.addressLine1
     - "string"
   * - postalAddress.addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - postalAddress.addressLine2
     - address.addressLine2
     - "string"
   * - postalAddress.addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - postalAddress.city
     - address.city
     - "string"
   * - postalAddress.city
     - shippingDetails.address.city
     - "string"
   * - postalAddress.country.id
     - address.country.code
     - "string"
   * - postalAddress.country.id
     - shippingDetails.address.country.code
     - "string"
   * - postalAddress.postalCode
     - address.postalCode
     - "string"
   * - postalAddress.postalCode
     - shippingDetails.address.postalCode
     - "string"


Tripletex Employee to Wave Customer
-----------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a Wave Customer must be established.

A Tripletex Employee will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Wave Customer Property
   * - email
     - email

Once a link between a Tripletex Employee and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
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
   * - address.country.id
     - address.country.code
     - "string"
   * - address.country.id
     - shippingDetails.address.country.code
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - shippingDetails.address.postalCode
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - N/A
   * - phoneNumberMobile
     - mobile
     - "string"
   * - phoneNumberWork
     - phone
     - "string"


Tripletex Customer (organisation data) to Wave Customer
-------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Wave Customer.

Once a link between a Tripletex Customer (organisation data) and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (organisation data) and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (organisation data) Property
     - Wave Customer Property
     - Wave Data Type
   * - deliveryAddress.addressLine1
     - address.addressLine1
     - "string"
   * - deliveryAddress.addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - address.addressLine2
     - "string"
   * - deliveryAddress.addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - deliveryAddress.city
     - address.city
     - "string"
   * - deliveryAddress.city
     - shippingDetails.address.city
     - "string"
   * - deliveryAddress.country.id
     - address.country.code
     - "string"
   * - deliveryAddress.country.id
     - shippingDetails.address.country.code
     - "string"
   * - deliveryAddress.postalCode
     - address.postalCode
     - "string"
   * - deliveryAddress.postalCode
     - shippingDetails.address.postalCode
     - "string"
   * - email
     - email
     - "string"
   * - phoneNumberMobile
     - mobile
     - "string"
   * - physicalAddress.addressLine1
     - address.addressLine1
     - "string"
   * - physicalAddress.addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - address.addressLine2
     - "string"
   * - physicalAddress.addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - physicalAddress.city
     - address.city
     - "string"
   * - physicalAddress.city
     - shippingDetails.address.city
     - "string"
   * - physicalAddress.country.id
     - address.country.code
     - "string"
   * - physicalAddress.country.id
     - shippingDetails.address.country.code
     - "string"
   * - physicalAddress.postalCode
     - address.postalCode
     - "string"
   * - physicalAddress.postalCode
     - shippingDetails.address.postalCode
     - "string"
   * - postalAddress.addressLine1
     - address.addressLine1
     - "string"
   * - postalAddress.addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - postalAddress.addressLine2
     - address.addressLine2
     - "string"
   * - postalAddress.addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - postalAddress.city
     - address.city
     - "string"
   * - postalAddress.city
     - shippingDetails.address.city
     - "string"
   * - postalAddress.country.id
     - address.country.code
     - "string"
   * - postalAddress.country.id
     - shippingDetails.address.country.code
     - "string"
   * - postalAddress.postalCode
     - address.postalCode
     - "string"
   * - postalAddress.postalCode
     - shippingDetails.address.postalCode
     - "string"


Tripletex Customer (human data) to Wave Customer (human data)
-------------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Wave Customer (human data).

Once a link between a Tripletex Customer (human data) and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (human data) and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (human data) Property
     - Wave Customer (human data) Property
     - Wave Data Type


Tripletex Customer to Wave Customer
-----------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Wave Customer.

Once a link between a Tripletex Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Wave Customer Property
     - Wave Data Type


Tripletex Customer to Wave Customer (human data)
------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Wave Customer (human data).

Once a link between a Tripletex Customer and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Wave Customer (human data) Property
     - Wave Data Type


Tripletex Order to Wave Invoice
-------------------------------
Every Tripletex Order will be synchronized with a Wave Invoice.

Once a link between a Tripletex Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Wave Invoice Property
     - Wave Data Type


Tripletex Product to Wave Product
---------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Wave Product.

Once a link between a Tripletex Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Wave Product Property
     - Wave Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - priceExcludingVatCurrency
     - unitPrice
     - "string"

