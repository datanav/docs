=====================================
SuperOffice to PowerOfficeGO Dataflow
=====================================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to PowerOfficeGOPowerOfficeGo Customers
-----------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGOPowerOfficeGo Customers must be established.

A new PowerOfficeGOPowerOfficeGo Customers will be created from a SuperOffice Contact if it is connected to a SuperOffice User, Person, Contact, Quoteline, or Quotealternative that is synchronized into PowerOfficeGOPowerOfficeGo.

A SuperOffice Contact will merge with a PowerOfficeGOPowerOfficeGo Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGOPowerOfficeGo Customers Property
   * - Emails.Value
     - EmailAddress

Once a link between a SuperOffice Contact and a PowerOfficeGOPowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGOPowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGOPowerOfficeGo Customers Property
     - PowerOfficeGOPowerOfficeGo Data Type
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
     - OrganizationNumber (Dependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.CountryCodeDependant on having wd:Q906278 in MailAddress.CountryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCodeDependant on having wd:Q906278 in MailAddress.countryCode)
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
   * - OrgNr (Dependant on having wd:Q852835 in Country.TwoLetterISOCountryDependant on having wd:Q852835 in Country.TwoLetterISOCountry)
     - Number
     - "string"
   * - OrgNr
     - OrganizationNumber (Dependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.CountryCodeDependant on having  in MailAddress.CountryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCodeDependant on having  in MailAddress.countryCode)
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


SuperOffice Person to PowerOfficeGO Contactperson
-------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a PowerOfficeGO Contactperson must be established.

A new PowerOfficeGO Contactperson will be created from a SuperOffice Person if it is connected to a SuperOffice Quotealternative that is synchronized into PowerOfficeGO.

A SuperOffice Person will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGO Contactperson Property
   * - Emails.Value
     - emailAddress

Once a link between a SuperOffice Person and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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
     - N/A
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


SuperOffice Person to PowerOfficeGOPowerOfficeGo Customers person
-----------------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a PowerOfficeGOPowerOfficeGo Customers person must be established.

A new PowerOfficeGOPowerOfficeGo Customers person will be created from a SuperOffice Person if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into PowerOfficeGOPowerOfficeGo.

A SuperOffice Person will merge with a PowerOfficeGOPowerOfficeGo Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGOPowerOfficeGo Customers person Property
   * - Emails.Value
     - EmailAddress

Once a link between a SuperOffice Person and a PowerOfficeGOPowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a PowerOfficeGOPowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGOPowerOfficeGo Customers person Property
     - PowerOfficeGOPowerOfficeGo Data Type
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
     - N/A
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


SuperOffice User to PowerOfficeGO Contactperson
-----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a PowerOfficeGO Contactperson must be established.

A SuperOffice User will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGO Contactperson Property
   * - personEmail
     - emailAddress

Once a link between a SuperOffice User and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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


SuperOffice User to PowerOfficeGO Customers person
--------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a PowerOfficeGO Customers person must be established.

A SuperOffice User will merge with a PowerOfficeGO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGO Customers person Property
   * - personEmail
     - EmailAddress

Once a link between a SuperOffice User and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - personEmail
     - EmailAddress
     - "string"


SuperOffice Contact to PowerOfficeGO Contactperson
--------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGO Contactperson must be established.

A new PowerOfficeGO Contactperson will be created from a SuperOffice Contact if it is connected to a SuperOffice Quotealternative that is synchronized into PowerOfficeGO.

Once a link between a SuperOffice Contact and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type


SuperOffice Contact to PowerOfficeGOPowerOfficeGo Customers person
------------------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOfficeGOPowerOfficeGo Customers person must be established.

A new PowerOfficeGOPowerOfficeGo Customers person will be created from a SuperOffice Contact if it is connected to a SuperOffice User, Person, Contact, Quoteline, or Quotealternative that is synchronized into PowerOfficeGOPowerOfficeGo.

Once a link between a SuperOffice Contact and a PowerOfficeGOPowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOfficeGOPowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOfficeGOPowerOfficeGo Customers person Property
     - PowerOfficeGOPowerOfficeGo Data Type
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


SuperOffice Person to PowerOfficeGoPowerOfficeGO Customers
----------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a PowerOfficeGoPowerOfficeGO Customers must be established.

A new PowerOfficeGoPowerOfficeGO Customers will be created from a SuperOffice Person if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into PowerOfficeGoPowerOfficeGO.

Once a link between a SuperOffice Person and a PowerOfficeGoPowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a PowerOfficeGoPowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOfficeGoPowerOfficeGO Customers Property
     - PowerOfficeGoPowerOfficeGO Data Type


SuperOffice Quotealternative to PowerOfficeGO Salesorders
---------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a PowerOfficeGO Salesorders must be established.

A new PowerOfficeGO Salesorders will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into PowerOfficeGO.

Once a link between a SuperOffice Quotealternative and a PowerOfficeGO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a PowerOfficeGO Salesorders:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - PowerOfficeGO Salesorders Property
     - PowerOfficeGO Data Type
   * - TotalPrice
     - TotalAmount
     - "string"
   * - sesam_SaleId (Dependant on having poweroffice-salesorder in sesam_AcceptedDependant on having poweroffice-salesorder in sesam_AcceptedDependant on having poweroffice-salesorder in sesam_AcceptedDependant on having poweroffice-salesorder in sesam_AcceptedDependant on having poweroffice-salesorder in sesam_Accepted)
     - Id
     - "string"


SuperOffice Product to PowerOfficeGO Product
--------------------------------------------
Every SuperOffice Product will be synchronized with a PowerOfficeGO Product.

Once a link between a SuperOffice Product and a PowerOfficeGO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a PowerOfficeGO Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - PowerOfficeGO Product Property
     - PowerOfficeGO Data Type
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
     - N/A
   * - UnitListPrice
     - SalesPrice
     - "string"
   * - UnitListPrice
     - salesPrice
     - N/A
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


SuperOffice Project to PowerOfficeGOPowerOffice GOPowerofficego Projects
------------------------------------------------------------------------
Every SuperOffice Project will be synchronized with a PowerOfficeGOPowerOffice GOPowerofficego Projects.

Once a link between a SuperOffice Project and a PowerOfficeGOPowerOffice GOPowerofficego Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Project and a PowerOfficeGOPowerOffice GOPowerofficego Projects:

.. list-table::
   :header-rows: 1

   * - SuperOffice Project Property
     - PowerOfficeGOPowerOffice GOPowerofficego Projects Property
     - PowerOfficeGOPowerOffice GOPowerofficego Data Type
   * - Associate.AssociateId
     - ProjectManagerEmployeeId
     - "integer"
   * - Name
     - Name
     - "string"


SuperOffice Quoteline to PowerOfficeGO Salesorderlines
------------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a SuperOffice Quoteline and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type
   * - DiscountPercent
     - Allowance
     - "float"
   * - DiscountPercent
     - Discount
     - "string"
   * - ERPDiscountPercent
     - Allowance
     - "float"
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
     - N/A
   * - QuoteAlternativeId
     - sesam_SalesOrderId
     - "string"
   * - QuoteAlternativeId
     - sesam_SalesOrdersId
     - "string"
   * - Rank
     - SortOrder
     - "integer"
   * - TotalPrice
     - TotalAmount
     - "string"
   * - UnitListPrice
     - ProductUnitPrice
     - N/A
   * - UnitListPrice
     - SalesOrderLineUnitPrice
     - "string"
   * - VAT
     - VatId
     - "string"
   * - VAT
     - VatReturnSpecification
     - "string"

