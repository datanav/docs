====================================
Wave Financial to Tripletex Dataflow
====================================

Generated: 2023-06-28 08:09:31

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Tripletex Contact
----------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Tripletex Contact must be established.

A Wave Customer will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Tripletex Contact Property
   * - email
     - email

Once a link between a Wave Customer and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - mobile
     - phoneNumberMobile
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - phone
     - phoneNumberWork
     - "string"


Wave Customer to Tripletex Employee
-----------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Tripletex Employee must be established.

A Wave Customer will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Tripletex Employee Property
   * - email
     - email

Once a link between a Wave Customer and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.country.code
     - address.country.id
     - "integer"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - id
     - id
     - "integer"
   * - mobile
     - phoneNumberMobile
     - "string"
   * - phone
     - phoneNumberWork
     - "string"


Wave Vendor to Tripletex Contact
--------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Tripletex Contact must be established.

A Wave Vendor will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Tripletex Contact Property
   * - email
     - email

Once a link between a Wave Vendor and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - mobile
     - phoneNumberMobile
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - phone
     - phoneNumberWork
     - "string"


Wave Vendor to Tripletex Employee
---------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Tripletex Employee must be established.

A Wave Vendor will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Tripletex Employee Property
   * - email
     - email

Once a link between a Wave Vendor and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - address.addressLine1
     - address.addressLine1
     - "string"
   * - address.addressLine2
     - address.addressLine2
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.country.code
     - address.country.id
     - "integer"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - id
     - id
     - "integer"
   * - mobile
     - phoneNumberMobile
     - "string"
   * - phone
     - phoneNumberWork
     - "string"


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
   * - name
     - name
     - "string"
   * - phone
     - phoneNumber
     - "string"

