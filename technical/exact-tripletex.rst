=================================
ExactOnline to Tripletex Dataflow
=================================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Accounts to Tripletex Customer
------------------------------------------
Every ExactOnline Accounts will be synchronized with a Tripletex Customer.

Once a link between a ExactOnline Accounts and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Accounts and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - ExactOnline Accounts Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"
   * - Website
     - website
     - "string"


ExactOnline Contacts to Tripletex Contact
-----------------------------------------
Every ExactOnline Contacts will be synchronized with a Tripletex Contact.

Once a link between a ExactOnline Contacts and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Contacts and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - ExactOnline Contacts Property
     - Tripletex Contact Property
     - Tripletex Data Type


ExactOnline Departments to Tripletex Department
-----------------------------------------------
Every ExactOnline Departments will be synchronized with a Tripletex Department.

If a matching Tripletex Department already exists, the ExactOnline Departments will be merged with the existing one.
If no matching Tripletex Department is found, a new Tripletex Department will be created.

A ExactOnline Departments will merge with a Tripletex Department if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - Tripletex Department Property
   * - Code
     - departmentNumber

Once a link between a ExactOnline Departments and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Departments and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - Code
     - departmentNumber
     - "string"


ExactOnline Employees to Tripletex Employee
-------------------------------------------
Every ExactOnline Employees will be synchronized with a Tripletex Employee.

Once a link between a ExactOnline Employees and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Employees and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - ExactOnline Employees Property
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


ExactOnline Items to Tripletex Product
--------------------------------------
Every ExactOnline Items will be synchronized with a Tripletex Product.

Once a link between a ExactOnline Items and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Items and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - ExactOnline Items Property
     - Tripletex Product Property
     - Tripletex Data Type


ExactOnline Salesorderlines to Tripletex Orderline
--------------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a Tripletex Orderline.

Once a link between a ExactOnline Salesorderlines and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - Tripletex Orderline Property
     - Tripletex Data Type


ExactOnline Salesorders to Tripletex Order
------------------------------------------
Every ExactOnline Salesorders will be synchronized with a Tripletex Order.

Once a link between a ExactOnline Salesorders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorders Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - Currency
     - currency.id
     - "integer"

