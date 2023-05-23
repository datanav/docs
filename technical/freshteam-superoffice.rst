=================================
Freshteam to SuperOffice Dataflow
=================================

Generated: 2023-05-23 06:26:42

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to SuperOffice Contact
-----------------------------------------
Every Tripletex Customer will be synchronized with a SuperOffice Contact.

If a matching SuperOffice Contact already exists, the Tripletex Customer will be merged with the existing one.
If no matching SuperOffice Contact is found, a new SuperOffice Contact will be created.

A Tripletex Customer will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - SuperOffice Contact Property
   * - email
     - Emails.Value
   * - invoiceEmail
     - Emails.Value
   * - overdueNoticeEmail
     - Emails.Value

Once a link between a Tripletex Customer and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - deliveryAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - deliveryAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - deliveryAddress.changes
     - Address.Postal.City
     - "string"
   * - deliveryAddress.city
     - Country.CountryId
     - "integer"
   * - deliveryAddress.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - id
     - ContactId
     - "integer"
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrgNr (Dependant on having NOR in Country.ThreeLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountry)
     - "string"
   * - phoneNumber
     - Phones.Value
     - "string"
   * - physicalAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - physicalAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - physicalAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - physicalAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - physicalAddress.city
     - Address.Postal.City
     - "string"
   * - physicalAddress.city
     - Address.Street.City
     - "string"
   * - physicalAddress.country.id
     - Country.CountryId
     - "integer"
   * - physicalAddress.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - physicalAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - postalAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - postalAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - postalAddress.city
     - Address.Postal.City
     - "string"
   * - postalAddress.country.id
     - Country.CountryId
     - "integer"
   * - postalAddress.postalCode
     - Address.Postal.Zipcode
     - "string"


HubSpot Department to SuperOffice Contact
-----------------------------------------
Every HubSpot Department will be synchronized with a SuperOffice Contact.

Once a link between a HubSpot Department and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Department and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Department Property
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
   * - first_name
     - Firstname
     - "string"
   * - id
     - PersonId
     - "integer"
   * - last_name
     - Lastname
     - "string"

