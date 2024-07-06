=================================
Freshteam to Superoffice Dataflow
=================================

Generated: 2024-07-06 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Department to Superoffice Contact
-------------------------------------------
Every Freshteam Department will be synchronized with a Superoffice Contact.

Once a link between a Freshteam Department and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - name
     - Name
     - "string"


Freshteam Employee to Superoffice Person
----------------------------------------
Every Freshteam Employee will be synchronized with a Superoffice Person.

Once a link between a Freshteam Employee and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Superoffice Person Property
     - Superoffice Data Type
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

