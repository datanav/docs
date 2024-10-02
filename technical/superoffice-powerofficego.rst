======================================
SuperOffice to PowerOffice GO Dataflow
======================================

Generated: 2024-10-02 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to PowerOffice GO Customers
-----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a PowerOffice GO Customers must be established.

A new PowerOffice GO Customers will be created from a SuperOffice Contact if it is connected to a SuperOffice User, Person, Contact, Quoteline, or Quotealternative that is synchronized into PowerOffice GO.

A SuperOffice Contact will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOffice GO Customers Property
   * - Emails.Value
     - EmailAddress

Once a link between a SuperOffice Contact and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
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
     - "integer"
   * - Country.CountryId
     - MailAddress.CountryCode
     - "string"
   * - Country.ThreeLetterISOCountry
     - OrganizationNumber (Dependant on having wd:Q906278 in MailAddress.CountryCode)
     - "string"
   * - Emails.Value
     - EmailAddress
     - "string"
   * - Name
     - Name
     - "string"
   * - OrgNr (Dependant on having wd:Q852835 in Country.TwoLetterISOCountry)
     - Number
     - "string"
   * - OrgNr
     - OrganizationNumber (Dependant on having  in MailAddress.CountryCode)
     - "string"
   * - Phones.Value
     - PhoneNumber
     - "string"
   * - Urls.Value
     - WebsiteUrl
     - "string"


SuperOffice Person to PowerOffice GO Contactperson
--------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a PowerOffice GO Contactperson must be established.

A new PowerOffice GO Contactperson will be created from a SuperOffice Person if it is connected to a SuperOffice Quotealternative that is synchronized into PowerOffice GO.

A SuperOffice Person will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOffice GO Contactperson Property
   * - Emails.Value
     - emailAddress

Once a link between a SuperOffice Person and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
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


SuperOffice Person to PowerOffice GO Customers
----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a PowerOffice GO Customers must be established.

A new PowerOffice GO Customers will be created from a SuperOffice Person if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into PowerOffice GO.

A SuperOffice Person will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOffice GO Customers Property
   * - Emails.Value
     - EmailAddress

Once a link between a SuperOffice Person and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
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


SuperOffice User to PowerOffice GO Contactperson
------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a PowerOffice GO Contactperson must be established.

A SuperOffice User will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOffice GO Contactperson Property
   * - personEmail
     - emailAddress

Once a link between a SuperOffice User and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
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


SuperOffice User to PowerOffice GO Customers
--------------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a PowerOffice GO Customers must be established.

A SuperOffice User will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOffice GO Customers Property
   * - personEmail
     - EmailAddress

Once a link between a SuperOffice User and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - personEmail
     - EmailAddress
     - "string"


SuperOffice Product to PowerOffice GO Product
---------------------------------------------
Every SuperOffice Product will be synchronized with a PowerOffice GO Product.

Once a link between a SuperOffice Product and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type
   * - Description
     - description
     - "string"
   * - Name
     - name
     - "string"
   * - ProductTypeKey
     - type
     - "integer"
   * - UnitCost
     - costPrice
     - N/A
   * - UnitListPrice
     - salesPrice
     - N/A
   * - VAT
     - vatCode
     - "string"


SuperOffice Project to PowerOffice GO Projects
----------------------------------------------
Every SuperOffice Project will be synchronized with a PowerOffice GO Projects.

Once a link between a SuperOffice Project and a PowerOffice GO Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Project and a PowerOffice GO Projects:

.. list-table::
   :header-rows: 1

   * - SuperOffice Project Property
     - PowerOffice GO Projects Property
     - PowerOffice GO Data Type


SuperOffice Quoteline to PowerOffice GO Salesorderlines
-------------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a SuperOffice Quoteline and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type
   * - DiscountPercent
     - Allowance
     - "float"
   * - ERPDiscountPercent
     - Allowance
     - "float"
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
   * - Rank
     - SortOrder
     - "integer"
   * - UnitListPrice
     - ProductUnitPrice
     - N/A

