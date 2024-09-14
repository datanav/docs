===================================
Exact Online to MemberCare Dataflow
===================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Online Accounts to MemberCare Companies
---------------------------------------------
Every Exact Online Accounts will be synchronized with a MemberCare Companies.

Once a link between a Exact Online Accounts and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Accounts and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Exact Online Accounts Property
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


Exact Online Contacts to MemberCare Persons
-------------------------------------------
Every Exact Online Contacts will be synchronized with a MemberCare Persons.

Once a link between a Exact Online Contacts and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Contacts and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Exact Online Contacts Property
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


Exact Online Currencies to MemberCare Companycategories
-------------------------------------------------------
Every Exact Online Currencies will be synchronized with a MemberCare Companycategories.

Once a link between a Exact Online Currencies and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Currencies and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Online Currencies Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


Exact Online Departments to MemberCare Companies
------------------------------------------------
Every Exact Online Departments will be synchronized with a MemberCare Companies.

Once a link between a Exact Online Departments and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Departments and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Exact Online Departments Property
     - MemberCare Companies Property
     - MemberCare Data Type


Exact Online Divisions to MemberCare Companies
----------------------------------------------
Every Exact Online Divisions will be synchronized with a MemberCare Companies.

Once a link between a Exact Online Divisions and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Divisions and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Exact Online Divisions Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Website
     - url
     - "string"


Exact Online Employees to MemberCare Persons
--------------------------------------------
Every Exact Online Employees will be synchronized with a MemberCare Persons.

Once a link between a Exact Online Employees and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Employees and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Exact Online Employees Property
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


Exact Online Items to MemberCare Products
-----------------------------------------
Every Exact Online Items will be synchronized with a MemberCare Products.

Once a link between a Exact Online Items and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Items and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Exact Online Items Property
     - MemberCare Products Property
     - MemberCare Data Type


Exact Online Quotations to MemberCare Invoices
----------------------------------------------
Every Exact Online Quotations will be synchronized with a MemberCare Invoices.

Once a link between a Exact Online Quotations and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Quotations and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Online Quotations Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Exact Online Salesorderlines to MemberCare Invoices
---------------------------------------------------
Every Exact Online Salesorderlines will be synchronized with a MemberCare Invoices.

Once a link between a Exact Online Salesorderlines and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorderlines and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorderlines Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - Quantity
     - id
     - "string"


Exact Online Salesorders to MemberCare Invoices
-----------------------------------------------
Every Exact Online Salesorders will be synchronized with a MemberCare Invoices.

Once a link between a Exact Online Salesorders and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorders and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorders Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Exact Online Units to MemberCare Companycategories
--------------------------------------------------
Every Exact Online Units will be synchronized with a MemberCare Companycategories.

Once a link between a Exact Online Units and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Units and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Online Units Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


Exact Online Vatcodes to MemberCare Companycategories
-----------------------------------------------------
Every Exact Online Vatcodes will be synchronized with a MemberCare Companycategories.

Once a link between a Exact Online Vatcodes and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Vatcodes and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - Exact Online Vatcodes Property
     - MemberCare Companycategories Property
     - MemberCare Data Type
   * - Description
     - description
     - "string"


Exact Online Addresses to MemberCare Countries
----------------------------------------------
Every Exact Online Addresses will be synchronized with a MemberCare Countries.

Once a link between a Exact Online Addresses and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Addresses and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Exact Online Addresses Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - CountryName
     - name
     - "string"


Exact Online Salesinvoices to MemberCare Invoices
-------------------------------------------------
Every Exact Online Salesinvoices will be synchronized with a MemberCare Invoices.

Once a link between a Exact Online Salesinvoices and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesinvoices and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesinvoices Property
     - MemberCare Invoices Property
     - MemberCare Data Type

