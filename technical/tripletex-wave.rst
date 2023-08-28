==========================
Tripletex to Wave Dataflow
==========================

Generated: 2023-08-28 15:12:46

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
   * - deliveryAddress.addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - deliveryAddress.city
     - shippingDetails.address.city
     - "string"
   * - deliveryAddress.country.id
     - shippingDetails.address.country.code
     - "string"
   * - deliveryAddress.postalCode
     - shippingDetails.address.postalCode
     - "string"
   * - name
     - name
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - phoneNumber
     - shippingDetails.phone
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
     - shippingDetails.address.addressLine1
     - "string"
   * - postalAddress.addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - postalAddress.city
     - shippingDetails.address.city
     - "string"
   * - postalAddress.country.id
     - shippingDetails.address.country.code
     - "string"
   * - postalAddress.postalCode
     - shippingDetails.address.postalCode
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

