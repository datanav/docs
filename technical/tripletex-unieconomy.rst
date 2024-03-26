================================
Tripletex to Unieconomy Dataflow
================================

Generated: 2024-03-26 14:24:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to  Companies
--------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a  Companies must be established.

A Tripletex Customer will merge with a  Companies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Companies Property
   * - organizationNumber
     - OrganizationNumber

Once a link between a Tripletex Customer and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Companies Property
     -  Data Type
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrganizationNumber
     - "string"


Tripletex Supplier to  Companies
--------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a  Companies must be established.

A Tripletex Supplier will merge with a  Companies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     -  Companies Property
   * - organizationNumber
     - OrganizationNumber

Once a link between a Tripletex Supplier and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     -  Companies Property
     -  Data Type
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrganizationNumber
     - "string"


Tripletex Supplier to  Customers
--------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a  Customers must be established.

A Tripletex Supplier will merge with a  Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     -  Customers Property
   * - organizationNumber
     - OrgNumber

Once a link between a Tripletex Supplier and a  Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a  Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     -  Customers Property
     -  Data Type
   * - organizationNumber
     - OrgNumber
     - "string"
   * - url
     - WebUrl
     - "string"


Tripletex Customer to  Customers
--------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a  Customers.

If a matching  Customers already exists, the Tripletex Customer will be merged with the existing one.
If no matching  Customers is found, a new  Customers will be created.

A Tripletex Customer will merge with a  Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Customers Property
   * - organizationNumber
     - OrgNumber

Once a link between a Tripletex Customer and a  Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Customers Property
     -  Data Type
   * - organizationNumber
     - OrgNumber
     - "string"
   * - url
     - WebUrl
     - "string"
   * - website
     - WebUrl
     - "string"


Tripletex Department to  Departments
------------------------------------
Every Tripletex Department will be synchronized with a  Departments.

Once a link between a Tripletex Department and a  Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Departments Property
     -  Data Type
   * - departmentNumber
     - DepartmentNumber
     - "string"
   * - name
     - Name
     - "string"

