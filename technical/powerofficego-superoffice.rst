=====================================
Powerofficego to SuperOffice Dataflow
=====================================

Generated: 2023-08-17 08:39:11

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customer to SuperOffice Contact
---------------------------------------------
Every Powerofficego Customer will be synchronized with a SuperOffice Contact.

Once a link between a Powerofficego Customer and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
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
   * - emailAddress
     - Emails.Value
     - "string"
   * - id
     - ContactId
     - "integer"
   * - legalName
     - Name
     - "string"
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
   * - mailAddress.countryCode
     - OrgNr (Dependant on having wd:Q906278 in Country.ThreeLetterISOCountryDependant on having wd:Q906278 in Country.TwoLetterISOCountry)
     - "string"
   * - mailAddress.zipCode
     - Address.Postal.Zipcode
     - "string"
   * - phoneNumber
     - Phones.Value
     - "string"
   * - phoneNumberMobile
     - Phones.Value
     - "string"
   * - streetAddresses.address1
     - Address.Street.Address1
     - "string"
   * - streetAddresses.address2
     - Address.Street.Address2
     - "string"
   * - streetAddresses.address3
     - Address.Street.Address3
     - "string"
   * - streetAddresses.city
     - Address.Street.City
     - "string"
   * - streetAddresses.countryCode
     - OrgNr (Dependant on having wd:Q906278 in Country.ThreeLetterISOCountry)
     - "string"
   * - streetAddresses.zipCode
     - Address.Street.Zipcode
     - "string"
   * - vatNumber
     - OrgNr (Dependant on having  in Country.TwoLetterISOCountry)
     - "string"
   * - websiteUrl
     - Domains
     - "list"
   * - websiteUrl
     - Urls.Value
     - "string"


Powerofficego Contactperson to SuperOffice Person
-------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a SuperOffice Person.

Once a link between a Powerofficego Contactperson and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - address1
     - Address.Postal.Address1
     - "string"
   * - address1
     - Address.Street.Address1
     - "string"
   * - address2
     - Address.Postal.Address2
     - "string"
   * - address2
     - Address.Street.Address2
     - "string"
   * - city
     - Address.Postal.City
     - "string"
   * - city
     - Address.Street.City
     - "string"
   * - dateOfBirth
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - emailAddress
     - Emails.Value
     - "string"
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
   * - partyId
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
   * - zipCode
     - Address.Street.Zipcode
     - "string"


Powerofficego Customer to SuperOffice Person
--------------------------------------------
Every Powerofficego Customer will be synchronized with a SuperOffice Person.

Once a link between a Powerofficego Customer and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - LastName
     - Lastname
     - "string"
   * - dateOfBirth
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - emailAddress
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"
   * - id
     - PersonId
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


Powerofficego Customers to SuperOffice Person
---------------------------------------------
Every Powerofficego Customers will be synchronized with a SuperOffice Person.

Once a link between a Powerofficego Customers and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - DateOfBirth
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - EmailAddress
     - Emails.Value
     - "string"
   * - FirstName
     - Firstname
     - "string"
   * - LastName
     - Lastname
     - "string"
   * - dateOfBirth
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - emailAddress
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"


Powerofficego Departments to SuperOffice Contact
------------------------------------------------
Every Powerofficego Departments will be synchronized with a SuperOffice Contact.

Once a link between a Powerofficego Departments and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Name
     - Name
     - "string"


Powerofficego Employee to SuperOffice Person
--------------------------------------------
Every Powerofficego Employee will be synchronized with a SuperOffice Person.

Once a link between a Powerofficego Employee and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employee and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
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


Powerofficego Employees to SuperOffice Person
---------------------------------------------
Every Powerofficego Employees will be synchronized with a SuperOffice Person.

Once a link between a Powerofficego Employees and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - DateOfBirth
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - DepartmendId
     - Contact.ContactId
     - "integer"
   * - FirstName
     - Firstname
     - "string"
   * - LastName
     - Lastname
     - "string"
   * - PhoneNumber
     - MobilePhones.Value
     - "string"
   * - dateOfBirth
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - firstName
     - Firstname
     - "string"
   * - lastName
     - Lastname
     - "string"
   * - phoneNumber
     - MobilePhones.Value
     - "string"


Powerofficego Supplier to SuperOffice Contact
---------------------------------------------
Every Powerofficego Supplier will be synchronized with a SuperOffice Contact.

Once a link between a Powerofficego Supplier and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
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
   * - WebsiteUrl
     - Urls.Value
     - "string"


Powerofficego Suppliers to SuperOffice Contact
----------------------------------------------
Every Powerofficego Suppliers will be synchronized with a SuperOffice Contact.

Once a link between a Powerofficego Suppliers and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
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
   * - WebsiteUrl
     - Urls.Value
     - "string"


Powerofficego Product to SuperOffice Product
--------------------------------------------
Every Powerofficego Product will be synchronized with a SuperOffice Product.

Once a link between a Powerofficego Product and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - CostPrice
     - UnitCost
     - "string"
   * - Description
     - Description
     - "string"
   * - Name
     - Name
     - "string"
   * - ProductGroupId
     - ProductCategoryKey
     - "string"
   * - SalesPrice
     - UnitListPrice
     - "decimal"
   * - Type
     - ProductTypeKey
     - "string"
   * - Unit
     - QuantityUnit
     - "string"
   * - VatCode
     - VAT
     - "integer"
   * - costPrice
     - UnitCost
     - "string"
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - productGroupId
     - ProductCategoryKey
     - "string"
   * - salesPrice
     - UnitListPrice
     - "decimal"
   * - type
     - ProductTypeKey
     - "string"
   * - unit
     - QuantityUnit
     - "string"
   * - unitOfMeasureCode
     - QuantityUnit
     - "string"
   * - vatCode
     - VAT
     - "integer"


Powerofficego Productgroup to SuperOffice Listproductcategoryitems
------------------------------------------------------------------
Every Powerofficego Productgroup will be synchronized with a SuperOffice Listproductcategoryitems.

Once a link between a Powerofficego Productgroup and a SuperOffice Listproductcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Productgroup and a SuperOffice Listproductcategoryitems:

.. list-table::
   :header-rows: 1

   * - Powerofficego Productgroup Property
     - SuperOffice Listproductcategoryitems Property
     - SuperOffice Data Type
   * - Name
     - Name
     - "string"


Powerofficego Salesorderline to SuperOffice Quoteline
-----------------------------------------------------
Every Powerofficego Salesorderline will be synchronized with a SuperOffice Quoteline.

Once a link between a Powerofficego Salesorderline and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderline and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderline Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - Description
     - Name
     - "string"
   * - Discount
     - DiscountPercent
     - "integer"
   * - Quantity
     - Quantity
     - "integer"
   * - SalesOrderLineUnitPrice
     - UnitListPrice
     - "string"
   * - VatReturnSpecification
     - VAT
     - "integer"

