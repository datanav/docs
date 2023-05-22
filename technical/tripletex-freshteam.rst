===============================
Tripletex to Freshteam Dataflow
===============================

Generated: 2023-05-22 22:07:15

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Employee to Freshteam Employee
----------------------------------------
Every Tripletex Employee will be synchronized with a Freshteam Employee.

If a matching Freshteam Employee already exists, the Tripletex Employee will be merged with the existing one.
If no matching Freshteam Employee is found, a new Freshteam Employee will be created.

A Tripletex Employee will merge with a Freshteam Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Freshteam Employee Property
   * - employeeNumber
     - employee_id

Once a link between a Tripletex Employee and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"

