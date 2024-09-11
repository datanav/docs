=====================================
ExactOnline to PowerOfficeGO Dataflow
=====================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Accounts to PowerOfficeGO Customers
-----------------------------------------------
Every ExactOnline Accounts will be synchronized with a PowerOfficeGO Customers.

Once a link between a ExactOnline Accounts and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Accounts and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - ExactOnline Accounts Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type
   * - Name
     - Name
     - "string"
   * - Website
     - WebsiteUrl
     - "string"


ExactOnline Contacts to PowerOfficeGO Contactperson
---------------------------------------------------
Every ExactOnline Contacts will be synchronized with a PowerOfficeGO Contactperson.

Once a link between a ExactOnline Contacts and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Contacts and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - ExactOnline Contacts Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
   * - BirthDate
     - dateOfBirth
     - N/A


ExactOnline Departments to PowerOfficeGO Departments
----------------------------------------------------
Every ExactOnline Departments will be synchronized with a PowerOfficeGO Departments.

If a matching PowerOfficeGO Departments already exists, the ExactOnline Departments will be merged with the existing one.
If no matching PowerOfficeGO Departments is found, a new PowerOfficeGO Departments will be created.

A ExactOnline Departments will merge with a PowerOfficeGO Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - PowerOfficeGO Departments Property
   * - Code
     - Code

Once a link between a ExactOnline Departments and a PowerOfficeGO Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Departments and a PowerOfficeGO Departments:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - PowerOfficeGO Departments Property
     - PowerOfficeGO Data Type
   * - Code
     - Code
     - "string"


ExactOnline Employees to PowerOfficeGO Employees
------------------------------------------------
Every ExactOnline Employees will be synchronized with a PowerOfficeGO Employees.

Once a link between a ExactOnline Employees and a PowerOfficeGO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Employees and a PowerOfficeGO Employees:

.. list-table::
   :header-rows: 1

   * - ExactOnline Employees Property
     - PowerOfficeGO Employees Property
     - PowerOfficeGO Data Type
   * - BirthDate
     - DateOfBirth
     - N/A


ExactOnline Items to PowerOfficeGO Product
------------------------------------------
Every ExactOnline Items will be synchronized with a PowerOfficeGO Product.

Once a link between a ExactOnline Items and a PowerOfficeGO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Items and a PowerOfficeGO Product:

.. list-table::
   :header-rows: 1

   * - ExactOnline Items Property
     - PowerOfficeGO Product Property
     - PowerOfficeGO Data Type


ExactOnline Salesorderlines to PowerOfficeGO Salesorderlines
------------------------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a ExactOnline Salesorderlines and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type


ExactOnline Salesorders to PowerOfficeGO Salesorders
----------------------------------------------------
Every ExactOnline Salesorders will be synchronized with a PowerOfficeGO Salesorders.

Once a link between a ExactOnline Salesorders and a PowerOfficeGO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorders and a PowerOfficeGO Salesorders:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorders Property
     - PowerOfficeGO Salesorders Property
     - PowerOfficeGO Data Type
   * - Currency
     - CurrencyCode
     - "string"

