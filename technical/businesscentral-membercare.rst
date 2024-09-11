=======================================
Business Central to MemberCare Dataflow
=======================================

Generated: 2024-09-11 11:40:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessCentral Companies to MemberCare Companies
-------------------------------------------------
Every BusinessCentral Companies will be synchronized with a MemberCare Companies.

Once a link between a BusinessCentral Companies and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Companies and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Companies Property
     - MemberCare Companies Property
     - MemberCare Data Type


BusinessCentral Contacts person to MemberCare Persons
-----------------------------------------------------
Every BusinessCentral Contacts person will be synchronized with a MemberCare Persons.

Once a link between a BusinessCentral Contacts person and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - city
     - addresses.postalCode.city
     - "string"
   * - country
     - addresses.country.id
     - "string"
   * - displayName
     - name
     - "string"
   * - id
     - addresses.id
     - "string"
   * - id
     - socialSecurityNumber.number (Dependant on having BusinessCentral-contact in socialSecurityNumber.iso2Letter)
     - "string"
   * - postalCode
     - addresses.postalCode.zipCode
     - "string"


BusinessCentral Customers person to MemberCare Persons
------------------------------------------------------
Every BusinessCentral Customers person will be synchronized with a MemberCare Persons.

Once a link between a BusinessCentral Customers person and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers person and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers person Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - city
     - addresses.postalCode.city
     - "string"
   * - country
     - addresses.country.id
     - "string"
   * - displayName
     - name
     - "string"
   * - id
     - addresses.id
     - "string"
   * - id
     - socialSecurityNumber.number (Dependant on having  in socialSecurityNumber.iso2Letter)
     - "string"
   * - postalCode
     - addresses.postalCode.zipCode
     - "string"


BusinessCentral Employees to MemberCare Persons
-----------------------------------------------
Every BusinessCentral Employees will be synchronized with a MemberCare Persons.

Once a link between a BusinessCentral Employees and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Employees and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Employees Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - birthDate
     - birthDate
     - "string"
   * - displayName
     - name
     - "string"
   * - givenName
     - firstname
     - "string"
   * - surname
     - lastname
     - "string"


BusinessCentral Items to MemberCare Products
--------------------------------------------
Every BusinessCentral Items will be synchronized with a MemberCare Products.

Once a link between a BusinessCentral Items and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Items and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Items Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - displayName
     - name
     - "string"


BusinessCentral Salesorderlines to MemberCare Invoices
------------------------------------------------------
Every BusinessCentral Salesorderlines will be synchronized with a MemberCare Invoices.

Once a link between a BusinessCentral Salesorderlines and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorderlines and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorderlines Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - quantity
     - invoiceItems.quantity
     - "string"
   * - unitPrice
     - invoiceItems.unitPrice
     - "string"


BusinessCentral Salesorders to MemberCare Invoices
--------------------------------------------------
Every BusinessCentral Salesorders will be synchronized with a MemberCare Invoices.

Once a link between a BusinessCentral Salesorders and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorders and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorders Property
     - MemberCare Invoices Property
     - MemberCare Data Type


BusinessCentral Salesquotes to MemberCare Invoices
--------------------------------------------------
Every BusinessCentral Salesquotes will be synchronized with a MemberCare Invoices.

Once a link between a BusinessCentral Salesquotes and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesquotes and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesquotes Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Business Central Customers company to MemberCare Companies
----------------------------------------------------------
Every Business Central Customers company will be synchronized with a MemberCare Companies.

Once a link between a Business Central Customers company and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - displayName
     - companyName
     - "string"
   * - displayName
     - name
     - "string"
   * - website
     - url
     - "string"


Business Central Salesorders to MemberCare Countries
----------------------------------------------------
Every Business Central Salesorders will be synchronized with a MemberCare Countries.

Once a link between a Business Central Salesorders and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - billToCountry
     - iso2Letter
     - "string"
   * - shipToCountry
     - iso2Letter
     - "string"


Business Central Salesquotes to MemberCare Countries
----------------------------------------------------
Every Business Central Salesquotes will be synchronized with a MemberCare Countries.

Once a link between a Business Central Salesquotes and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesquotes and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - billToCountry
     - name
     - "string"
   * - shipToCountry
     - name
     - "string"

