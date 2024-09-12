================================
Unieconomy to Tripletex Dataflow
================================

Generated: 2024-09-12 12:58:41

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


Unieconomy Companies to Tripletex Supplier
------------------------------------------
Before any synchronization can take place, a link between a Unieconomy Companies and a Tripletex Supplier must be established.

A Unieconomy Companies will merge with a Tripletex Supplier if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Companies Property
     - Tripletex Supplier Property
   * - OrganizationNumber
     - organizationNumber

Once a link between a Unieconomy Companies and a Tripletex Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Companies and a Tripletex Supplier:

.. list-table::
   :header-rows: 1

   * - Unieconomy Companies Property
     - Tripletex Supplier Property
     - Tripletex Data Type


Unieconomy Customers to Tripletex Supplier
------------------------------------------
Before any synchronization can take place, a link between a Unieconomy Customers and a Tripletex Supplier must be established.

A Unieconomy Customers will merge with a Tripletex Supplier if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - Tripletex Supplier Property
   * - OrgNumber
     - organizationNumber

Once a link between a Unieconomy Customers and a Tripletex Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Customers and a Tripletex Supplier:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - Tripletex Supplier Property
     - Tripletex Data Type


Unieconomy Countries to Tripletex Country
-----------------------------------------
Every Unieconomy Countries will be synchronized with a Tripletex Country.

If a matching Tripletex Country already exists, the Unieconomy Countries will be merged with the existing one.
If no matching Tripletex Country is found, a new Tripletex Country will be created.

A Unieconomy Countries will merge with a Tripletex Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Countries Property
     - Tripletex Country Property
   * - Name
     - name
   * - CountryCode
     - isoAlpha2Code

Once a link between a Unieconomy Countries and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Countries and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - Unieconomy Countries Property
     - Tripletex Country Property
     - Tripletex Data Type


Unieconomy Currencycodes to Tripletex Currency
----------------------------------------------
Every Unieconomy Currencycodes will be synchronized with a Tripletex Currency.

If a matching Tripletex Currency already exists, the Unieconomy Currencycodes will be merged with the existing one.
If no matching Tripletex Currency is found, a new Tripletex Currency will be created.

A Unieconomy Currencycodes will merge with a Tripletex Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - Tripletex Currency Property
   * - Code
     - code

Once a link between a Unieconomy Currencycodes and a Tripletex Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Currencycodes and a Tripletex Currency:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - Tripletex Currency Property
     - Tripletex Data Type


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

