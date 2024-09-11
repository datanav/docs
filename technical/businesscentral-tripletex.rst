======================================
Business Central to Tripletex Dataflow
======================================

Generated: 2024-09-11 07:54:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Customers to Tripletex Contact
---------------------------------------
Before any synchronization can take place, a link between a Business Customers and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a Business Customers if it is connected to a Business Businesscentral-salesorders that is synchronized into Tripletex.

Once a link between a Business Customers and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Business Customers Property
     - Tripletex Contact Property
     - Tripletex Data Type


Business Customers to Tripletex Customer
----------------------------------------
Before any synchronization can take place, a link between a Business Customers and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Business Customers if it is connected to a Business Businesscentral-customers, Businesscentral-salesorders, Businesscentral-contact-person, or Businesscentral-contacts-person that is synchronized into Tripletex.

Once a link between a Business Customers and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Business Customers Property
     - Tripletex Customer Property
     - Tripletex Data Type


Business Customers to Tripletex Customer person
-----------------------------------------------
Before any synchronization can take place, a link between a Business Customers and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a Business Customers if it is connected to a Business Businesscentral-customers, Businesscentral-salesorders, Businesscentral-contact-person, or Businesscentral-contacts-person that is synchronized into Tripletex.

Once a link between a Business Customers and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Business Customers Property
     - Tripletex Customer person Property
     - Tripletex Data Type


Business Contacts person to Tripletex Contact
---------------------------------------------
Every Business Contacts person will be synchronized with a Tripletex Contact.

Once a link between a Business Contacts person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
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


Business Contacts person to Tripletex Customer person
-----------------------------------------------------
Every Business Contacts person will be synchronized with a Tripletex Customer person.

Once a link between a Business Contacts person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
     - Tripletex Customer person Property
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
     - "string"


Business Customers company to Tripletex Customer
------------------------------------------------
Every Business Customers company will be synchronized with a Tripletex Customer.

Once a link between a Business Customers company and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers company and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Business Customers company Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - address.city
     - deliveryAddress.city
     - "string"
   * - address.city
     - physicalAddress.city
     - "string"
   * - address.city
     - postalAddress.city
     - "string"
   * - address.countryLetterCode
     - deliveryAddress.country.id
     - "string"
   * - address.countryLetterCode
     - physicalAddress.country.id
     - "integer"
   * - address.countryLetterCode
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
     - invoiceSendMethod
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
   * - type
     - isPrivateIndividual
     - "string"
   * - website
     - website
     - "string"


Business Customers person to Tripletex Customer person
------------------------------------------------------
Every Business Customers person will be synchronized with a Tripletex Customer person.

Once a link between a Business Customers person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Business Customers person Property
     - Tripletex Customer person Property
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
     - "string"


Business Employees to Tripletex Employee
----------------------------------------
Every Business Employees will be synchronized with a Tripletex Employee.

Once a link between a Business Employees and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Employees and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Business Employees Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - birthDate
     - dateOfBirth
     - N/A
   * - displayName
     - firstName
     - "string"
   * - displayName
     - lastName
     - "string"
   * - email
     - email
     - "string"
   * - givenName
     - firstName
     - "string"
   * - givenName
     - lastName
     - "string"
   * - mobilePhone
     - phoneNumberMobile
     - "string"
   * - phoneNumber
     - phoneNumberWork
     - "string"
   * - surname
     - firstName
     - "string"
   * - surname
     - lastName
     - "string"


Business Items to Tripletex Product
-----------------------------------
Every Business Items will be synchronized with a Tripletex Product.

If a matching Tripletex Product already exists, the Business Items will be merged with the existing one.
If no matching Tripletex Product is found, a new Tripletex Product will be created.

A Business Items will merge with a Tripletex Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Items Property
     - Tripletex Product Property
   * - gtin
     - ean

Once a link between a Business Items and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Items and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Business Items Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - displayName
     - name
     - "string"
   * - displayName.string
     - name
     - "string"
   * - displayName2
     - name
     - "string"
   * - gtin
     - ean
     - "string"
   * - inventory
     - stockOfGoods
     - "integer"
   * - taxGroupCode
     - vatType.id
     - "integer"
   * - unitCost
     - costExcludingVatCurrency
     - "float"
   * - unitPrice
     - priceExcludingVatCurrency
     - "float"


Business Salesorderlines to Tripletex Orderline
-----------------------------------------------
Every Business Salesorderlines will be synchronized with a Tripletex Orderline.

Once a link between a Business Salesorderlines and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorderlines and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Business Salesorderlines Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - amountExcludingTax
     - unitPriceExcludingVatCurrency
     - "float"
   * - description
     - count
     - N/A
   * - description
     - description
     - "string"
   * - description
     - discount
     - "float"
   * - description
     - unitCostCurrency
     - "float"
   * - description
     - unitPriceExcludingVatCurrency
     - "float"
   * - description
     - vatType.id
     - "integer"
   * - discountPercent
     - count
     - N/A
   * - discountPercent
     - description
     - "string"
   * - discountPercent
     - discount
     - "float"
   * - discountPercent
     - unitCostCurrency
     - "float"
   * - discountPercent
     - unitPriceExcludingVatCurrency
     - "float"
   * - discountPercent
     - vatType.id
     - "integer"
   * - documentId
     - order.id
     - "integer"
   * - invoiceQuantity
     - count
     - "float"
   * - itemId
     - product.id
     - "integer"
   * - quantity
     - count
     - N/A
   * - quantity
     - description
     - "string"
   * - quantity
     - discount
     - "float"
   * - quantity
     - unitCostCurrency
     - "float"
   * - quantity
     - unitPriceExcludingVatCurrency
     - "float"
   * - quantity
     - vatType.id
     - "integer"
   * - taxPercent
     - count
     - N/A
   * - taxPercent
     - description
     - "string"
   * - taxPercent
     - discount
     - "float"
   * - taxPercent
     - unitCostCurrency
     - "float"
   * - taxPercent
     - unitPriceExcludingVatCurrency
     - "float"
   * - taxPercent
     - vatType.id
     - "integer"
   * - unitPrice
     - count
     - N/A
   * - unitPrice
     - description
     - "string"
   * - unitPrice
     - discount
     - "float"
   * - unitPrice
     - unitCostCurrency
     - "float"
   * - unitPrice
     - unitPriceExcludingVatCurrency
     - "float"
   * - unitPrice
     - vatType.id
     - "integer"


Business Salesorders to Tripletex Order
---------------------------------------
Every Business Salesorders will be synchronized with a Tripletex Order.

Once a link between a Business Salesorders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Business Salesorders Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - currencyId
     - currency.id
     - "integer"
   * - customerId
     - contact.id
     - "integer"
   * - customerId
     - customer.id
     - "integer"
   * - orderDate
     - orderDate
     - N/A
   * - requestedDeliveryDate
     - deliveryDate
     - N/A
   * - salesperson
     - ourContactEmployee.id
     - "integer"

