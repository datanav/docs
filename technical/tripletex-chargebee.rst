===============================
Tripletex to Chargebee Dataflow
===============================

Generated: 2024-10-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Chargebee Customer
---------------------------------------
Every Tripletex Contact will be synchronized with a Chargebee Customer.

Once a link between a Tripletex Contact and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - email
     - email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"


Tripletex Customer to Chargebee Business_entity
-----------------------------------------------
Every Tripletex Customer will be synchronized with a Chargebee Business_entity.

Once a link between a Tripletex Customer and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - name
     - name
     - "string"


Tripletex Customer (human data) to Chargebee Customer
-----------------------------------------------------
Every Tripletex Customer (human data) will be synchronized with a Chargebee Customer.

Once a link between a Tripletex Customer (human data) and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (human data) and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (human data) Property
     - Chargebee Customer Property
     - Chargebee Data Type


Tripletex Department to Chargebee Business_entity
-------------------------------------------------
Every Tripletex Department will be synchronized with a Chargebee Business_entity.

Once a link between a Tripletex Department and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - name
     - name
     - "string"


Tripletex Employee to Chargebee Customer
----------------------------------------
Every Tripletex Employee will be synchronized with a Chargebee Customer.

Once a link between a Tripletex Employee and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"


Tripletex Order to Chargebee Order
----------------------------------
Every Tripletex Order will be synchronized with a Chargebee Order.

Once a link between a Tripletex Order and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - contact.id
     - customer_id
     - "string"
   * - currency.id
     - currency_code
     - "string"
   * - customer.id
     - customer_id
     - "string"


Tripletex Orderline to Chargebee Order
--------------------------------------
Every Tripletex Orderline will be synchronized with a Chargebee Order.

Once a link between a Tripletex Orderline and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - count
     - order_line_items.amount
     - "string"
   * - currency.id
     - currency_code
     - "string"
   * - description
     - order_line_items.description
     - "string"
   * - unitPriceExcludingVatCurrency
     - order_line_items.unit_price
     - "string"
   * - vatType.id
     - order_line_items.tax_amount
     - "string"


Tripletex Product to Chargebee Item
-----------------------------------
Every Tripletex Product will be synchronized with a Chargebee Item.

Once a link between a Tripletex Product and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Chargebee Item Property
     - Chargebee Data Type


Tripletex Customer to Chargebee Address
---------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Chargebee Address.

Once a link between a Tripletex Customer and a Chargebee Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Chargebee Address:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Chargebee Address Property
     - Chargebee Data Type


Tripletex Customer to Chargebee Customer
----------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Chargebee Customer.

Once a link between a Tripletex Customer and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Chargebee Customer Property
     - Chargebee Data Type


Tripletex Customer (location data) to Chargebee Address
-------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Chargebee Address.

Once a link between a Tripletex Customer (location data) and a Chargebee Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (location data) and a Chargebee Address:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (location data) Property
     - Chargebee Address Property
     - Chargebee Data Type


Tripletex Customer (human data) to Chargebee Customer
-----------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Chargebee Customer.

Once a link between a Tripletex Customer (human data) and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (human data) and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (human data) Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - email
     - email
     - "string"


Tripletex Order to Chargebee Order
----------------------------------
Every Tripletex Order will be synchronized with a Chargebee Order.

Once a link between a Tripletex Order and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Chargebee Order Property
     - Chargebee Data Type


Tripletex Product to Chargebee Item
-----------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Chargebee Item.

Once a link between a Tripletex Product and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Chargebee Item Property
     - Chargebee Data Type

