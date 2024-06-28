=====================================
Powerofficego to Superoffice Dataflow
=====================================

Generated: 2024-06-28 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to Superoffice Person
-------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Superoffice Person.

If a matching Superoffice Person already exists, the Powerofficego Contactperson will be merged with the existing one.
If no matching Superoffice Person is found, a new Superoffice Person will be created.

A Powerofficego Contactperson will merge with a Superoffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Superoffice Person Property
   * - emailAddress
     - Emails.Value

Once a link between a Powerofficego Contactperson and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Superoffice Person Property
     - Superoffice Data Type
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
     - N/A
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


Powerofficego Customers person to Superoffice Person
----------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Superoffice Person.

If a matching Superoffice Person already exists, the Powerofficego Customers person will be merged with the existing one.
If no matching Superoffice Person is found, a new Superoffice Person will be created.

A Powerofficego Customers person will merge with a Superoffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Superoffice Person Property
   * - EmailAddress
     - Emails.Value

Once a link between a Powerofficego Customers person and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - DateOfBirth
     - BirthDate
     - N/A
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


Powerofficego Customers to Superoffice Contact
----------------------------------------------
Every Powerofficego Customers will be synchronized with a Superoffice Contact.

If a matching Superoffice Contact already exists, the Powerofficego Customers will be merged with the existing one.
If no matching Superoffice Contact is found, a new Superoffice Contact will be created.

A Powerofficego Customers will merge with a Superoffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Superoffice Contact Property
   * - EmailAddress
     - Emails.Value

Once a link between a Powerofficego Customers and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Superoffice Contact Property
     - Superoffice Data Type
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


Powerofficego Departments to Superoffice Contact
------------------------------------------------
Every Powerofficego Departments will be synchronized with a Superoffice Contact.

Once a link between a Powerofficego Departments and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - Code
     - OrgNr (Dependant on having wd:Q2366457 in Country.TwoLetterISOCountry)
     - "string"
   * - Name
     - Name
     - "string"


Powerofficego Employees to Superoffice Person
---------------------------------------------
Every Powerofficego Employees will be synchronized with a Superoffice Person.

Once a link between a Powerofficego Employees and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - DateOfBirth
     - BirthDate
     - N/A
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
     - N/A
   * - firstName
     - Firstname
     - "string"
   * - lastName
     - Lastname
     - "string"
   * - phoneNumber
     - MobilePhones.Value
     - "string"


Powerofficego Product to Superoffice Product
--------------------------------------------
Every Powerofficego Product will be synchronized with a Superoffice Product.

Once a link between a Powerofficego Product and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Superoffice Product Property
     - Superoffice Data Type
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
     - N/A
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
     - N/A
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
     - N/A


Powerofficego Quote to Superoffice Quotealternative
---------------------------------------------------
Every Powerofficego Quote will be synchronized with a Superoffice Quotealternative.

Once a link between a Powerofficego Quote and a Superoffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Quote and a Superoffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Powerofficego Quote Property
     - Superoffice Quotealternative Property
     - Superoffice Data Type
   * - TotalAmount
     - TotalPrice
     - "float"


Powerofficego Salesorderlines to Superoffice Quoteline
------------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Superoffice Quoteline.

Once a link between a Powerofficego Salesorderlines and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Superoffice Quoteline Property
     - Superoffice Data Type
   * - Allowance
     - DiscountPercent
     - "integer"
   * - Allowance
     - ERPDiscountPercent
     - N/A
   * - Description
     - Name
     - "string"
   * - ProductId
     - ERPProductKey
     - "string"
   * - ProductUnitPrice
     - UnitListPrice
     - N/A
   * - Quantity
     - Quantity
     - N/A
   * - SortOrder
     - Rank
     - "integer"
   * - TotalAmount
     - TotalPrice
     - N/A
   * - VatId
     - VAT
     - "integer"
   * - VatRate
     - VAT
     - "integer"
   * - sesam_SalesOrderId
     - QuoteAlternativeId
     - "integer"

