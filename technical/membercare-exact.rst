============================
Membercare to Exact Dataflow
============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companies to Exact Accounts
--------------------------------------
Every Membercare Companies will be synchronized with a Exact Accounts.

Once a link between a Membercare Companies and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Exact Accounts Property
     - Exact Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.id
     - ID
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"
   * - addresses.postalCode.zipCode
     - Postcode
     - "string"
   * - companyName
     - Name
     - "string"
   * - url
     - Website
     - "string"


Membercare Companycategories to Exact Currencies
------------------------------------------------
Every Membercare Companycategories will be synchronized with a Exact Currencies.

Once a link between a Membercare Companycategories and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companycategories and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Membercare Companycategories Property
     - Exact Currencies Property
     - Exact Data Type


Membercare Countries to Exact Currencies
----------------------------------------
Every Membercare Countries will be synchronized with a Exact Currencies.

Once a link between a Membercare Countries and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Countries and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Membercare Countries Property
     - Exact Currencies Property
     - Exact Data Type
   * - name
     - Description
     - "string"


Membercare Invoices to Exact Quotations
---------------------------------------
Every Membercare Invoices will be synchronized with a Exact Quotations.

Once a link between a Membercare Invoices and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Exact Quotations Property
     - Exact Data Type


Membercare Organizations to Exact Accounts
------------------------------------------
Every Membercare Organizations will be synchronized with a Exact Accounts.

Once a link between a Membercare Organizations and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Organizations and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Membercare Organizations Property
     - Exact Accounts Property
     - Exact Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.id
     - ID
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"
   * - addresses.postalCode.zipCode
     - Postcode
     - "string"
   * - company.addresses.addressDescription
     - Country
     - "string"
   * - company.addresses.id
     - ID
     - "string"
   * - company.addresses.municipality
     - Postcode
     - "string"
   * - company.addresses.start
     - City
     - "string"
   * - name
     - Name
     - "string"


Membercare Persons to Exact Contacts
------------------------------------
Every Membercare Persons will be synchronized with a Exact Contacts.

Once a link between a Membercare Persons and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Persons and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Membercare Persons Property
     - Exact Contacts Property
     - Exact Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"
   * - birthDate
     - BirthDate
     - "string"
   * - firstname
     - FirstName
     - "string"
   * - firstname
     - FullName
     - "string"
   * - firstname
     - LastName
     - "string"
   * - name
     - FirstName
     - "string"
   * - name
     - FullName
     - "string"
   * - name
     - LastName
     - "string"


Membercare Products to Exact Items
----------------------------------
Every Membercare Products will be synchronized with a Exact Items.

Once a link between a Membercare Products and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Products and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Membercare Products Property
     - Exact Items Property
     - Exact Data Type


Membercare Companies to Exact Addresses
---------------------------------------
Every Membercare Companies will be synchronized with a Exact Addresses.

Once a link between a Membercare Companies and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Exact Addresses Property
     - Exact Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"


Membercare Invoices to Exact Salesinvoices
------------------------------------------
Every Membercare Invoices will be synchronized with a Exact Salesinvoices.

Once a link between a Membercare Invoices and a Exact Salesinvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Exact Salesinvoices:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Exact Salesinvoices Property
     - Exact Data Type


Membercare Invoices to Exact Salesorderlines
--------------------------------------------
Every Membercare Invoices will be synchronized with a Exact Salesorderlines.

Once a link between a Membercare Invoices and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Exact Salesorderlines Property
     - Exact Data Type
   * - id
     - Quantity
     - "string"


Membercare Organizations to Exact Addresses
-------------------------------------------
Every Membercare Organizations will be synchronized with a Exact Addresses.

Once a link between a Membercare Organizations and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Organizations and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Membercare Organizations Property
     - Exact Addresses Property
     - Exact Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"
   * - company.addresses.addressDescription
     - Country
     - "string"
   * - company.addresses.start
     - City
     - "string"


Membercare Persons to Exact Addresses
-------------------------------------
Every Membercare Persons will be synchronized with a Exact Addresses.

Once a link between a Membercare Persons and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Persons and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Membercare Persons Property
     - Exact Addresses Property
     - Exact Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"

