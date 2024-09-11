======================================
Tripletex to Business Central Dataflow
======================================

Generated: 2024-09-11 07:54:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Business Customers company
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Business Customers company must be established.

A new Business Customers company will be created from a Tripletex Contact if it is connected to a Tripletex Order that is synchronized into Business.

Once a link between a Tripletex Contact and a Business Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Business Customers company:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Business Customers company Property
     - Business Data Type


Tripletex Contact to Business Customers person
----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a Business Customers person must be established.

A new Business Customers person will be created from a Tripletex Contact if it is connected to a Tripletex Order that is synchronized into Business.

Once a link between a Tripletex Contact and a Business Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Business Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Business Customers person Property
     - Business Data Type
   * - email
     - email
     - "string"
   * - email
     - id (Dependant on having wd:Q1273217 in type)
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Customer to Business Customers person
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Business Customers person must be established.

A new Business Customers person will be created from a Tripletex Customer if it is connected to a Tripletex Order that is synchronized into Business.

Once a link between a Tripletex Customer and a Business Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Business Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Business Customers person Property
     - Business Data Type


Tripletex Customer to Businesscentral Companies
-----------------------------------------------
Every Tripletex Customer will be synchronized with a Businesscentral Companies.

Once a link between a Tripletex Customer and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Tripletex Department to Businesscentral Companies
-------------------------------------------------
Every Tripletex Department will be synchronized with a Businesscentral Companies.

Once a link between a Tripletex Department and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Tripletex Contact to Business Contacts person
---------------------------------------------
Every Tripletex Contact will be synchronized with a Business Contacts person.

Once a link between a Tripletex Contact and a Business Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Business Contacts person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Business Contacts person Property
     - Business Data Type
   * - email
     - email
     - "string"
   * - phoneNumberMobile
     - mobilePhoneNumber
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Customer to Business Customers company
------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Business Customers company.

Once a link between a Tripletex Customer and a Business Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Business Customers company:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Business Customers company Property
     - Business Data Type
   * - deliveryAddress.addressLine1
     - addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - addressLine2
     - "string"
   * - deliveryAddress.city
     - address.city
     - "string"
   * - deliveryAddress.city
     - city
     - "string"
   * - deliveryAddress.country.id
     - address.countryLetterCode
     - "string"
   * - deliveryAddress.country.id
     - country
     - "string"
   * - deliveryAddress.postalCode
     - address.postalCode
     - "string"
   * - deliveryAddress.postalCode
     - postalCode
     - "string"
   * - email
     - id (Dependant on having wd:Q1273217 in type)
     - "string"
   * - id
     - id
     - "string"
   * - isPrivateIndividual
     - type
     - "string"
   * - name
     - displayName
     - "string"
   * - organizationNumber
     - id (Dependant on having NO in typeDependant on having wd:Q11994066 in type)
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - addressLine2
     - "string"
   * - physicalAddress.city
     - address.city
     - "string"
   * - physicalAddress.city
     - city
     - "string"
   * - physicalAddress.country.id
     - address.countryLetterCode
     - "string"
   * - physicalAddress.country.id
     - country
     - "string"
   * - physicalAddress.postalCode
     - address.postalCode
     - "string"
   * - physicalAddress.postalCode
     - postalCode
     - "string"
   * - postalAddress.addressLine1
     - addressLine1
     - "string"
   * - postalAddress.addressLine2
     - addressLine2
     - "string"
   * - postalAddress.city
     - address.city
     - "string"
   * - postalAddress.city
     - city
     - "string"
   * - postalAddress.country.id
     - address.countryLetterCode
     - "string"
   * - postalAddress.country.id
     - country
     - "string"
   * - postalAddress.postalCode
     - address.postalCode
     - "string"
   * - postalAddress.postalCode
     - postalCode
     - "string"
   * - website
     - website
     - "string"


Tripletex Customer person to Business Contacts person
-----------------------------------------------------
Every Tripletex Customer person will be synchronized with a Business Contacts person.

Once a link between a Tripletex Customer person and a Business Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Business Contacts person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Business Contacts person Property
     - Business Data Type
   * - deliveryAddress.addressLine1
     - addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - addressLine2
     - "string"
   * - deliveryAddress.city
     - city
     - "string"
   * - deliveryAddress.country.id
     - country
     - "string"
   * - deliveryAddress.postalCode
     - postalCode
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - isPrivateIndividual
     - type
     - "string"
   * - name
     - displayName
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - phoneNumberMobile
     - mobilePhoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - addressLine2
     - "string"
   * - physicalAddress.city
     - city
     - "string"
   * - physicalAddress.country.id
     - country
     - "string"
   * - physicalAddress.postalCode
     - postalCode
     - "string"
   * - postalAddress.addressLine1
     - addressLine1
     - "string"
   * - postalAddress.addressLine2
     - addressLine2
     - "string"
   * - postalAddress.city
     - city
     - "string"
   * - postalAddress.country.id
     - country
     - "string"
   * - postalAddress.postalCode
     - postalCode
     - "string"


Tripletex Customer person to Business Customers person
------------------------------------------------------
Every Tripletex Customer person will be synchronized with a Business Customers person.

Once a link between a Tripletex Customer person and a Business Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Business Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Business Customers person Property
     - Business Data Type
   * - deliveryAddress.addressLine1
     - addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - addressLine2
     - "string"
   * - deliveryAddress.city
     - city
     - "string"
   * - deliveryAddress.country.id
     - country
     - "string"
   * - deliveryAddress.postalCode
     - postalCode
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - isPrivateIndividual
     - type
     - "string"
   * - name
     - displayName
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - addressLine2
     - "string"
   * - physicalAddress.city
     - city
     - "string"
   * - physicalAddress.country.id
     - country
     - "string"
   * - physicalAddress.postalCode
     - postalCode
     - "string"
   * - postalAddress.addressLine1
     - addressLine1
     - "string"
   * - postalAddress.addressLine2
     - addressLine2
     - "string"
   * - postalAddress.city
     - city
     - "string"
   * - postalAddress.country.id
     - country
     - "string"
   * - postalAddress.postalCode
     - postalCode
     - "string"


Tripletex Employee to Business Employees
----------------------------------------
Every Tripletex Employee will be synchronized with a Business Employees.

Once a link between a Tripletex Employee and a Business Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Business Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Business Employees Property
     - Business Data Type
   * - address.addressLine1
     - addressLine1
     - "string"
   * - address.addressLine2
     - addressLine2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.id
     - country
     - "string"
   * - address.postalCode
     - postalCode
     - "string"
   * - dateOfBirth
     - birthDate
     - "string"
   * - email
     - email
     - "string"
   * - firstName
     - displayName
     - "string"
   * - firstName
     - givenName
     - "string"
   * - firstName
     - surname
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - displayName
     - "string"
   * - lastName
     - givenName
     - "string"
   * - lastName
     - surname
     - "string"
   * - phoneNumberMobile
     - mobilePhone
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Order to Business Salesorders
---------------------------------------
Every Tripletex Order will be synchronized with a Business Salesorders.

Once a link between a Tripletex Order and a Business Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Business Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Business Salesorders Property
     - Business Data Type
   * - contact.id
     - customerId
     - "string"
   * - currency.id
     - currencyId
     - "string"
   * - customer.id
     - customerId
     - "string"
   * - deliveryDate
     - requestedDeliveryDate
     - N/A
   * - orderDate
     - orderDate
     - N/A
   * - ourContactEmployee.id
     - salesperson
     - "string"


Tripletex Orderline to Business Salesorderlines
-----------------------------------------------
Every Tripletex Orderline will be synchronized with a Business Salesorderlines.

Once a link between a Tripletex Orderline and a Business Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Business Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Business Salesorderlines Property
     - Business Data Type
   * - count
     - description
     - "string"
   * - count
     - discountPercent
     - N/A
   * - count
     - invoiceQuantity
     - "string"
   * - count
     - quantity
     - N/A
   * - count
     - taxPercent
     - N/A
   * - count
     - unitPrice
     - "float"
   * - description
     - description
     - "string"
   * - description
     - discountPercent
     - N/A
   * - description
     - quantity
     - N/A
   * - description
     - taxPercent
     - N/A
   * - description
     - unitPrice
     - "float"
   * - discount
     - description
     - "string"
   * - discount
     - discountPercent
     - N/A
   * - discount
     - quantity
     - N/A
   * - discount
     - taxPercent
     - N/A
   * - discount
     - unitPrice
     - "float"
   * - order.id
     - documentId
     - "string"
   * - product.id
     - itemId
     - "string"
   * - unitCostCurrency
     - description
     - "string"
   * - unitCostCurrency
     - discountPercent
     - N/A
   * - unitCostCurrency
     - quantity
     - N/A
   * - unitCostCurrency
     - taxPercent
     - N/A
   * - unitCostCurrency
     - unitPrice
     - "float"
   * - unitPriceExcludingVatCurrency
     - amountExcludingTax
     - "string"
   * - unitPriceExcludingVatCurrency
     - description
     - "string"
   * - unitPriceExcludingVatCurrency
     - discountPercent
     - N/A
   * - unitPriceExcludingVatCurrency
     - quantity
     - N/A
   * - unitPriceExcludingVatCurrency
     - taxPercent
     - N/A
   * - unitPriceExcludingVatCurrency
     - unitPrice
     - "float"
   * - vatType.id
     - description
     - "string"
   * - vatType.id
     - discountPercent
     - N/A
   * - vatType.id
     - quantity
     - N/A
   * - vatType.id
     - taxPercent
     - N/A
   * - vatType.id
     - unitPrice
     - "float"


Tripletex Product to Business Items
-----------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Business Items.

If a matching Business Items already exists, the Tripletex Product will be merged with the existing one.
If no matching Business Items is found, a new Business Items will be created.

A Tripletex Product will merge with a Business Items if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Business Items Property
   * - ean
     - gtin

Once a link between a Tripletex Product and a Business Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Business Items:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Business Items Property
     - Business Data Type
   * - costExcludingVatCurrency
     - unitCost
     - N/A
   * - ean
     - gtin
     - "string"
   * - name
     - displayName
     - "string"
   * - name
     - displayName.string
     - "string"
   * - name
     - displayName2
     - "string"
   * - priceExcludingVatCurrency
     - unitPrice
     - N/A
   * - vatType.id
     - taxGroupCode
     - "string"

