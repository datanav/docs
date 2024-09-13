===============================
Chargebee to Tripletex Dataflow
===============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to Tripletex Contact
---------------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into Tripletex.

Once a link between a Chargebee Customer and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - email
     - email
     - "string"
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"


Chargebee Customer to Tripletex Customer
----------------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into Tripletex.

Once a link between a Chargebee Customer and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Tripletex Customer Property
     - Tripletex Data Type


Chargebee Customer to Tripletex Customer person
-----------------------------------------------
Every Chargebee Customer will be synchronized with a Tripletex Customer person.

Once a link between a Chargebee Customer and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Tripletex Customer person Property
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

