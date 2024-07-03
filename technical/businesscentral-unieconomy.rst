======================================
Businesscentral to Unieconomy Dataflow
======================================

Generated: 2024-07-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers company to Unieconomy Companies
---------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Unieconomy Companies.

Once a link between a Businesscentral Customers company and a Unieconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Unieconomy Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Unieconomy Companies Property
     - Unieconomy Data Type
   * - displayName
     - Name
     - "string"
   * - id (Dependant on having wd:Q11994066 in typeDependant on having wd:Q11994066 in type)
     - OrganizationNumber
     - "string"


Businesscentral Customers company to Unieconomy Customers
---------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Unieconomy Customers.

Once a link between a Businesscentral Customers company and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Unieconomy Customers Property
     - Unieconomy Data Type
   * - id (Dependant on having wd:Q11994066 in typeDependant on having wd:Q11994066 in type)
     - OrgNumber
     - "string"
   * - website
     - WebUrl
     - "string"

