==================================
ExactOnline to MemberCare Dataflow
==================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Accounts to MemberCare Companies
--------------------------------------------
Every ExactOnline Accounts will be synchronized with a MemberCare Companies.

Once a link between a ExactOnline Accounts and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Accounts and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - ExactOnline Accounts Property
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


ExactOnline Contacts to MemberCare Persons
------------------------------------------
Every ExactOnline Contacts will be synchronized with a MemberCare Persons.

Once a link between a ExactOnline Contacts and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Contacts and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - ExactOnline Contacts Property
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


ExactOnline Currencies to MemberCare Companycategories
------------------------------------------------------
Every ExactOnline Currencies will be synchronized with a MemberCare Companycategories.

Once a link between a ExactOnline Currencies and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Currencies and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - ExactOnline Currencies Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


ExactOnline Departments to MemberCare Companies
-----------------------------------------------
Every ExactOnline Departments will be synchronized with a MemberCare Companies.

Once a link between a ExactOnline Departments and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Departments and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - MemberCare Companies Property
     - MemberCare Data Type


ExactOnline Divisions to MemberCare Companies
---------------------------------------------
Every ExactOnline Divisions will be synchronized with a MemberCare Companies.

Once a link between a ExactOnline Divisions and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Divisions and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - ExactOnline Divisions Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Website
     - url
     - "string"


ExactOnline Employees to MemberCare Persons
-------------------------------------------
Every ExactOnline Employees will be synchronized with a MemberCare Persons.

Once a link between a ExactOnline Employees and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Employees and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - ExactOnline Employees Property
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


ExactOnline Items to MemberCare Products
----------------------------------------
Every ExactOnline Items will be synchronized with a MemberCare Products.

Once a link between a ExactOnline Items and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Items and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - ExactOnline Items Property
     - MemberCare Products Property
     - MemberCare Data Type


ExactOnline Quotations to MemberCare Invoices
---------------------------------------------
Every ExactOnline Quotations will be synchronized with a MemberCare Invoices.

Once a link between a ExactOnline Quotations and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Quotations and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - ExactOnline Quotations Property
     - MemberCare Invoices Property
     - MemberCare Data Type


ExactOnline Salesorderlines to MemberCare Invoices
--------------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a MemberCare Invoices.

Once a link between a ExactOnline Salesorderlines and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - Quantity
     - id
     - "string"


ExactOnline Salesorders to MemberCare Invoices
----------------------------------------------
Every ExactOnline Salesorders will be synchronized with a MemberCare Invoices.

Once a link between a ExactOnline Salesorders and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorders and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorders Property
     - MemberCare Invoices Property
     - MemberCare Data Type


ExactOnline Units to MemberCare Companycategories
-------------------------------------------------
Every ExactOnline Units will be synchronized with a MemberCare Companycategories.

Once a link between a ExactOnline Units and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Units and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - ExactOnline Units Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


ExactOnline Vatcodes to MemberCare Companycategories
----------------------------------------------------
Every ExactOnline Vatcodes will be synchronized with a MemberCare Companycategories.

Once a link between a ExactOnline Vatcodes and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Vatcodes and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - ExactOnline Vatcodes Property
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

