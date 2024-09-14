=================================
Freshteam to SuperOffice Dataflow
=================================

Generated: 2024-09-14 00:00:00

Introduction
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
     - N/A
   * - designation
     - Contact.ContactId
     - "integer"
   * - first_name
     - Firstname
     - "string"
   * - id
     - PersonId
     - "integer"
   * - last_name
     - Lastname
     - "string"
   * - personal_email
     - Emails.Value
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.name)
     - MobilePhones.Value
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.name)
     - OfficePhones.Value
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.name)
     - PrivatePhones.Value
     - "string"

