===================================
SuperOffice to SuperOffice Dataflow
===================================

Generated: 2024-09-12 13:14:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to SuperOffice Contact
------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a SuperOffice Contact must be established.

A SuperOffice Contact will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - SuperOffice Contact Property
   * - ContactId
     - ContactId
   * - Emails.Value
     - Emails.Value

Once a link between a SuperOffice Contact and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Address.Postal.Address1
     - Address.Postal.Address1
     - "string"
   * - Address.Postal.Address1
     - Address.Street.Address1
     - "string"
   * - Address.Postal.Address2
     - Address.Postal.Address2
     - "string"
   * - Address.Postal.Address2
     - Address.Street.Address2
     - "string"
   * - Address.Postal.Address3
     - Address.Postal.Address3
     - "string"
   * - Address.Postal.Address3
     - Address.Street.Address3
     - "string"
   * - Address.Postal.City
     - Address.Postal.City
     - "string"
   * - Address.Postal.City
     - Address.Street.City
     - "string"
   * - Address.Postal.Zipcode
     - Address.Postal.Zipcode
     - "string"
   * - Address.Postal.Zipcode
     - Address.Street.Zipcode
     - "string"
   * - Address.Street.Address1
     - Address.Postal.Address1
     - "string"
   * - Address.Street.Address1
     - Address.Street.Address1
     - "string"
   * - Address.Street.Address2
     - Address.Postal.Address2
     - "string"
   * - Address.Street.Address2
     - Address.Street.Address2
     - "string"
   * - Address.Street.Address3
     - Address.Postal.Address3
     - "string"
   * - Address.Street.Address3
     - Address.Street.Address3
     - "string"
   * - Address.Street.City
     - Address.Postal.City
     - "string"
   * - Address.Street.City
     - Address.Street.City
     - "string"
   * - Address.Street.Zipcode
     - Address.Postal.Zipcode
     - "string"
   * - Address.Street.Zipcode
     - Address.Street.Zipcode
     - "string"
   * - ContactId
     - ContactId
     - "integer"
   * - Country.CountryId
     - Country.CountryId
     - N/A
   * - Country.ThreeLetterISOCountry
     - OrgNr (Dependant on having wd:Q906278 in Country.TwoLetterISOCountryDependant on having wd:Q906278 in Country.ThreeLetterISOCountryDependant on having wd:Q906278 in Country.ThreeLetterISOCountryDependant on having wd:Q906278 in Country.ThreeLetterISOCountryDependant on having wd:Q906278 in Country.TwoLetterISOCountryDependant on having wd:Q906278 in Country.ThreeLetterISOCountry)
     - "string"
   * - Domains
     - Domains
     - N/A
   * - Emails.Value
     - Emails.Value
     - "string"
   * - Name
     - Name
     - "string"
   * - OrgNr
     - OrgNr (Dependant on having  in Country.ThreeLetterISOCountryDependant on having  in Country.ThreeLetterISOCountry)
     - "string"
   * - Phones.Value
     - Phones.Value
     - "string"


SuperOffice Ownercontactlink to SuperOffice Contact
---------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Ownercontactlink and a SuperOffice Contact must be established.

A SuperOffice Ownercontactlink will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - SuperOffice Contact Property
   * - contact_id
     - ContactId

Once a link between a SuperOffice Ownercontactlink and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - contact_id
     - ContactId
     - "string"
   * - name
     - Name
     - "string"


SuperOffice Person to SuperOffice Person
----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a SuperOffice Person must be established.

A SuperOffice Person will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - SuperOffice Person Property
   * - Emails.Value
     - Emails.Value

Once a link between a SuperOffice Person and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - Address.Postal.Address1
     - Address.Postal.Address1
     - "string"
   * - Address.Postal.Address2
     - Address.Postal.Address2
     - "string"
   * - Address.Postal.Address3
     - Address.Postal.Address3
     - "string"
   * - Address.Postal.City
     - Address.Postal.City
     - "string"
   * - Address.Postal.Zipcode
     - Address.Postal.Zipcode
     - "string"
   * - Address.Street.Address1
     - Address.Street.Address1
     - "string"
   * - Address.Street.Address2
     - Address.Street.Address2
     - "string"
   * - Address.Street.Address3
     - Address.Street.Address3
     - "string"
   * - Address.Street.City
     - Address.Street.City
     - "string"
   * - Address.Street.Zipcode
     - Address.Street.Zipcode
     - "string"
   * - BirthDate
     - BirthDate
     - N/A
   * - Contact.ContactId
     - Contact.ContactId
     - "integer"
   * - Country.CountryId
     - Country.CountryId
     - "integer"
   * - Emails.Value
     - Emails.Value
     - "string"
   * - Firstname
     - Firstname
     - "string"
   * - Lastname
     - Lastname
     - "string"
   * - MobilePhones.Value
     - MobilePhones.Value
     - "string"
   * - OfficePhones.Value
     - OfficePhones.Value
     - "string"
   * - PersonId
     - PersonId
     - "integer"
   * - PrivatePhones.Value
     - PrivatePhones.Value
     - "string"


SuperOffice Product to SuperOffice Product
------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Product and a SuperOffice Product must be established.

A SuperOffice Product will merge with a SuperOffice Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - SuperOffice Product Property
   * - ProductId
     - ProductId
   * - ERPProductKey
     - ERPProductKey

Once a link between a SuperOffice Product and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - Description
     - Description
     - "string"
   * - ERPPriceListKey
     - ERPPriceListKey
     - "string"
   * - Name
     - Name
     - "string"
   * - ProductCategoryKey
     - ProductCategoryKey
     - "string"
   * - ProductFamilyKey
     - ProductFamilyKey
     - "string"
   * - ProductId
     - ProductId
     - "integer"
   * - ProductTypeKey
     - ProductTypeKey
     - "string"
   * - QuantityUnit
     - QuantityUnit
     - "string"
   * - Supplier
     - Supplier
     - "string"
   * - UnitCost
     - UnitCost
     - "string"
   * - UnitListPrice
     - UnitListPrice
     - N/A
   * - Url
     - Url
     - "string"
   * - VAT
     - VAT
     - "integer"


SuperOffice Quote to SuperOffice Sale
-------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quote and a SuperOffice Sale must be established.

A SuperOffice Quote will merge with a SuperOffice Sale if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     - SuperOffice Sale Property
   * - SaleId
     - SaleId

Once a link between a SuperOffice Quote and a SuperOffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quote and a SuperOffice Sale:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     - SuperOffice Sale Property
     - SuperOffice Data Type
   * - AcceptedQuoteAlternativeId
     - Status
     - "string"


SuperOffice Sale to SuperOffice Sale
------------------------------------
Before any synchronization can take place, a link between a SuperOffice Sale and a SuperOffice Sale must be established.

A SuperOffice Sale will merge with a SuperOffice Sale if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - SuperOffice Sale Property
   * - SaleId
     - SaleId

Once a link between a SuperOffice Sale and a SuperOffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a SuperOffice Sale:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - SuperOffice Sale Property
     - SuperOffice Data Type
   * - Amount
     - Amount
     - "float"
   * - Contact.ContactId
     - Contact.ContactId
     - "integer"
   * - Contact.ContactId
     - Person.PersonId
     - "integer"
   * - Currency.Id
     - Currency.Id
     - "integer"
   * - Heading
     - Heading
     - "string"
   * - Person.PersonId
     - Contact.ContactId
     - "integer"
   * - Person.PersonId
     - Person.PersonId
     - "integer"
   * - Project.ProjectId
     - Project.ProjectId
     - "integer"
   * - SaleText
     - SaleText
     - "string"
   * - Saledate
     - Saledate
     - N/A
   * - Status
     - Status
     - "string"


SuperOffice User to SuperOffice Person
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a SuperOffice Person must be established.

A SuperOffice User will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Person Property
   * - personEmail
     - Emails.Value

Once a link between a SuperOffice User and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - contactId
     - Contact.ContactId
     - "integer"
   * - firstName
     - Firstname
     - "string"
   * - lastName
     - Lastname
     - "string"
   * - personEmail
     - Emails.Value
     - "string"


SuperOffice Contact to SuperOffice Person
-----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a SuperOffice Person must be established.

A new SuperOffice Person will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, or Quote that is synchronized into SuperOffice.

Once a link between a SuperOffice Contact and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - SuperOffice Person Property
     - SuperOffice Data Type


SuperOffice Person to SuperOffice Contact
-----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a SuperOffice Contact must be established.

A new SuperOffice Contact will be created from a SuperOffice Person if it is connected to a SuperOffice Sale, or Quote that is synchronized into SuperOffice.

Once a link between a SuperOffice Person and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - SuperOffice Contact Property
     - SuperOffice Data Type


SuperOffice Sale classification status to SuperOffice Quotealternative
----------------------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Sale classification status and a SuperOffice Quotealternative must be established.

A new SuperOffice Quotealternative will be created from a SuperOffice Sale classification status if it is connected to a SuperOffice Sale, Quote, Quoteline, or Quotealternative that is synchronized into SuperOffice.

Once a link between a SuperOffice Sale classification status and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale classification status and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale classification status Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type

