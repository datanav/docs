============================
Businesscentral to  Dataflow
============================

Generated: 2024-08-29 09:15:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers to  Customer
--------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a  Customer must be established.

A new  Customer will be created from a Businesscentral Customers if it is connected to a Businesscentral Salesorders, Salesquotes, or Salesorderlines that is synchronized into .

Once a link between a Businesscentral Customers and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     -  Customer Property
     -  Data Type


Businesscentral Companies to  Business_entity
---------------------------------------------
Every Businesscentral Companies will be synchronized with a  Business_entity.

Once a link between a Businesscentral Companies and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     -  Business_entity Property
     -  Data Type


Businesscentral Contacts person to  Customer
--------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Customer.

Once a link between a Businesscentral Contacts person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Customer Property
     -  Data Type
   * - email
     - email
     - "string"


Businesscentral Employees to  Customer
--------------------------------------
Every Businesscentral Employees will be synchronized with a  Customer.

Once a link between a Businesscentral Employees and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     -  Customer Property
     -  Data Type
   * - givenName
     - first_name
     - "string"
   * - personalEmail
     - email
     - "string"
   * - surname
     - last_name
     - "string"


Businesscentral Salesorderlines to  Order
-----------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Order.

Once a link between a Businesscentral Salesorderlines and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Order Property
     -  Data Type
   * - quantity
     - order_line_items.amount
     - "string"
   * - taxPercent
     - order_line_items.tax_amount
     - "string"
   * - unitPrice
     - order_line_items.unit_price
     - "string"


Businesscentral Salesquotes to  Order
-------------------------------------
Every Businesscentral Salesquotes will be synchronized with a  Order.

Once a link between a Businesscentral Salesquotes and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesquotes and a  Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesquotes Property
     -  Order Property
     -  Data Type


Businesscentral Customers company to  Business_entity
-----------------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Business_entity.

Once a link between a Businesscentral Customers company and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Business_entity Property
     -  Data Type
   * - displayName
     - name
     - "string"


Businesscentral Customers person to  Customer
---------------------------------------------
Every Businesscentral Customers person will be synchronized with a  Customer.

Once a link between a Businesscentral Customers person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     -  Customer Property
     -  Data Type
   * - email
     - email
     - "string"


Businesscentral Items to  Item
------------------------------
Every Businesscentral Items will be synchronized with a  Item.

Once a link between a Businesscentral Items and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Item:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Item Property
     -  Data Type


Businesscentral Salesorders to  Order
-------------------------------------
Every Businesscentral Salesorders will be synchronized with a  Order.

Once a link between a Businesscentral Salesorders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a  Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     -  Order Property
     -  Data Type
   * - currencyId
     - currency_code
     - "string"
   * - customerId
     - customer_id
     - "string"

