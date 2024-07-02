=====================================
Businesscentral to Freshteam Dataflow
=====================================

Generated: 2024-07-02 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Employees to Freshteam Employee
-----------------------------------------------
Every Businesscentral Employees will be synchronized with a Freshteam Employee.

Once a link between a Businesscentral Employees and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - birthDate
     - date_of_birth
     - "string"
   * - email
     - official_email
     - "string"
   * - email
     - personal_email
     - "string"
   * - givenName
     - first_name
     - "string"
   * - jobTitle
     - designation
     - "string"
   * - mobilePhone
     - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - "string"
   * - personalEmail
     - personal_email
     - "string"
   * - phoneNumber
     - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.name)
     - "string"
   * - surname
     - last_name
     - "string"

