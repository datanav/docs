====================================
PowerOffice GO to Freshteam Dataflow
====================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Departments to Freshteam Department
--------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a Freshteam Department.

Once a link between a PowerOffice GO Departments and a Freshteam Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Freshteam Department:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Freshteam Department Property
     - Freshteam Data Type
   * - CreatedDateTimeOffset
     - created_at
     - "string"
   * - Name
     - name
     - "string"


PowerOffice GO Employees to Freshteam Employee
----------------------------------------------
Every PowerOffice GO Employees will be synchronized with a Freshteam Employee.

If a matching Freshteam Employee already exists, the PowerOffice GO Employees will be merged with the existing one.
If no matching Freshteam Employee is found, a new Freshteam Employee will be created.

A PowerOffice GO Employees will merge with a Freshteam Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Freshteam Employee Property
   * - Number
     - employee_id

Once a link between a PowerOffice GO Employees and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - DateOfBirth
     - date_of_birth
     - "string"
   * - DepartmentId (Dependant on having wd:Q703534 in JobTitle)
     - designation
     - "string"
   * - EmailAddress
     - official_email
     - "string"
   * - EmailAddress
     - personal_email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - Id
     - id
     - "string"
   * - JobTitle
     - designation
     - "string"
   * - LastChanged
     - updated_at
     - "string"
   * - LastName
     - last_name
     - "string"
   * - MailAddress.City
     - address.city
     - "string"
   * - MailAddress.City
     - communication_address.communication_city
     - "string"
   * - MailAddress.CountryCode
     - Billing_Country
     - "string"
   * - MailAddress.CountryCode
     - Shipping_Country
     - "string"
   * - MailAddress.CountryCode
     - address.country
     - "string"
   * - MailAddress.CountryCode
     - address.country_code
     - "string"
   * - MailAddress.CountryCode
     - communication_address.communication_country
     - "string"
   * - MailAddress.CountryCode
     - communication_address.communication_country_code
     - "string"
   * - MailAddress.ZipCode
     - address.zip_code
     - "string"
   * - MailAddress.ZipCode
     - communication_address.communication_zip_code
     - "string"
   * - MailAddress.city
     - address.city
     - "string"
   * - MailAddress.city
     - communication_address.communication_city
     - "string"
   * - MailAddress.countryCode
     - address.country_code
     - "string"
   * - MailAddress.countryCode
     - communication_address.communication_country_code
     - "string"
   * - MailAddress.zipCode
     - address.zip_code
     - "string"
   * - MailAddress.zipCode
     - communication_address.communication_zip_code
     - "string"
   * - PhoneNumber
     - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.name)
     - "string"
   * - dateOfBirth
     - date_of_birth
     - "string"
   * - emailAddress
     - official_email
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"

