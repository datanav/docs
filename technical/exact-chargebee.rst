===========================
Exact to Chargebee Dataflow
===========================

Generated: 2024-09-03 08:55:46

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to  Business_entity
----------------------------------
Every Exact Accounts will be synchronized with a  Business_entity.

Once a link between a Exact Accounts and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     -  Business_entity Property
     -  Data Type
   * - Name
     - name
     - "string"


Exact Addresses to  Address
---------------------------
Every Exact Addresses will be synchronized with a  Address.

Once a link between a Exact Addresses and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Addresses and a  Address:

.. list-table::
   :header-rows: 1

   * - Exact Addresses Property
     -  Address Property
     -  Data Type
   * - City
     - city
     - "string"
   * - Country
     - country
     - "string"
   * - CountryName
     - country
     - "string"


Exact Contacts to  Customer
---------------------------
Every Exact Contacts will be synchronized with a  Customer.

Once a link between a Exact Contacts and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a  Customer:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     -  Customer Property
     -  Data Type


Exact Currencies to  Currency
-----------------------------
Every Exact Currencies will be synchronized with a  Currency.

Once a link between a Exact Currencies and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a  Currency:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     -  Currency Property
     -  Data Type


Exact Departments to  Business_entity
-------------------------------------
Every Exact Departments will be synchronized with a  Business_entity.

Once a link between a Exact Departments and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     -  Business_entity Property
     -  Data Type


Exact Divisions to  Business_entity
-----------------------------------
Every Exact Divisions will be synchronized with a  Business_entity.

Once a link between a Exact Divisions and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     -  Business_entity Property
     -  Data Type


Exact Employees to  Customer
----------------------------
Every Exact Employees will be synchronized with a  Customer.

Once a link between a Exact Employees and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a  Customer:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
     -  Customer Property
     -  Data Type


Exact Quotations to  Order
--------------------------
Every Exact Quotations will be synchronized with a  Order.

Once a link between a Exact Quotations and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Quotations and a  Order:

.. list-table::
   :header-rows: 1

   * - Exact Quotations Property
     -  Order Property
     -  Data Type
   * - Currency
     - currency_code
     - "string"


Exact Salesinvoices to  Order
-----------------------------
Every Exact Salesinvoices will be synchronized with a  Order.

Once a link between a Exact Salesinvoices and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesinvoices and a  Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesinvoices Property
     -  Order Property
     -  Data Type
   * - Currency
     - currency_code
     - "string"


Exact Salesorderlines to  Order
-------------------------------
Every Exact Salesorderlines will be synchronized with a  Order.

Once a link between a Exact Salesorderlines and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a  Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     -  Order Property
     -  Data Type


Exact Units to  Currency
------------------------
Every Exact Units will be synchronized with a  Currency.

Once a link between a Exact Units and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Units and a  Currency:

.. list-table::
   :header-rows: 1

   * - Exact Units Property
     -  Currency Property
     -  Data Type


Exact Vatcodes to  Currency
---------------------------
Every Exact Vatcodes will be synchronized with a  Currency.

Once a link between a Exact Vatcodes and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Vatcodes and a  Currency:

.. list-table::
   :header-rows: 1

   * - Exact Vatcodes Property
     -  Currency Property
     -  Data Type


Exact Items to  Item
--------------------
Every Exact Items will be synchronized with a  Item.

Once a link between a Exact Items and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a  Item:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     -  Item Property
     -  Data Type


Exact Salesorders to  Order
---------------------------
Every Exact Salesorders will be synchronized with a  Order.

Once a link between a Exact Salesorders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a  Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     -  Order Property
     -  Data Type
   * - Currency
     - currency_code
     - "string"

