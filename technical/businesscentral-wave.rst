=================================
Business Central to Wave Dataflow
=================================

Generated: 2024-10-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Customers (organisation data) to Wave Customer
---------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Wave Customer.

Once a link between a Business Central Customers (organisation data) and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Wave Customer Property
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


Business Central Customers (human data) to Wave Customer (human data)
---------------------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Wave Customer (human data).

Once a link between a Business Central Customers (human data) and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - Wave Customer (human data) Property
     - Wave Data Type


Business Central Customers (organisation data) to Wave Customer
---------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Wave Customer.

Once a link between a Business Central Customers (organisation data) and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Wave Customer Property
     - Wave Data Type
   * - email
     - email
     - "string"


Business Central Customers (human data) to Wave Customer (human data)
---------------------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Wave Customer (human data).

Once a link between a Business Central Customers (human data) and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - Wave Customer (human data) Property
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
   * - unitPrice
     - unitPrice
     - "string"


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

