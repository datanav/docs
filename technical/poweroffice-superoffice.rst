===================================
Poweroffice to SuperOffice Dataflow
===================================

Generated: 2023-08-01 14:00:16

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Poweroffice to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Poweroffice Productgroup to SuperOffice Listproductcategoryitems
----------------------------------------------------------------
Before any synchronization can take place, a link between a Poweroffice Productgroup and a SuperOffice Listproductcategoryitems must be established.

A new SuperOffice Listproductcategoryitems will be created from a Poweroffice Productgroup if it is connected to a Poweroffice Product that is synchronized into SuperOffice.

Once a link between a Poweroffice Productgroup and a SuperOffice Listproductcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Productgroup and a SuperOffice Listproductcategoryitems:

.. list-table::
   :header-rows: 1

   * - Poweroffice Productgroup Property
     - SuperOffice Listproductcategoryitems Property
     - SuperOffice Data Type


Poweroffice Contactperson to SuperOffice Person
-----------------------------------------------
Every Poweroffice Contactperson will be synchronized with a SuperOffice Person.

Once a link between a Poweroffice Contactperson and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Contactperson and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Poweroffice Contactperson Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - city
     - Address.Postal.City
     - "string"
   * - dateOfBirth
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - firstName
     - Firstname
     - "string"
   * - id
     - PersonId
     - "integer"
   * - lastName
     - Lastname
     - "string"
   * - partyCustomerCode
     - Contact.ContactId
     - "integer"
   * - partySupplierCode
     - Contact.ContactId
     - "integer"
   * - phoneNumber
     - OfficePhones.Value
     - "string"
   * - residenceCountryCode
     - Country.CountryId
     - "integer"
   * - zipCode
     - Address.Postal.Zipcode
     - "string"


Poweroffice Customer to SuperOffice Contact
-------------------------------------------
Every Poweroffice Customer will be synchronized with a SuperOffice Contact.

Once a link between a Poweroffice Customer and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Customer and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - EmailAddress
     - Emails.Value
     - "string"
   * - LegalName
     - Name
     - "string"
   * - PhoneNumber
     - Phones.Value
     - "string"
   * - WebsiteUrl
     - Domains
     - "list"
   * - id
     - ContactId
     - "integer"
   * - mailAddress.address1
     - Address.Postal.Address1
     - "string"
   * - mailAddress.address2
     - Address.Postal.Address2
     - "string"
   * - mailAddress.address3
     - Address.Postal.Address3
     - "string"
   * - mailAddress.city
     - Address.Postal.City
     - "string"
   * - mailAddress.countryCode
     - Country.CountryId
     - "integer"
   * - mailAddress.zipCode
     - Address.Postal.Zipcode
     - "string"


Poweroffice Employee to SuperOffice Person
------------------------------------------
Every Poweroffice Employee will be synchronized with a SuperOffice Person.

Once a link between a Poweroffice Employee and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Employee and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Poweroffice Employee Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - DateOfBirth
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - FirstName
     - Firstname
     - "string"
   * - Id
     - PersonId
     - "integer"
   * - LastName
     - Lastname
     - "string"
   * - MailAddress.Address1
     - Address.Postal.Address1
     - "string"
   * - MailAddress.Address2
     - Address.Postal.Address2
     - "string"
   * - MailAddress.Address3
     - Address.Postal.Address3
     - "string"
   * - MailAddress.City
     - Address.Postal.City
     - "string"
   * - MailAddress.CountryCode
     - Country.CountryId
     - "integer"
   * - MailAddress.ZipCode
     - Address.Postal.Zipcode
     - "string"


Poweroffice Supplier to SuperOffice Contact
-------------------------------------------
Every Poweroffice Supplier will be synchronized with a SuperOffice Contact.

Once a link between a Poweroffice Supplier and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Supplier and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Poweroffice Supplier Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - EmailAddress
     - Emails.Value
     - "string"
   * - LegalName
     - Name
     - "string"
   * - PhoneNumber
     - Phones.Value
     - "string"
   * - WebsiteUrl
     - Domains
     - "list"

