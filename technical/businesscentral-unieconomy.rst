=======================================
Business Central to Unieconomy Dataflow
=======================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Contacts person to Unieconomy Countries
--------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Contacts person and a Unieconomy Countries must be established.

A Business Central Contacts person will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Unieconomy Countries Property
   * - country
     - CountryCode

Once a link between a Business Central Contacts person and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


Business Central Customers company to Unieconomy Countries
----------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers company and a Unieconomy Countries must be established.

A Business Central Customers company will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Unieconomy Countries Property
   * - country
     - CountryCode

Once a link between a Business Central Customers company and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


Business Central Customers person to Unieconomy Countries
---------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers person and a Unieconomy Countries must be established.

A Business Central Customers person will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Unieconomy Countries Property
   * - country
     - CountryCode

Once a link between a Business Central Customers person and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


Business Central Employees to Unieconomy Countries
--------------------------------------------------
Before any synchronization can take place, a link between a Business Central Employees and a Unieconomy Countries must be established.

A Business Central Employees will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - Unieconomy Countries Property
   * - country
     - CountryCode

Once a link between a Business Central Employees and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


Business Central Currencies to Unieconomy Currencycodes
-------------------------------------------------------
Every Business Central Currencies will be synchronized with a Unieconomy Currencycodes.

If a matching Unieconomy Currencycodes already exists, the Business Central Currencies will be merged with the existing one.
If no matching Unieconomy Currencycodes is found, a new Unieconomy Currencycodes will be created.

A Business Central Currencies will merge with a Unieconomy Currencycodes if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - Unieconomy Currencycodes Property
   * - code
     - Code

Once a link between a Business Central Currencies and a Unieconomy Currencycodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Currencies and a Unieconomy Currencycodes:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - Unieconomy Currencycodes Property
     - Unieconomy Data Type


Business Central Customers company to Unieconomy Companies
----------------------------------------------------------
Every Business Central Customers company will be synchronized with a Unieconomy Companies.

Once a link between a Business Central Customers company and a Unieconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Unieconomy Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Unieconomy Companies Property
     - Unieconomy Data Type
   * - displayName
     - Name
     - "string"
   * - id (Dependant on having wd:Q11994066 in typeDependant on having wd:Q11994066 in type)
     - OrganizationNumber
     - "string"


Business Central Customers company to Unieconomy Customers
----------------------------------------------------------
Every Business Central Customers company will be synchronized with a Unieconomy Customers.

Once a link between a Business Central Customers company and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Unieconomy Customers Property
     - Unieconomy Data Type
   * - id (Dependant on having wd:Q11994066 in typeDependant on having wd:Q11994066 in type)
     - OrgNumber
     - "string"
   * - website
     - WebUrl
     - "string"


Business Central Salesorders to Unieconomy Countries
----------------------------------------------------
Every Business Central Salesorders will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the Business Central Salesorders will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A Business Central Salesorders will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Unieconomy Countries Property
   * - billToCountry
     - CountryCode
   * - shipToCountry
     - CountryCode

Once a link between a Business Central Salesorders and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


Business Central Salesquotes to Unieconomy Countries
----------------------------------------------------
Every Business Central Salesquotes will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the Business Central Salesquotes will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A Business Central Salesquotes will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - Unieconomy Countries Property
   * - billToCountry
     - Name
   * - shipToCountry
     - Name

Once a link between a Business Central Salesquotes and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesquotes and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - Unieconomy Countries Property
     - Unieconomy Data Type

