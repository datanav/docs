===============================
Exact to Powerofficego Dataflow
===============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Powerofficego Customers
-----------------------------------------
Every Exact Accounts will be synchronized with a Powerofficego Customers.

Once a link between a Exact Accounts and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Powerofficego Customers Property
     - Powerofficego Data Type
   * - Name
     - Name
     - "string"
   * - Website
     - WebsiteUrl
     - "string"


Exact Contacts to Powerofficego Contactperson
---------------------------------------------
Every Exact Contacts will be synchronized with a Powerofficego Contactperson.

Once a link between a Exact Contacts and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
   * - BirthDate
     - dateOfBirth
     - N/A


Exact Departments to Powerofficego Departments
----------------------------------------------
Every Exact Departments will be synchronized with a Powerofficego Departments.

If a matching Powerofficego Departments already exists, the Exact Departments will be merged with the existing one.
If no matching Powerofficego Departments is found, a new Powerofficego Departments will be created.

A Exact Departments will merge with a Powerofficego Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Powerofficego Departments Property
   * - Code
     - Code

Once a link between a Exact Departments and a Powerofficego Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Powerofficego Departments:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Powerofficego Departments Property
     - Powerofficego Data Type
   * - Code
     - Code
     - "string"


Exact Employees to Powerofficego Employees
------------------------------------------
Every Exact Employees will be synchronized with a Powerofficego Employees.

Once a link between a Exact Employees and a Powerofficego Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a Powerofficego Employees:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
     - Powerofficego Employees Property
     - Powerofficego Data Type
   * - BirthDate
     - DateOfBirth
     - N/A


Exact Items to Powerofficego Product
------------------------------------
Every Exact Items will be synchronized with a Powerofficego Product.

Once a link between a Exact Items and a Powerofficego Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Powerofficego Product:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Powerofficego Product Property
     - Powerofficego Data Type


Exact Salesorderlines to Powerofficego Salesorderlines
------------------------------------------------------
Every Exact Salesorderlines will be synchronized with a Powerofficego Salesorderlines.

Once a link between a Exact Salesorderlines and a Powerofficego Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Powerofficego Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Powerofficego Salesorderlines Property
     - Powerofficego Data Type


Exact Salesorders to Powerofficego Salesorders
----------------------------------------------
Every Exact Salesorders will be synchronized with a Powerofficego Salesorders.

Once a link between a Exact Salesorders and a Powerofficego Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Powerofficego Salesorders:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Powerofficego Salesorders Property
     - Powerofficego Data Type
   * - Currency
     - CurrencyCode
     - "string"

