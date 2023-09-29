====================================
Wave Financial to Tripletex Dataflow
====================================

Generated: 2023-09-29 14:25:45

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to Tripletex Contact
-----------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a Tripletex Contact must be established.

A Wave Customer person will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Tripletex Contact Property
   * - email
     - email

Once a link between a Wave Customer person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Tripletex Contact Property
     - Tripletex Data Type


Wave Customer person to Tripletex Employee
------------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a Tripletex Employee must be established.

A Wave Customer person will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Tripletex Employee Property
   * - email
     - email

Once a link between a Wave Customer person and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
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
   * - shippingDetails.address.addressLine1
     - address.addressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - address.addressLine2
     - "string"
   * - shippingDetails.address.city
     - address.city
     - "string"
   * - shippingDetails.address.country.code
     - address.country.id
     - "integer"
   * - shippingDetails.address.postalCode
     - address.postalCode
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
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - lastName
     - lastName
     - "string"
   * - mobile
     - phoneNumberMobile
     - "string"
   * - phone
     - phoneNumberWork
     - "string"
   * - shippingDetails.address.addressLine1
     - address.addressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - address.addressLine2
     - "string"
   * - shippingDetails.address.city
     - address.city
     - "string"
   * - shippingDetails.address.country.code
     - address.country.id
     - "integer"
   * - shippingDetails.address.postalCode
     - address.postalCode
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
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
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
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - lastName
     - lastName
     - "string"
   * - mobile
     - phoneNumberMobile
     - "string"
   * - phone
     - phoneNumberWork
     - "string"


Wave Customer to Tripletex Department
-------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Tripletex Department must be established.

A new Tripletex Department will be created from a Wave Customer if it is connected to a Wave Vendor, Customer, or Customer-person that is synchronized into Tripletex.

Once a link between a Wave Customer and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - name
     - name
     - "string"


Wave Vendor to Tripletex Customer
---------------------------------
Every Wave Vendor will be synchronized with a Tripletex Customer.

Once a link between a Wave Vendor and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - address.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - address.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - address.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - address.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - address.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - address.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - address.city
     - deliveryAddress.city
     - "string"
   * - address.city
     - physicalAddress.city
     - "string"
   * - address.city
     - postalAddress.city
     - "string"
   * - address.country.code
     - deliveryAddress.country.id
     - "string"
   * - address.country.code
     - physicalAddress.country.id
     - "integer"
   * - address.country.code
     - postalAddress.country.id
     - "integer"
   * - address.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - address.postalCode
     - physicalAddress.postalCode
     - "string"
   * - address.postalCode
     - postalAddress.postalCode
     - "string"
   * - id
     - id
     - "integer"
   * - name
     - name
     - "string"
   * - phone
     - phoneNumber
     - "string"


Wave Customer to Tripletex Contact
----------------------------------
Every Wave Customer will be synchronized with a Tripletex Contact.

If a matching Tripletex Contact already exists, the Wave Customer will be merged with the existing one.
If no matching Tripletex Contact is found, a new Tripletex Contact will be created.

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
   * - email
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - customer.id
     - "integer"
   * - lastName
     - lastName
     - "string"
   * - mobile
     - phoneNumberMobile
     - "if","matches","+* *","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - phone
     - phoneNumberWork
     - "string"
   * - shippingDetails.phone
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
   * - address.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - address.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - address.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - address.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - address.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - address.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - address.city
     - deliveryAddress.city
     - "string"
   * - address.city
     - physicalAddress.city
     - "string"
   * - address.city
     - postalAddress.city
     - "string"
   * - address.country.code
     - deliveryAddress.country.id
     - "string"
   * - address.country.code
     - physicalAddress.country.id
     - "integer"
   * - address.country.code
     - postalAddress.country.id
     - "integer"
   * - address.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - address.postalCode
     - physicalAddress.postalCode
     - "string"
   * - address.postalCode
     - postalAddress.postalCode
     - "string"
   * - id
     - id
     - "integer"
   * - name
     - name
     - "string"
   * - phone
     - phoneNumber
     - "string"
   * - shippingDetails.address.addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - shippingDetails.address.addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - shippingDetails.address.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - shippingDetails.address.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - shippingDetails.address.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - shippingDetails.address.city
     - deliveryAddress.city
     - "string"
   * - shippingDetails.address.city
     - physicalAddress.city
     - "string"
   * - shippingDetails.address.city
     - postalAddress.city
     - "string"
   * - shippingDetails.address.country.code
     - deliveryAddress.country.id
     - "string"
   * - shippingDetails.address.country.code
     - physicalAddress.country.id
     - "integer"
   * - shippingDetails.address.country.code
     - postalAddress.country.id
     - "integer"
   * - shippingDetails.address.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - shippingDetails.address.postalCode
     - physicalAddress.postalCode
     - "string"
   * - shippingDetails.address.postalCode
     - postalAddress.postalCode
     - "string"
   * - shippingDetails.phone
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
     - contact.id
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


Wave Invoice to Tripletex Orderline
-----------------------------------
Every Wave Invoice will be synchronized with a Tripletex Orderline.

Once a link between a Wave Invoice and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - id
     - order.id
     - "integer"
   * - items.description
     - description
     - "string"
   * - items.price
     - unitPriceExcludingVatCurrency
     - "float"
   * - items.product.id
     - product.id
     - "integer"
   * - items.quantity
     - count
     - "float"


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
   * - address.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - address.addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - address.addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - address.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - address.city
     - deliveryAddress.changes
     - "string"
   * - address.city
     - physicalAddress.city
     - "string"
   * - address.city
     - postalAddress.city
     - "string"
   * - address.country.code
     - deliveryAddress.city
     - "string"
   * - address.country.code
     - physicalAddress.country.id
     - "integer"
   * - address.country.code
     - postalAddress.country.id
     - "integer"
   * - address.postalCode
     - deliveryAddress.postalCode
     - "string"
   * - address.postalCode
     - physicalAddress.postalCode
     - "string"
   * - address.postalCode
     - postalAddress.postalCode
     - "string"
   * - id
     - id
     - "integer"
   * - name
     - name
     - "string"
   * - phone
     - phoneNumber
     - "string"

