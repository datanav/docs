=======================================
Business Central to Unieconomy Dataflow
=======================================

Generated: 2024-10-28 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Customers (organisation data) to Unieconomy Companies
----------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Unieconomy Companies.

Once a link between a Business Central Customers (organisation data) and a Unieconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Unieconomy Companies:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Unieconomy Companies Property
     - Unieconomy Data Type
   * - displayName
     - Name
     - "string"
   * - id (Dependant on having wd:Q11994066 in type)
     - OrganizationNumber
     - "string"


Business Central Customers (organisation data) to Unieconomy Customers
----------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Unieconomy Customers.

Once a link between a Business Central Customers (organisation data) and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Unieconomy Customers Property
     - Unieconomy Data Type
   * - id (Dependant on having wd:Q11994066 in type)
     - OrgNumber
     - "string"
   * - website
     - WebUrl
     - "string"


Business Central Customers (organisation data) to Unieconomy Customers
----------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a Unieconomy Customers.

Once a link between a Business Central Customers (organisation data) and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - Unieconomy Customers Property
     - Unieconomy Data Type

