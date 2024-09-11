======================================
BusinessCentral to MemberCare Dataflow
======================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Companies to MemberCare Companies
------------------------------------------
Every Business Companies will be synchronized with a MemberCare Companies.

Once a link between a Business Companies and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Companies and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Business Companies Property
     - MemberCare Companies Property
     - MemberCare Data Type


Business Contacts person to MemberCare Persons
----------------------------------------------
Every Business Contacts person will be synchronized with a MemberCare Persons.

Once a link between a Business Contacts person and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
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


Business Customers person to MemberCare Persons
-----------------------------------------------
Every Business Customers person will be synchronized with a MemberCare Persons.

Once a link between a Business Customers person and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers person and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Business Customers person Property
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


Business Employees to MemberCare Persons
----------------------------------------
Every Business Employees will be synchronized with a MemberCare Persons.

Once a link between a Business Employees and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Employees and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Business Employees Property
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


Business Items to MemberCare Products
-------------------------------------
Every Business Items will be synchronized with a MemberCare Products.

Once a link between a Business Items and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Items and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Business Items Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - displayName
     - name
     - "string"


Business Salesorderlines to MemberCare Invoices
-----------------------------------------------
Every Business Salesorderlines will be synchronized with a MemberCare Invoices.

Once a link between a Business Salesorderlines and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorderlines and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Business Salesorderlines Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - quantity
     - invoiceItems.quantity
     - "string"
   * - unitPrice
     - invoiceItems.unitPrice
     - "string"


Business Salesorders to MemberCare Invoices
-------------------------------------------
Every Business Salesorders will be synchronized with a MemberCare Invoices.

Once a link between a Business Salesorders and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesorders and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Business Salesorders Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Business Salesquotes to MemberCare Invoices
-------------------------------------------
Every Business Salesquotes will be synchronized with a MemberCare Invoices.

Once a link between a Business Salesquotes and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Salesquotes and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Business Salesquotes Property
     - MemberCare Invoices Property
     - MemberCare Data Type


BusinessCentral Customers company to MemberCare Companies
---------------------------------------------------------
Every BusinessCentral Customers company will be synchronized with a MemberCare Companies.

Once a link between a BusinessCentral Customers company and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers company and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers company Property
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


BusinessCentral Salesorders to MemberCare Countries
---------------------------------------------------
Every BusinessCentral Salesorders will be synchronized with a MemberCare Countries.

Once a link between a BusinessCentral Salesorders and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesorders and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesorders Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - billToCountry
     - iso2Letter
     - "string"
   * - shipToCountry
     - iso2Letter
     - "string"


BusinessCentral Salesquotes to MemberCare Countries
---------------------------------------------------
Every BusinessCentral Salesquotes will be synchronized with a MemberCare Countries.

Once a link between a BusinessCentral Salesquotes and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Salesquotes and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Salesquotes Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - billToCountry
     - name
     - "string"
   * - shipToCountry
     - name
     - "string"

