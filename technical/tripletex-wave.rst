==========================
Tripletex to Wave Dataflow
==========================

Generated: 2023-10-05 06:06:17

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Wave Customer person
-----------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Wave Customer person must be established.

A new Wave Customer person will be created from a Tripletex Contact if it is connected to a Tripletex Order that is synchronized into Wave.

Once a link between a Tripletex Contact and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Wave Customer person Property
     - Wave Data Type
   * - email
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "if","or","is-empty","_."],"eq","","_."]],"-","_."]
   * - phoneNumberMobile
     - mobile
     - "string"
   * - phoneNumberWork
     - phone
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
   * - customer.id
     - id
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


Tripletex Customer to Wave Customer person
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Wave Customer person must be established.

A new Wave Customer person will be created from a Tripletex Customer if it is connected to a Tripletex Order, Contact, Customer, Employee, or Department that is synchronized into Wave.

Once a link between a Tripletex Customer and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Wave Customer person Property
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
   * - id
     - id
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


Tripletex Customer to Wave Customer
-----------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Wave Customer must be established.

A new Wave Customer will be created from a Tripletex Customer if it is connected to a Tripletex Order, Contact, Invoice, Customer, Employee, Orderline, or Department that is synchronized into Wave.

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


Tripletex Department to Wave Customer person
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a Wave Customer person must be established.

A new Wave Customer person will be created from a Tripletex Department if it is connected to a Tripletex Contact, Customer, Employee, or Department that is synchronized into Wave.

Once a link between a Tripletex Department and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Wave Customer person Property
     - Wave Data Type


Tripletex Department to Wave Customer
-------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a Wave Customer must be established.

A new Wave Customer will be created from a Tripletex Department if it is connected to a Tripletex Contact, Customer, Employee, or Department that is synchronized into Wave.

Once a link between a Tripletex Department and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Wave Customer Property
     - Wave Data Type
   * - name
     - name
     - "if","or","is-empty","_."],"eq","","_."]],"-","_."]


Tripletex Order to Wave Invoice
-------------------------------
Before any synchronization can take place, a link between a Tripletex Order and a Wave Invoice must be established.

A new Wave Invoice will be created from a Tripletex Order if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into Wave.

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
Before any synchronization can take place, a link between a Tripletex Product and a Wave Product must be established.

A new Wave Product will be created from a Tripletex Product if it is connected to a Tripletex Order, Invoice, or Orderline that is synchronized into Wave.

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
   * - department.id
     - id
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
   * - phoneNumberWork
     - phone
     - "string"

