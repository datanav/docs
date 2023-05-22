=================================
Freshteam to SuperOffice Dataflow
=================================

Generated: 2023-05-22 22:07:15

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to SuperOffice Person
----------------------------------------
Every Freshteam Employee will be synchronized with a SuperOffice Person.

Once a link between a Freshteam Employee and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - address.city
     - Address.Street.City
     - "string"
   * - address.country_code
     - Country.CountryId
     - "integer"
   * - address.zip_code
     - Address.Street.Zipcode
     - "string"
   * - communication_address.communication_city
     - Address.Postal.City
     - "string"
   * - communication_address.communication_country_code
     - Country.CountryId
     - "integer"
   * - communication_address.communication_zip_code
     - Address.Postal.Zipcode
     - "string"
   * - first_name
     - Firstname
     - "string"
   * - id
     - PersonId
     - "integer"
   * - last_name
     - Lastname
     - "string"

