===============================
Chargebee to Tripletex Dataflow
===============================

Generated: 2024-10-02 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Address to Tripletex Customer
---------------------------------------
Every Chargebee Address will be synchronized with a Tripletex Customer.

Once a link between a Chargebee Address and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - addr
     - deliveryAddress.addressLine1
     - "string"
   * - addr
     - physicalAddress.addressLine1
     - "string"
   * - addr
     - postalAddress.addressLine1
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
   * - subscription_id
     - id
     - "integer"
   * - zip
     - deliveryAddress.postalCode
     - "string"
   * - zip
     - physicalAddress.postalCode
     - "string"
   * - zip
     - postalAddress.postalCode
     - "string"


Chargebee Address to Tripletex Customer (human data)
----------------------------------------------------
Every Chargebee Address will be synchronized with a Tripletex Customer (human data).

Once a link between a Chargebee Address and a Tripletex Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Tripletex Customer (human data):

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Tripletex Customer (human data) Property
     - Tripletex Data Type
   * - addr
     - deliveryAddress.addressLine1
     - "string"
   * - addr
     - physicalAddress.addressLine1
     - "string"
   * - addr
     - postalAddress.addressLine1
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
   * - subscription_id
     - id
     - "integer"
   * - zip
     - deliveryAddress.postalCode
     - "string"
   * - zip
     - physicalAddress.postalCode
     - "string"
   * - zip
     - postalAddress.postalCode
     - "string"


Chargebee Customer to Tripletex Customer
----------------------------------------
Every Chargebee Customer will be synchronized with a Tripletex Customer.

Once a link between a Chargebee Customer and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Tripletex Customer Property
     - Tripletex Data Type


Chargebee Customer to Tripletex Customer (human data)
-----------------------------------------------------
Every Chargebee Customer will be synchronized with a Tripletex Customer (human data).

Once a link between a Chargebee Customer and a Tripletex Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Tripletex Customer (human data):

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Tripletex Customer (human data) Property
     - Tripletex Data Type
   * - email
     - email
     - "string"


Chargebee Item to Tripletex Product
-----------------------------------
Every Chargebee Item will be synchronized with a Tripletex Product.

Once a link between a Chargebee Item and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Tripletex Product Property
     - Tripletex Data Type


Chargebee Order to Tripletex Order
----------------------------------
Every Chargebee Order will be synchronized with a Tripletex Order.

Once a link between a Chargebee Order and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - currency_code
     - currency.id
     - "integer"
   * - customer_id
     - contact.id
     - "integer"
   * - customer_id
     - customer.id
     - "integer"

