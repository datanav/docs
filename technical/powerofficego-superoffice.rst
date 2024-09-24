======================================
PowerOffice GO to SuperOffice Dataflow
======================================

Generated: 2024-09-24 00:00:01

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
     - Address.Street.Address1
     - "string"
   * - address2
     - Address.Street.Address2
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
   * - partyId
     - Contact.ContactId
     - "integer"
   * - phoneNumber
     - OfficePhones.Value
     - "string"
   * - residenceCountryCode
     - Country.CountryId
     - "integer"
   * - zipCode
     - Address.Street.Zipcode
     - "string"


PowerOffice GO Customers (human data) to SuperOffice Person
-----------------------------------------------------------
Every PowerOffice GO Customers (human data) will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the PowerOffice GO Customers (human data) will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A PowerOffice GO Customers (human data) will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (human data) Property
     - SuperOffice Person Property
   * - EmailAddress
     - Emails.Value

Once a link between a PowerOffice GO Customers (human data) and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers (human data) and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers (human data) Property
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
   * - Name
     - Name
     - "string"
   * - Number
     - OrgNr (Dependant on having wd:Q852835 in Country.TwoLetterISOCountry)
     - "string"
   * - OrganizationNumber
     - OrgNr (Dependant on having  in Country.TwoLetterISOCountry)
     - "string"
   * - PhoneNumber
     - Phones.Value
     - "string"
   * - WebsiteUrl
     - Urls.Value
     - "string"


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
   * - EmailAddress
     - Emails.Value
     - "string"
   * - FirstName
     - Firstname
     - "string"
   * - LastName
     - Lastname
     - "string"
   * - PhoneNumber
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
   * - costPrice
     - UnitCost
     - "string"
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - salesPrice
     - UnitListPrice
     - N/A
   * - type
     - ProductTypeKey
     - "string"
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
     - ERPDiscountPercent
     - "integer"
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
   * - VatRate
     - VAT
     - "integer"
   * - sesam_SalesOrderId
     - QuoteAlternativeId
     - "integer"

