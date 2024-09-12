====================================
PowerOffice GO to Chargebee Dataflow
====================================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to Chargebee Customer
--------------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a Chargebee Customer.

Once a link between a PowerOffice GO Contactperson and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
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


PowerOffice GO Customers to Chargebee Customer
----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers and a Chargebee Customer must be established.

A new Chargebee Customer will be created from a PowerOffice GO Customers if it is connected to a PowerOffice GO Powerofficego-salesorders, or Powerofficego-salesorderlines that is synchronized into Chargebee.

Once a link between a PowerOffice GO Customers and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Chargebee Customer Property
     - Chargebee Data Type


PowerOffice GO Customers to Chargebee Business_entity
-----------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Chargebee Business_entity.

Once a link between a PowerOffice GO Customers and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - Name
     - name
     - "string"


PowerOffice GO Departments to Chargebee Business_entity
-------------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a Chargebee Business_entity.

Once a link between a PowerOffice GO Departments and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - Name
     - name
     - "string"


PowerOffice GO Employees to Chargebee Customer
----------------------------------------------
Every PowerOffice GO Employees will be synchronized with a Chargebee Customer.

Once a link between a PowerOffice GO Employees and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
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


PowerOffice GO Salesorderlines to Chargebee Order
-------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a Chargebee Order.

Once a link between a PowerOffice GO Salesorderlines and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
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


PowerOffice GO Customers person to Chargebee Customer
-----------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a Chargebee Customer.

Once a link between a PowerOffice GO Customers person and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
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


PowerOffice GO Product to Chargebee Item
----------------------------------------
Every PowerOffice GO Product will be synchronized with a Chargebee Item.

Once a link between a PowerOffice GO Product and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - Chargebee Item Property
     - Chargebee Data Type
   * - name
     - name
     - "string"


PowerOffice GO Salesorders to Chargebee Order
---------------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a Chargebee Order.

Once a link between a PowerOffice GO Salesorders and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
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

