==================================
BusinessCentral to Trello Dataflow
==================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessCentral to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Companies to Trello Organizations
------------------------------------------
Every Business Companies will be synchronized with a Trello Organizations.

Once a link between a Business Companies and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Companies and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - Business Companies Property
     - Trello Organizations Property
     - Trello Data Type


Business Contacts person to Trello Members
------------------------------------------
Every Business Contacts person will be synchronized with a Trello Members.

Once a link between a Business Contacts person and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Contacts person and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Business Contacts person Property
     - Trello Members Property
     - Trello Data Type
   * - displayName
     - fullName
     - "string"
   * - email
     - email
     - "string"


Business Customers person to Trello Members
-------------------------------------------
Every Business Customers person will be synchronized with a Trello Members.

Once a link between a Business Customers person and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Customers person and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Business Customers person Property
     - Trello Members Property
     - Trello Data Type
   * - displayName
     - fullName
     - "string"
   * - email
     - email
     - "string"


BusinessCentral Customers company to Trello Organizations
---------------------------------------------------------
Every BusinessCentral Customers company will be synchronized with a Trello Organizations.

Once a link between a BusinessCentral Customers company and a Trello Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers company and a Trello Organizations:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers company Property
     - Trello Organizations Property
     - Trello Data Type
   * - displayName
     - name
     - "string"
   * - website
     - website
     - "string"


BusinessCentral Employees to Trello Members
-------------------------------------------
Every BusinessCentral Employees will be synchronized with a Trello Members.

Once a link between a BusinessCentral Employees and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Employees and a Trello Members:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Employees Property
     - Trello Members Property
     - Trello Data Type
   * - displayName
     - fullName
     - "string"
   * - personalEmail
     - email
     - "string"

