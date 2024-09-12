================================
Tripletex to Unieconomy Dataflow
================================

Generated: 2024-09-12 13:14:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Unieconomy Companies
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Unieconomy Companies must be established.

A Tripletex Customer will merge with a Unieconomy Companies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Unieconomy Companies Property
   * - organizationNumber
     - OrganizationNumber

Once a link between a Tripletex Customer and a Unieconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Unieconomy Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Unieconomy Companies Property
     - Unieconomy Data Type
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrganizationNumber
     - "string"


Tripletex Supplier to Unieconomy Companies
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a Unieconomy Companies must be established.

A Tripletex Supplier will merge with a Unieconomy Companies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Unieconomy Companies Property
   * - organizationNumber
     - OrganizationNumber

Once a link between a Tripletex Supplier and a Unieconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a Unieconomy Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Unieconomy Companies Property
     - Unieconomy Data Type
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrganizationNumber
     - "string"


Tripletex Supplier to Unieconomy Customers
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a Unieconomy Customers must be established.

A Tripletex Supplier will merge with a Unieconomy Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Unieconomy Customers Property
   * - organizationNumber
     - OrgNumber

Once a link between a Tripletex Supplier and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Unieconomy Customers Property
     - Unieconomy Data Type
   * - organizationNumber
     - OrgNumber
     - "string"
   * - url
     - WebUrl
     - "string"


Tripletex Customer to Unieconomy Customers
------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Unieconomy Customers.

If a matching Unieconomy Customers already exists, the Tripletex Customer will be merged with the existing one.
If no matching Unieconomy Customers is found, a new Unieconomy Customers will be created.

A Tripletex Customer will merge with a Unieconomy Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Unieconomy Customers Property
   * - organizationNumber
     - OrgNumber

Once a link between a Tripletex Customer and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Unieconomy Customers Property
     - Unieconomy Data Type
   * - organizationNumber
     - OrgNumber
     - "string"
   * - url
     - WebUrl
     - "string"
   * - website
     - WebUrl
     - "string"


Tripletex Department to Unieconomy Departments
----------------------------------------------
Every Tripletex Department will be synchronized with a Unieconomy Departments.

Once a link between a Tripletex Department and a Unieconomy Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Unieconomy Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Unieconomy Departments Property
     - Unieconomy Data Type
   * - departmentNumber
     - DepartmentNumber
     - "string"
   * - name
     - Name
     - "string"

