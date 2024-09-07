=======================
Exact to Exact Dataflow
=======================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Addresses to Exact Addresses
----------------------------------
Before any synchronization can take place, a link between a Exact Addresses and a Exact Addresses must be established.

A Exact Addresses will merge with a Exact Addresses if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Exact Addresses Property
     - Exact Addresses Property
   * - ID
     - ID

Once a link between a Exact Addresses and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Addresses and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Exact Addresses Property
     - Exact Addresses Property
     - Exact Data Type


Exact Departments to Exact Departments
--------------------------------------
Before any synchronization can take place, a link between a Exact Departments and a Exact Departments must be established.

A Exact Departments will merge with a Exact Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Exact Departments Property
   * - Code
     - Code

Once a link between a Exact Departments and a Exact Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Exact Departments:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Exact Departments Property
     - Exact Data Type


Exact Quotations to Exact Addresses
-----------------------------------
Before any synchronization can take place, a link between a Exact Quotations and a Exact Addresses must be established.

A Exact Quotations will merge with a Exact Addresses if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Exact Quotations Property
     - Exact Addresses Property
   * - DeliveryAddress
     - ID

Once a link between a Exact Quotations and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Quotations and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Exact Quotations Property
     - Exact Addresses Property
     - Exact Data Type


Exact Departments to Exact Accounts
-----------------------------------
Every Exact Departments will be synchronized with a Exact Accounts.

Once a link between a Exact Departments and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Exact Accounts Property
     - Exact Data Type


Exact Divisions to Exact Accounts
---------------------------------
Every Exact Divisions will be synchronized with a Exact Accounts.

Once a link between a Exact Divisions and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - Exact Accounts Property
     - Exact Data Type
   * - Website
     - Website
     - "string"


Exact Employees to Exact Contacts
---------------------------------
Every Exact Employees will be synchronized with a Exact Contacts.

Once a link between a Exact Employees and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
     - Exact Contacts Property
     - Exact Data Type
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


Exact Salesinvoices to Exact Quotations
---------------------------------------
Every Exact Salesinvoices will be synchronized with a Exact Quotations.

Once a link between a Exact Salesinvoices and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesinvoices and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Exact Salesinvoices Property
     - Exact Quotations Property
     - Exact Data Type
   * - Currency
     - Currency
     - "string"
   * - Description
     - Description
     - "string"
   * - DueDate
     - DueDate
     - "string"


Exact Salesorderlines to Exact Quotations
-----------------------------------------
Every Exact Salesorderlines will be synchronized with a Exact Quotations.

Once a link between a Exact Salesorderlines and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorderlines and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Exact Salesorderlines Property
     - Exact Quotations Property
     - Exact Data Type


Exact Salesorders to Exact Quotations
-------------------------------------
Every Exact Salesorders will be synchronized with a Exact Quotations.

Once a link between a Exact Salesorders and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     - Exact Quotations Property
     - Exact Data Type
   * - Currency
     - Currency
     - "string"
   * - DeliveryDate
     - DeliveryDate
     - "string"
   * - Description
     - Description
     - "string"


Exact Units to Exact Currencies
-------------------------------
Every Exact Units will be synchronized with a Exact Currencies.

Once a link between a Exact Units and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Units and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Exact Units Property
     - Exact Currencies Property
     - Exact Data Type
   * - Description
     - Description
     - "string"


Exact Vatcodes to Exact Currencies
----------------------------------
Every Exact Vatcodes will be synchronized with a Exact Currencies.

Once a link between a Exact Vatcodes and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Vatcodes and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Exact Vatcodes Property
     - Exact Currencies Property
     - Exact Data Type


Exact Accounts to Exact Addresses
---------------------------------
Every Exact Accounts will be synchronized with a Exact Addresses.

Once a link between a Exact Accounts and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Exact Addresses Property
     - Exact Data Type
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


Exact Employees to Exact Addresses
----------------------------------
Every Exact Employees will be synchronized with a Exact Addresses.

Once a link between a Exact Employees and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
     - Exact Addresses Property
     - Exact Data Type
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

