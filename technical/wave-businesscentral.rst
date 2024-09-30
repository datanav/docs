=================================
Wave to Business Central Dataflow
=================================

Generated: 2024-09-30 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Business Central Companies
-------------------------------------------
Every Wave Customer will be synchronized with a Business Central Companies.

Once a link between a Wave Customer and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Central Companies Property
     - Business Central Data Type


Wave Customer to Business Central Contacts (human data)
-------------------------------------------------------
Every Wave Customer will be synchronized with a Business Central Contacts (human data).

Once a link between a Wave Customer and a Business Central Contacts (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Central Contacts (human data):

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Central Contacts (human data) Property
     - Business Central Data Type
   * - email
     - email
     - "string"
   * - mobile
     - mobilePhoneNumber
     - "string"


Wave Customer to Business Central Customers (organisation data)
---------------------------------------------------------------
Every Wave Customer will be synchronized with a Business Central Customers (organisation data).

Once a link between a Wave Customer and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type
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
   * - website
     - website
     - "string"


Wave Customer to Business Central Customers (human data)
--------------------------------------------------------
Every Wave Customer will be synchronized with a Business Central Customers (human data).

Once a link between a Wave Customer and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Central Customers (human data) Property
     - Business Central Data Type


Wave Customer (organisation data) to Business Central Customers (organisation data)
-----------------------------------------------------------------------------------
Every Wave Customer (organisation data) will be synchronized with a Business Central Customers (organisation data).

Once a link between a Wave Customer (organisation data) and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer (organisation data) and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Wave Customer (organisation data) Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type


Wave Customer (human data) to Business Central Customers (human data)
---------------------------------------------------------------------
Every Wave Customer (human data) will be synchronized with a Business Central Customers (human data).

Once a link between a Wave Customer (human data) and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer (human data) and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - Wave Customer (human data) Property
     - Business Central Customers (human data) Property
     - Business Central Data Type
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


Wave Invoice to Business Central Salesorderlines
------------------------------------------------
Every Wave Invoice will be synchronized with a Business Central Salesorderlines.

Once a link between a Wave Invoice and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
   * - id
     - documentId
     - "string"
   * - items.price
     - unitPrice
     - "float"
   * - items.product.id
     - itemId
     - "string"
   * - items.quantity
     - quantity
     - N/A


Wave Invoice to Business Central Salesorders
--------------------------------------------
Every Wave Invoice will be synchronized with a Business Central Salesorders.

Once a link between a Wave Invoice and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Business Central Salesorders Property
     - Business Central Data Type
   * - currency.code
     - currencyId
     - "string"
   * - customer.id
     - customerId
     - "string"


Wave Product to Business Central Items
--------------------------------------
Every Wave Product will be synchronized with a Business Central Items.

Once a link between a Wave Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Business Central Items Property
     - Business Central Data Type
   * - name
     - displayName
     - "string"
   * - unitPrice
     - unitPrice
     - N/A


Wave Vendor to Business Central Contacts (human data)
-----------------------------------------------------
Every Wave Vendor will be synchronized with a Business Central Contacts (human data).

Once a link between a Wave Vendor and a Business Central Contacts (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Business Central Contacts (human data):

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Business Central Contacts (human data) Property
     - Business Central Data Type
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
   * - mobile
     - mobilePhoneNumber
     - "string"
   * - phone
     - phoneNumber
     - "string"

