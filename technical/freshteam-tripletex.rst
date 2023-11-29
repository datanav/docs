======================
Freshteam to  Dataflow
======================

Generated: 2023-11-29 23:37:13

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to  Department
-----------------------------------
Every Freshteam Department will be synchronized with a  Department.

Once a link between a Freshteam Department and a  Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a  Department:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     -  Department Property
     -  Data Type
   * - name
     - name
     - "string"


Freshteam Employee to  Employee
-------------------------------
Every Freshteam Employee will be synchronized with a  Employee.

If a matching  Employee already exists, the Freshteam Employee will be merged with the existing one.
If no matching  Employee is found, a new  Employee will be created.

A Freshteam Employee will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     -  Employee Property
   * - employee_id
     - employeeNumber

Once a link between a Freshteam Employee and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a  Employee:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     -  Employee Property
     -  Data Type
   * - date_of_birth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - designation
     - department.id
     - "if", "neq", "_.", "X"], "integer", "string"]
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"
   * - official_email
     - email
     - "string"
   * - personal_email
     - email
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.name)
     - phoneNumberHome
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.name)
     - phoneNumberMobile
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.name)
     - phoneNumberWork
     - "string"

