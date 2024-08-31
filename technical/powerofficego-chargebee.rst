==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-08-31 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to  Customer
----------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Customer.

Once a link between a Powerofficego Contactperson and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Customer Property
     -  Data Type
   * - emailAddress
     - email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"


Powerofficego Customers to  Customer
------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a  Customer must be established.

A new  Customer will be created from a Powerofficego Customers if it is connected to a Powerofficego Salesorders, or Salesorderlines that is synchronized into .

Once a link between a Powerofficego Customers and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Customer Property
     -  Data Type


Powerofficego Customers to  Business_entity
-------------------------------------------
Every Powerofficego Customers will be synchronized with a  Business_entity.

Once a link between a Powerofficego Customers and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Business_entity Property
     -  Data Type
   * - Name
     - name
     - "string"


Powerofficego Departments to  Business_entity
---------------------------------------------
Every Powerofficego Departments will be synchronized with a  Business_entity.

Once a link between a Powerofficego Departments and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Business_entity Property
     -  Data Type
   * - Name
     - name
     - "string"


Powerofficego Employees to  Customer
------------------------------------
Every Powerofficego Employees will be synchronized with a  Customer.

Once a link between a Powerofficego Employees and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a  Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     -  Customer Property
     -  Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - LastName
     - last_name
     - "string"


Powerofficego Salesorderlines to  Order
---------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a  Order.

Once a link between a Powerofficego Salesorderlines and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a  Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     -  Order Property
     -  Data Type
   * - ProductUnitPrice
     - order_line_items.unit_price
     - "string"
   * - Quantity
     - order_line_items.amount
     - "string"
   * - VatRate
     - order_line_items.tax_amount
     - "string"


Powerofficego Customers person to  Customer
-------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Customer.

Once a link between a Powerofficego Customers person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Customer Property
     -  Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - LastName
     - last_name
     - "string"


Powerofficego Product to  Item
------------------------------
Every Powerofficego Product will be synchronized with a  Item.

Once a link between a Powerofficego Product and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a  Item:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     -  Item Property
     -  Data Type
   * - name
     - name
     - "string"


Powerofficego Salesorders to  Order
-----------------------------------
Every Powerofficego Salesorders will be synchronized with a  Order.

Once a link between a Powerofficego Salesorders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a  Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     -  Order Property
     -  Data Type
   * - CurrencyCode
     - currency_code
     - "string"
   * - CustomerId
     - customer_id
     - "string"
   * - CustomerReferenceContactPersonId
     - customer_id
     - "string"

