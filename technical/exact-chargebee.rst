===========================
Exact to Chargebee Dataflow
===========================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Chargebee Business_entity
-------------------------------------------
Every Exact Accounts will be synchronized with a Chargebee Business_entity.

Once a link between a Exact Accounts and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - Name
     - name
     - "string"


Exact Addresses to Chargebee Address
------------------------------------
Every Exact Addresses will be synchronized with a Chargebee Address.

Once a link between a Exact Addresses and a Chargebee Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Addresses and a Chargebee Address:

.. list-table::
   :header-rows: 1

   * - Exact Addresses Property
     - Chargebee Address Property
     - Chargebee Data Type
   * - City
     - city
     - "string"
   * - Country
     - country
     - "string"
   * - CountryName
     - country
     - "string"


Exact Contacts to Chargebee Customer
------------------------------------
Every Exact Contacts will be synchronized with a Chargebee Customer.

Once a link between a Exact Contacts and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - Chargebee Customer Property
     - Chargebee Data Type


Exact Currencies to Chargebee Currency
--------------------------------------
Every Exact Currencies will be synchronized with a Chargebee Currency.

Once a link between a Exact Currencies and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     - Chargebee Currency Property
     - Chargebee Data Type


Exact Departments to Chargebee Business_entity
----------------------------------------------
Every Exact Departments will be synchronized with a Chargebee Business_entity.

Once a link between a Exact Departments and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Chargebee Business_entity Property
     - Chargebee Data Type


Exact Divisions to Chargebee Business_entity
--------------------------------------------
Every Exact Divisions will be synchronized with a Chargebee Business_entity.

Once a link between a Exact Divisions and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - Chargebee Business_entity Property
     - Chargebee Data Type


Exact Employees to Chargebee Customer
-------------------------------------
Every Exact Employees will be synchronized with a Chargebee Customer.

Once a link between a Exact Employees and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
     - Chargebee Customer Property
     - Chargebee Data Type


Exact Quotations to Chargebee Order
-----------------------------------
Every Exact Quotations will be synchronized with a Chargebee Order.

Once a link between a Exact Quotations and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Quotations and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Exact Quotations Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - Currency
     - currency_code
     - "string"


Exact Salesinvoices to Chargebee Order
--------------------------------------
Every Exact Salesinvoices will be synchronized with a Chargebee Order.

Once a link between a Exact Salesinvoices and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesinvoices and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesinvoices Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - Currency
     - currency_code
     - "string"


Exact Salesorderlines to Chargebee Order
----------------------------------------
Every Exact Salesorderlines will be synchronized with a Chargebee Order.

Once a link between a Exact Salesorderlines and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Chargebee Order Property
     - Chargebee Data Type


Exact Units to Chargebee Currency
---------------------------------
Every Exact Units will be synchronized with a Chargebee Currency.

Once a link between a Exact Units and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Units and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - Exact Units Property
     - Chargebee Currency Property
     - Chargebee Data Type


Exact Vatcodes to Chargebee Currency
------------------------------------
Every Exact Vatcodes will be synchronized with a Chargebee Currency.

Once a link between a Exact Vatcodes and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Vatcodes and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - Exact Vatcodes Property
     - Chargebee Currency Property
     - Chargebee Data Type


Exact Items to Chargebee Item
-----------------------------
Every Exact Items will be synchronized with a Chargebee Item.

Once a link between a Exact Items and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Chargebee Item Property
     - Chargebee Data Type


Exact Salesorders to Chargebee Order
------------------------------------
Every Exact Salesorders will be synchronized with a Chargebee Order.

Once a link between a Exact Salesorders and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - Currency
     - currency_code
     - "string"

