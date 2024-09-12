==================================
Exact Online to Tripletex Dataflow
==================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Online Accounts to Tripletex Customer
-------------------------------------------
Every Exact Online Accounts will be synchronized with a Tripletex Customer.

Once a link between a Exact Online Accounts and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Accounts and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Exact Online Accounts Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"
   * - Website
     - website
     - "string"


Exact Online Addresses to Tripletex Country
-------------------------------------------
Every Exact Online Addresses will be synchronized with a Tripletex Country.

Once a link between a Exact Online Addresses and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Addresses and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - Exact Online Addresses Property
     - Tripletex Country Property
     - Tripletex Data Type


Exact Online Contacts to Tripletex Contact
------------------------------------------
Every Exact Online Contacts will be synchronized with a Tripletex Contact.

Once a link between a Exact Online Contacts and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Contacts and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Exact Online Contacts Property
     - Tripletex Contact Property
     - Tripletex Data Type


Exact Online Currencies to Tripletex Currency
---------------------------------------------
Every Exact Online Currencies will be synchronized with a Tripletex Currency.

Once a link between a Exact Online Currencies and a Tripletex Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Currencies and a Tripletex Currency:

.. list-table::
   :header-rows: 1

   * - Exact Online Currencies Property
     - Tripletex Currency Property
     - Tripletex Data Type


Exact Online Departments to Tripletex Department
------------------------------------------------
Every Exact Online Departments will be synchronized with a Tripletex Department.

If a matching Tripletex Department already exists, the Exact Online Departments will be merged with the existing one.
If no matching Tripletex Department is found, a new Tripletex Department will be created.

A Exact Online Departments will merge with a Tripletex Department if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Exact Online Departments Property
     - Tripletex Department Property
   * - Code
     - departmentNumber

Once a link between a Exact Online Departments and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Departments and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Exact Online Departments Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - Code
     - departmentNumber
     - "string"


Exact Online Employees to Tripletex Employee
--------------------------------------------
Every Exact Online Employees will be synchronized with a Tripletex Employee.

Once a link between a Exact Online Employees and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Employees and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Exact Online Employees Property
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


Exact Online Items to Tripletex Product
---------------------------------------
Every Exact Online Items will be synchronized with a Tripletex Product.

Once a link between a Exact Online Items and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Items and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Exact Online Items Property
     - Tripletex Product Property
     - Tripletex Data Type


Exact Online Salesinvoices to Tripletex Invoice
-----------------------------------------------
Every Exact Online Salesinvoices will be synchronized with a Tripletex Invoice.

Once a link between a Exact Online Salesinvoices and a Tripletex Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesinvoices and a Tripletex Invoice:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesinvoices Property
     - Tripletex Invoice Property
     - Tripletex Data Type


Exact Online Salesorderlines to Tripletex Orderline
---------------------------------------------------
Every Exact Online Salesorderlines will be synchronized with a Tripletex Orderline.

Once a link between a Exact Online Salesorderlines and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorderlines and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorderlines Property
     - Tripletex Orderline Property
     - Tripletex Data Type


Exact Online Salesorders to Tripletex Order
-------------------------------------------
Every Exact Online Salesorders will be synchronized with a Tripletex Order.

Once a link between a Exact Online Salesorders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorders Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - Currency
     - currency.id
     - "integer"


Exact Online Units to Tripletex Productunit
-------------------------------------------
Every Exact Online Units will be synchronized with a Tripletex Productunit.

Once a link between a Exact Online Units and a Tripletex Productunit is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Units and a Tripletex Productunit:

.. list-table::
   :header-rows: 1

   * - Exact Online Units Property
     - Tripletex Productunit Property
     - Tripletex Data Type


Exact Online Vatcodes to Tripletex Vattype
------------------------------------------
Every Exact Online Vatcodes will be synchronized with a Tripletex Vattype.

Once a link between a Exact Online Vatcodes and a Tripletex Vattype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Vatcodes and a Tripletex Vattype:

.. list-table::
   :header-rows: 1

   * - Exact Online Vatcodes Property
     - Tripletex Vattype Property
     - Tripletex Data Type

