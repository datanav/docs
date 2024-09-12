======================================
PowerOffice GO to SuperOffice Dataflow
======================================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to SuperOffice Person
--------------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the PowerOffice GO Contactperson will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A PowerOffice GO Contactperson will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - SuperOffice Person Property
   * - emailAddress
     - Emails.Value

Once a link between a PowerOffice GO Contactperson and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
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


PowerOffice GO Customers person to SuperOffice Person
-----------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the PowerOffice GO Customers person will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A PowerOffice GO Customers person will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - SuperOffice Person Property
   * - EmailAddress
     - Emails.Value

Once a link between a PowerOffice GO Customers person and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - SuperOffice Person Property
     - SuperOffice Data Type
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


PowerOffice GO Customers to SuperOffice Contact
-----------------------------------------------
Every PowerOffice GO Customers will be synchronized with a SuperOffice Contact.

If a matching SuperOffice Contact already exists, the PowerOffice GO Customers will be merged with the existing one.
If no matching SuperOffice Contact is found, a new SuperOffice Contact will be created.

A PowerOffice GO Customers will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - SuperOffice Contact Property
   * - EmailAddress
     - Emails.Value

Once a link between a PowerOffice GO Customers and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
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


PowerOffice GO Departments to SuperOffice Contact
-------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a SuperOffice Contact.

Once a link between a PowerOffice GO Departments and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - Code
     - OrgNr (Dependant on having wd:Q2366457 in Country.TwoLetterISOCountry)
     - "string"
   * - Name
     - Name
     - "string"


PowerOffice GO Employees to SuperOffice Person
----------------------------------------------
Every PowerOffice GO Employees will be synchronized with a SuperOffice Person.

Once a link between a PowerOffice GO Employees and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - SuperOffice Person Property
     - SuperOffice Data Type
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


PowerOffice GO Product to SuperOffice Product
---------------------------------------------
Every PowerOffice GO Product will be synchronized with a SuperOffice Product.

Once a link between a PowerOffice GO Product and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
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


PowerOffice GO Quote to SuperOffice Quotealternative
----------------------------------------------------
Every PowerOffice GO Quote will be synchronized with a SuperOffice Quotealternative.

Once a link between a PowerOffice GO Quote and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Quote and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Quote Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - TotalAmount
     - TotalPrice
     - "float"


PowerOffice GO Salesorderlines to SuperOffice Quoteline
-------------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a SuperOffice Quoteline.

Once a link between a PowerOffice GO Salesorderlines and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
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

