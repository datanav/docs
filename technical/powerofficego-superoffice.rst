==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-03-26 13:42:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to  Person
--------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Person.

If a matching  Person already exists, the Powerofficego Contactperson will be merged with the existing one.
If no matching  Person is found, a new  Person will be created.

A Powerofficego Contactperson will merge with a  Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Person Property
   * - emailAddress
     - Emails.Value

Once a link between a Powerofficego Contactperson and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Person Property
     -  Data Type
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
     - "datetime-format","%Y-%m-%dT%H:%M:%SZ","_."]
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


Powerofficego Customers person to  Person
-----------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a  Person must be established.

A Powerofficego Customers person will merge with a  Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Person Property
   * - EmailAddress
     - Emails.Value

Once a link between a Powerofficego Customers person and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Person Property
     -  Data Type
   * - DateOfBirth
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%SZ","_."]
   * - EmailAddress
     - Emails.Value
     - "string"
   * - FirstName
     - Firstname
     - "string"
   * - Id
     - PersonId
     - "integer"
   * - LastName
     - Lastname
     - "string"
   * - MailAddress.AddressLine1
     - Address.Street.Address1
     - "string"
   * - MailAddress.AddressLine2
     - Address.Street.Address2
     - "string"
   * - MailAddress.City
     - Address.Street.City
     - "string"
   * - MailAddress.CountryCode
     - Country.CountryId
     - "integer"
   * - MailAddress.ZipCode
     - Address.Street.Zipcode
     - "string"
   * - PhoneNumber
     - OfficePhones.Value
     - "string"


Powerofficego Customers to SuperOffice Contact
----------------------------------------------
Every Powerofficego Customers will be synchronized with a SuperOffice Contact.

If a matching SuperOffice Contact already exists, the Powerofficego Customers will be merged with the existing one.
If no matching SuperOffice Contact is found, a new SuperOffice Contact will be created.

A Powerofficego Customers will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - SuperOffice Contact Property
   * - EmailAddress
     - Emails.Value

Once a link between a Powerofficego Customers and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - EmailAddress
     - Emails.Value
     - "string"
   * - Id
     - ContactId
     - "integer"
   * - MailAddress.AddressLine1
     - Address.Postal.Address1
     - "string"
   * - MailAddress.AddressLine1
     - Address.Street.Address1
     - "string"
   * - MailAddress.AddressLine2
     - Address.Postal.Address2
     - "string"
   * - MailAddress.AddressLine2
     - Address.Street.Address2
     - "string"
   * - MailAddress.City
     - Address.Postal.City
     - "string"
   * - MailAddress.City
     - Address.Street.City
     - "string"
   * - MailAddress.CountryCode
     - Country.CountryId
     - "integer"
   * - MailAddress.ZipCode
     - Address.Postal.Zipcode
     - "string"
   * - MailAddress.ZipCode
     - Address.Street.Zipcode
     - "string"
   * - MailAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - MailAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - MailAddress.city
     - Address.Postal.City
     - "string"
   * - MailAddress.countryCode
     - Country.CountryId
     - "integer"
   * - MailAddress.zipCode
     - Address.Postal.Zipcode
     - "string"
   * - Name
     - Name
     - "string"
   * - Number
     - OrgNr (Dependant on having wd:Q852835 in Country.TwoLetterISOCountryDependant on having wd:Q852835 in Country.TwoLetterISOCountry)
     - "string"
   * - Number
     - Phones.Value
     - "string"
   * - OrganizationNumber
     - OrgNr (Dependant on having  in Country.TwoLetterISOCountryDependant on having  in Country.TwoLetterISOCountryDependant on having  in Country.TwoLetterISOCountryDependant on having  in Country.TwoLetterISOCountryDependant on having  in Country.TwoLetterISOCountryDependant on having  in Country.TwoLetterISOCountryDependant on having  in Country.TwoLetterISOCountry)
     - "string"
   * - PhoneNumber
     - Phones.Value
     - "string"
   * - WebsiteUrl
     - Urls.Value
     - "string"


Powerofficego Salesorders to SuperOffice Quotealternative
---------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Salesorders and a SuperOffice Quotealternative must be established.

A new SuperOffice Quotealternative will be created from a Powerofficego Salesorders if it is connected to a Powerofficego Salesorderline, or Salesorderlines that is synchronized into SuperOffice.

Once a link between a Powerofficego Salesorders and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - NetAmount
     - TotalPrice
     - "float"
   * - TotalAmount
     - TotalPrice
     - "float"


Powerofficego Departments to  Contact
-------------------------------------
Every Powerofficego Departments will be synchronized with a  Contact.

Once a link between a Powerofficego Departments and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Contact Property
     -  Data Type
   * - Name
     - Name
     - "string"


Powerofficego Employees to  Person
----------------------------------
Every Powerofficego Employees will be synchronized with a  Person.

Once a link between a Powerofficego Employees and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a  Person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     -  Person Property
     -  Data Type
   * - DateOfBirth
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%SZ","_."]
   * - DepartmendId
     - Contact.ContactId
     - "integer"
   * - DepartmentId (Dependant on having wd:Q703534 in JobTitle)
     - Contact.ContactId
     - "integer"
   * - EmailAddress
     - Emails.Value
     - "string"
   * - FirstName
     - Firstname
     - "string"
   * - JobTitle
     - Contact.ContactId
     - "integer"
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
   * - unitOfMeasureCode
     - VAT
     - "integer"
   * - vatCode
     - VAT
     - "integer", "decimal"]


Powerofficego Quote to  Quotealternative
----------------------------------------
Every Powerofficego Quote will be synchronized with a  Quotealternative.

Once a link between a Powerofficego Quote and a  Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Quote and a  Quotealternative:

.. list-table::
   :header-rows: 1

   * - Powerofficego Quote Property
     -  Quotealternative Property
     -  Data Type
   * - TotalAmount
     - TotalPrice
     - "float"


Powerofficego Salesorderlines to  Quoteline
-------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a  Quoteline.

Once a link between a Powerofficego Salesorderlines and a  Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a  Quoteline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     -  Quoteline Property
     -  Data Type
   * - Allowance
     - DiscountPercent
     - "integer"
   * - Allowance
     - ERPDiscountPercent
     - "decimal"
   * - Description
     - Name
     - "string"
   * - ProductId
     - ERPProductKey
     - "string"
   * - ProductUnitPrice
     - UnitListPrice
     - "if-null", "integer", "string"], "decimal"]
   * - Quantity
     - Quantity
     - "integer", "decimal"]
   * - SortOrder
     - Rank
     - "integer"
   * - TotalAmount
     - TotalPrice
     - "if-null", "integer", "string"], "decimal"]
   * - VatId
     - VAT
     - "integer"
   * - VatRate
     - VAT
     - "integer"
   * - sesam_SalesOrderId
     - QuoteAlternativeId
     - "integer"

