===========================
Exact to Tripletex Dataflow
===========================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Tripletex Customer
------------------------------------
Every Exact Accounts will be synchronized with a Tripletex Customer.

Once a link between a Exact Accounts and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"
   * - Website
     - website
     - "string"


Exact Contacts to Tripletex Contact
-----------------------------------
Every Exact Contacts will be synchronized with a Tripletex Contact.

Once a link between a Exact Contacts and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - Tripletex Contact Property
     - Tripletex Data Type


Exact Departments to Tripletex Department
-----------------------------------------
Every Exact Departments will be synchronized with a Tripletex Department.

If a matching Tripletex Department already exists, the Exact Departments will be merged with the existing one.
If no matching Tripletex Department is found, a new Tripletex Department will be created.

A Exact Departments will merge with a Tripletex Department if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Tripletex Department Property
   * - Code
     - departmentNumber

Once a link between a Exact Departments and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - Code
     - departmentNumber
     - "string"


Exact Employees to Tripletex Employee
-------------------------------------
Every Exact Employees will be synchronized with a Tripletex Employee.

Once a link between a Exact Employees and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - BirthDate
     - dateOfBirth
     - N/A
   * - City
     - address.city
     - "string"
   * - Country
     - address.country.id
     - "integer"
   * - ID
     - id
     - "integer"
   * - Postcode
     - address.postalCode
     - "string"


Exact Items to Tripletex Product
--------------------------------
Every Exact Items will be synchronized with a Tripletex Product.

Once a link between a Exact Items and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Tripletex Product Property
     - Tripletex Data Type


Exact Salesorderlines to Tripletex Orderline
--------------------------------------------
Every Exact Salesorderlines will be synchronized with a Tripletex Orderline.

Once a link between a Exact Salesorderlines and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Tripletex Orderline Property
     - Tripletex Data Type


Exact Salesorders to Tripletex Order
------------------------------------
Every Exact Salesorders will be synchronized with a Tripletex Order.

Once a link between a Exact Salesorders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - Currency
     - currency.id
     - "integer"

