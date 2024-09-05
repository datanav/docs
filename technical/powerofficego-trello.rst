================================
Powerofficego to Trello Dataflow
================================

Generated: 2024-09-05 12:11:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to  Members
---------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Members.

Once a link between a Powerofficego Contactperson and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Members:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Members Property
     -  Data Type
   * - emailAddress
     - email
     - "string"


Powerofficego Customers person to  Members
------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Members.

Once a link between a Powerofficego Customers person and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Members:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Members Property
     -  Data Type
   * - EmailAddress
     - email
     - "string"


Powerofficego Customers to  Organizations
-----------------------------------------
Every Powerofficego Customers will be synchronized with a  Organizations.

Once a link between a Powerofficego Customers and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Organizations Property
     -  Data Type
   * - Name
     - name
     - "string"
   * - WebsiteUrl
     - website
     - "string"


Powerofficego Departments to  Organizations
-------------------------------------------
Every Powerofficego Departments will be synchronized with a  Organizations.

Once a link between a Powerofficego Departments and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Organizations Property
     -  Data Type
   * - Name
     - name
     - "string"


Powerofficego Projects to  Actions
----------------------------------
Every Powerofficego Projects will be synchronized with a  Actions.

Once a link between a Powerofficego Projects and a  Actions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Projects and a  Actions:

.. list-table::
   :header-rows: 1

   * - Powerofficego Projects Property
     -  Actions Property
     -  Data Type
   * - ProjectManagerEmployeeId
     - memberCreator.id
     - "string"
   * - StartDate
     - date
     - "string"


Powerofficego Projects to  Boards
---------------------------------
Every Powerofficego Projects will be synchronized with a  Boards.

Once a link between a Powerofficego Projects and a  Boards is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Projects and a  Boards:

.. list-table::
   :header-rows: 1

   * - Powerofficego Projects Property
     -  Boards Property
     -  Data Type
   * - Name
     - name
     - "string"


Powerofficego Employees to Trello Members
-----------------------------------------
Every Powerofficego Employees will be synchronized with a Trello Members.

Once a link between a Powerofficego Employees and a Trello Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Trello Members:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Trello Members Property
     - Trello Data Type
   * - EmailAddress
     - email
     - "string"

