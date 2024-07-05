================================
Unieconomy to Tripletex Dataflow
================================

Generated: 2024-07-05 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Companies to Tripletex Customer
------------------------------------------
Before any synchronization can take place, a link between a Unieconomy Companies and a Tripletex Customer must be established.

A Unieconomy Companies will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Companies Property
     - Tripletex Customer Property
   * - OrganizationNumber
     - organizationNumber

Once a link between a Unieconomy Companies and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Companies and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Unieconomy Companies Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


Unieconomy Customers to Tripletex Customer
------------------------------------------
Every Unieconomy Customers will be synchronized with a Tripletex Customer.

If a matching Tripletex Customer already exists, the Unieconomy Customers will be merged with the existing one.
If no matching Tripletex Customer is found, a new Tripletex Customer will be created.

A Unieconomy Customers will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - Tripletex Customer Property
   * - OrgNumber
     - organizationNumber

Once a link between a Unieconomy Customers and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Customers and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - WebUrl
     - website
     - "string"


Unieconomy Departments to Tripletex Department
----------------------------------------------
Every Unieconomy Departments will be synchronized with a Tripletex Department.

Once a link between a Unieconomy Departments and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Departments and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Unieconomy Departments Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"

