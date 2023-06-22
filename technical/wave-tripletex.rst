====================================
Wave Financial to Tripletex Dataflow
====================================

Generated: 2023-06-22 11:38:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Tripletex Customer
-----------------------------------
Every Wave Customer will be synchronized with a Tripletex Customer.

Once a link between a Wave Customer and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - name
     - name
     - "string"
   * - phone
     - phoneNumber
     - "string"


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
   * - dueDate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - total.currency.symbol
     - currency.id
     - "integer"


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
   * - name
     - name
     - "string"
   * - phone
     - phoneNumber
     - "string"

