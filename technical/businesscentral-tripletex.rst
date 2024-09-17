======================================
Business Central to Tripletex Dataflow
======================================

Generated: 2024-09-17 07:26:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Items to Tripletex Product
-------------------------------------------
Before any synchronization can take place, a link between a Business Central Items and a Tripletex Product must be established.

A new Tripletex Product will be created from a Business Central Items if it is connected to a Business Central Businesscentral-salesorderlines that is synchronized into Tripletex.

A Business Central Items will merge with a Tripletex Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Tripletex Product Property
   * - gtin
     - ean

Once a link between a Business Central Items and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Tripletex Product Property
     - Tripletex Data Type


Business Central Customers to Tripletex Contact
-----------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a Business Central Customers if it is connected to a Business Central Businesscentral-salesorders that is synchronized into Tripletex.

Once a link between a Business Central Customers and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Customers Property
     - Tripletex Contact Property
     - Tripletex Data Type


Business Central Customers to Tripletex Customer
------------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Business Central Customers if it is connected to a Business Central Businesscentral-customers, Businesscentral-salesorders, Businesscentral-contact-person, or Businesscentral-contacts-person that is synchronized into Tripletex.

Once a link between a Business Central Customers and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers Property
     - Tripletex Customer Property
     - Tripletex Data Type


Business Central Customers to Tripletex Customer person
-------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a Business Central Customers if it is connected to a Business Central Businesscentral-customers, Businesscentral-salesorders, Businesscentral-contact-person, or Businesscentral-contacts-person that is synchronized into Tripletex.

Once a link between a Business Central Customers and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers Property
     - Tripletex Customer person Property
     - Tripletex Data Type


Business Central Salesorders to Tripletex Order
-----------------------------------------------
Before any synchronization can take place, a link between a Business Central Salesorders and a Tripletex Order must be established.

A new Tripletex Order will be created from a Business Central Salesorders if it is connected to a Business Central Businesscentral-salesorderlines that is synchronized into Tripletex.

Once a link between a Business Central Salesorders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Tripletex Order Property
     - Tripletex Data Type


Business Central Contacts person to Tripletex Contact
-----------------------------------------------------
Every Business Central Contacts person will be synchronized with a Tripletex Contact.

Once a link between a Business Central Contacts person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Tripletex Contact Property
     - Tripletex Data Type


Business Central Contacts person to Tripletex Customer person
-------------------------------------------------------------
Every Business Central Contacts person will be synchronized with a Tripletex Customer person.

Once a link between a Business Central Contacts person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Tripletex Customer person Property
     - Tripletex Data Type


Business Central Customers company to Tripletex Customer
--------------------------------------------------------
Every Business Central Customers company will be synchronized with a Tripletex Customer.

Once a link between a Business Central Customers company and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Tripletex Customer Property
     - Tripletex Data Type


Business Central Customers company to Tripletex Customer person
---------------------------------------------------------------
Every Business Central Customers company will be synchronized with a Tripletex Customer person.

Once a link between a Business Central Customers company and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Tripletex Customer person Property
     - Tripletex Data Type


Business Central Customers person to Tripletex Customer
-------------------------------------------------------
Every Business Central Customers person will be synchronized with a Tripletex Customer.

Once a link between a Business Central Customers person and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Tripletex Customer Property
     - Tripletex Data Type


Business Central Customers person to Tripletex Customer person
--------------------------------------------------------------
Every Business Central Customers person will be synchronized with a Tripletex Customer person.

Once a link between a Business Central Customers person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Tripletex Customer person Property
     - Tripletex Data Type


Business Central Customers person to Tripletex Customer person
--------------------------------------------------------------
Every Business Central Customers person will be synchronized with a Tripletex Customer person.

Once a link between a Business Central Customers person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Tripletex Customer person Property
     - Tripletex Data Type


Business Central Employees to Tripletex Employee
------------------------------------------------
Every Business Central Employees will be synchronized with a Tripletex Employee.

Once a link between a Business Central Employees and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - Tripletex Employee Property
     - Tripletex Data Type


Business Central Items to Tripletex Product
-------------------------------------------
Every Business Central Items will be synchronized with a Tripletex Product.

Once a link between a Business Central Items and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Tripletex Product Property
     - Tripletex Data Type


Business Central Salesorderlines to Tripletex Orderline
-------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a Tripletex Orderline.

Once a link between a Business Central Salesorderlines and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - Tripletex Orderline Property
     - Tripletex Data Type


Business Central Salesorders to Tripletex Order
-----------------------------------------------
Every Business Central Salesorders will be synchronized with a Tripletex Order.

Once a link between a Business Central Salesorders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Tripletex Order Property
     - Tripletex Data Type

