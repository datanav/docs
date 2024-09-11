===================================
ExactOnline to ExactOnline Dataflow
===================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ExactOnline to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Addresses to ExactOnline Addresses
----------------------------------------------
Before any synchronization can take place, a link between a ExactOnline Addresses and a ExactOnline Addresses must be established.

A ExactOnline Addresses will merge with a ExactOnline Addresses if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - ExactOnline Addresses Property
     - ExactOnline Addresses Property
   * - ID
     - ID

Once a link between a ExactOnline Addresses and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Addresses and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - ExactOnline Addresses Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type


ExactOnline Departments to ExactOnline Departments
--------------------------------------------------
Before any synchronization can take place, a link between a ExactOnline Departments and a ExactOnline Departments must be established.

A ExactOnline Departments will merge with a ExactOnline Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - ExactOnline Departments Property
   * - Code
     - Code

Once a link between a ExactOnline Departments and a ExactOnline Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Departments and a ExactOnline Departments:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - ExactOnline Departments Property
     - ExactOnline Data Type


ExactOnline Quotations to ExactOnline Addresses
-----------------------------------------------
Before any synchronization can take place, a link between a ExactOnline Quotations and a ExactOnline Addresses must be established.

A ExactOnline Quotations will merge with a ExactOnline Addresses if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - ExactOnline Quotations Property
     - ExactOnline Addresses Property
   * - DeliveryAddress
     - ID

Once a link between a ExactOnline Quotations and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Quotations and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - ExactOnline Quotations Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type


ExactOnline Departments to ExactOnline Accounts
-----------------------------------------------
Every ExactOnline Departments will be synchronized with a ExactOnline Accounts.

Once a link between a ExactOnline Departments and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Departments and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type


ExactOnline Divisions to ExactOnline Accounts
---------------------------------------------
Every ExactOnline Divisions will be synchronized with a ExactOnline Accounts.

Once a link between a ExactOnline Divisions and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Divisions and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - ExactOnline Divisions Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
   * - Website
     - Website
     - "string"


ExactOnline Employees to ExactOnline Contacts
---------------------------------------------
Every ExactOnline Employees will be synchronized with a ExactOnline Contacts.

Once a link between a ExactOnline Employees and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Employees and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - ExactOnline Employees Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
   * - BirthDate
     - BirthDate
     - "string"
   * - BusinessEmail
     - BusinessEmail
     - "string"
   * - BusinessMobile
     - Mobile
     - "string"
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"
   * - Email
     - Email
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - FirstName
     - FullName
     - "string"
   * - FirstName
     - LastName
     - "string"
   * - FullName
     - FirstName
     - "string"
   * - FullName
     - FullName
     - "string"
   * - FullName
     - LastName
     - "string"
   * - LastName
     - FirstName
     - "string"
   * - LastName
     - FullName
     - "string"
   * - LastName
     - LastName
     - "string"
   * - Phone
     - Phone
     - "string"


ExactOnline Salesinvoices to ExactOnline Quotations
---------------------------------------------------
Every ExactOnline Salesinvoices will be synchronized with a ExactOnline Quotations.

Once a link between a ExactOnline Salesinvoices and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesinvoices and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesinvoices Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
   * - Currency
     - Currency
     - "string"
   * - Description
     - Description
     - "string"
   * - DueDate
     - DueDate
     - "string"


ExactOnline Salesorderlines to ExactOnline Quotations
-----------------------------------------------------
Every ExactOnline Salesorderlines will be synchronized with a ExactOnline Quotations.

Once a link between a ExactOnline Salesorderlines and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorderlines and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorderlines Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type


ExactOnline Salesorders to ExactOnline Quotations
-------------------------------------------------
Every ExactOnline Salesorders will be synchronized with a ExactOnline Quotations.

Once a link between a ExactOnline Salesorders and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Salesorders and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - ExactOnline Salesorders Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
   * - Currency
     - Currency
     - "string"
   * - DeliveryDate
     - DeliveryDate
     - "string"
   * - Description
     - Description
     - "string"


ExactOnline Units to ExactOnline Currencies
-------------------------------------------
Every ExactOnline Units will be synchronized with a ExactOnline Currencies.

Once a link between a ExactOnline Units and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Units and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - ExactOnline Units Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - Description
     - Description
     - "string"


ExactOnline Vatcodes to ExactOnline Currencies
----------------------------------------------
Every ExactOnline Vatcodes will be synchronized with a ExactOnline Currencies.

Once a link between a ExactOnline Vatcodes and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Vatcodes and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - ExactOnline Vatcodes Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type


ExactOnline Accounts to ExactOnline Addresses
---------------------------------------------
Every ExactOnline Accounts will be synchronized with a ExactOnline Addresses.

Once a link between a ExactOnline Accounts and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Accounts and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - ExactOnline Accounts Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
   * - AddressLine1
     - AddressLine1
     - "string"
   * - AddressLine2
     - AddressLine2
     - "string"
   * - AddressLine3
     - AddressLine3
     - "string"
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"


ExactOnline Employees to ExactOnline Addresses
----------------------------------------------
Every ExactOnline Employees will be synchronized with a ExactOnline Addresses.

Once a link between a ExactOnline Employees and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Employees and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - ExactOnline Employees Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
   * - AddressLine2
     - AddressLine2
     - "string"
   * - AddressLine3
     - AddressLine3
     - "string"
   * - AddressStreet
     - AddressLine1
     - "string"
   * - City
     - City
     - "string"
   * - Country
     - Country
     - "string"

