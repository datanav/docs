==================================
ExactOnline to MemberCare Dataflow
==================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to MemberCare Companies
--------------------------------------
Every Exact Accounts will be synchronized with a MemberCare Companies.

Once a link between a Exact Accounts and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - MemberCare Companies Property
     - MemberCare Data Type
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


Exact Contacts to MemberCare Persons
------------------------------------
Every Exact Contacts will be synchronized with a MemberCare Persons.

Once a link between a Exact Contacts and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - MemberCare Persons Property
     - MemberCare Data Type
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


Exact Currencies to MemberCare Companycategories
------------------------------------------------
Every Exact Currencies will be synchronized with a MemberCare Companycategories.

Once a link between a Exact Currencies and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Currencies and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Currencies Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


Exact Departments to MemberCare Companies
-----------------------------------------
Every Exact Departments will be synchronized with a MemberCare Companies.

Once a link between a Exact Departments and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - MemberCare Companies Property
     - MemberCare Data Type


Exact Divisions to MemberCare Companies
---------------------------------------
Every Exact Divisions will be synchronized with a MemberCare Companies.

Once a link between a Exact Divisions and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Website
     - url
     - "string"


Exact Employees to MemberCare Persons
-------------------------------------
Every Exact Employees will be synchronized with a MemberCare Persons.

Once a link between a Exact Employees and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
     - MemberCare Persons Property
     - MemberCare Data Type
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


Exact Items to MemberCare Products
----------------------------------
Every Exact Items will be synchronized with a MemberCare Products.

Once a link between a Exact Items and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - MemberCare Products Property
     - MemberCare Data Type


Exact Quotations to MemberCare Invoices
---------------------------------------
Every Exact Quotations will be synchronized with a MemberCare Invoices.

Once a link between a Exact Quotations and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Quotations and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Quotations Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Exact Salesorderlines to MemberCare Invoices
--------------------------------------------
Every Exact Salesorderlines will be synchronized with a MemberCare Invoices.

Once a link between a Exact Salesorderlines and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - Quantity
     - id
     - "string"


Exact Salesorders to MemberCare Invoices
----------------------------------------
Every Exact Salesorders will be synchronized with a MemberCare Invoices.

Once a link between a Exact Salesorders and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Exact Units to MemberCare Companycategories
-------------------------------------------
Every Exact Units will be synchronized with a MemberCare Companycategories.

Once a link between a Exact Units and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Units and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Units Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


Exact Vatcodes to MemberCare Companycategories
----------------------------------------------
Every Exact Vatcodes will be synchronized with a MemberCare Companycategories.

Once a link between a Exact Vatcodes and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Vatcodes and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Vatcodes Property
     - MemberCare Companycategories Property
     - MemberCare Data Type
   * - Description
     - description
     - "string"


ExactOnline Addresses to MemberCare Countries
---------------------------------------------
Every ExactOnline Addresses will be synchronized with a MemberCare Countries.

Once a link between a ExactOnline Addresses and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Addresses and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - ExactOnline Addresses Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - CountryName
     - name
     - "string"


ExactOnline Salesinvoices to MemberCare Invoices
------------------------------------------------
Every ExactOnline Salesinvoices will be synchronized with a MemberCare Invoices.

Once a link between a ExactOnline Salesinvoices and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesinvoices and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesinvoices Property
     - MemberCare Invoices Property
     - MemberCare Data Type

