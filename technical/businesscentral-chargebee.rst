=====================================
BusinessCentral to Chargebee Dataflow
=====================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessCentral Customers to Chargebee Customer
-----------------------------------------------
Before any synchronization can take place, a link between a BusinessCentral Customers and a Chargebee Customer must be established.

A new Chargebee Customer will be created from a BusinessCentral Customers if it is connected to a BusinessCentral Salesorders, Salesquotes, or Salesorderlines that is synchronized into Chargebee.

Once a link between a BusinessCentral Customers and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers Property
     - Chargebee Customer Property
     - Chargebee Data Type


Business Companies to Chargebee Business_entity
-----------------------------------------------
Every Business Companies will be synchronized with a Chargebee Business_entity.

Once a link between a Business Companies and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Companies and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Business Companies Property
     - Chargebee Business_entity Property
     - Chargebee Data Type


Business Contacts person to Chargebee Customer
----------------------------------------------
Every Business Contacts person will be synchronized with a Chargebee Customer.

Once a link between a Business Contacts person and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - email
     - email
     - "string"


Business Employees to Chargebee Customer
----------------------------------------
Every Business Employees will be synchronized with a Chargebee Customer.

Once a link between a Business Employees and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Employees and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Business Employees Property
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


Business Salesorderlines to Chargebee Order
-------------------------------------------
Every Business Salesorderlines will be synchronized with a Chargebee Order.

Once a link between a Business Salesorderlines and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorderlines and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Business Salesorderlines Property
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


Business Salesquotes to Chargebee Order
---------------------------------------
Every Business Salesquotes will be synchronized with a Chargebee Order.

Once a link between a Business Salesquotes and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesquotes and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Business Salesquotes Property
     - Chargebee Order Property
     - Chargebee Data Type


BusinessCentral Customers company to Chargebee Business_entity
--------------------------------------------------------------
Every BusinessCentral Customers company will be synchronized with a Chargebee Business_entity.

Once a link between a BusinessCentral Customers company and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers company and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers company Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - displayName
     - name
     - "string"


BusinessCentral Customers person to Chargebee Customer
------------------------------------------------------
Every BusinessCentral Customers person will be synchronized with a Chargebee Customer.

Once a link between a BusinessCentral Customers person and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers person and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers person Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - email
     - email
     - "string"


BusinessCentral Items to Chargebee Item
---------------------------------------
Every BusinessCentral Items will be synchronized with a Chargebee Item.

Once a link between a BusinessCentral Items and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Items and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
     - Chargebee Item Property
     - Chargebee Data Type
   * - displayName
     - name
     - "string"


BusinessCentral Salesorders to Chargebee Order
----------------------------------------------
Every BusinessCentral Salesorders will be synchronized with a Chargebee Order.

Once a link between a BusinessCentral Salesorders and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorders and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorders Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - currencyId
     - currency_code
     - "string"
   * - customerId
     - customer_id
     - "string"

