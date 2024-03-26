========================
SuperOffice to  Dataflow
========================

Generated: 2024-03-26 13:42:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Contact
-------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a  Contact must be established.

A SuperOffice Contact will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Contact Property
   * - ContactId
     - ContactId
   * - Emails.Value
     - Emails.Value

Once a link between a SuperOffice Contact and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Contact Property
     -  Data Type
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
     - "integer"
   * - Country.ThreeLetterISOCountry
     - OrgNr (Dependant on having wd:Q906278 in Country.TwoLetterISOCountryDependant on having wd:Q906278 in Country.ThreeLetterISOCountryDependant on having wd:Q906278 in Country.ThreeLetterISOCountryDependant on having wd:Q906278 in Country.ThreeLetterISOCountryDependant on having wd:Q906278 in Country.TwoLetterISOCountryDependant on having wd:Q906278 in Country.ThreeLetterISOCountry)
     - "string"
   * - Domains
     - Domains
     - "list"
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


SuperOffice Ownercontactlink to  Contact
----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Ownercontactlink and a  Contact must be established.

A SuperOffice Ownercontactlink will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     -  Contact Property
   * - contact_id
     - ContactId

Once a link between a SuperOffice Ownercontactlink and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a  Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     -  Contact Property
     -  Data Type
   * - contact_id
     - ContactId
     - "string"
   * - name
     - Name
     - "string"


SuperOffice Person to  Person
-----------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a  Person must be established.

A SuperOffice Person will merge with a  Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Person Property
   * - Emails.Value
     - Emails.Value

Once a link between a SuperOffice Person and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Person Property
     -  Data Type
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
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
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


SuperOffice Product to  Product
-------------------------------
Before any synchronization can take place, a link between a SuperOffice Product and a  Product must be established.

A SuperOffice Product will merge with a  Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Product Property
   * - ProductId
     - ProductId
   * - ERPProductKey
     - ERPProductKey

Once a link between a SuperOffice Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Product Property
     -  Data Type
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
     - "decimal"
   * - Url
     - Url
     - "string"
   * - VAT
     - VAT
     - "integer"


SuperOffice Quote to  Sale
--------------------------
Before any synchronization can take place, a link between a SuperOffice Quote and a  Sale must be established.

A SuperOffice Quote will merge with a  Sale if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     -  Sale Property
   * - SaleId
     - SaleId

Once a link between a SuperOffice Quote and a  Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quote and a  Sale:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     -  Sale Property
     -  Data Type
   * - AcceptedQuoteAlternativeId
     - Status
     - "string"


SuperOffice Sale to  Sale
-------------------------
Before any synchronization can take place, a link between a SuperOffice Sale and a  Sale must be established.

A SuperOffice Sale will merge with a  Sale if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     -  Sale Property
   * - SaleId
     - SaleId

Once a link between a SuperOffice Sale and a  Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a  Sale:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     -  Sale Property
     -  Data Type
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
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - Status
     - Status
     - "string"


SuperOffice User to  Person
---------------------------
Before any synchronization can take place, a link between a SuperOffice User and a  Person must be established.

A SuperOffice User will merge with a  Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Person Property
   * - personEmail
     - Emails.Value

Once a link between a SuperOffice User and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a  Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Person Property
     -  Data Type
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


SuperOffice Contact to  Person
------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a  Person must be established.

A new  Person will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, or Quote that is synchronized into .

Once a link between a SuperOffice Contact and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Person Property
     -  Data Type


SuperOffice Person to  Contact
------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a  Contact must be established.

A new  Contact will be created from a SuperOffice Person if it is connected to a SuperOffice Sale, or Quote that is synchronized into .

Once a link between a SuperOffice Person and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Contact Property
     -  Data Type


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

