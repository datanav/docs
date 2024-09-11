===================================
MemberCare to Exact Online Dataflow
===================================

Generated: 2024-09-11 08:07:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Companies to Exact Accounts
--------------------------------------
Every MemberCare Companies will be synchronized with a Exact Accounts.

Once a link between a MemberCare Companies and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
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


MemberCare Companycategories to Exact Currencies
------------------------------------------------
Every MemberCare Companycategories will be synchronized with a Exact Currencies.

Once a link between a MemberCare Companycategories and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companycategories and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - MemberCare Companycategories Property
     - Exact Currencies Property
     - Exact Data Type


MemberCare Countries to Exact Currencies
----------------------------------------
Every MemberCare Countries will be synchronized with a Exact Currencies.

Once a link between a MemberCare Countries and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Countries and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - MemberCare Countries Property
     - Exact Currencies Property
     - Exact Data Type
   * - name
     - Description
     - "string"


MemberCare Invoices to Exact Quotations
---------------------------------------
Every MemberCare Invoices will be synchronized with a Exact Quotations.

Once a link between a MemberCare Invoices and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - Exact Quotations Property
     - Exact Data Type


MemberCare Organizations to Exact Accounts
------------------------------------------
Every MemberCare Organizations will be synchronized with a Exact Accounts.

Once a link between a MemberCare Organizations and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
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


MemberCare Persons to Exact Contacts
------------------------------------
Every MemberCare Persons will be synchronized with a Exact Contacts.

Once a link between a MemberCare Persons and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Persons and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - MemberCare Persons Property
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


MemberCare Products to Exact Items
----------------------------------
Every MemberCare Products will be synchronized with a Exact Items.

Once a link between a MemberCare Products and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Products and a Exact Items:

.. list-table::
   :header-rows: 1

   * - MemberCare Products Property
     - Exact Items Property
     - Exact Data Type


MemberCare Companies to Exact Addresses
---------------------------------------
Every MemberCare Companies will be synchronized with a Exact Addresses.

Once a link between a MemberCare Companies and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - Exact Addresses Property
     - Exact Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"


MemberCare Invoices to Exact Salesinvoices
------------------------------------------
Every MemberCare Invoices will be synchronized with a Exact Salesinvoices.

Once a link between a MemberCare Invoices and a Exact Salesinvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Exact Salesinvoices:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - Exact Salesinvoices Property
     - Exact Data Type


MemberCare Invoices to Exact Salesorderlines
--------------------------------------------
Every MemberCare Invoices will be synchronized with a Exact Salesorderlines.

Once a link between a MemberCare Invoices and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - Exact Salesorderlines Property
     - Exact Data Type
   * - id
     - Quantity
     - "string"


MemberCare Organizations to Exact Addresses
-------------------------------------------
Every MemberCare Organizations will be synchronized with a Exact Addresses.

Once a link between a MemberCare Organizations and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
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


MemberCare Persons to Exact Addresses
-------------------------------------
Every MemberCare Persons will be synchronized with a Exact Addresses.

Once a link between a MemberCare Persons and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Persons and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - MemberCare Persons Property
     - Exact Addresses Property
     - Exact Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"

