=====================================
SuperOffice to PowerOfficeGo Dataflow
=====================================

Generated: 2023-11-27 20:43:47

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to PowerOfficeGo Customers
----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a SuperOffice Contact if it is connected to a SuperOffice User, Person, Contact, Quoteline, or Quotealternative that is synchronized into PowerOfficeGo.

A SuperOffice Contact will merge with a PowerOfficeGo Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGo Customers Property
   * - Emails.Value
     - EmailAddress
   * - Emails.Value
     - InvoiceEmailAddress
   * - Emails.Value
     - PaymentReminderEmailAddress

Once a link between a SuperOffice Contact and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - Address.Postal.Address1
     - MailAddress.AddressLine1
     - "string"
   * - Address.Postal.Address1
     - MailAddress.addressLine1
     - "string"
   * - Address.Postal.Address2
     - MailAddress.AddressLine2
     - "string"
   * - Address.Postal.Address2
     - MailAddress.addressLine2
     - "string"
   * - Address.Postal.City
     - MailAddress.City
     - "string"
   * - Address.Postal.City
     - MailAddress.city
     - "string"
   * - Address.Postal.Zipcode
     - MailAddress.ZipCode
     - "string"
   * - Address.Postal.Zipcode
     - MailAddress.zipCode
     - "string"
   * - Address.Street.Address1
     - MailAddress.AddressLine1
     - "string"
   * - Address.Street.Address2
     - MailAddress.AddressLine2
     - "string"
   * - Address.Street.City
     - MailAddress.City
     - "string"
   * - Address.Street.Zipcode
     - MailAddress.ZipCode
     - "string"
   * - ContactId
     - Id
     - "string"
   * - Country.CountryId
     - MailAddress.CountryCode
     - "string"
   * - Country.CountryId
     - MailAddress.countryCode
     - "string"
   * - Country.ThreeLetterISOCountry
     - OrganizationNumber (Dependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.CountryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCode)
     - "string"
   * - Emails.Value
     - EmailAddress
     - "string"
   * - Emails.Value
     - PaymentReminderEmailAddress
     - "string"
   * - Name
     - Name
     - "string"
   * - OrgNr
     - OrganizationNumber (Dependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.CountryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCode)
     - "string"
   * - OrgNr (Dependant on having wd:Q1273217 in Country.ThreeLetterISOCountryDependant on having wd:Q1273217 in Country.TwoLetterISOCountry)
     - PaymentReminderEmailAddress
     - "string"
   * - Phones.Value
     - Number
     - "string"
   * - Phones.Value
     - PhoneNumber
     - "string"
   * - Urls.Value
     - WebsiteUrl
     - "string"


SuperOffice Person to PowerOfficeGo Contactperson
-------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a PowerOfficeGo Contactperson must be established.

A new PowerOfficeGo Contactperson will be created from a SuperOffice Person if it is connected to a SuperOffice Quotealternative that is synchronized into PowerOfficeGo.

A SuperOffice Person will merge with a PowerOfficeGo Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGo Contactperson Property
   * - Emails.Value
     - emailAddress

Once a link between a SuperOffice Person and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - Address.Street.Address1
     - address1
     - "string"
   * - Address.Street.Address2
     - address2
     - "string"
   * - Address.Street.City
     - city
     - "string"
   * - Address.Street.Zipcode
     - zipCode
     - "string"
   * - BirthDate
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - Contact.ContactId
     - partyId
     - "integer"
   * - Country.CountryId
     - residenceCountryCode
     - "string"
   * - Emails.Value
     - emailAddress
     - "string"
   * - Firstname
     - firstName
     - "string"
   * - Lastname
     - lastName
     - "string"
   * - OfficePhones.Value
     - phoneNumber
     - "string"
   * - PersonId
     - id
     - "integer"


SuperOffice Pricelist to PowerOfficeGo Currency
-----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Pricelist and a PowerOfficeGo Currency must be established.

A SuperOffice Pricelist will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - PowerOfficeGo Currency Property
   * - Currency
     - Code
   * - Currency
     - code

Once a link between a SuperOffice Pricelist and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Pricelist and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


SuperOffice User to PowerOfficeGo Contactperson
-----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a PowerOfficeGo Contactperson must be established.

A SuperOffice User will merge with a PowerOfficeGo Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGo Contactperson Property
   * - personEmail
     - emailAddress

Once a link between a SuperOffice User and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - contactId
     - partyId
     - "integer"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - personEmail
     - emailAddress
     - "string"


SuperOffice Contact to PowerOfficeGo Contactperson
--------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGo Contactperson must be established.

A new PowerOfficeGo Contactperson will be created from a SuperOffice Contact if it is connected to a SuperOffice Quotealternative that is synchronized into PowerOfficeGo.

Once a link between a SuperOffice Contact and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type


SuperOffice Contact to PowerOfficeGo Customers person
-----------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a SuperOffice Contact if it is connected to a SuperOffice User, Person, Contact, Quoteline, or Quotealternative that is synchronized into PowerOfficeGo.

Once a link between a SuperOffice Contact and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
   * - Address.Postal.Address1
     - MailAddress.AddressLine1
     - "string"
   * - Address.Postal.Address2
     - MailAddress.AddressLine2
     - "string"
   * - Address.Postal.City
     - MailAddress.City
     - "string"
   * - Address.Postal.Zipcode
     - MailAddress.ZipCode
     - "string"
   * - Address.Street.Address1
     - MailAddress.AddressLine1
     - "string"
   * - Address.Street.Address2
     - MailAddress.AddressLine2
     - "string"
   * - Address.Street.City
     - MailAddress.City
     - "string"
   * - Address.Street.Zipcode
     - MailAddress.ZipCode
     - "string"
   * - ContactId
     - Id
     - "string"
   * - Country.CountryId
     - MailAddress.CountryCode
     - "string"


SuperOffice Contact to PowerOfficeGo Departments
------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGo Departments must be established.

A new PowerOfficeGo Departments will be created from a SuperOffice Contact if it is connected to a SuperOffice User that is synchronized into PowerOfficeGo.

Once a link between a SuperOffice Contact and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type
   * - CreatedDate
     - CreatedDateTimeOffset
     - "string"
   * - Name
     - Name
     - "string"


SuperOffice Person to PowerOfficeGo Customers person
----------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a SuperOffice Person if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into PowerOfficeGo.

Once a link between a SuperOffice Person and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
   * - Address.Street.Address1
     - MailAddress.AddressLine1
     - "string"
   * - Address.Street.Address2
     - MailAddress.AddressLine2
     - "string"
   * - Address.Street.City
     - MailAddress.City
     - "string"
   * - Address.Street.Zipcode
     - MailAddress.ZipCode
     - "string"
   * - BirthDate
     - DateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - Country.CountryId
     - MailAddress.CountryCode
     - "string"
   * - Emails.Value
     - EmailAddress
     - "string"
   * - Firstname
     - FirstName
     - "string"
   * - Lastname
     - LastName
     - "string"
   * - OfficePhones.Value
     - PhoneNumber
     - "string"
   * - PersonId
     - Id
     - "integer"


SuperOffice Person to PowerOfficeGo Customers
---------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a SuperOffice Person if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into PowerOfficeGo.

Once a link between a SuperOffice Person and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type


SuperOffice Quotealternative to PowerOfficeGo Salesorder
--------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a PowerOfficeGo Salesorder must be established.

A new PowerOfficeGo Salesorder will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into PowerOfficeGo.

Once a link between a SuperOffice Quotealternative and a PowerOfficeGo Salesorder is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a PowerOfficeGo Salesorder:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - PowerOfficeGo Salesorder Property
     - PowerOfficeGo Data Type


SuperOffice Quotealternative to PowerOfficeGo Salesorders
---------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a PowerOfficeGo Salesorders must be established.

A new PowerOfficeGo Salesorders will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into PowerOfficeGo.

Once a link between a SuperOffice Quotealternative and a PowerOfficeGo Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a PowerOfficeGo Salesorders:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - PowerOfficeGo Salesorders Property
     - PowerOfficeGo Data Type
   * - TotalPrice
     - TotalAmount
     - "string"
   * - sesam_SaleId (Dependant on having poweroffice-salesorder in sesam_AcceptedDependant on having poweroffice-salesorder in sesam_AcceptedDependant on having poweroffice-salesorder in sesam_AcceptedDependant on having poweroffice-salesorder in sesam_AcceptedDependant on having poweroffice-salesorder in sesam_Accepted)
     - Id
     - "string"


SuperOffice Quoteline to PowerOfficeGo Outgoinginvoices
-------------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a SuperOffice Quoteline and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - QuoteAlternativeId
     - OrderNo
     - "string"
   * - TotalPrice
     - NetAmount
     - "string"


SuperOffice Listcurrencyitems to PowerOfficeGo Currency
-------------------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a PowerOfficeGo Currency.

If a matching PowerOfficeGo Currency already exists, the SuperOffice Listcurrencyitems will be merged with the existing one.
If no matching PowerOfficeGo Currency is found, a new PowerOfficeGo Currency will be created.

A SuperOffice Listcurrencyitems will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - PowerOfficeGo Currency Property
   * - Name
     - Code
   * - Name
     - code

Once a link between a SuperOffice Listcurrencyitems and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


SuperOffice Listproductcategoryitems to PowerOfficeGo Productgroup
------------------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a PowerOfficeGo Productgroup.

Once a link between a SuperOffice Listproductcategoryitems and a PowerOfficeGo Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a PowerOfficeGo Productgroup:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     - PowerOfficeGo Productgroup Property
     - PowerOfficeGo Data Type
   * - Name
     - Name
     - "string"


SuperOffice Ownercontactlink to PowerOfficeGo Departments
---------------------------------------------------------
Every SuperOffice Ownercontactlink will be synchronized with a PowerOfficeGo Departments.

Once a link between a SuperOffice Ownercontactlink and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type
   * - name
     - Name
     - "string"


SuperOffice Product to PowerOfficeGo Product
--------------------------------------------
Every SuperOffice Product will be synchronized with a PowerOfficeGo Product.

Once a link between a SuperOffice Product and a PowerOfficeGo Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a PowerOfficeGo Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - PowerOfficeGo Product Property
     - PowerOfficeGo Data Type
   * - Description
     - Description
     - "string"
   * - Description
     - description
     - "string"
   * - Name
     - Name
     - "string"
   * - Name
     - name
     - "string"
   * - ProductCategoryKey
     - ProductGroupId
     - "string"
   * - ProductCategoryKey
     - productGroupId
     - "integer"
   * - ProductTypeKey
     - Type
     - "string"
   * - ProductTypeKey
     - type
     - "integer"
   * - QuantityUnit
     - Unit
     - "string"
   * - QuantityUnit
     - unit
     - "string"
   * - QuantityUnit
     - unitOfMeasureCode
     - "string"
   * - UnitCost
     - CostPrice
     - "string"
   * - UnitCost
     - costPrice
     - "if", "is-decimal", "decimal", "integer"]
   * - UnitListPrice
     - SalesPrice
     - "string"
   * - UnitListPrice
     - salesPrice
     - "if", "is-decimal", "decimal", "integer"]
   * - VAT
     - VatCode
     - "string"
   * - VAT
     - unitOfMeasureCode
     - "string"
   * - VAT
     - vatCode
     - "string"
   * - VATInfo
     - unitOfMeasureCode
     - "string"


SuperOffice Product to PowerOfficeGo Vatcodes
---------------------------------------------
Every SuperOffice Product will be synchronized with a PowerOfficeGo Vatcodes.

Once a link between a SuperOffice Product and a PowerOfficeGo Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a PowerOfficeGo Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - PowerOfficeGo Vatcodes Property
     - PowerOfficeGo Data Type
   * - QuantityUnit
     - Name
     - "string"
   * - VAT
     - Rate
     - "string"
   * - VAT
     - rate
     - "string"
   * - VATInfo
     - Name
     - "string"
   * - VATInfo
     - name
     - "string"


SuperOffice Quotealternative to PowerOfficeGo Vatcodes
------------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a PowerOfficeGo Vatcodes.

Once a link between a SuperOffice Quotealternative and a PowerOfficeGo Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a PowerOfficeGo Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - PowerOfficeGo Vatcodes Property
     - PowerOfficeGo Data Type
   * - VAT
     - Rate
     - "string"
   * - VAT
     - rate
     - "string"
   * - VATInfo
     - Name
     - "string"
   * - VATInfo
     - name
     - "string"


SuperOffice Quoteline to PowerOfficeGo Salesorderlines
------------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOfficeGo Salesorderlines.

Once a link between a SuperOffice Quoteline and a PowerOfficeGo Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOfficeGo Salesorderlines:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOfficeGo Salesorderlines Property
     - PowerOfficeGo Data Type
   * - DiscountPercent
     - Allowance
     - "float"
   * - DiscountPercent
     - Discount
     - "string"
   * - ERPProductKey
     - ProductCode
     - "string"
   * - ERPProductKey
     - ProductId
     - "integer"
   * - Name
     - Description
     - "string"
   * - Quantity
     - Quantity
     - "integer"
   * - QuoteAlternativeId
     - sesam_SalesOrderId
     - "string"
   * - QuoteAlternativeId
     - sesam_SalesOrdersId
     - "string"
   * - TotalPrice
     - TotalAmount
     - "string"
   * - UnitListPrice
     - ProductUnitPrice
     - "if", "is-decimal", "decimal", "integer"]
   * - UnitListPrice
     - SalesOrderLineUnitPrice
     - "string"
   * - VAT
     - VatReturnSpecification
     - "string"


SuperOffice Quoteline to PowerOfficeGo Vatcodes
-----------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOfficeGo Vatcodes.

Once a link between a SuperOffice Quoteline and a PowerOfficeGo Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOfficeGo Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOfficeGo Vatcodes Property
     - PowerOfficeGo Data Type
   * - VAT
     - Rate
     - "string"
   * - VAT
     - rate
     - "string"
   * - VATInfo
     - Name
     - "string"
   * - VATInfo
     - name
     - "string"


SuperOffice User to PowerOfficeGo Employees
-------------------------------------------
Every SuperOffice User will be synchronized with a PowerOfficeGo Employees.

Once a link between a SuperOffice User and a PowerOfficeGo Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a PowerOfficeGo Employees:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGo Employees Property
     - PowerOfficeGo Data Type
   * - contactCategory
     - MailAddress.CountryCode
     - "string"
   * - contactCategory
     - MailAddress.countryCode
     - "string"
   * - contactId
     - DepartmendId
     - "string"
   * - contactId
     - DepartmentId (Dependant on having wd:Q703534 in JobTitle)
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - lastName
     - lastName
     - "string"

