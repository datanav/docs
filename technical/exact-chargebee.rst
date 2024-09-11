==================================
Exact Online to Chargebee Dataflow
==================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Accounts to Chargebee Business_entity
-------------------------------------------------
Every ExactOnline Accounts will be synchronized with a Chargebee Business_entity.

Once a link between a ExactOnline Accounts and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Accounts and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - ExactOnline Accounts Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - Name
     - name
     - "string"


ExactOnline Addresses to Chargebee Address
------------------------------------------
Every ExactOnline Addresses will be synchronized with a Chargebee Address.

Once a link between a ExactOnline Addresses and a Chargebee Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Addresses and a Chargebee Address:

.. list-table::
   :header-rows: 1

   * - ExactOnline Addresses Property
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


ExactOnline Contacts to Chargebee Customer
------------------------------------------
Every ExactOnline Contacts will be synchronized with a Chargebee Customer.

Once a link between a ExactOnline Contacts and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Contacts and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - ExactOnline Contacts Property
     - Chargebee Customer Property
     - Chargebee Data Type


ExactOnline Currencies to Chargebee Currency
--------------------------------------------
Every ExactOnline Currencies will be synchronized with a Chargebee Currency.

Once a link between a ExactOnline Currencies and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Currencies and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - ExactOnline Currencies Property
     - Chargebee Currency Property
     - Chargebee Data Type


ExactOnline Departments to Chargebee Business_entity
----------------------------------------------------
Every ExactOnline Departments will be synchronized with a Chargebee Business_entity.

Once a link between a ExactOnline Departments and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Departments and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - Chargebee Business_entity Property
     - Chargebee Data Type


ExactOnline Divisions to Chargebee Business_entity
--------------------------------------------------
Every ExactOnline Divisions will be synchronized with a Chargebee Business_entity.

Once a link between a ExactOnline Divisions and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Divisions and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - ExactOnline Divisions Property
     - Chargebee Business_entity Property
     - Chargebee Data Type


ExactOnline Employees to Chargebee Customer
-------------------------------------------
Every ExactOnline Employees will be synchronized with a Chargebee Customer.

Once a link between a ExactOnline Employees and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Employees and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - ExactOnline Employees Property
     - Chargebee Customer Property
     - Chargebee Data Type


ExactOnline Quotations to Chargebee Order
-----------------------------------------
Every ExactOnline Quotations will be synchronized with a Chargebee Order.

Once a link between a ExactOnline Quotations and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Quotations and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - ExactOnline Quotations Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - Currency
     - currency_code
     - "string"


ExactOnline Salesinvoices to Chargebee Order
--------------------------------------------
Every ExactOnline Salesinvoices will be synchronized with a Chargebee Order.

Once a link between a ExactOnline Salesinvoices and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesinvoices and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesinvoices Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - Currency
     - currency_code
     - "string"


ExactOnline Salesorderlines to Chargebee Order
----------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a Chargebee Order.

Once a link between a ExactOnline Salesorderlines and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - Chargebee Order Property
     - Chargebee Data Type


ExactOnline Units to Chargebee Currency
---------------------------------------
Every ExactOnline Units will be synchronized with a Chargebee Currency.

Once a link between a ExactOnline Units and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Units and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - ExactOnline Units Property
     - Chargebee Currency Property
     - Chargebee Data Type


ExactOnline Vatcodes to Chargebee Currency
------------------------------------------
Every ExactOnline Vatcodes will be synchronized with a Chargebee Currency.

Once a link between a ExactOnline Vatcodes and a Chargebee Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Vatcodes and a Chargebee Currency:

.. list-table::
   :header-rows: 1

   * - ExactOnline Vatcodes Property
     - Chargebee Currency Property
     - Chargebee Data Type


ExactOnline Items to Chargebee Item
-----------------------------------
Every ExactOnline Items will be synchronized with a Chargebee Item.

Once a link between a ExactOnline Items and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Items and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - ExactOnline Items Property
     - Chargebee Item Property
     - Chargebee Data Type


ExactOnline Salesorders to Chargebee Order
------------------------------------------
Every ExactOnline Salesorders will be synchronized with a Chargebee Order.

Once a link between a ExactOnline Salesorders and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorders and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorders Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - Currency
     - currency_code
     - "string"

