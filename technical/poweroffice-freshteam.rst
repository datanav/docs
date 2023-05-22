=================================
Poweroffice to Freshteam Dataflow
=================================

Generated: 2023-05-22 22:07:15

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Poweroffice to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Poweroffice Employee to Freshteam Employee
------------------------------------------
Every Poweroffice Employee will be synchronized with a Freshteam Employee.

Once a link between a Poweroffice Employee and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Employee and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Poweroffice Employee Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - EmailAddress
     - official_email
     - "string"
   * - FirstName
     - first_name
     - "string"
   * - Id
     - id
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

