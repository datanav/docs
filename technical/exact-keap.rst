======================
Exact to Keap Dataflow
======================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Accounts to Keap Companies
--------------------------------
Every Exact Accounts will be synchronized with a Keap Companies.

Once a link between a Exact Accounts and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Accounts and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Exact Accounts Property
     - Keap Companies Property
     - Keap Data Type
   * - Name
     - company_name
     - "string"
   * - Phone
     - phone_number.number
     - "string"


Exact Contacts to Keap Contacts
-------------------------------
Every Exact Contacts will be synchronized with a Keap Contacts.

Once a link between a Exact Contacts and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Contacts and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Exact Contacts Property
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


Exact Departments to Keap Companies
-----------------------------------
Every Exact Departments will be synchronized with a Keap Companies.

Once a link between a Exact Departments and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Departments and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Exact Departments Property
     - Keap Companies Property
     - Keap Data Type


Exact Divisions to Keap Companies
---------------------------------
Every Exact Divisions will be synchronized with a Keap Companies.

Once a link between a Exact Divisions and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Divisions and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Exact Divisions Property
     - Keap Companies Property
     - Keap Data Type


Exact Employees to Keap Contacts
--------------------------------
Every Exact Employees will be synchronized with a Keap Contacts.

Once a link between a Exact Employees and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Employees and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Exact Employees Property
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


Exact Items to Keap Product
---------------------------
Every Exact Items will be synchronized with a Keap Product.

Once a link between a Exact Items and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     - Keap Product Property
     - Keap Data Type

