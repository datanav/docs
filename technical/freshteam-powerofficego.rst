====================================
Freshteam to PowerOffice GO Dataflow
====================================

Generated: 2024-10-01 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to PowerOffice GO Employees
----------------------------------------------
Before any synchronization can take place, a link between a Freshteam Employee and a PowerOffice GO Employees must be established.

A Freshteam Employee will merge with a PowerOffice GO Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - PowerOffice GO Employees Property
   * - employee_id
     - Number

Once a link between a Freshteam Employee and a PowerOffice GO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a PowerOffice GO Employees:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - PowerOffice GO Employees Property
     - PowerOffice GO Data Type
   * - address.city
     - MailAddress.City
     - "string"
   * - address.country
     - MailAddress.CountryCode
     - "string"
   * - address.zip_code
     - MailAddress.ZipCode
     - "string"
   * - communication_address.communication_city
     - MailAddress.City
     - "string"
   * - communication_address.communication_country
     - MailAddress.CountryCode
     - "string"
   * - communication_address.communication_zip_code
     - MailAddress.ZipCode
     - "string"
   * - date_of_birth
     - DateOfBirth
     - N/A
   * - first_name
     - FirstName
     - "string"
   * - id
     - Id
     - "string"
   * - last_name
     - LastName
     - "string"
   * - official_email
     - EmailAddress
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - PhoneNumber
     - "string"


Freshteam Department to PowerOffice GO Departments
--------------------------------------------------
Every Freshteam Department will be synchronized with a PowerOffice GO Departments.

Once a link between a Freshteam Department and a PowerOffice GO Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a PowerOffice GO Departments:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - PowerOffice GO Departments Property
     - PowerOffice GO Data Type
   * - name
     - Name
     - "string"


Freshteam Employee to PowerOffice GO Employees
----------------------------------------------
Every Freshteam Employee will be synchronized with a PowerOffice GO Employees.

Once a link between a Freshteam Employee and a PowerOffice GO Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a PowerOffice GO Employees:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - PowerOffice GO Employees Property
     - PowerOffice GO Data Type
   * - official_email
     - EmailAddress
     - "string"

