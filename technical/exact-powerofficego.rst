======================================
ExactOnline to PowerOffice GO Dataflow
======================================

Generated: 2024-09-11 08:35:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to PowerOffice Customers
---------------------------------------
Every Exact Accounts will be synchronized with a PowerOffice Customers.

Once a link between a Exact Accounts and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - PowerOffice Customers Property
     - PowerOffice Data Type
   * - Name
     - Name
     - "string"
   * - Website
     - WebsiteUrl
     - "string"


Exact Contacts to PowerOffice Contactperson
-------------------------------------------
Every Exact Contacts will be synchronized with a PowerOffice Contactperson.

Once a link between a Exact Contacts and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
   * - BirthDate
     - dateOfBirth
     - N/A


Exact Departments to PowerOffice Departments
--------------------------------------------
Every Exact Departments will be synchronized with a PowerOffice Departments.

If a matching PowerOffice Departments already exists, the Exact Departments will be merged with the existing one.
If no matching PowerOffice Departments is found, a new PowerOffice Departments will be created.

A Exact Departments will merge with a PowerOffice Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - PowerOffice Departments Property
   * - Code
     - Code

Once a link between a Exact Departments and a PowerOffice Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a PowerOffice Departments:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - PowerOffice Departments Property
     - PowerOffice Data Type
   * - Code
     - Code
     - "string"


Exact Employees to PowerOffice Employees
----------------------------------------
Every Exact Employees will be synchronized with a PowerOffice Employees.

Once a link between a Exact Employees and a PowerOffice Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a PowerOffice Employees:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
     - PowerOffice Employees Property
     - PowerOffice Data Type
   * - BirthDate
     - DateOfBirth
     - N/A


Exact Items to PowerOffice Product
----------------------------------
Every Exact Items will be synchronized with a PowerOffice Product.

Once a link between a Exact Items and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - PowerOffice Product Property
     - PowerOffice Data Type


Exact Salesorderlines to PowerOffice Salesorderlines
----------------------------------------------------
Every Exact Salesorderlines will be synchronized with a PowerOffice Salesorderlines.

Once a link between a Exact Salesorderlines and a PowerOffice Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a PowerOffice Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - PowerOffice Salesorderlines Property
     - PowerOffice Data Type


Exact Salesorders to PowerOffice Salesorders
--------------------------------------------
Every Exact Salesorders will be synchronized with a PowerOffice Salesorders.

Once a link between a Exact Salesorders and a PowerOffice Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a PowerOffice Salesorders:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - PowerOffice Salesorders Property
     - PowerOffice Data Type
   * - Currency
     - CurrencyCode
     - "string"

