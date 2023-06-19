===============================
Freshteam to Tripletex Dataflow
===============================

Generated: 2023-06-19 09:22:34

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Tripletex Employee
----------------------------------------
Every Freshteam Employee will be synchronized with a Tripletex Employee.

If a matching Tripletex Employee already exists, the Freshteam Employee will be merged with the existing one.
If no matching Tripletex Employee is found, a new Tripletex Employee will be created.

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
   * - date_of_birth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"
   * - phone_numbers (Dependant on having wd:Q67372736 in phone_numbers.type)
     - phoneNumberHome
     - "string"
   * - phone_numbers (Dependant on having wd:Q17517 in phone_numbers.type)
     - phoneNumberMobile
     - "string"
   * - phone_numbers (Dependant on having wd:Q214995 in phone_numbers.type)
     - phoneNumberWork
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.type)
     - phoneNumberHome
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.type)
     - phoneNumberMobile
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.type)
     - phoneNumberWork
     - "string"
   * - phone_numbers.value (Dependant on having wd:Q67372736 in phone_numbers.type)
     - phoneNumberHome
     - "string"
   * - phone_numbers.value (Dependant on having wd:Q17517 in phone_numbers.type)
     - phoneNumberMobile
     - "string"
   * - phone_numbers.value (Dependant on having wd:Q214995 in phone_numbers.type)
     - phoneNumberWork
     - "string"

