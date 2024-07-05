=====================================
Businesscentral to Tripletex Dataflow
=====================================

Generated: 2024-07-05 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers to Tripletex Contact
----------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a Businesscentral Customers if it is connected to a Businesscentral Salesorders that is synchronized into Tripletex.

Once a link between a Businesscentral Customers and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     - Tripletex Contact Property
     - Tripletex Data Type


Businesscentral Customers to Tripletex Customer
-----------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Businesscentral Customers if it is connected to a Businesscentral Customers, Salesorders, Contact-person, or Contacts-person that is synchronized into Tripletex.

Once a link between a Businesscentral Customers and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     - Tripletex Customer Property
     - Tripletex Data Type


Businesscentral Customers to Tripletex Customer person
------------------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a Businesscentral Customers if it is connected to a Businesscentral Customers, Salesorders, Contact-person, or Contacts-person that is synchronized into Tripletex.

Once a link between a Businesscentral Customers and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     - Tripletex Customer person Property
     - Tripletex Data Type


Businesscentral Contacts person to Tripletex Contact
----------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Tripletex Contact.

Once a link between a Businesscentral Contacts person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
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


Businesscentral Contacts person to Tripletex Customer person
------------------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Tripletex Customer person.

Once a link between a Businesscentral Contacts person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
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


Businesscentral Customers company to Tripletex Customer
-------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Tripletex Customer.

Once a link between a Businesscentral Customers company and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
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


Businesscentral Customers person to Tripletex Customer person
-------------------------------------------------------------
Every Businesscentral Customers person will be synchronized with a Tripletex Customer person.

Once a link between a Businesscentral Customers person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
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


Businesscentral Employees to Tripletex Employee
-----------------------------------------------
Every Businesscentral Employees will be synchronized with a Tripletex Employee.

Once a link between a Businesscentral Employees and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
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


Businesscentral Items to Tripletex Product
------------------------------------------
Every Businesscentral Items will be synchronized with a Tripletex Product.

If a matching Tripletex Product already exists, the Businesscentral Items will be merged with the existing one.
If no matching Tripletex Product is found, a new Tripletex Product will be created.

A Businesscentral Items will merge with a Tripletex Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Tripletex Product Property
   * - gtin
     - ean

Once a link between a Businesscentral Items and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
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


Businesscentral Salesorderlines to Tripletex Orderline
------------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a Tripletex Orderline.

Once a link between a Businesscentral Salesorderlines and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
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


Businesscentral Salesorders to Tripletex Order
----------------------------------------------
Every Businesscentral Salesorders will be synchronized with a Tripletex Order.

Once a link between a Businesscentral Salesorders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
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

