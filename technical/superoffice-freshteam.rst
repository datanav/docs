=================================
SuperOffice to Freshteam Dataflow
=================================

Generated: 2023-11-09 12:49:17

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to Freshteam Employee
----------------------------------------
Every SuperOffice Person will be synchronized with a Freshteam Employee.

Once a link between a SuperOffice Person and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - Address.Postal.City
     - communication_address.communication_city
     - "string"
   * - Address.Postal.Zipcode
     - communication_address.communication_zip_code
     - "string"
   * - Address.Street.City
     - address.city
     - "string"
   * - Address.Street.Zipcode
     - address.zip_code
     - "string"
   * - BirthDate
     - date_of_birth
     - "string"
   * - Contact.ContactId
     - designation
     - "string"
   * - Country.CountryId
     - address.country_code
     - "string"
   * - Country.CountryId
     - communication_address.communication_country_code
     - "string"
   * - Firstname
     - first_name
     - "string"
   * - Lastname
     - last_name
     - "string"
   * - MobilePhones.Value
     - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.name)
     - "string"
   * - OfficePhones.Value
     - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.name)
     - "string"
   * - PersonId
     - id
     - "string"
   * - PrivatePhones.Value
     - phone_numbers.number (Dependant on having wd:Q67372736 in phone_numbers.nameDependant on having wd:Q67372736 in phone_numbers.name)
     - "string"


SuperOffice Ownercontactlink to Freshteam Department
----------------------------------------------------
Every SuperOffice Ownercontactlink will be synchronized with a Freshteam Department.

Once a link between a SuperOffice Ownercontactlink and a Freshteam Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a Freshteam Department:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - Freshteam Department Property
     - Freshteam Data Type
   * - name
     - name
     - "string"


SuperOffice User to Freshteam Employee
--------------------------------------
Every SuperOffice User will be synchronized with a Freshteam Employee.

Once a link between a SuperOffice User and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - contactCategory
     - Billing_Country
     - "string"
   * - contactCategory
     - Shipping_Country
     - "string"
   * - contactId
     - designation
     - "string"
   * - firstName
     - first_name
     - "string"
   * - lastName
     - last_name
     - "string"

