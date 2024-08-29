======================
Freshteam to  Dataflow
======================

Generated: 2024-08-29 12:48:38

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to  Accounts
---------------------------------
Every Freshteam Department will be synchronized with a  Accounts.

Once a link between a Freshteam Department and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     -  Accounts Property
     -  Data Type
   * - name
     - Name
     - "string"


Freshteam Employee to  Contacts
-------------------------------
Every Freshteam Employee will be synchronized with a  Contacts.

Once a link between a Freshteam Employee and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     -  Contacts Property
     -  Data Type
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

