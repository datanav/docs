=================================
Freshteam to SuperOffice Dataflow
=================================

Generated: 2023-06-19 11:58:35

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to SuperOffice Contact
-------------------------------------------
Every Freshteam Department will be synchronized with a SuperOffice Contact.

Once a link between a Freshteam Department and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"


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
   * - date_of_birth
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - first_name
     - Firstname
     - "string"
   * - id
     - PersonId
     - "integer"
   * - last_name
     - Lastname
     - "string"
   * - phone_numbers (Dependant on having wd:Q17517 in phone_numbers.type)
     - MobilePhones.Value
     - "string"
   * - phone_numbers (Dependant on having wd:Q214995 in phone_numbers.type)
     - OfficePhones.Value
     - "string"
   * - phone_numbers (Dependant on having wd:Q67372736 in phone_numbers.type)
     - PrivatePhones.Value
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.type)
     - MobilePhones.Value
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.type)
     - OfficePhones.Value
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.type)
     - PrivatePhones.Value
     - "string"
   * - phone_numbers.value (Dependant on having wd:Q17517 in phone_numbers.type)
     - MobilePhones.Value
     - "string"
   * - phone_numbers.value (Dependant on having wd:Q214995 in phone_numbers.type)
     - OfficePhones.Value
     - "string"
   * - phone_numbers.value (Dependant on having wd:Q67372736 in phone_numbers.type)
     - PrivatePhones.Value
     - "string"

