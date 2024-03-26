==========================================
Wave Financial to Businesscentral Dataflow
==========================================

Generated: 2024-03-26 14:14:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to  Customers person
----------------------------------
Before any synchronization can take place, a link between a Wave Customer and a  Customers person must be established.

A new  Customers person will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into .

Once a link between a Wave Customer and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Customers person Property
     -  Data Type
   * - address.addressLine1
     - addressLine1
     - "string"
   * - address.addressLine2
     - addressLine2
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.city
     - addressLine2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.code
     - country
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - postalCode
     - "string"
   * - id
     - id
     - "string"
   * - shippingDetails.address.addressLine1
     - addressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - addressLine2
     - "string"
   * - shippingDetails.address.city
     - address.city
     - "string"
   * - shippingDetails.address.city
     - addressLine2
     - "string"
   * - shippingDetails.address.city
     - city
     - "string"
   * - shippingDetails.address.country.code
     - country
     - "string"
   * - shippingDetails.address.postalCode
     - address.postalCode
     - "string"
   * - shippingDetails.address.postalCode
     - postalCode
     - "string"


Wave Customer to  Companies
---------------------------
Every Wave Customer will be synchronized with a  Companies.

Once a link between a Wave Customer and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Companies:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Companies Property
     -  Data Type


Wave Customer to  Contacts person
---------------------------------
Every Wave Customer will be synchronized with a  Contacts person.

Once a link between a Wave Customer and a  Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Contacts person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Contacts person Property
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
   * - address.country.code
     - country
     - "string"
   * - address.postalCode
     - postalCode
     - "string"
   * - email
     - email
     - "string"
   * - firstName
     - displayName
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - displayName
     - "string"
   * - mobile
     - mobilePhoneNumber
     - "string"
   * - shippingDetails.address.addressLine1
     - addressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - addressLine2
     - "string"
   * - shippingDetails.address.city
     - city
     - "string"
   * - shippingDetails.address.country.code
     - country
     - "string"
   * - shippingDetails.address.postalCode
     - postalCode
     - "string"


Wave Customer to  Customers company
-----------------------------------
Every Wave Customer will be synchronized with a  Customers company.

Once a link between a Wave Customer and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Customers company Property
     -  Data Type
   * - address.addressLine1
     - addressLine1
     - "string"
   * - address.addressLine2
     - addressLine2
     - "string"
   * - address.city
     - address.city
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.code
     - address.countryLetterCode
     - "string"
   * - address.country.code
     - country
     - "string"
   * - address.postalCode
     - address.postalCode
     - "string"
   * - address.postalCode
     - postalCode
     - "string"
   * - id
     - id
     - "string"
   * - name
     - displayName
     - "string"
   * - phone
     - phoneNumber
     - "string"
   * - shippingDetails.address.addressLine1
     - addressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - addressLine2
     - "string"
   * - shippingDetails.address.city
     - address.city
     - "string"
   * - shippingDetails.address.city
     - city
     - "string"
   * - shippingDetails.address.country.code
     - address.countryLetterCode
     - "string"
   * - shippingDetails.address.country.code
     - country
     - "string"
   * - shippingDetails.address.postalCode
     - address.postalCode
     - "string"
   * - shippingDetails.address.postalCode
     - postalCode
     - "string"
   * - shippingDetails.phone
     - phoneNumber
     - "string"
   * - website
     - website
     - "string"


Wave Invoice to  Salesorderlines
--------------------------------
Every Wave Invoice will be synchronized with a  Salesorderlines.

Once a link between a Wave Invoice and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Salesorderlines Property
     -  Data Type
   * - id
     - documentId
     - "string"
   * - items.description
     - description
     - "string"
   * - items.description
     - discountPercent
     - "decimal"
   * - items.description
     - quantity
     - "integer", "decimal"]
   * - items.description
     - taxPercent
     - "decimal"
   * - items.description
     - unitPrice
     - "float"
   * - items.price
     - amountExcludingTax
     - "string"
   * - items.price
     - description
     - "string"
   * - items.price
     - discountPercent
     - "decimal"
   * - items.price
     - quantity
     - "integer", "decimal"]
   * - items.price
     - taxPercent
     - "decimal"
   * - items.price
     - unitPrice
     - "float"
   * - items.product.id
     - itemId
     - "string"
   * - items.quantity
     - description
     - "string"
   * - items.quantity
     - discountPercent
     - "decimal"
   * - items.quantity
     - invoiceQuantity
     - "string"
   * - items.quantity
     - quantity
     - "integer", "decimal"]
   * - items.quantity
     - taxPercent
     - "decimal"
   * - items.quantity
     - unitPrice
     - "float"


Wave Invoice to  Salesorders
----------------------------
Every Wave Invoice will be synchronized with a  Salesorders.

Once a link between a Wave Invoice and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Salesorders Property
     -  Data Type
   * - currency.code
     - currencyId
     - "string"
   * - customer.id
     - customerId
     - "string"
   * - total.value
     - totalAmountExcludingTax
     - "string"


Wave Product to  Items
----------------------
Every Wave Product will be synchronized with a  Items.

Once a link between a Wave Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Items:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Items Property
     -  Data Type
   * - name
     - displayName
     - "string"
   * - name
     - displayName.string
     - "string"
   * - name
     - displayName2
     - "string"
   * - unitPrice
     - unitPrice
     - "decimal"


Wave Vendor to  Contacts person
-------------------------------
Every Wave Vendor will be synchronized with a  Contacts person.

Once a link between a Wave Vendor and a  Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Contacts person:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Contacts person Property
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
   * - address.country.code
     - country
     - "string"
   * - address.postalCode
     - postalCode
     - "string"
   * - email
     - email
     - "string"
   * - firstName
     - displayName
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - displayName
     - "string"
   * - mobile
     - mobilePhoneNumber
     - "string"
   * - phone
     - phoneNumber
     - "string"

