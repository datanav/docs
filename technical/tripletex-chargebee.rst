======================
Tripletex to  Dataflow
======================

Generated: 2024-08-29 09:21:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to  Customer
------------------------------
Every Tripletex Contact will be synchronized with a  Customer.

Once a link between a Tripletex Contact and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Customer Property
     -  Data Type
   * - email
     - email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"


Tripletex Customer to  Customer
-------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a  Customer must be established.

A new  Customer will be created from a Tripletex Customer if it is connected to a Tripletex Order, or Orderline that is synchronized into .

Once a link between a Tripletex Customer and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Customer Property
     -  Data Type


Tripletex Customer to  Business_entity
--------------------------------------
Every Tripletex Customer will be synchronized with a  Business_entity.

Once a link between a Tripletex Customer and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Business_entity Property
     -  Data Type
   * - name
     - name
     - "string"


Tripletex Department to  Business_entity
----------------------------------------
Every Tripletex Department will be synchronized with a  Business_entity.

Once a link between a Tripletex Department and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Business_entity Property
     -  Data Type
   * - name
     - name
     - "string"


Tripletex Employee to  Customer
-------------------------------
Every Tripletex Employee will be synchronized with a  Customer.

Once a link between a Tripletex Employee and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Customer Property
     -  Data Type
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"


Tripletex Order to  Item
------------------------
Every Tripletex Order will be synchronized with a  Item.

Once a link between a Tripletex Order and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a  Item:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     -  Item Property
     -  Data Type


Tripletex Orderline to  Item
----------------------------
Every Tripletex Orderline will be synchronized with a  Item.

Once a link between a Tripletex Orderline and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a  Item:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     -  Item Property
     -  Data Type


Tripletex Orderline to  Order
-----------------------------
Every Tripletex Orderline will be synchronized with a  Order.

Once a link between a Tripletex Orderline and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a  Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     -  Order Property
     -  Data Type
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


Tripletex Customer person to  Customer
--------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a  Customer.

Once a link between a Tripletex Customer person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     -  Customer Property
     -  Data Type
   * - email
     - email
     - "string"


Tripletex Order to  Order
-------------------------
Every Tripletex Order will be synchronized with a  Order.

Once a link between a Tripletex Order and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a  Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     -  Order Property
     -  Data Type
   * - contact.id
     - customer_id
     - "string"
   * - currency.id
     - currency_code
     - "string"
   * - customer.id
     - customer_id
     - "string"


Tripletex Product to  Item
--------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Item.

Once a link between a Tripletex Product and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Item:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Item Property
     -  Data Type
   * - name
     - name
     - "string"


Tripletex Product to  Item_family
---------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Item_family.

Once a link between a Tripletex Product and a  Item_family is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Item_family:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Item_family Property
     -  Data Type

