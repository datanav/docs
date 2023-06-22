==========================
Tripletex to Wave Dataflow
==========================

Generated: 2023-06-22 14:18:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Currency to Wave Currency
-----------------------------------
Every Tripletex Currency will be synchronized with a Wave Currency.

If a matching Wave Currency already exists, the Tripletex Currency will be merged with the existing one.
If no matching Wave Currency is found, a new Wave Currency will be created.

A Tripletex Currency will merge with a Wave Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - Wave Currency Property
   * - code
     - code

Once a link between a Tripletex Currency and a Wave Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a Wave Currency:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - Wave Currency Property
     - Wave Data Type
   * - displayName
     - name
     - "string"


Tripletex Customer to Wave Customer
-----------------------------------
Every Tripletex Customer will be synchronized with a Wave Customer.

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


Tripletex Product to Wave Product
---------------------------------
Every Tripletex Product will be synchronized with a Wave Product.

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

