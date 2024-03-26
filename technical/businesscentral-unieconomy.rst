======================================
Businesscentral to Unieconomy Dataflow
======================================

Generated: 2024-03-26 14:24:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers company to  Companies
-----------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Companies.

Once a link between a Businesscentral Customers company and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Companies:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Companies Property
     -  Data Type
   * - displayName
     - Name
     - "string"
   * - id (Dependant on having wd:Q11994066 in typeDependant on having wd:Q11994066 in type)
     - OrganizationNumber
     - "string"


Businesscentral Customers company to  Customers
-----------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Customers.

Once a link between a Businesscentral Customers company and a  Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Customers:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Customers Property
     -  Data Type
   * - id (Dependant on having wd:Q11994066 in typeDependant on having wd:Q11994066 in type)
     - OrgNumber
     - "string"
   * - website
     - WebUrl
     - "string"

