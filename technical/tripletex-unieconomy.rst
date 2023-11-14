================================
Tripletex to UniEconomy Dataflow
================================

Generated: 2023-11-14 12:59:13

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to UniEconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to UniEconomy Companies
------------------------------------------
Every Tripletex Customer will be synchronized with a UniEconomy Companies.

If a matching UniEconomy Companies already exists, the Tripletex Customer will be merged with the existing one.
If no matching UniEconomy Companies is found, a new UniEconomy Companies will be created.

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
   * - organizationNumber
     - OrganizationNumber
     - "string"


Tripletex Supplier to UniEconomy Companies
------------------------------------------
Every Tripletex Supplier will be synchronized with a UniEconomy Companies.

If a matching UniEconomy Companies already exists, the Tripletex Supplier will be merged with the existing one.
If no matching UniEconomy Companies is found, a new UniEconomy Companies will be created.

A Tripletex Supplier will merge with a UniEconomy Companies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - UniEconomy Companies Property
   * - organizationNumber
     - OrganizationNumber

Once a link between a Tripletex Supplier and a UniEconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a UniEconomy Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - UniEconomy Companies Property
     - UniEconomy Data Type
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrganizationNumber
     - "string"


Tripletex Supplier to UniEconomy Customers
------------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a UniEconomy Customers must be established.

A Tripletex Supplier will merge with a UniEconomy Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - UniEconomy Customers Property
   * - organizationNumber
     - OrgNumber

Once a link between a Tripletex Supplier and a UniEconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a UniEconomy Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - UniEconomy Customers Property
     - UniEconomy Data Type
   * - organizationNumber
     - OrgNumber
     - "string"


Tripletex Department to UniEconomy Companies
--------------------------------------------
Every Tripletex Department will be synchronized with a UniEconomy Companies.

Once a link between a Tripletex Department and a UniEconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a UniEconomy Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - UniEconomy Companies Property
     - UniEconomy Data Type
   * - name
     - Name
     - "string"


Tripletex Customer to UniEconomy Customers
------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a UniEconomy Customers.

If a matching UniEconomy Customers already exists, the Tripletex Customer will be merged with the existing one.
If no matching UniEconomy Customers is found, a new UniEconomy Customers will be created.

A Tripletex Customer will merge with a UniEconomy Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - UniEconomy Customers Property
   * - organizationNumber
     - OrgNumber

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
   * - url
     - WebUrl
     - "string"
   * - website
     - WebUrl
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
   * - name
     - Name
     - "string"

