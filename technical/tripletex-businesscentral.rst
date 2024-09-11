=====================================
Tripletex to BusinessCentral Dataflow
=====================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to BusinessCentral Customers company
------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a BusinessCentral Customers company must be established.

A new BusinessCentral Customers company will be created from a Tripletex Contact if it is connected to a Tripletex Order that is synchronized into BusinessCentral.

Once a link between a Tripletex Contact and a BusinessCentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a BusinessCentral Customers company:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - BusinessCentral Customers company Property
     - BusinessCentral Data Type


Tripletex Contact to BusinessCentral Customers person
-----------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a BusinessCentral Customers person must be established.

A new BusinessCentral Customers person will be created from a Tripletex Contact if it is connected to a Tripletex Order that is synchronized into BusinessCentral.

Once a link between a Tripletex Contact and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type
   * - email
     - email
     - "string"
   * - email
     - id (Dependant on having wd:Q1273217 in type)
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Customer to BusinessCentral Customers person
------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a BusinessCentral Customers person must be established.

A new BusinessCentral Customers person will be created from a Tripletex Customer if it is connected to a Tripletex Order that is synchronized into BusinessCentral.

Once a link between a Tripletex Customer and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type


Tripletex Customer to BusinessCentral Companies
-----------------------------------------------
Every Tripletex Customer will be synchronized with a BusinessCentral Companies.

Once a link between a Tripletex Customer and a BusinessCentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a BusinessCentral Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - BusinessCentral Companies Property
     - BusinessCentral Data Type


Tripletex Department to BusinessCentral Companies
-------------------------------------------------
Every Tripletex Department will be synchronized with a BusinessCentral Companies.

Once a link between a Tripletex Department and a BusinessCentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a BusinessCentral Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - BusinessCentral Companies Property
     - BusinessCentral Data Type


Tripletex Contact to BusinessCentral Contacts person
----------------------------------------------------
Every Tripletex Contact will be synchronized with a BusinessCentral Contacts person.

Once a link between a Tripletex Contact and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
   * - email
     - email
     - "string"
   * - phoneNumberMobile
     - mobilePhoneNumber
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Customer to BusinessCentral Customers company
-------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a BusinessCentral Customers company.

Once a link between a Tripletex Customer and a BusinessCentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a BusinessCentral Customers company:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - BusinessCentral Customers company Property
     - BusinessCentral Data Type
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


Tripletex Customer person to BusinessCentral Contacts person
------------------------------------------------------------
Every Tripletex Customer person will be synchronized with a BusinessCentral Contacts person.

Once a link between a Tripletex Customer person and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
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


Tripletex Customer person to BusinessCentral Customers person
-------------------------------------------------------------
Every Tripletex Customer person will be synchronized with a BusinessCentral Customers person.

Once a link between a Tripletex Customer person and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type
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


Tripletex Employee to BusinessCentral Employees
-----------------------------------------------
Every Tripletex Employee will be synchronized with a BusinessCentral Employees.

Once a link between a Tripletex Employee and a BusinessCentral Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a BusinessCentral Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - BusinessCentral Employees Property
     - BusinessCentral Data Type
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


Tripletex Order to BusinessCentral Salesorders
----------------------------------------------
Every Tripletex Order will be synchronized with a BusinessCentral Salesorders.

Once a link between a Tripletex Order and a BusinessCentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a BusinessCentral Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - BusinessCentral Salesorders Property
     - BusinessCentral Data Type
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


Tripletex Orderline to BusinessCentral Salesorderlines
------------------------------------------------------
Every Tripletex Orderline will be synchronized with a BusinessCentral Salesorderlines.

Once a link between a Tripletex Orderline and a BusinessCentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a BusinessCentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - BusinessCentral Salesorderlines Property
     - BusinessCentral Data Type
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


Tripletex Product to BusinessCentral Items
------------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a BusinessCentral Items.

If a matching BusinessCentral Items already exists, the Tripletex Product will be merged with the existing one.
If no matching BusinessCentral Items is found, a new BusinessCentral Items will be created.

A Tripletex Product will merge with a BusinessCentral Items if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - BusinessCentral Items Property
   * - ean
     - gtin

Once a link between a Tripletex Product and a BusinessCentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a BusinessCentral Items:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - BusinessCentral Items Property
     - BusinessCentral Data Type
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

