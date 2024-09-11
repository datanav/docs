=============================
Exact Online to Keap Dataflow
=============================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact Online to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ExactOnline Accounts to Keap Companies
--------------------------------------
Every ExactOnline Accounts will be synchronized with a Keap Companies.

Once a link between a ExactOnline Accounts and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Accounts and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - ExactOnline Accounts Property
     - Keap Companies Property
     - Keap Data Type
   * - Name
     - company_name
     - "string"
   * - Phone
     - phone_number.number
     - "string"


ExactOnline Contacts to Keap Contacts
-------------------------------------
Every ExactOnline Contacts will be synchronized with a Keap Contacts.

Once a link between a ExactOnline Contacts and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Contacts and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - ExactOnline Contacts Property
     - Keap Contacts Property
     - Keap Data Type
   * - BirthDate
     - birthday
     - "string"
   * - FirstName
     - family_name
     - "string"
   * - FirstName
     - given_name
     - "string"
   * - FullName
     - family_name
     - "string"
   * - FullName
     - given_name
     - "string"
   * - LastName
     - family_name
     - "string"
   * - LastName
     - given_name
     - "string"


ExactOnline Departments to Keap Companies
-----------------------------------------
Every ExactOnline Departments will be synchronized with a Keap Companies.

Once a link between a ExactOnline Departments and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Departments and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - ExactOnline Departments Property
     - Keap Companies Property
     - Keap Data Type


ExactOnline Divisions to Keap Companies
---------------------------------------
Every ExactOnline Divisions will be synchronized with a Keap Companies.

Once a link between a ExactOnline Divisions and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Divisions and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - ExactOnline Divisions Property
     - Keap Companies Property
     - Keap Data Type


ExactOnline Employees to Keap Contacts
--------------------------------------
Every ExactOnline Employees will be synchronized with a Keap Contacts.

Once a link between a ExactOnline Employees and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Employees and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - ExactOnline Employees Property
     - Keap Contacts Property
     - Keap Data Type
   * - BirthDate
     - birthday
     - "string"
   * - FirstName
     - family_name
     - "string"
   * - FirstName
     - given_name
     - "string"
   * - FullName
     - family_name
     - "string"
   * - FullName
     - given_name
     - "string"
   * - LastName
     - family_name
     - "string"
   * - LastName
     - given_name
     - "string"


ExactOnline Items to Keap Product
---------------------------------
Every ExactOnline Items will be synchronized with a Keap Product.

Once a link between a ExactOnline Items and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ExactOnline Items and a Keap Product:

.. list-table::
   :header-rows: 1

   * - ExactOnline Items Property
     - Keap Product Property
     - Keap Data Type

