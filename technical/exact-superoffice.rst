===================================
ExactOnline to SuperOffice Dataflow
===================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Salesorders to SuperOffice Quotealternative
-------------------------------------------------------
Before any synchronization can take place, a link between a ExactOnline Salesorders and a SuperOffice Quotealternative must be established.

A new SuperOffice Quotealternative will be created from a ExactOnline Salesorders if it is connected to a ExactOnline Exact-salesorderlines that is synchronized into SuperOffice.

Once a link between a ExactOnline Salesorders and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorders and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorders Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - Description
     - Name
     - "string"
   * - Discount
     - DiscountPercent
     - "integer"


Exact Accounts to SuperOffice Contact
-------------------------------------
Every Exact Accounts will be synchronized with a SuperOffice Contact.

Once a link between a Exact Accounts and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Name
     - Name
     - "string"
   * - Website
     - Urls.Value
     - "string"


Exact Contacts to SuperOffice Person
------------------------------------
Every Exact Contacts will be synchronized with a SuperOffice Person.

Once a link between a Exact Contacts and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - BirthDate
     - BirthDate
     - N/A


Exact Departments to SuperOffice Contact
----------------------------------------
Every Exact Departments will be synchronized with a SuperOffice Contact.

Once a link between a Exact Departments and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Code
     - OrgNr (Dependant on having wd:Q2366457 in Country.TwoLetterISOCountry)
     - "string"


Exact Divisions to SuperOffice Contact
--------------------------------------
Every Exact Divisions will be synchronized with a SuperOffice Contact.

Once a link between a Exact Divisions and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Website
     - Urls.Value
     - "string"


Exact Employees to SuperOffice Person
-------------------------------------
Every Exact Employees will be synchronized with a SuperOffice Person.

Once a link between a Exact Employees and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
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


ExactOnline Items to SuperOffice Product
----------------------------------------
Every ExactOnline Items will be synchronized with a SuperOffice Product.

Once a link between a ExactOnline Items and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Items and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - ExactOnline Items Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - Code
     - Code
     - "string"


ExactOnline Quotations to SuperOffice Quotealternative
------------------------------------------------------
Every ExactOnline Quotations will be synchronized with a SuperOffice Quotealternative.

Once a link between a ExactOnline Quotations and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Quotations and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - ExactOnline Quotations Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - Description
     - Name
     - "string"


ExactOnline Salesorderlines to SuperOffice Quoteline
----------------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a SuperOffice Quoteline.

Once a link between a ExactOnline Salesorderlines and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type

