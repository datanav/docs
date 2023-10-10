===================================
Powerofficego to Freshteam Dataflow
===================================

Generated: 2023-10-10 20:55:48

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to Freshteam Employee
-------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Freshteam Employee.

Once a link between a Powerofficego Contactperson and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - dateOfBirth
     - date_of_birth
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"
   * - partyId
     - designation
     - "string"
   * - phoneNumber
     - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.name)
     - "string"


Powerofficego Departments to Freshteam Department
-------------------------------------------------
Every Powerofficego Departments will be synchronized with a Freshteam Department.

Once a link between a Powerofficego Departments and a Freshteam Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Freshteam Department:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Freshteam Department Property
     - Freshteam Data Type
   * - CreatedDateTimeOffset
     - created_at
     - "string"
   * - Name
     - name
     - "string"


Powerofficego Employees to Freshteam Employee
---------------------------------------------
Every Powerofficego Employees will be synchronized with a Freshteam Employee.

Once a link between a Powerofficego Employees and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - DateOfBirth
     - date_of_birth
     - "string"
   * - DepartmentId
     - designation
     - "string"
   * - EmailAddress
     - official_email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - Id
     - id
     - "string"
   * - LastChanged
     - updated_at
     - "string"
   * - LastName
     - last_name
     - "string"
   * - MailAddress.City
     - communication_address.communication_city
     - "string"
   * - MailAddress.CountryCode
     - communication_address.communication_country_code
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

