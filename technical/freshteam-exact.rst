==================================
Freshteam to Exact Online Dataflow
==================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to Exact Online Accounts
---------------------------------------------
Every Freshteam Department will be synchronized with a Exact Online Accounts.

Once a link between a Freshteam Department and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Exact Online Accounts Property
     - Exact Online Data Type
   * - name
     - Name
     - "string"


Freshteam Employee to Exact Online Contacts
-------------------------------------------
Every Freshteam Employee will be synchronized with a Exact Online Contacts.

Once a link between a Freshteam Employee and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Exact Online Contacts Property
     - Exact Online Data Type
   * - address.city
     - City
     - "string"
   * - address.country
     - Country
     - "string"
   * - communication_address.communication_city
     - City
     - "string"
   * - communication_address.communication_country
     - Country
     - "string"
   * - date_of_birth
     - BirthDate
     - "string"
   * - first_name
     - FirstName
     - "string"
   * - last_name
     - LastName
     - "string"
   * - official_email
     - BusinessEmail
     - "string"
   * - personal_email
     - Email
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q4830453 in phone_numbers.name)
     - BusinessMobile
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - Mobile
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.name)
     - Phone
     - "string"


Freshteam Department to Exact Online Departments
------------------------------------------------
Every Freshteam Department will be synchronized with a Exact Online Departments.

Once a link between a Freshteam Department and a Exact Online Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Exact Online Departments:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Exact Online Departments Property
     - Exact Online Data Type


Freshteam Employee to Exact Online Employees
--------------------------------------------
Every Freshteam Employee will be synchronized with a Exact Online Employees.

Once a link between a Freshteam Employee and a Exact Online Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Exact Online Employees:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Exact Online Employees Property
     - Exact Online Data Type
   * - date_of_birth
     - BirthDate
     - "string"
   * - first_name
     - FirstName
     - "string"
   * - last_name
     - LastName
     - "string"
   * - official_email
     - BusinessEmail
     - "string"
   * - personal_email
     - Email
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - BusinessMobile
     - "string"
   * - phone_numbers.number (Dependant on having  in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.name)
     - Mobile
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.name)
     - Phone
     - "string"

