=================================
Freshteam to ExactOnline Dataflow
=================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to Exact Accounts
--------------------------------------
Every Freshteam Department will be synchronized with a Exact Accounts.

Once a link between a Freshteam Department and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Exact Accounts Property
     - Exact Data Type
   * - name
     - Name
     - "string"


Freshteam Employee to Exact Contacts
------------------------------------
Every Freshteam Employee will be synchronized with a Exact Contacts.

Once a link between a Freshteam Employee and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Exact Contacts Property
     - Exact Data Type
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


Freshteam Department to ExactOnline Departments
-----------------------------------------------
Every Freshteam Department will be synchronized with a ExactOnline Departments.

Once a link between a Freshteam Department and a ExactOnline Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a ExactOnline Departments:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - ExactOnline Departments Property
     - ExactOnline Data Type


Freshteam Employee to ExactOnline Employees
-------------------------------------------
Every Freshteam Employee will be synchronized with a ExactOnline Employees.

Once a link between a Freshteam Employee and a ExactOnline Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a ExactOnline Employees:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - ExactOnline Employees Property
     - ExactOnline Data Type
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

