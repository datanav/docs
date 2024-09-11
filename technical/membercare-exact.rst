==================================
MemberCare to ExactOnline Dataflow
==================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Companies to ExactOnline Accounts
--------------------------------------------
Every MemberCare Companies will be synchronized with a ExactOnline Accounts.

Once a link between a MemberCare Companies and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
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


MemberCare Companycategories to ExactOnline Currencies
------------------------------------------------------
Every MemberCare Companycategories will be synchronized with a ExactOnline Currencies.

Once a link between a MemberCare Companycategories and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companycategories and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - MemberCare Companycategories Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type


MemberCare Countries to ExactOnline Currencies
----------------------------------------------
Every MemberCare Countries will be synchronized with a ExactOnline Currencies.

Once a link between a MemberCare Countries and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Countries and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - MemberCare Countries Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - name
     - Description
     - "string"


MemberCare Invoices to ExactOnline Quotations
---------------------------------------------
Every MemberCare Invoices will be synchronized with a ExactOnline Quotations.

Once a link between a MemberCare Invoices and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


MemberCare Organizations to ExactOnline Accounts
------------------------------------------------
Every MemberCare Organizations will be synchronized with a ExactOnline Accounts.

Once a link between a MemberCare Organizations and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
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


MemberCare Persons to ExactOnline Contacts
------------------------------------------
Every MemberCare Persons will be synchronized with a ExactOnline Contacts.

Once a link between a MemberCare Persons and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Persons and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - MemberCare Persons Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


MemberCare Products to ExactOnline Items
----------------------------------------
Every MemberCare Products will be synchronized with a ExactOnline Items.

Once a link between a MemberCare Products and a ExactOnline Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Products and a ExactOnline Items:

.. list-table::
   :header-rows: 1

   * - MemberCare Products Property
     - ExactOnline Items Property
     - ExactOnline Data Type


MemberCare Companies to ExactOnline Addresses
---------------------------------------------
Every MemberCare Companies will be synchronized with a ExactOnline Addresses.

Once a link between a MemberCare Companies and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"


MemberCare Invoices to ExactOnline Salesinvoices
------------------------------------------------
Every MemberCare Invoices will be synchronized with a ExactOnline Salesinvoices.

Once a link between a MemberCare Invoices and a ExactOnline Salesinvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a ExactOnline Salesinvoices:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - ExactOnline Salesinvoices Property
     - ExactOnline Data Type


MemberCare Invoices to ExactOnline Salesorderlines
--------------------------------------------------
Every MemberCare Invoices will be synchronized with a ExactOnline Salesorderlines.

Once a link between a MemberCare Invoices and a ExactOnline Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a ExactOnline Salesorderlines:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - ExactOnline Salesorderlines Property
     - ExactOnline Data Type
   * - id
     - Quantity
     - "string"


MemberCare Organizations to ExactOnline Addresses
-------------------------------------------------
Every MemberCare Organizations will be synchronized with a ExactOnline Addresses.

Once a link between a MemberCare Organizations and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
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


MemberCare Persons to ExactOnline Addresses
-------------------------------------------
Every MemberCare Persons will be synchronized with a ExactOnline Addresses.

Once a link between a MemberCare Persons and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Persons and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - MemberCare Persons Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"

