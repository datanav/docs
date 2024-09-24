======================================
Business Central to Chargebee Dataflow
======================================

Generated: 2024-09-24 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Companies to Chargebee Business_entity
-------------------------------------------------------
Every Business Central Companies will be synchronized with a Chargebee Business_entity.

Once a link between a Business Central Companies and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Companies and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Business Central Companies Property
     - Chargebee Business_entity Property
     - Chargebee Data Type


Business Central Contacts (human data) to Chargebee Customer
------------------------------------------------------------
Every Business Central Contacts (human data) will be synchronized with a Chargebee Customer.

Once a link between a Business Central Contacts (human data) and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts (human data) and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts (human data) Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - email
     - email
     - "string"


Business Central Customers (organisation data) to Chargebee Business_entity
---------------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Chargebee Business_entity.

Once a link between a Business Central Customers (organisation data) and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - displayName
     - name
     - "string"


Business Central Customers (human data) to Chargebee Customer
-------------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Chargebee Customer.

Once a link between a Business Central Customers (human data) and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - Chargebee Customer Property
     - Chargebee Data Type


Business Central Employees to Chargebee Customer
------------------------------------------------
Every Business Central Employees will be synchronized with a Chargebee Customer.

Once a link between a Business Central Employees and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
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


Business Central Items to Chargebee Item
----------------------------------------
Every Business Central Items will be synchronized with a Chargebee Item.

Once a link between a Business Central Items and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Chargebee Item Property
     - Chargebee Data Type


Business Central Salesorderlines to Chargebee Order
---------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a Chargebee Order.

Once a link between a Business Central Salesorderlines and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
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


Business Central Salesorders to Chargebee Order
-----------------------------------------------
Every Business Central Salesorders will be synchronized with a Chargebee Order.

Once a link between a Business Central Salesorders and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - currencyId
     - currency_code
     - "string"
   * - customerId
     - customer_id
     - "string"


Business Central Salesquotes to Chargebee Order
-----------------------------------------------
Every Business Central Salesquotes will be synchronized with a Chargebee Order.

Once a link between a Business Central Salesquotes and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesquotes and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - Chargebee Order Property
     - Chargebee Data Type


Business Central Customers (location data) to Chargebee Address
---------------------------------------------------------------
Every Business Central Customers (location data) will be synchronized with a Chargebee Address.

Once a link between a Business Central Customers (location data) and a Chargebee Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (location data) and a Chargebee Address:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (location data) Property
     - Chargebee Address Property
     - Chargebee Data Type


Business Central Customers (organisation data) to Chargebee Business_entity
---------------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Chargebee Business_entity.

Once a link between a Business Central Customers (organisation data) and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Chargebee Business_entity Property
     - Chargebee Data Type


Business Central Customers (human data) to Chargebee Customer
-------------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Chargebee Customer.

Once a link between a Business Central Customers (human data) and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - Chargebee Customer Property
     - Chargebee Data Type


Business Central Customers (location data) to Chargebee Address
---------------------------------------------------------------
Every Business Central Customers (location data) will be synchronized with a Chargebee Address.

Once a link between a Business Central Customers (location data) and a Chargebee Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (location data) and a Chargebee Address:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (location data) Property
     - Chargebee Address Property
     - Chargebee Data Type


Business Central Customers (human data) to Chargebee Customer
-------------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a Chargebee Customer.

Once a link between a Business Central Customers (human data) and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - email
     - email
     - "string"


Business Central Items to Chargebee Item
----------------------------------------
Every Business Central Items will be synchronized with a Chargebee Item.

Once a link between a Business Central Items and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Chargebee Item Property
     - Chargebee Data Type


Business Central Salesorders to Chargebee Order
-----------------------------------------------
Every Business Central Salesorders will be synchronized with a Chargebee Order.

Once a link between a Business Central Salesorders and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Chargebee Order Property
     - Chargebee Data Type

