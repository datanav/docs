===================================
Freshteam to PowerOfficeGo Dataflow
===================================

Generated: 2023-08-01 14:00:20

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to PowerOfficeGo Employee
--------------------------------------------
Every Freshteam Employee will be synchronized with a PowerOfficeGo Employee.

Once a link between a Freshteam Employee and a PowerOfficeGo Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a PowerOfficeGo Employee:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - PowerOfficeGo Employee Property
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
   * - first_name
     - FirstName
     - "string"
   * - last_name
     - LastName
     - "string"
   * - official_email
     - EmailAddress
     - "string"
   * - updated_at
     - LastChanged
     - "string"

