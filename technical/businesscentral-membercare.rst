=======================================
Business Central to MemberCare Dataflow
=======================================

Generated: 2024-11-04 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Companies to MemberCare Companies
--------------------------------------------------
Every Business Central Companies will be synchronized with a MemberCare Companies.

Once a link between a Business Central Companies and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Companies and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Companies Property
     - MemberCare Companies Property
     - MemberCare Data Type


Business Central Contacts (human data) to MemberCare Persons
------------------------------------------------------------
Every Business Central Contacts (human data) will be synchronized with a MemberCare Persons.

Once a link between a Business Central Contacts (human data) and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts (human data) and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts (human data) Property
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


Business Central Customers (organisation data) to MemberCare Companies
----------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a MemberCare Companies.

Once a link between a Business Central Customers (organisation data) and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - displayName
     - companyName
     - "string"
   * - website
     - url
     - "string"


Business Central Customers (human data) to MemberCare Persons
-------------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a MemberCare Persons.

Once a link between a Business Central Customers (human data) and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
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


Business Central Employees to MemberCare Persons
------------------------------------------------
Every Business Central Employees will be synchronized with a MemberCare Persons.

Once a link between a Business Central Employees and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
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


Business Central Items to MemberCare Products
---------------------------------------------
Every Business Central Items will be synchronized with a MemberCare Products.

Once a link between a Business Central Items and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - displayName
     - name
     - "string"


Business Central Salesorderlines to MemberCare Invoices
-------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a MemberCare Invoices.

Once a link between a Business Central Salesorderlines and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - quantity
     - invoiceItems.quantity
     - "string"
   * - unitPrice
     - invoiceItems.unitPrice
     - "string"


Business Central Salesorders to MemberCare Invoices
---------------------------------------------------
Every Business Central Salesorders will be synchronized with a MemberCare Invoices.

Once a link between a Business Central Salesorders and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Business Central Salesquotes to MemberCare Invoices
---------------------------------------------------
Every Business Central Salesquotes will be synchronized with a MemberCare Invoices.

Once a link between a Business Central Salesquotes and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesquotes and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Business Central Customers (organisation data) to MemberCare Companies
----------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a MemberCare Companies.

Once a link between a Business Central Customers (organisation data) and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - MemberCare Companies Property
     - MemberCare Data Type


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

