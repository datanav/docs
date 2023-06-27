===============================
Tripletex to Freshteam Dataflow
===============================

Generated: 2023-06-27 11:28:38

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
   * - address.city
     - address.city
     - "string"
   * - address.country.id
     - address.country_code
     - "string"
   * - address.postalCode
     - address.zip_code
     - "string"
   * - dateOfBirth
     - date_of_birth
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
     - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.name)
     - "string"
   * - phoneNumberMobile
     - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.name)
     - "string"
   * - phoneNumberWork
     - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.name)
     - "string"

