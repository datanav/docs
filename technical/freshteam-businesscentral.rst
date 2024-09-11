======================================
Freshteam to Business Central Dataflow
======================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to Businesscentral Companies
-------------------------------------------------
Every Freshteam Department will be synchronized with a Businesscentral Companies.

Once a link between a Freshteam Department and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Freshteam Employee to Business Employees
----------------------------------------
Every Freshteam Employee will be synchronized with a Business Employees.

Once a link between a Freshteam Employee and a Business Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Business Employees:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Business Employees Property
     - Business Data Type
   * - address.city
     - city
     - "string"
   * - address.country
     - country
     - "string"
   * - address.zip_code
     - postalCode
     - "string"
   * - communication_address.communication_city
     - city
     - "string"
   * - communication_address.communication_country
     - country
     - "string"
   * - communication_address.communication_zip_code
     - postalCode
     - "string"
   * - date_of_birth
     - birthDate
     - "string"
   * - designation
     - jobTitle
     - "string"
   * - first_name
     - givenName
     - "string"
   * - id
     - id
     - "string"
   * - last_name
     - surname
     - "string"
   * - official_email
     - email
     - "string"
   * - personal_email
     - email
     - "string"
   * - personal_email
     - personalEmail
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - mobilePhone
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.name)
     - phoneNumber
     - "string"

