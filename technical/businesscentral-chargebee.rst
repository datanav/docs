=====================================
Businesscentral to Chargebee Dataflow
=====================================

Generated: 2024-09-08 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers to Chargebee Customer
-----------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a Chargebee Customer must be established.

A new Chargebee Customer will be created from a Businesscentral Customers if it is connected to a Businesscentral Salesorders, Salesquotes, or Salesorderlines that is synchronized into Chargebee.

Once a link between a Businesscentral Customers and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     - Chargebee Customer Property
     - Chargebee Data Type


Businesscentral Companies to Chargebee Business_entity
------------------------------------------------------
Every Businesscentral Companies will be synchronized with a Chargebee Business_entity.

Once a link between a Businesscentral Companies and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     - Chargebee Business_entity Property
     - Chargebee Data Type


Businesscentral Contacts person to Chargebee Customer
-----------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Chargebee Customer.

Once a link between a Businesscentral Contacts person and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - email
     - email
     - "string"


Businesscentral Employees to Chargebee Customer
-----------------------------------------------
Every Businesscentral Employees will be synchronized with a Chargebee Customer.

Once a link between a Businesscentral Employees and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - givenName
     - first_name
     - "string"
   * - personalEmail
     - email
     - "string"
   * - surname
     - last_name
     - "string"


Businesscentral Salesorderlines to Chargebee Order
--------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a Chargebee Order.

Once a link between a Businesscentral Salesorderlines and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - quantity
     - order_line_items.amount
     - "string"
   * - taxPercent
     - order_line_items.tax_amount
     - "string"
   * - unitPrice
     - order_line_items.unit_price
     - "string"


Businesscentral Salesquotes to Chargebee Order
----------------------------------------------
Every Businesscentral Salesquotes will be synchronized with a Chargebee Order.

Once a link between a Businesscentral Salesquotes and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesquotes and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesquotes Property
     - Chargebee Order Property
     - Chargebee Data Type


Businesscentral Customers company to Chargebee Business_entity
--------------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Chargebee Business_entity.

Once a link between a Businesscentral Customers company and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - displayName
     - name
     - "string"


Businesscentral Customers person to Chargebee Customer
------------------------------------------------------
Every Businesscentral Customers person will be synchronized with a Chargebee Customer.

Once a link between a Businesscentral Customers person and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - email
     - email
     - "string"


Businesscentral Items to Chargebee Item
---------------------------------------
Every Businesscentral Items will be synchronized with a Chargebee Item.

Once a link between a Businesscentral Items and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Chargebee Item Property
     - Chargebee Data Type
   * - displayName
     - name
     - "string"


Businesscentral Salesorders to Chargebee Order
----------------------------------------------
Every Businesscentral Salesorders will be synchronized with a Chargebee Order.

Once a link between a Businesscentral Salesorders and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - currencyId
     - currency_code
     - "string"
   * - customerId
     - customer_id
     - "string"

