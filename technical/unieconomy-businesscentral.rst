=======================================
Unieconomy to Business Central Dataflow
=======================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Companies to Business Central Companies
--------------------------------------------------
Every Unieconomy Companies will be synchronized with a Business Central Companies.

Once a link between a Unieconomy Companies and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Companies and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Unieconomy Companies Property
     - Business Central Companies Property
     - Business Central Data Type


Unieconomy Customers to Business Central Companies
--------------------------------------------------
Every Unieconomy Customers will be synchronized with a Business Central Companies.

Once a link between a Unieconomy Customers and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Customers and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - Business Central Companies Property
     - Business Central Data Type


Unieconomy Departments to Business Central Companies
----------------------------------------------------
Every Unieconomy Departments will be synchronized with a Business Central Companies.

Once a link between a Unieconomy Departments and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Departments and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Unieconomy Departments Property
     - Business Central Companies Property
     - Business Central Data Type


Unieconomy Currencycodes to Business Central Currencies
-------------------------------------------------------
Every Unieconomy Currencycodes will be synchronized with a Business Central Currencies.

If a matching Business Central Currencies already exists, the Unieconomy Currencycodes will be merged with the existing one.
If no matching Business Central Currencies is found, a new Business Central Currencies will be created.

A Unieconomy Currencycodes will merge with a Business Central Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - Business Central Currencies Property
   * - Code
     - code

Once a link between a Unieconomy Currencycodes and a Business Central Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Currencycodes and a Business Central Currencies:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - Business Central Currencies Property
     - Business Central Data Type


Unieconomy Customers to Business Central Customers company
----------------------------------------------------------
Every Unieconomy Customers will be synchronized with a Business Central Customers company.

Once a link between a Unieconomy Customers and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Customers and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - Business Central Customers company Property
     - Business Central Data Type
   * - WebUrl
     - website
     - "string"

