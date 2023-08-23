===========================
Asana to Tripletex Dataflow
===========================

Generated: 2023-08-23 09:03:51

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to Tripletex Customer
---------------------------------
Every Asana Teams will be synchronized with a Tripletex Customer.

Once a link between a Asana Teams and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - Tripletex Customer Property
     - Tripletex Data Type


Asana Projects to Tripletex Project
-----------------------------------
Every Asana Projects will be synchronized with a Tripletex Project.

Once a link between a Asana Projects and a Tripletex Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Projects and a Tripletex Project:

.. list-table::
   :header-rows: 1

   * - Asana Projects Property
     - Tripletex Project Property
     - Tripletex Data Type
   * - due_date
     - endDate
     - "datetime-format","%Y-%m-%d","_."]
   * - due_on
     - endDate
     - "datetime-format","%Y-%m-%d","_."]
   * - name
     - name
     - "string"
   * - owner.gid
     - projectManager.id
     - "integer"
   * - start_on
     - startDate
     - "datetime-format","%Y-%m-%d","_."]


Asana Users to Tripletex Employee
---------------------------------
Every Asana Users will be synchronized with a Tripletex Employee.

Once a link between a Asana Users and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Users and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Asana Users Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - email
     - email
     - "string"
   * - name
     - firstName
     - "string"

