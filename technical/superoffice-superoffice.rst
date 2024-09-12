===================================
SuperOffice to SuperOffice Dataflow
===================================

Generated: 2024-09-12 12:58:41

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


SuperOffice Contact to SuperOffice Ownercontactlink
---------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a SuperOffice Ownercontactlink must be established.

A SuperOffice Contact will merge with a SuperOffice Ownercontactlink if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - SuperOffice Ownercontactlink Property
   * - ContactId
     - contact_id

Once a link between a SuperOffice Contact and a SuperOffice Ownercontactlink is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a SuperOffice Ownercontactlink:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - SuperOffice Ownercontactlink Property
     - SuperOffice Data Type


SuperOffice Listcountryitems to SuperOffice Listcountryitems
------------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Listcountryitems and a SuperOffice Listcountryitems must be established.

A SuperOffice Listcountryitems will merge with a SuperOffice Listcountryitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     - SuperOffice Listcountryitems Property
   * - Name
     - Name
   * - TwoLetterISOCountry
     - TwoLetterISOCountry
   * - ThreeLetterISOCountry
     - ThreeLetterISOCountry

Once a link between a SuperOffice Listcountryitems and a SuperOffice Listcountryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcountryitems and a SuperOffice Listcountryitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     - SuperOffice Listcountryitems Property
     - SuperOffice Data Type


SuperOffice Listcurrencyitems to SuperOffice Listcurrencyitems
--------------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Listcurrencyitems and a SuperOffice Listcurrencyitems must be established.

A SuperOffice Listcurrencyitems will merge with a SuperOffice Listcurrencyitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - SuperOffice Listcurrencyitems Property
   * - Name
     - Name

Once a link between a SuperOffice Listcurrencyitems and a SuperOffice Listcurrencyitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a SuperOffice Listcurrencyitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - SuperOffice Listcurrencyitems Property
     - SuperOffice Data Type
   * - Name
     - Name
     - "string"
   * - Tooltip
     - Tooltip
     - "string"


SuperOffice Listcurrencyitems to SuperOffice Pricelist
------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Listcurrencyitems and a SuperOffice Pricelist must be established.

A SuperOffice Listcurrencyitems will merge with a SuperOffice Pricelist if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - SuperOffice Pricelist Property
   * - Name
     - Currency

Once a link between a SuperOffice Listcurrencyitems and a SuperOffice Pricelist is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a SuperOffice Pricelist:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - SuperOffice Pricelist Property
     - SuperOffice Data Type
   * - Name
     - Currency
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


SuperOffice Ownercontactlink to SuperOffice Ownercontactlink
------------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Ownercontactlink and a SuperOffice Ownercontactlink must be established.

A SuperOffice Ownercontactlink will merge with a SuperOffice Ownercontactlink if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - SuperOffice Ownercontactlink Property
   * - contact_id
     - contact_id

Once a link between a SuperOffice Ownercontactlink and a SuperOffice Ownercontactlink is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a SuperOffice Ownercontactlink:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - SuperOffice Ownercontactlink Property
     - SuperOffice Data Type


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


SuperOffice Person to SuperOffice User
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a SuperOffice User must be established.

A SuperOffice Person will merge with a SuperOffice User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - SuperOffice User Property
   * - Emails.Value
     - personEmail

Once a link between a SuperOffice Person and a SuperOffice User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a SuperOffice User:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - SuperOffice User Property
     - SuperOffice Data Type


SuperOffice Pricelist to SuperOffice Listcurrencyitems
------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Pricelist and a SuperOffice Listcurrencyitems must be established.

A SuperOffice Pricelist will merge with a SuperOffice Listcurrencyitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - SuperOffice Listcurrencyitems Property
   * - Currency
     - Name

Once a link between a SuperOffice Pricelist and a SuperOffice Listcurrencyitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Pricelist and a SuperOffice Listcurrencyitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - SuperOffice Listcurrencyitems Property
     - SuperOffice Data Type
   * - Currency
     - Name
     - "string"
   * - Description
     - Tooltip
     - "string"


SuperOffice Pricelist to SuperOffice Pricelist
----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Pricelist and a SuperOffice Pricelist must be established.

A SuperOffice Pricelist will merge with a SuperOffice Pricelist if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - SuperOffice Pricelist Property
   * - Currency
     - Currency

Once a link between a SuperOffice Pricelist and a SuperOffice Pricelist is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Pricelist and a SuperOffice Pricelist:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - SuperOffice Pricelist Property
     - SuperOffice Data Type


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


SuperOffice Quote to SuperOffice Quote
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quote and a SuperOffice Quote must be established.

A SuperOffice Quote will merge with a SuperOffice Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     - SuperOffice Quote Property
   * - SaleId
     - SaleId

Once a link between a SuperOffice Quote and a SuperOffice Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quote and a SuperOffice Quote:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     - SuperOffice Quote Property
     - SuperOffice Data Type
   * - AcceptedQuoteAlternativeId
     - AcceptedQuoteAlternativeId
     - "string"
   * - PoNumber
     - PoNumber
     - "string"


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


SuperOffice Role to SuperOffice Role
------------------------------------
Before any synchronization can take place, a link between a SuperOffice Role and a SuperOffice Role must be established.

A SuperOffice Role will merge with a SuperOffice Role if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Role Property
     - SuperOffice Role Property
   * - name
     - name

Once a link between a SuperOffice Role and a SuperOffice Role is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Role and a SuperOffice Role:

.. list-table::
   :header-rows: 1

   * - SuperOffice Role Property
     - SuperOffice Role Property
     - SuperOffice Data Type


SuperOffice Sale to SuperOffice Quote
-------------------------------------
Before any synchronization can take place, a link between a SuperOffice Sale and a SuperOffice Quote must be established.

A SuperOffice Sale will merge with a SuperOffice Quote if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - SuperOffice Quote Property
   * - SaleId
     - SaleId

Once a link between a SuperOffice Sale and a SuperOffice Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a SuperOffice Quote:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - SuperOffice Quote Property
     - SuperOffice Data Type
   * - Status
     - AcceptedQuoteAlternativeId
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


SuperOffice User to SuperOffice User
------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a SuperOffice User must be established.

A SuperOffice User will merge with a SuperOffice User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice User Property
   * - personEmail
     - personEmail

Once a link between a SuperOffice User and a SuperOffice User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a SuperOffice User:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice User Property
     - SuperOffice Data Type


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


SuperOffice User to SuperOffice Listcategoryitems
-------------------------------------------------
Every SuperOffice User will be synchronized with a SuperOffice Listcategoryitems.

Once a link between a SuperOffice User and a SuperOffice Listcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a SuperOffice Listcategoryitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Listcategoryitems Property
     - SuperOffice Data Type
   * - contactCategory
     - Name
     - "string"

