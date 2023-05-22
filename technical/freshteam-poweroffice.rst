=================================
Freshteam to PowerOffice Dataflow
=================================

Generated: 2023-05-22 22:07:15

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to PowerOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to PowerOffice Employee
------------------------------------------
Every Freshteam Employee will be synchronized with a PowerOffice Employee.

Once a link between a Freshteam Employee and a PowerOffice Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a PowerOffice Employee:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - PowerOffice Employee Property
     - PowerOffice Data Type
   * - communication_address.communication_city
     - MailAddress.City
     - "string"
   * - communication_address.communication_country_code
     - MailAddress.CountryCode
     - "string"
   * - communication_address.communication_zip_code
     - MailAddress.ZipCode
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

