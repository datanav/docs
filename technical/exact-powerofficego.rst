=======================================
Exact Online to PowerOffice GO Dataflow
=======================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Online Accounts to PowerOffice GO Customers
-------------------------------------------------
Every Exact Online Accounts will be synchronized with a PowerOffice GO Customers.

Once a link between a Exact Online Accounts and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Accounts and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Exact Online Accounts Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - Name
     - Name
     - "string"
   * - Website
     - WebsiteUrl
     - "string"


Exact Online Contacts to PowerOffice GO Contactperson
-----------------------------------------------------
Every Exact Online Contacts will be synchronized with a PowerOffice GO Contactperson.

Once a link between a Exact Online Contacts and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Contacts and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Exact Online Contacts Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - BirthDate
     - dateOfBirth
     - N/A


Exact Online Departments to PowerOffice GO Departments
------------------------------------------------------
Every Exact Online Departments will be synchronized with a PowerOffice GO Departments.

If a matching PowerOffice GO Departments already exists, the Exact Online Departments will be merged with the existing one.
If no matching PowerOffice GO Departments is found, a new PowerOffice GO Departments will be created.

A Exact Online Departments will merge with a PowerOffice GO Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Exact Online Departments Property
     - PowerOffice GO Departments Property
   * - Code
     - Code

Once a link between a Exact Online Departments and a PowerOffice GO Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Departments and a PowerOffice GO Departments:

.. list-table::
   :header-rows: 1

   * - Exact Online Departments Property
     - PowerOffice GO Departments Property
     - PowerOffice GO Data Type
   * - Code
     - Code
     - "string"


Exact Online Employees to PowerOffice GO Employees
--------------------------------------------------
Every Exact Online Employees will be synchronized with a PowerOffice GO Employees.

Once a link between a Exact Online Employees and a PowerOffice GO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Employees and a PowerOffice GO Employees:

.. list-table::
   :header-rows: 1

   * - Exact Online Employees Property
     - PowerOffice GO Employees Property
     - PowerOffice GO Data Type
   * - BirthDate
     - DateOfBirth
     - N/A


Exact Online Items to PowerOffice GO Product
--------------------------------------------
Every Exact Online Items will be synchronized with a PowerOffice GO Product.

Once a link between a Exact Online Items and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Items and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - Exact Online Items Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type


Exact Online Salesorderlines to PowerOffice GO Salesorderlines
--------------------------------------------------------------
Every Exact Online Salesorderlines will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a Exact Online Salesorderlines and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorderlines and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorderlines Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type


Exact Online Salesorders to PowerOffice GO Salesorders
------------------------------------------------------
Every Exact Online Salesorders will be synchronized with a PowerOffice GO Salesorders.

Once a link between a Exact Online Salesorders and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorders and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorders Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type
   * - Currency
     - CurrencyCode
     - "string"

