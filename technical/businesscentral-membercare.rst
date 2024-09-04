======================================
Businesscentral to Membercare Dataflow
======================================

Generated: 2024-09-04 10:50:42

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
   * - id
     - addresses.id
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
   * - id
     - addresses.id
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


Businesscentral Customers company to Membercare Companies
---------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Membercare Companies.

Once a link between a Businesscentral Customers company and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Membercare Companies Property
     - Membercare Data Type
   * - displayName
     - companyName
     - "string"
   * - displayName
     - name
     - "string"
   * - website
     - url
     - "string"


Businesscentral Salesorders to Membercare Countries
---------------------------------------------------
Every Businesscentral Salesorders will be synchronized with a Membercare Countries.

Once a link between a Businesscentral Salesorders and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     - Membercare Countries Property
     - Membercare Data Type
   * - billToCountry
     - iso2Letter
     - "string"
   * - shipToCountry
     - iso2Letter
     - "string"


Businesscentral Salesquotes to Membercare Countries
---------------------------------------------------
Every Businesscentral Salesquotes will be synchronized with a Membercare Countries.

Once a link between a Businesscentral Salesquotes and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesquotes and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesquotes Property
     - Membercare Countries Property
     - Membercare Data Type
   * - billToCountry
     - name
     - "string"
   * - shipToCountry
     - name
     - "string"

