==========================
Tripletex to Wave Dataflow
==========================

Generated: 2023-09-06 14:15:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Wave Customer
-----------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Wave Customer must be established.

A new Wave Customer will be created from a Tripletex Customer if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into Wave.

Once a link between a Tripletex Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Wave Customer Property
     - Wave Data Type
   * - name
     - name
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - physicalAddress.addressLine1
     - address.addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - address.addressLine2
     - "string"
   * - physicalAddress.city
     - address.city
     - "string"
   * - physicalAddress.country.id
     - address.country.code
     - "string"
   * - physicalAddress.postalCode
     - address.postalCode
     - "string"


Tripletex Contact to Wave Customer
----------------------------------
Every Tripletex Contact will be synchronized with a Wave Customer.

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
     - "string"
   * - phoneNumberMobile
     - mobile
     - "string"


Tripletex Employee to Wave Customer
-----------------------------------
Every Tripletex Employee will be synchronized with a Wave Customer.

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
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.country.id
     - address.country.code
     - "string"
   * - address.postalCode
     - address.postalCode
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
   * - phoneNumberMobile
     - mobile
     - "string"


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
   * - currency.id
     - currency.code
     - "string"
   * - customer.id
     - customer.id
     - "string"
   * - invoiceComment
     - title
     - "string"
   * - reference
     - poNumber
     - "string"


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


Tripletex Supplier to Wave Vendor
---------------------------------
Every Tripletex Supplier will be synchronized with a Wave Vendor.

Once a link between a Tripletex Supplier and a Wave Vendor is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a Wave Vendor:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Wave Vendor Property
     - Wave Data Type
   * - name
     - name
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - physicalAddress.addressLine1
     - address.addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - address.addressLine2
     - "string"
   * - physicalAddress.city
     - address.city
     - "string"
   * - physicalAddress.country.id
     - address.country.code
     - "string"
   * - physicalAddress.postalCode
     - address.postalCode
     - "string"

