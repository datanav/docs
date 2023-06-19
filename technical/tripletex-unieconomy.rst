================================
Tripletex to UniEconomy Dataflow
================================

Generated: 2023-06-19 11:19:27

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to UniEconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to UniEconomy Companies
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a UniEconomy Companies must be established.

A Tripletex Customer will merge with a UniEconomy Companies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - UniEconomy Companies Property
   * - organizationNumber
     - OrganizationNumber

Once a link between a Tripletex Customer and a UniEconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a UniEconomy Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - UniEconomy Companies Property
     - UniEconomy Data Type
   * - name
     - Name
     - "string"


Tripletex Customer to UniEconomy Customers
------------------------------------------
Every Tripletex Customer will be synchronized with a UniEconomy Customers.

Once a link between a Tripletex Customer and a UniEconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a UniEconomy Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - UniEconomy Customers Property
     - UniEconomy Data Type
   * - organizationNumber
     - OrgNumber
     - "string"


Tripletex Department to UniEconomy Departments
----------------------------------------------
Every Tripletex Department will be synchronized with a UniEconomy Departments.

Once a link between a Tripletex Department and a UniEconomy Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a UniEconomy Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - UniEconomy Departments Property
     - UniEconomy Data Type
   * - departmentNumber
     - DepartmentNumber
     - "string"
   * - departmentNumber
     - DepartmentNumberNumeric
     - "string"
   * - name
     - Name
     - "string"

