===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-03-26 13:42:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to  Contact
--------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a  Contact must be established.

A Wave Customer person will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Contact Property
   * - email
     - email

Once a link between a Wave Customer person and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Contact Property
     -  Data Type


Wave Customer person to  Employee
---------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a  Employee must be established.

A Wave Customer person will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Employee Property
   * - email
     - email

Once a link between a Wave Customer person and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Employee:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Employee Property
     -  Data Type
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
   * - address.countryCode
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


Wave Customer to  Employee
--------------------------
Before any synchronization can take place, a link between a Wave Customer and a  Employee must be established.

A Wave Customer will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Employee Property
   * - email
     - email

Once a link between a Wave Customer and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Employee:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Employee Property
     -  Data Type
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
   * - address.countryCode
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


Wave Vendor to  Employee
------------------------
Before any synchronization can take place, a link between a Wave Vendor and a  Employee must be established.

A Wave Vendor will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Employee Property
   * - email
     - email

Once a link between a Wave Vendor and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Employee:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Employee Property
     -  Data Type
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


Wave Customer to  Customer person
---------------------------------
Before any synchronization can take place, a link between a Wave Customer and a  Customer person must be established.

A new  Customer person will be created from a Wave Customer if it is connected to a Wave Vendor, Invoice, Customer, or Customer-person that is synchronized into .

Once a link between a Wave Customer and a  Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Customer person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Customer person Property
     -  Data Type
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


Wave Vendor to  Customer person
-------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a  Customer person must be established.

A new  Customer person will be created from a Wave Vendor if it is connected to a Wave Vendor, Customer, or Customer-person that is synchronized into .

Once a link between a Wave Vendor and a  Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Customer person:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Customer person Property
     -  Data Type
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


Wave Vendor to  Customer
------------------------
Before any synchronization can take place, a link between a Wave Vendor and a  Customer must be established.

A new  Customer will be created from a Wave Vendor if it is connected to a Wave Vendor, Customer, or Customer-person that is synchronized into .

Once a link between a Wave Vendor and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Customer:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Customer Property
     -  Data Type
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
   * - website
     - website
     - "string"


Wave Customer to  Contact
-------------------------
Every Wave Customer will be synchronized with a  Contact.

If a matching  Contact already exists, the Wave Customer will be merged with the existing one.
If no matching  Contact is found, a new  Contact will be created.

A Wave Customer will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Contact Property
   * - email
     - email

Once a link between a Wave Customer and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Contact Property
     -  Data Type
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


Wave Customer to  Customer
--------------------------
Every Wave Customer will be synchronized with a  Customer.

Once a link between a Wave Customer and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Customer Property
     -  Data Type
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
   * - address.countryCode
     - deliveryAddress.country.id
     - "string"
   * - address.countryCode
     - physicalAddress.country.id
     - "integer"
   * - address.countryCode
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
   * - website
     - url
     - "string"
   * - website
     - website
     - "string"


Wave Invoice to  Order
----------------------
Every Wave Invoice will be synchronized with a  Order.

Once a link between a Wave Invoice and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Order Property
     -  Data Type
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


Wave Invoice to  Orderline
--------------------------
Every Wave Invoice will be synchronized with a  Orderline.

Once a link between a Wave Invoice and a  Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Orderline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Orderline Property
     -  Data Type
   * - id
     - order.id
     - "integer"
   * - items.description
     - count
     - "integer", "decimal"]
   * - items.description
     - description
     - "string"
   * - items.description
     - discount
     - "float"
   * - items.description
     - unitCostCurrency
     - "float"
   * - items.description
     - unitPriceExcludingVatCurrency
     - "float"
   * - items.description
     - vatType.id
     - "integer"
   * - items.price
     - count
     - "integer", "decimal"]
   * - items.price
     - description
     - "string"
   * - items.price
     - discount
     - "float"
   * - items.price
     - unitCostCurrency
     - "float"
   * - items.price
     - unitPriceExcludingVatCurrency
     - "float"
   * - items.price
     - vatType.id
     - "integer"
   * - items.product.id
     - product.id
     - "integer"
   * - items.quantity
     - count
     - "integer", "decimal"]
   * - items.quantity
     - description
     - "string"
   * - items.quantity
     - discount
     - "float"
   * - items.quantity
     - unitCostCurrency
     - "float"
   * - items.quantity
     - unitPriceExcludingVatCurrency
     - "float"
   * - items.quantity
     - vatType.id
     - "integer"


Wave Product to  Product
------------------------
Every Wave Product will be synchronized with a  Product.

Once a link between a Wave Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Product Property
     -  Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - unitPrice
     - priceExcludingVatCurrency
     - "float"


Wave Vendor to  Contact
-----------------------
Every Wave Vendor will be synchronized with a  Contact.

If a matching  Contact already exists, the Wave Vendor will be merged with the existing one.
If no matching  Contact is found, a new  Contact will be created.

A Wave Vendor will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Contact Property
   * - email
     - email

Once a link between a Wave Vendor and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Contact Property
     -  Data Type
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

