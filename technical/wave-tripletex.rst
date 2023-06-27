====================================
Wave Financial to Tripletex Dataflow
====================================

Generated: 2023-06-27 06:42:23

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Invoice to Tripletex Order
-------------------------------
Every Wave Invoice will be synchronized with a Tripletex Order.

Once a link between a Wave Invoice and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - currency.code
     - currency.id
     - "integer"
   * - customer.id
     - customer.id
     - "integer"
   * - poNumber
     - reference
     - "string"
   * - title
     - invoiceComment
     - "string"


Wave Product to Tripletex Product
---------------------------------
Every Wave Product will be synchronized with a Tripletex Product.

Once a link between a Wave Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - unitPrice
     - priceExcludingVatCurrency
     - "float"


Wave Vendor to Tripletex Supplier
---------------------------------
Every Wave Vendor will be synchronized with a Tripletex Supplier.

Once a link between a Wave Vendor and a Tripletex Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Tripletex Supplier:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Tripletex Supplier Property
     - Tripletex Data Type
   * - address.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - address.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - address.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - address.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - address.city
     - deliveryAddress.changes
     - "string"
   * - address.city
     - physicalAddress.city
     - "string"
   * - address.country.code
     - deliveryAddress.city
     - "string"
   * - address.country.code
     - physicalAddress.country.id
     - "integer"
   * - address.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - address.postalCode
     - physicalAddress.postalCode
     - "string"
   * - name
     - name
     - "string"
   * - phone
     - phoneNumber
     - "string"

