====================================
Exact Online to SuperOffice Dataflow
====================================

Generated: 2024-09-11 11:41:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Online Salesorders to SuperOffice Quotealternative
--------------------------------------------------------
Before any synchronization can take place, a link between a Exact Online Salesorders and a SuperOffice Quotealternative must be established.

A new SuperOffice Quotealternative will be created from a Exact Online Salesorders if it is connected to a Exact Online Exact-salesorderlines that is synchronized into SuperOffice.

Once a link between a Exact Online Salesorders and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorders and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorders Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - Description
     - Name
     - "string"
   * - Discount
     - DiscountPercent
     - "integer"


ExactOnline Accounts to SuperOffice Contact
-------------------------------------------
Every ExactOnline Accounts will be synchronized with a SuperOffice Contact.

Once a link between a ExactOnline Accounts and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Accounts and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - ExactOnline Accounts Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Name
     - Name
     - "string"
   * - Website
     - Urls.Value
     - "string"


ExactOnline Contacts to SuperOffice Person
------------------------------------------
Every ExactOnline Contacts will be synchronized with a SuperOffice Person.

Once a link between a ExactOnline Contacts and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Contacts and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - ExactOnline Contacts Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - BirthDate
     - BirthDate
     - N/A


ExactOnline Departments to SuperOffice Contact
----------------------------------------------
Every ExactOnline Departments will be synchronized with a SuperOffice Contact.

Once a link between a ExactOnline Departments and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Departments and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Code
     - OrgNr (Dependant on having wd:Q2366457 in Country.TwoLetterISOCountry)
     - "string"


ExactOnline Divisions to SuperOffice Contact
--------------------------------------------
Every ExactOnline Divisions will be synchronized with a SuperOffice Contact.

Once a link between a ExactOnline Divisions and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Divisions and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - ExactOnline Divisions Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Website
     - Urls.Value
     - "string"


ExactOnline Employees to SuperOffice Person
-------------------------------------------
Every ExactOnline Employees will be synchronized with a SuperOffice Person.

Once a link between a ExactOnline Employees and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Employees and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - ExactOnline Employees Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - BirthDate
     - BirthDate
     - N/A
   * - City
     - Address.Street.City
     - "string"
   * - Country
     - Country.CountryId
     - "integer"
   * - ID
     - PersonId
     - "integer"
   * - Postcode
     - Address.Street.Zipcode
     - "string"


Exact Online Items to SuperOffice Product
-----------------------------------------
Every Exact Online Items will be synchronized with a SuperOffice Product.

Once a link between a Exact Online Items and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Items and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Exact Online Items Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - Code
     - Code
     - "string"


Exact Online Quotations to SuperOffice Quotealternative
-------------------------------------------------------
Every Exact Online Quotations will be synchronized with a SuperOffice Quotealternative.

Once a link between a Exact Online Quotations and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Quotations and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Exact Online Quotations Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - Description
     - Name
     - "string"


Exact Online Salesorderlines to SuperOffice Quoteline
-----------------------------------------------------
Every Exact Online Salesorderlines will be synchronized with a SuperOffice Quoteline.

Once a link between a Exact Online Salesorderlines and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Salesorderlines and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Exact Online Salesorderlines Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type

