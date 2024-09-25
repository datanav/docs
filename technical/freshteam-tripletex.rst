===============================
Freshteam to Tripletex Dataflow
===============================

Generated: 2024-09-25 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Tripletex Employee
----------------------------------------
Before any synchronization can take place, a link between a Freshteam Employee and a Tripletex Employee must be established.

A Freshteam Employee will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Tripletex Employee Property
   * - employee_id
     - employeeNumber

Once a link between a Freshteam Employee and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Tripletex Employee Property
     - Tripletex Data Type


Freshteam Department to Tripletex Department
--------------------------------------------
Every Freshteam Department will be synchronized with a Tripletex Department.

Once a link between a Freshteam Department and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - name
     - name
     - "string"


Freshteam Employee to Tripletex Employee
----------------------------------------
Every Freshteam Employee will be synchronized with a Tripletex Employee.

Once a link between a Freshteam Employee and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - date_of_birth
     - dateOfBirth
     - N/A
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"
   * - official_email
     - email
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.name)
     - phoneNumberHome
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - phoneNumberMobile
     - N/A
   * - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.name)
     - phoneNumberWork
     - "string"

