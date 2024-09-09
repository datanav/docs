=============================
Exact to Superoffice Dataflow
=============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Salesorders to Superoffice Quotealternative
-------------------------------------------------
Before any synchronization can take place, a link between a Exact Salesorders and a Superoffice Quotealternative must be established.

A new Superoffice Quotealternative will be created from a Exact Salesorders if it is connected to a Exact Salesorderlines that is synchronized into Superoffice.

Once a link between a Exact Salesorders and a Superoffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Superoffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Superoffice Quotealternative Property
     - Superoffice Data Type
   * - Description
     - Name
     - "string"
   * - Discount
     - DiscountPercent
     - "integer"


Exact Accounts to Superoffice Contact
-------------------------------------
Every Exact Accounts will be synchronized with a Superoffice Contact.

Once a link between a Exact Accounts and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - Name
     - Name
     - "string"
   * - Website
     - Urls.Value
     - "string"


Exact Contacts to Superoffice Person
------------------------------------
Every Exact Contacts will be synchronized with a Superoffice Person.

Once a link between a Exact Contacts and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - BirthDate
     - BirthDate
     - N/A


Exact Departments to Superoffice Contact
----------------------------------------
Every Exact Departments will be synchronized with a Superoffice Contact.

Once a link between a Exact Departments and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - Code
     - OrgNr (Dependant on having wd:Q2366457 in Country.TwoLetterISOCountry)
     - "string"


Exact Divisions to Superoffice Contact
--------------------------------------
Every Exact Divisions will be synchronized with a Superoffice Contact.

Once a link between a Exact Divisions and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - Website
     - Urls.Value
     - "string"


Exact Employees to Superoffice Person
-------------------------------------
Every Exact Employees will be synchronized with a Superoffice Person.

Once a link between a Exact Employees and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
     - Superoffice Person Property
     - Superoffice Data Type
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


Exact Items to Superoffice Product
----------------------------------
Every Exact Items will be synchronized with a Superoffice Product.

Once a link between a Exact Items and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Superoffice Product Property
     - Superoffice Data Type
   * - Code
     - Code
     - "string"


Exact Quotations to Superoffice Quotealternative
------------------------------------------------
Every Exact Quotations will be synchronized with a Superoffice Quotealternative.

Once a link between a Exact Quotations and a Superoffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Quotations and a Superoffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Exact Quotations Property
     - Superoffice Quotealternative Property
     - Superoffice Data Type
   * - Description
     - Name
     - "string"


Exact Salesorderlines to Superoffice Quoteline
----------------------------------------------
Every Exact Salesorderlines will be synchronized with a Superoffice Quoteline.

Once a link between a Exact Salesorderlines and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Superoffice Quoteline Property
     - Superoffice Data Type

