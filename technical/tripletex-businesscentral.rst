======================
Tripletex to  Dataflow
======================

Generated: 2024-03-26 13:42:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to  Customers company
---------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a  Customers company must be established.

A new  Customers company will be created from a Tripletex Contact if it is connected to a Tripletex Order that is synchronized into .

Once a link between a Tripletex Contact and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Customers company Property
     -  Data Type


Tripletex Contact to  Customers person
--------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a  Customers person must be established.

A new  Customers person will be created from a Tripletex Contact if it is connected to a Tripletex Order that is synchronized into .

Once a link between a Tripletex Contact and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Customers person Property
     -  Data Type
   * - email
     - email
     - "string"
   * - email
     - id (Dependant on having wd:Q1273217 in type)
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Customer to  Customers person
---------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a  Customers person must be established.

A new  Customers person will be created from a Tripletex Customer if it is connected to a Tripletex Order that is synchronized into .

Once a link between a Tripletex Customer and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Customers person Property
     -  Data Type


Tripletex Customer to  Companies
--------------------------------
Every Tripletex Customer will be synchronized with a  Companies.

Once a link between a Tripletex Customer and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Companies Property
     -  Data Type


Tripletex Department to  Companies
----------------------------------
Every Tripletex Department will be synchronized with a  Companies.

Once a link between a Tripletex Department and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Companies Property
     -  Data Type


Tripletex Contact to  Contacts person
-------------------------------------
Every Tripletex Contact will be synchronized with a  Contacts person.

Once a link between a Tripletex Contact and a  Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Contacts person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Contacts person Property
     -  Data Type
   * - email
     - email
     - "string"
   * - phoneNumberMobile
     - mobilePhoneNumber
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Customer to  Customers company
----------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a  Customers company.

Once a link between a Tripletex Customer and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Customers company Property
     -  Data Type
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


Tripletex Customer person to  Contacts person
---------------------------------------------
Every Tripletex Customer person will be synchronized with a  Contacts person.

Once a link between a Tripletex Customer person and a  Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a  Contacts person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     -  Contacts person Property
     -  Data Type
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
   * - id
     - id
     - "string"
   * - isPrivateIndividual
     - type
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


Tripletex Customer person to  Customers person
----------------------------------------------
Every Tripletex Customer person will be synchronized with a  Customers person.

Once a link between a Tripletex Customer person and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     -  Customers person Property
     -  Data Type
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


Tripletex Employee to  Employees
--------------------------------
Every Tripletex Employee will be synchronized with a  Employees.

Once a link between a Tripletex Employee and a  Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Employees Property
     -  Data Type
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


Tripletex Order to  Salesorders
-------------------------------
Every Tripletex Order will be synchronized with a  Salesorders.

Once a link between a Tripletex Order and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     -  Salesorders Property
     -  Data Type
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
     - "datetime-parse", "%Y-%m-%dT%H:%M:%S.%fZ"
   * - orderDate
     - orderDate
     - "datetime-parse", "%Y-%m-%dT%H:%M:%S.%fZ"
   * - ourContactEmployee.id
     - salesperson
     - "string"


Tripletex Orderline to  Salesorderlines
---------------------------------------
Every Tripletex Orderline will be synchronized with a  Salesorderlines.

Once a link between a Tripletex Orderline and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     -  Salesorderlines Property
     -  Data Type
   * - count
     - description
     - "string"
   * - count
     - discountPercent
     - "decimal"
   * - count
     - invoiceQuantity
     - "string"
   * - count
     - quantity
     - "integer", "decimal"]
   * - count
     - taxPercent
     - "decimal"
   * - count
     - unitPrice
     - "float"
   * - description
     - description
     - "string"
   * - description
     - discountPercent
     - "decimal"
   * - description
     - quantity
     - "integer", "decimal"]
   * - description
     - taxPercent
     - "decimal"
   * - description
     - unitPrice
     - "float"
   * - discount
     - description
     - "string"
   * - discount
     - discountPercent
     - "decimal"
   * - discount
     - quantity
     - "integer", "decimal"]
   * - discount
     - taxPercent
     - "decimal"
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
     - "decimal"
   * - unitCostCurrency
     - quantity
     - "integer", "decimal"]
   * - unitCostCurrency
     - taxPercent
     - "decimal"
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
     - "decimal"
   * - unitPriceExcludingVatCurrency
     - quantity
     - "integer", "decimal"]
   * - unitPriceExcludingVatCurrency
     - taxPercent
     - "decimal"
   * - unitPriceExcludingVatCurrency
     - unitPrice
     - "float"
   * - vatType.id
     - description
     - "string"
   * - vatType.id
     - discountPercent
     - "decimal"
   * - vatType.id
     - quantity
     - "integer", "decimal"]
   * - vatType.id
     - taxPercent
     - "decimal"
   * - vatType.id
     - unitPrice
     - "float"


Tripletex Product to  Items
---------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Items.

If a matching  Items already exists, the Tripletex Product will be merged with the existing one.
If no matching  Items is found, a new  Items will be created.

A Tripletex Product will merge with a  Items if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Items Property
   * - ean
     - gtin

Once a link between a Tripletex Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Items:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Items Property
     -  Data Type
   * - costExcludingVatCurrency
     - unitCost
     - "decimal"
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
     - "decimal"
   * - vatType.id
     - taxGroupCode
     - "string"

