===================================
Business Central to Trello Dataflow
===================================

Generated: 2024-09-11 11:40:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessCentral Companies to Trello Organizations
-------------------------------------------------
Every BusinessCentral Companies will be synchronized with a Trello Organizations.

Once a link between a BusinessCentral Companies and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Companies and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Companies Property
     - Trello Organizations Property
     - Trello Data Type


BusinessCentral Contacts person to Trello Members
-------------------------------------------------
Every BusinessCentral Contacts person will be synchronized with a Trello Members.

Once a link between a BusinessCentral Contacts person and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a Trello Members:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - Trello Members Property
     - Trello Data Type
   * - displayName
     - fullName
     - "string"
   * - email
     - email
     - "string"


BusinessCentral Customers person to Trello Members
--------------------------------------------------
Every BusinessCentral Customers person will be synchronized with a Trello Members.

Once a link between a BusinessCentral Customers person and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers person and a Trello Members:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers person Property
     - Trello Members Property
     - Trello Data Type
   * - displayName
     - fullName
     - "string"
   * - email
     - email
     - "string"


Business Central Customers company to Trello Organizations
----------------------------------------------------------
Every Business Central Customers company will be synchronized with a Trello Organizations.

Once a link between a Business Central Customers company and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - Trello Organizations Property
     - Trello Data Type
   * - displayName
     - name
     - "string"
   * - website
     - website
     - "string"


Business Central Employees to Trello Members
--------------------------------------------
Every Business Central Employees will be synchronized with a Trello Members.

Once a link between a Business Central Employees and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - Trello Members Property
     - Trello Data Type
   * - displayName
     - fullName
     - "string"
   * - personalEmail
     - email
     - "string"

