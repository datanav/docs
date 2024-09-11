==================================
Unieconomy to ExactOnline Dataflow
==================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Companies to Exact Accounts
--------------------------------------
Every Unieconomy Companies will be synchronized with a Exact Accounts.

Once a link between a Unieconomy Companies and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Companies and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Unieconomy Companies Property
     - Exact Accounts Property
     - Exact Data Type
   * - Name
     - Name
     - "string"


Unieconomy Departments to Exact Accounts
----------------------------------------
Every Unieconomy Departments will be synchronized with a Exact Accounts.

Once a link between a Unieconomy Departments and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Departments and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Unieconomy Departments Property
     - Exact Accounts Property
     - Exact Data Type
   * - Name
     - Name
     - "string"


Unieconomy Currencycodes to ExactOnline Currencies
--------------------------------------------------
Every Unieconomy Currencycodes will be synchronized with a ExactOnline Currencies.

Once a link between a Unieconomy Currencycodes and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Currencycodes and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - Code
     - Code
     - "string"
   * - Name
     - Description
     - "string"


Unieconomy Customers to ExactOnline Accounts
--------------------------------------------
Every Unieconomy Customers will be synchronized with a ExactOnline Accounts.

Once a link between a Unieconomy Customers and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Customers and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
   * - CurrencyCodeID
     - Currency
     - "string"
   * - WebUrl
     - Website
     - "string"


Unieconomy Departments to ExactOnline Departments
-------------------------------------------------
Every Unieconomy Departments will be synchronized with a ExactOnline Departments.

Once a link between a Unieconomy Departments and a ExactOnline Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Departments and a ExactOnline Departments:

.. list-table::
   :header-rows: 1

   * - Unieconomy Departments Property
     - ExactOnline Departments Property
     - ExactOnline Data Type
   * - DepartmentNumber
     - Description
     - "string"

