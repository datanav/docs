===============================
Tripletex to Freshteam Dataflow
===============================

Generated: 2024-09-24 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Employee to Freshteam Employee
----------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a Freshteam Employee must be established.

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
   * - dateOfBirth
     - date_of_birth
     - "string"
   * - email
     - official_email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"
   * - phoneNumberHome
     - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.name)
     - "string"
   * - phoneNumberMobile
     - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - "string"
   * - phoneNumberWork
     - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.name)
     - "string"


Tripletex Department to Freshteam Department
--------------------------------------------
Every Tripletex Department will be synchronized with a Freshteam Department.

Once a link between a Tripletex Department and a Freshteam Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Freshteam Department:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Freshteam Department Property
     - Freshteam Data Type


Tripletex Employee to Freshteam Employee
----------------------------------------
Every Tripletex Employee will be synchronized with a Freshteam Employee.

Once a link between a Tripletex Employee and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - email
     - official_email
     - "string"

