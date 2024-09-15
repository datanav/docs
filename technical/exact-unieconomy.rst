===================================
Exact Online to Unieconomy Dataflow
===================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Online Accounts to Unieconomy Customers
---------------------------------------------
Every Exact Online Accounts will be synchronized with a Unieconomy Customers.

Once a link between a Exact Online Accounts and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Accounts and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - Exact Online Accounts Property
     - Unieconomy Customers Property
     - Unieconomy Data Type
   * - Website
     - WebUrl
     - "string"


Exact Online Departments to Unieconomy Departments
--------------------------------------------------
Every Exact Online Departments will be synchronized with a Unieconomy Departments.

Once a link between a Exact Online Departments and a Unieconomy Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Online Departments and a Unieconomy Departments:

.. list-table::
   :header-rows: 1

   * - Exact Online Departments Property
     - Unieconomy Departments Property
     - Unieconomy Data Type
   * - Description
     - DepartmentNumber
     - "string"

