==========================
Chargebee to Wave Dataflow
==========================

Generated: 2024-09-29 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Address to Wave Customer
----------------------------------
Every Chargebee Address will be synchronized with a Wave Customer.

Once a link between a Chargebee Address and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Wave Customer Property
     - Wave Data Type
   * - addr
     - address.addressLine1
     - "string"
   * - addr
     - shippingDetails.address.addressLine1
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
   * - zip
     - address.postalCode
     - "string"
   * - zip
     - shippingDetails.address.postalCode
     - "string"


Chargebee Address to Wave Customer (human data)
-----------------------------------------------
Every Chargebee Address will be synchronized with a Wave Customer (human data).

Once a link between a Chargebee Address and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Wave Customer (human data) Property
     - Wave Data Type
   * - addr
     - address.addressLine1
     - "string"
   * - addr
     - shippingDetails.address.addressLine1
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
   * - zip
     - address.postalCode
     - "string"
   * - zip
     - shippingDetails.address.postalCode
     - "string"


Chargebee Customer to Wave Customer
-----------------------------------
Every Chargebee Customer will be synchronized with a Wave Customer.

Once a link between a Chargebee Customer and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Wave Customer Property
     - Wave Data Type
   * - email
     - email
     - "string"
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"


Chargebee Customer to Wave Customer (human data)
------------------------------------------------
Every Chargebee Customer will be synchronized with a Wave Customer (human data).

Once a link between a Chargebee Customer and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Wave Customer (human data) Property
     - Wave Data Type
   * - email
     - email
     - "string"
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - N/A


Chargebee Item to Wave Product
------------------------------
Every Chargebee Item will be synchronized with a Wave Product.

Once a link between a Chargebee Item and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Wave Product Property
     - Wave Data Type


Chargebee Order to Wave Invoice
-------------------------------
Every Chargebee Order will be synchronized with a Wave Invoice.

Once a link between a Chargebee Order and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Wave Invoice Property
     - Wave Data Type
   * - currency_code
     - currency.code
     - "string"
   * - customer_id
     - customer.id
     - "string"
   * - order_line_items.amount
     - items.quantity
     - N/A
   * - order_line_items.description
     - items.description
     - "string"
   * - order_line_items.unit_price
     - items.price
     - "string"

