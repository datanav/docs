===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-08-29 08:00:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to  Customer
--------------------------
Before any synchronization can take place, a link between a Wave Customer and a  Customer must be established.

A new  Customer will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into .

Once a link between a Wave Customer and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Customer Property
     -  Data Type


Wave Customer to  Business_entity
---------------------------------
Every Wave Customer will be synchronized with a  Business_entity.

Once a link between a Wave Customer and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Business_entity Property
     -  Data Type
   * - name
     - name
     - "string"


Wave Customer person to  Customer
---------------------------------
Every Wave Customer person will be synchronized with a  Customer.

Once a link between a Wave Customer person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
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


Wave Invoice to  Order
----------------------
Every Wave Invoice will be synchronized with a  Order.

Once a link between a Wave Invoice and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Order Property
     -  Data Type
   * - currency.code
     - currency_code
     - "string"
   * - customer.id
     - customer_id
     - "string"
   * - items.description
     - order_line_items.description
     - "string"
   * - items.price
     - order_line_items.unit_price
     - "string"
   * - items.quantity
     - order_line_items.amount
     - "string"

