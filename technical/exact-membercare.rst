============================
Exact to Membercare Dataflow
============================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Membercare Companies
--------------------------------------
Every Exact Accounts will be synchronized with a Membercare Companies.

Once a link between a Exact Accounts and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Membercare Companies Property
     - Membercare Data Type
   * - City
     - addresses.postalCode.city
     - "string"
   * - Country
     - addresses.country.id
     - "string"
   * - ID
     - addresses.id
     - "string"
   * - Name
     - companyName
     - "string"
   * - Postcode
     - addresses.postalCode.zipCode
     - "string"
   * - Website
     - url
     - "string"


Exact Contacts to Membercare Persons
------------------------------------
Every Exact Contacts will be synchronized with a Membercare Persons.

Once a link between a Exact Contacts and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - Membercare Persons Property
     - Membercare Data Type
   * - BirthDate
     - birthDate
     - "string"
   * - FirstName
     - firstname
     - "string"
   * - FirstName
     - name
     - "string"
   * - FullName
     - firstname
     - "string"
   * - FullName
     - name
     - "string"
   * - LastName
     - firstname
     - "string"
   * - LastName
     - name
     - "string"


Exact Currencies to Membercare Companycategories
------------------------------------------------
Every Exact Currencies will be synchronized with a Membercare Companycategories.

Once a link between a Exact Currencies and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     - Membercare Companycategories Property
     - Membercare Data Type


Exact Departments to Membercare Companies
-----------------------------------------
Every Exact Departments will be synchronized with a Membercare Companies.

Once a link between a Exact Departments and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Membercare Companies Property
     - Membercare Data Type


Exact Divisions to Membercare Companies
---------------------------------------
Every Exact Divisions will be synchronized with a Membercare Companies.

Once a link between a Exact Divisions and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - Membercare Companies Property
     - Membercare Data Type
   * - Website
     - url
     - "string"


Exact Employees to Membercare Persons
-------------------------------------
Every Exact Employees will be synchronized with a Membercare Persons.

Once a link between a Exact Employees and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
     - Membercare Persons Property
     - Membercare Data Type
   * - BirthDate
     - birthDate
     - "string"
   * - City
     - addresses.postalCode.city
     - "string"
   * - Country
     - addresses.country.id
     - "string"
   * - FirstName
     - firstname
     - "string"
   * - FirstName
     - name
     - "string"
   * - FullName
     - firstname
     - "string"
   * - FullName
     - name
     - "string"
   * - ID
     - addresses.id
     - "string"
   * - LastName
     - firstname
     - "string"
   * - LastName
     - name
     - "string"
   * - Postcode
     - addresses.postalCode.zipCode
     - "string"


Exact Items to Membercare Products
----------------------------------
Every Exact Items will be synchronized with a Membercare Products.

Once a link between a Exact Items and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Membercare Products Property
     - Membercare Data Type


Exact Quotations to Membercare Invoices
---------------------------------------
Every Exact Quotations will be synchronized with a Membercare Invoices.

Once a link between a Exact Quotations and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Quotations and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Quotations Property
     - Membercare Invoices Property
     - Membercare Data Type


Exact Salesorderlines to Membercare Invoices
--------------------------------------------
Every Exact Salesorderlines will be synchronized with a Membercare Invoices.

Once a link between a Exact Salesorderlines and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - Quantity
     - id
     - "string"


Exact Salesorders to Membercare Invoices
----------------------------------------
Every Exact Salesorders will be synchronized with a Membercare Invoices.

Once a link between a Exact Salesorders and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Membercare Invoices Property
     - Membercare Data Type


Exact Units to Membercare Companycategories
-------------------------------------------
Every Exact Units will be synchronized with a Membercare Companycategories.

Once a link between a Exact Units and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Units and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Units Property
     - Membercare Companycategories Property
     - Membercare Data Type


Exact Vatcodes to Membercare Companycategories
----------------------------------------------
Every Exact Vatcodes will be synchronized with a Membercare Companycategories.

Once a link between a Exact Vatcodes and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Vatcodes and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Vatcodes Property
     - Membercare Companycategories Property
     - Membercare Data Type
   * - Description
     - description
     - "string"


Exact Addresses to Membercare Countries
---------------------------------------
Every Exact Addresses will be synchronized with a Membercare Countries.

Once a link between a Exact Addresses and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Addresses and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Exact Addresses Property
     - Membercare Countries Property
     - Membercare Data Type
   * - CountryName
     - name
     - "string"


Exact Salesinvoices to Membercare Invoices
------------------------------------------
Every Exact Salesinvoices will be synchronized with a Membercare Invoices.

Once a link between a Exact Salesinvoices and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesinvoices and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Salesinvoices Property
     - Membercare Invoices Property
     - Membercare Data Type

