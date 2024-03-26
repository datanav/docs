======================
Tripletex to  Dataflow
======================

Generated: 2024-03-26 13:42:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Department to  Department
-----------------------------------
Every Tripletex Department will be synchronized with a  Department.

Once a link between a Tripletex Department and a  Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Department:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Department Property
     -  Data Type
   * - changes.timestamp
     - created_at
     - "string"
   * - name
     - name
     - "string"


Tripletex Employee to  Employee
-------------------------------
Every Tripletex Employee will be synchronized with a  Employee.

If a matching  Employee already exists, the Tripletex Employee will be merged with the existing one.
If no matching  Employee is found, a new  Employee will be created.

A Tripletex Employee will merge with a  Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Employee Property
   * - employeeNumber
     - employee_id

Once a link between a Tripletex Employee and a  Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Employee:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Employee Property
     -  Data Type
   * - dateOfBirth
     - date_of_birth
     - "string"
   * - department.id (Dependant on having wd:Q703534 in  )
     - designation
     - "string"
   * - email
     - official_email
     - "string"
   * - email
     - personal_email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - last_name
     - "string"
   * - phoneNumberHome
     - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.name)
     - "string"
   * - phoneNumberMobile
     - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.name)
     - "string"
   * - phoneNumberWork
     - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.name)
     - "string"

