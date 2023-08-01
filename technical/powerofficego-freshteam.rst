===================================
Powerofficego to Freshteam Dataflow
===================================

Generated: 2023-08-01 14:00:20

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Employee to Freshteam Employee
--------------------------------------------
Every Powerofficego Employee will be synchronized with a Freshteam Employee.

Once a link between a Powerofficego Employee and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employee and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - DateOfBirth
     - date_of_birth
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
   * - id
     - id
     - "string"

