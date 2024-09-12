=================================
Business Central to Wave Dataflow
=================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Contacts person to Wave Country
------------------------------------------------
Before any synchronization can take place, a link between a Business Central Contacts person and a Wave Country must be established.

A Business Central Contacts person will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Wave Country Property
   * - country
     - code

Once a link between a Business Central Contacts person and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Wave Country Property
     - Wave Data Type


Business Central Customers company to Wave Country
--------------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers company and a Wave Country must be established.

A Business Central Customers company will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Wave Country Property
   * - country
     - code

Once a link between a Business Central Customers company and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Wave Country Property
     - Wave Data Type


Business Central Customers person to Wave Country
-------------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers person and a Wave Country must be established.

A Business Central Customers person will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Wave Country Property
   * - country
     - code

Once a link between a Business Central Customers person and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Wave Country Property
     - Wave Data Type


Business Central Employees to Wave Country
------------------------------------------
Before any synchronization can take place, a link between a Business Central Employees and a Wave Country must be established.

A Business Central Employees will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - Wave Country Property
   * - country
     - code

Once a link between a Business Central Employees and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - Wave Country Property
     - Wave Data Type


Businesscentral Customers to Wave Customer
------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a Wave Customer must be established.

A new Wave Customer will be created from a Businesscentral Customers if it is connected to a Businesscentral Customers, Salesorders, or Customers-company that is synchronized into Wave.

Once a link between a Businesscentral Customers and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     - Wave Customer Property
     - Wave Data Type


Businesscentral Customers to Wave Customer person
-------------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a Wave Customer person must be established.

A new Wave Customer person will be created from a Businesscentral Customers if it is connected to a Businesscentral Customers, Salesorders, or Customers-company that is synchronized into Wave.

Once a link between a Businesscentral Customers and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     - Wave Customer person Property
     - Wave Data Type


Business Central Currencies to Wave Currency
--------------------------------------------
Every Business Central Currencies will be synchronized with a Wave Currency.

If a matching Wave Currency already exists, the Business Central Currencies will be merged with the existing one.
If no matching Wave Currency is found, a new Wave Currency will be created.

A Business Central Currencies will merge with a Wave Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - Wave Currency Property
   * - code
     - code

Once a link between a Business Central Currencies and a Wave Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Currencies and a Wave Currency:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - Wave Currency Property
     - Wave Data Type


Business Central Customers company to Wave Customer
---------------------------------------------------
Every Business Central Customers company will be synchronized with a Wave Customer.

Once a link between a Business Central Customers company and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Wave Customer Property
     - Wave Data Type
   * - address.city
     - address.city
     - "string"
   * - address.city
     - shippingDetails.address.city
     - "string"
   * - address.countryLetterCode
     - address.country.code
     - "string"
   * - address.countryLetterCode
     - shippingDetails.address.country.code
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - shippingDetails.address.postalCode
     - "string"
   * - addressLine1
     - address.addressLine1
     - "string"
   * - addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - addressLine2
     - address.addressLine2
     - "string"
   * - addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - city
     - address.city
     - "string"
   * - city
     - shippingDetails.address.city
     - "string"
   * - country
     - address.country.code
     - "string"
   * - country
     - shippingDetails.address.country.code
     - "string"
   * - displayName
     - name
     - N/A
   * - phoneNumber
     - phone
     - "string"
   * - postalCode
     - address.postalCode
     - "string"
   * - postalCode
     - shippingDetails.address.postalCode
     - "string"
   * - website
     - website
     - "string"


Business Central Customers person to Wave Customer person
---------------------------------------------------------
Every Business Central Customers person will be synchronized with a Wave Customer person.

Once a link between a Business Central Customers person and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Wave Customer person Property
     - Wave Data Type
   * - addressLine1
     - address.addressLine1
     - "string"
   * - addressLine1
     - shippingDetails.address.addressLine1
     - "string"
   * - addressLine2
     - address.addressLine2
     - "string"
   * - addressLine2
     - shippingDetails.address.addressLine2
     - "string"
   * - city
     - address.city
     - "string"
   * - city
     - shippingDetails.address.city
     - "string"
   * - country
     - address.country.code
     - "string"
   * - country
     - shippingDetails.address.country.code
     - "string"
   * - displayName
     - name
     - N/A
   * - email
     - email
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - postalCode
     - address.postalCode
     - "string"
   * - postalCode
     - shippingDetails.address.postalCode
     - "string"


Business Central Items to Wave Product
--------------------------------------
Every Business Central Items will be synchronized with a Wave Product.

Once a link between a Business Central Items and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Wave Product Property
     - Wave Data Type
   * - displayName
     - name
     - "string"
   * - displayName.string
     - name
     - "string"
   * - displayName2
     - name
     - "string"
   * - unitPrice
     - unitPrice
     - "string"


Business Central Salesorders to Wave Country
--------------------------------------------
Every Business Central Salesorders will be synchronized with a Wave Country.

If a matching Wave Country already exists, the Business Central Salesorders will be merged with the existing one.
If no matching Wave Country is found, a new Wave Country will be created.

A Business Central Salesorders will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Wave Country Property
   * - billToCountry
     - code
   * - shipToCountry
     - code

Once a link between a Business Central Salesorders and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Wave Country Property
     - Wave Data Type


Business Central Salesorders to Wave Invoice
--------------------------------------------
Every Business Central Salesorders will be synchronized with a Wave Invoice.

Once a link between a Business Central Salesorders and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Wave Invoice Property
     - Wave Data Type
   * - currencyId
     - currency.code
     - "string"
   * - customerId
     - customer.id
     - "string"


Business Central Salesquotes to Wave Country
--------------------------------------------
Every Business Central Salesquotes will be synchronized with a Wave Country.

If a matching Wave Country already exists, the Business Central Salesquotes will be merged with the existing one.
If no matching Wave Country is found, a new Wave Country will be created.

A Business Central Salesquotes will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - Wave Country Property
   * - billToCountry
     - name
   * - shipToCountry
     - name

Once a link between a Business Central Salesquotes and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesquotes and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - Wave Country Property
     - Wave Data Type

