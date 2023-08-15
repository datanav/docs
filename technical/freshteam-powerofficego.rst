===================================
Freshteam to PowerOfficeGo Dataflow
===================================

Generated: 2023-08-15 10:23:35

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to PowerOfficeGo Departments
-------------------------------------------------
Every Freshteam Department will be synchronized with a PowerOfficeGo Departments.

Once a link between a Freshteam Department and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type
   * - created_at
     - CreatedDateTimeOffset
     - "string"
   * - name
     - Name
     - "string"


Freshteam Employee to PowerOfficeGo Employees
---------------------------------------------
Every Freshteam Employee will be synchronized with a PowerOfficeGo Employees.

Once a link between a Freshteam Employee and a PowerOfficeGo Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a PowerOfficeGo Employees:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - PowerOfficeGo Employees Property
     - PowerOfficeGo Data Type
   * - communication_address.communication_city
     - MailAddress.City
     - "string"
   * - communication_address.communication_country_code
     - MailAddress.CountryCode
     - "string"
   * - communication_address.communication_zip_code
     - MailAddress.ZipCode
     - "string"
   * - date_of_birth
     - DateOfBirth
     - "string"
   * - date_of_birth
     - dateOfBirth
     - "string"
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
   * - official_email
     - emailAddress
     - "string"
   * - updated_at
     - LastChanged
     - "string"

