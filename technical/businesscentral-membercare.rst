======================================
BusinessCentral to MemberCare Dataflow
======================================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Companies to Membercare Companies
-------------------------------------------------
Every Businesscentral Companies will be synchronized with a Membercare Companies.

Once a link between a Businesscentral Companies and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     - Membercare Companies Property
     - Membercare Data Type


Businesscentral Contacts person to Membercare Persons
-----------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Membercare Persons.

Once a link between a Businesscentral Contacts person and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Membercare Persons Property
     - Membercare Data Type
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


Businesscentral Customers person to Membercare Persons
------------------------------------------------------
Every Businesscentral Customers person will be synchronized with a Membercare Persons.

Once a link between a Businesscentral Customers person and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     - Membercare Persons Property
     - Membercare Data Type
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


Businesscentral Employees to Membercare Persons
-----------------------------------------------
Every Businesscentral Employees will be synchronized with a Membercare Persons.

Once a link between a Businesscentral Employees and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     - Membercare Persons Property
     - Membercare Data Type
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


Businesscentral Items to Membercare Products
--------------------------------------------
Every Businesscentral Items will be synchronized with a Membercare Products.

Once a link between a Businesscentral Items and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Membercare Products Property
     - Membercare Data Type
   * - displayName
     - name
     - "string"


Businesscentral Salesorderlines to Membercare Invoices
------------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a Membercare Invoices.

Once a link between a Businesscentral Salesorderlines and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - quantity
     - invoiceItems.quantity
     - "string"
   * - unitPrice
     - invoiceItems.unitPrice
     - "string"


Businesscentral Salesorders to Membercare Invoices
--------------------------------------------------
Every Businesscentral Salesorders will be synchronized with a Membercare Invoices.

Once a link between a Businesscentral Salesorders and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     - Membercare Invoices Property
     - Membercare Data Type


Businesscentral Salesquotes to Membercare Invoices
--------------------------------------------------
Every Businesscentral Salesquotes will be synchronized with a Membercare Invoices.

Once a link between a Businesscentral Salesquotes and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesquotes and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesquotes Property
     - Membercare Invoices Property
     - Membercare Data Type


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

