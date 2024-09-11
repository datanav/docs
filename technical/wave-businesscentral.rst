=================================
Wave to Business Central Dataflow
=================================

Generated: 2024-09-11 07:54:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Business Customers person
------------------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Business Customers person must be established.

A new Business Customers person will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into Business.

Once a link between a Wave Customer and a Business Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Customers person Property
     - Business Data Type
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


Wave Customer to Businesscentral Companies
------------------------------------------
Every Wave Customer will be synchronized with a Businesscentral Companies.

Once a link between a Wave Customer and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Wave Customer to Business Contacts person
-----------------------------------------
Every Wave Customer will be synchronized with a Business Contacts person.

Once a link between a Wave Customer and a Business Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Contacts person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Contacts person Property
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


Wave Customer to Business Customers company
-------------------------------------------
Every Wave Customer will be synchronized with a Business Customers company.

Once a link between a Wave Customer and a Business Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Customers company:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Customers company Property
     - Business Data Type
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


Wave Customer person to Business Customers person
-------------------------------------------------
Every Wave Customer person will be synchronized with a Business Customers person.

Once a link between a Wave Customer person and a Business Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Business Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Business Customers person Property
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
   * - address.country.code
     - country
     - "string"
   * - address.postalCode
     - postalCode
     - "string"
   * - email
     - email
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
     - city
     - "string"
   * - shippingDetails.address.country.code
     - country
     - "string"
   * - shippingDetails.address.postalCode
     - postalCode
     - "string"
   * - shippingDetails.phone
     - phoneNumber
     - "string"


Wave Invoice to Business Salesorderlines
----------------------------------------
Every Wave Invoice will be synchronized with a Business Salesorderlines.

Once a link between a Wave Invoice and a Business Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Business Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Business Salesorderlines Property
     - Business Data Type
   * - id
     - documentId
     - "string"
   * - items.description
     - description
     - "string"
   * - items.description
     - discountPercent
     - N/A
   * - items.description
     - quantity
     - N/A
   * - items.description
     - taxPercent
     - N/A
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
     - N/A
   * - items.price
     - quantity
     - N/A
   * - items.price
     - taxPercent
     - N/A
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
     - N/A
   * - items.quantity
     - invoiceQuantity
     - "string"
   * - items.quantity
     - quantity
     - N/A
   * - items.quantity
     - taxPercent
     - N/A
   * - items.quantity
     - unitPrice
     - "float"


Wave Invoice to Business Salesorders
------------------------------------
Every Wave Invoice will be synchronized with a Business Salesorders.

Once a link between a Wave Invoice and a Business Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Business Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Business Salesorders Property
     - Business Data Type
   * - currency.code
     - currencyId
     - "string"
   * - customer.id
     - customerId
     - "string"
   * - total.value
     - totalAmountExcludingTax
     - "string"


Wave Product to Business Items
------------------------------
Every Wave Product will be synchronized with a Business Items.

Once a link between a Wave Product and a Business Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Business Items:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Business Items Property
     - Business Data Type
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
     - N/A


Wave Vendor to Business Contacts person
---------------------------------------
Every Wave Vendor will be synchronized with a Business Contacts person.

Once a link between a Wave Vendor and a Business Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Business Contacts person:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Business Contacts person Property
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

