======================================
Business Central to Tripletex Dataflow
======================================

Generated: 2024-09-23 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Items to Tripletex Product
-------------------------------------------
Before any synchronization can take place, a link between a Business Central Items and a Tripletex Product must be established.

A new Tripletex Product will be created from a Business Central Items if it is connected to a Business Central Businesscentral-salesorderlines that is synchronized into Tripletex.

A Business Central Items will merge with a Tripletex Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Tripletex Product Property
   * - gtin
     - ean

Once a link between a Business Central Items and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - displayName
     - name
     - "string"
   * - gtin
     - ean
     - "string"
   * - inventory
     - stockOfGoods
     - "integer"
   * - unitCost
     - costExcludingVatCurrency
     - "float"
   * - unitPrice
     - priceExcludingVatCurrency
     - "float"


Business Central Contacts (human data) to Tripletex Contact
-----------------------------------------------------------
Every Business Central Contacts (human data) will be synchronized with a Tripletex Contact.

Once a link between a Business Central Contacts (human data) and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts (human data) and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts (human data) Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - email
     - email
     - "string"
   * - mobilePhoneNumber
     - phoneNumberMobile
     - N/A
   * - phoneNumber
     - phoneNumberWork
     - "string"


Business Central Contacts (classification data) to Tripletex Customer (classification data)
-------------------------------------------------------------------------------------------
Every Business Central Contacts (classification data) will be synchronized with a Tripletex Customer (classification data).

Once a link between a Business Central Contacts (classification data) and a Tripletex Customer (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts (classification data) and a Tripletex Customer (classification data):

.. list-table::
   :header-rows: 1

   * - Business Central Contacts (classification data) Property
     - Tripletex Customer (classification data) Property
     - Tripletex Data Type
   * - addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - addressLine1
     - postalAddress.addressLine1
     - "string"
   * - addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - addressLine2
     - postalAddress.addressLine2
     - "string"
   * - city
     - deliveryAddress.city
     - "string"
   * - city
     - physicalAddress.city
     - "string"
   * - city
     - postalAddress.city
     - "string"
   * - country
     - deliveryAddress.country.id
     - "string"
   * - country
     - physicalAddress.country.id
     - "integer"
   * - country
     - postalAddress.country.id
     - "integer"
   * - displayName
     - name
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "integer"
   * - mobilePhoneNumber
     - phoneNumberMobile
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - postalCode
     - deliveryAddress.postalCode
     - "string"
   * - postalCode
     - physicalAddress.postalCode
     - "string"
   * - postalCode
     - postalAddress.postalCode
     - "string"
   * - type
     - isPrivateIndividual
     - "boolean"


Business Central Customers (organisation data) to Tripletex Customer
--------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Tripletex Customer.

Once a link between a Business Central Customers (organisation data) and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - addressLine1
     - postalAddress.addressLine1
     - "string"
   * - addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - addressLine2
     - postalAddress.addressLine2
     - "string"
   * - city
     - deliveryAddress.city
     - "string"
   * - city
     - physicalAddress.city
     - "string"
   * - city
     - postalAddress.city
     - "string"
   * - country
     - deliveryAddress.country.id
     - "string"
   * - country
     - physicalAddress.country.id
     - "integer"
   * - country
     - postalAddress.country.id
     - "integer"
   * - displayName
     - name
     - "string"
   * - id
     - id
     - "integer"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - postalCode
     - deliveryAddress.postalCode
     - "string"
   * - postalCode
     - physicalAddress.postalCode
     - "string"
   * - postalCode
     - postalAddress.postalCode
     - "string"
   * - website
     - website
     - "string"


Business Central Customers (human data) to Tripletex Customer (human data)
--------------------------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Tripletex Customer (human data).

Once a link between a Business Central Customers (human data) and a Tripletex Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Tripletex Customer (human data):

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - Tripletex Customer (human data) Property
     - Tripletex Data Type
   * - addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - addressLine1
     - postalAddress.addressLine1
     - "string"
   * - addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - addressLine2
     - postalAddress.addressLine2
     - "string"
   * - city
     - deliveryAddress.city
     - "string"
   * - city
     - physicalAddress.city
     - "string"
   * - city
     - postalAddress.city
     - "string"
   * - country
     - deliveryAddress.country.id
     - "string"
   * - country
     - physicalAddress.country.id
     - "integer"
   * - country
     - postalAddress.country.id
     - "integer"
   * - id
     - id
     - "integer"
   * - postalCode
     - deliveryAddress.postalCode
     - "string"
   * - postalCode
     - physicalAddress.postalCode
     - "string"
   * - postalCode
     - postalAddress.postalCode
     - "string"


Business Central Customers (organisation data) to Tripletex Customer
--------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Tripletex Customer.

Once a link between a Business Central Customers (organisation data) and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Tripletex Customer Property
     - Tripletex Data Type


Business Central Customers (classification data) to Tripletex Customer (classification data)
--------------------------------------------------------------------------------------------
Every Business Central Customers (classification data) will be synchronized with a Tripletex Customer (classification data).

Once a link between a Business Central Customers (classification data) and a Tripletex Customer (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (classification data) and a Tripletex Customer (classification data):

.. list-table::
   :header-rows: 1

   * - Business Central Customers (classification data) Property
     - Tripletex Customer (classification data) Property
     - Tripletex Data Type


Business Central Customers (human data) to Tripletex Customer (human data)
--------------------------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Tripletex Customer (human data).

Once a link between a Business Central Customers (human data) and a Tripletex Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Tripletex Customer (human data):

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - Tripletex Customer (human data) Property
     - Tripletex Data Type
   * - addressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - addressLine1
     - physicalAddress.addressLine1
     - "string"
   * - addressLine1
     - postalAddress.addressLine1
     - "string"
   * - addressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - addressLine2
     - physicalAddress.addressLine2
     - "string"
   * - addressLine2
     - postalAddress.addressLine2
     - "string"
   * - city
     - deliveryAddress.city
     - "string"
   * - city
     - physicalAddress.city
     - "string"
   * - city
     - postalAddress.city
     - "string"
   * - country
     - deliveryAddress.country.id
     - "string"
   * - country
     - physicalAddress.country.id
     - "integer"
   * - country
     - postalAddress.country.id
     - "integer"
   * - displayName
     - name
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "integer"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - postalCode
     - deliveryAddress.postalCode
     - "string"
   * - postalCode
     - physicalAddress.postalCode
     - "string"
   * - postalCode
     - postalAddress.postalCode
     - "string"
   * - type
     - isPrivateIndividual
     - "boolean"


Business Central Employees to Tripletex Employee
------------------------------------------------
Every Business Central Employees will be synchronized with a Tripletex Employee.

Once a link between a Business Central Employees and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - birthDate
     - dateOfBirth
     - N/A
   * - email
     - email
     - "string"
   * - givenName
     - firstName
     - "string"
   * - mobilePhone
     - phoneNumberMobile
     - N/A
   * - phoneNumber
     - phoneNumberWork
     - "string"
   * - surname
     - lastName
     - "string"


Business Central Items to Tripletex Product
-------------------------------------------
Every Business Central Items will be synchronized with a Tripletex Product.

Once a link between a Business Central Items and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Tripletex Product Property
     - Tripletex Data Type


Business Central Salesorderlines to Tripletex Orderline
-------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a Tripletex Orderline.

Once a link between a Business Central Salesorderlines and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - Tripletex Orderline Property
     - Tripletex Data Type


Business Central Salesorders to Tripletex Order
-----------------------------------------------
Every Business Central Salesorders will be synchronized with a Tripletex Order.

Once a link between a Business Central Salesorders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Tripletex Order Property
     - Tripletex Data Type

