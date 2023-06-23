===============================
Freshteam to Tripletex Dataflow
===============================

Generated: 2023-06-23 11:19:51

Introduction.
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


Freshteam Employee to Tripletex Contact
---------------------------------------
Every Freshteam Employee will be synchronized with a Tripletex Contact.

Once a link between a Freshteam Employee and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - first_name
     - firstName
     - "string"
   * - last_name
     - lastName
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - phoneNumberMobile
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.name)
     - phoneNumberWork
     - "string"

