===================================
Freshteam to Powerofficego Dataflow
===================================

Generated: 2024-06-29 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to Powerofficego Departments
-------------------------------------------------
Every Freshteam Department will be synchronized with a Powerofficego Departments.

Once a link between a Freshteam Department and a Powerofficego Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Powerofficego Departments:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Powerofficego Departments Property
     - Powerofficego Data Type
   * - created_at
     - CreatedDateTimeOffset
     - "string"
   * - name
     - Name
     - "string"


Freshteam Employee to Powerofficego Employees
---------------------------------------------
Every Freshteam Employee will be synchronized with a Powerofficego Employees.

If a matching Powerofficego Employees already exists, the Freshteam Employee will be merged with the existing one.
If no matching Powerofficego Employees is found, a new Powerofficego Employees will be created.

A Freshteam Employee will merge with a Powerofficego Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Powerofficego Employees Property
   * - employee_id
     - Number

Once a link between a Freshteam Employee and a Powerofficego Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Powerofficego Employees:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Powerofficego Employees Property
     - Powerofficego Data Type
   * - Billing_Country
     - MailAddress.CountryCode
     - "string"
   * - Shipping_Country
     - MailAddress.CountryCode
     - "string"
   * - address.city
     - MailAddress.City
     - "string"
   * - address.city
     - MailAddress.city
     - "string"
   * - address.country
     - MailAddress.CountryCode
     - "string"
   * - address.country_code
     - MailAddress.CountryCode
     - "string"
   * - address.country_code
     - MailAddress.countryCode
     - "string"
   * - address.zip_code
     - MailAddress.ZipCode
     - "string"
   * - address.zip_code
     - MailAddress.zipCode
     - "string"
   * - communication_address.communication_city
     - MailAddress.City
     - "string"
   * - communication_address.communication_city
     - MailAddress.city
     - "string"
   * - communication_address.communication_country
     - MailAddress.CountryCode
     - "string"
   * - communication_address.communication_country_code
     - MailAddress.CountryCode
     - "string"
   * - communication_address.communication_country_code
     - MailAddress.countryCode
     - "string"
   * - communication_address.communication_zip_code
     - MailAddress.ZipCode
     - "string"
   * - communication_address.communication_zip_code
     - MailAddress.zipCode
     - "string"
   * - created_at
     - EmployeeCreatedDateTimeOffset
     - "string"
   * - created_at
     - employeeCreatedDateTimeOffset
     - "string"
   * - date_of_birth
     - DateOfBirth
     - N/A
   * - date_of_birth
     - dateOfBirth
     - "string"
   * - designation
     - DepartmentId (Dependant on having wd:Q703534 in JobTitle)
     - "string"
   * - designation
     - JobTitle
     - "string"
   * - employee_id
     - Number
     - "string"
   * - first_name
     - FirstName
     - "string"
   * - first_name
     - firstName
     - "string"
   * - id
     - Id
     - "string"
   * - last_name
     - LastName
     - "string"
   * - last_name
     - lastName
     - "string"
   * - official_email
     - EmailAddress
     - "string"
   * - official_email
     - emailAddress
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.name)
     - PhoneNumber
     - "string"
   * - updated_at
     - LastChanged
     - "string"

