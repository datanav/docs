===================================
Powerofficego to Chargebee Dataflow
===================================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to Chargebee Customer
-------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Chargebee Customer.

Once a link between a Powerofficego Contactperson and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - emailAddress
     - email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"


Powerofficego Customers to Chargebee Customer
---------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Chargebee Customer must be established.

A new Chargebee Customer will be created from a Powerofficego Customers if it is connected to a Powerofficego Salesorders, or Salesorderlines that is synchronized into Chargebee.

Once a link between a Powerofficego Customers and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Chargebee Customer Property
     - Chargebee Data Type


Powerofficego Customers to Chargebee Business_entity
----------------------------------------------------
Every Powerofficego Customers will be synchronized with a Chargebee Business_entity.

Once a link between a Powerofficego Customers and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - Name
     - name
     - "string"


Powerofficego Departments to Chargebee Business_entity
------------------------------------------------------
Every Powerofficego Departments will be synchronized with a Chargebee Business_entity.

Once a link between a Powerofficego Departments and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - Name
     - name
     - "string"


Powerofficego Employees to Chargebee Customer
---------------------------------------------
Every Powerofficego Employees will be synchronized with a Chargebee Customer.

Once a link between a Powerofficego Employees and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - LastName
     - last_name
     - "string"


Powerofficego Salesorderlines to Chargebee Order
------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Chargebee Order.

Once a link between a Powerofficego Salesorderlines and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - ProductUnitPrice
     - order_line_items.unit_price
     - "string"
   * - Quantity
     - order_line_items.amount
     - "string"
   * - VatRate
     - order_line_items.tax_amount
     - "string"


Powerofficego Customers person to Chargebee Customer
----------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Chargebee Customer.

Once a link between a Powerofficego Customers person and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - LastName
     - last_name
     - "string"


Powerofficego Product to Chargebee Item
---------------------------------------
Every Powerofficego Product will be synchronized with a Chargebee Item.

Once a link between a Powerofficego Product and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Chargebee Item Property
     - Chargebee Data Type
   * - name
     - name
     - "string"


Powerofficego Salesorders to Chargebee Order
--------------------------------------------
Every Powerofficego Salesorders will be synchronized with a Chargebee Order.

Once a link between a Powerofficego Salesorders and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - CurrencyCode
     - currency_code
     - "string"
   * - CustomerId
     - customer_id
     - "string"
   * - CustomerReferenceContactPersonId
     - customer_id
     - "string"

