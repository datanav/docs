===========================
Asana to Tripletex Dataflow
===========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
   * - completed_at
     - endDate
     - N/A
   * - due_date
     - endDate
     - N/A
   * - due_on
     - endDate
     - N/A
   * - name
     - name
     - "string"
   * - owner.gid
     - projectManager.id
     - "integer"
   * - start_on
     - startDate
     - N/A


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
   * - workspaces.gid
     - department.id
     - N/A

