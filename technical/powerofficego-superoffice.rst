=====================================
Powerofficego to SuperOffice Dataflow
=====================================

Generated: 2023-11-29 14:44:42

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to SuperOffice Person
-------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the Powerofficego Contactperson will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A Powerofficego Contactperson will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - SuperOffice Person Property
   * - emailAddress
     - Emails.Value

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


Powerofficego Customers person to SuperOffice Person
----------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a SuperOffice Person must be established.

A Powerofficego Customers person will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - SuperOffice Person Property
   * - EmailAddress
     - Emails.Value

Once a link between a Powerofficego Customers person and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - SuperOffice Person Property
     - SuperOffice Data Type
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
   * - InvoiceEmailAddress
     - Emails.Value
   * - PaymentReminderEmailAddress
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
     - Phones.Value
     - "string"
   * - OrganizationNumber
     - OrgNr (Dependant on having  in Country.TwoLetterISOCountryDependant on having  in Country.TwoLetterISOCountryDependant on having  in Country.TwoLetterISOCountryDependant on having  in Country.TwoLetterISOCountryDependant on having  in Country.TwoLetterISOCountryDependant on having  in Country.TwoLetterISOCountry)
     - "string"
   * - PhoneNumber
     - Phones.Value
     - "string"
   * - WebsiteUrl
     - Urls.Value
     - "string"


Powerofficego Product classification type to SuperOffice Listproducttypeitems
-----------------------------------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Product classification type and a SuperOffice Listproducttypeitems must be established.

A new SuperOffice Listproducttypeitems will be created from a Powerofficego Product classification type if it is connected to a Powerofficego Product that is synchronized into SuperOffice.

Once a link between a Powerofficego Product classification type and a SuperOffice Listproducttypeitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product classification type and a SuperOffice Listproducttypeitems:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product classification type Property
     - SuperOffice Listproducttypeitems Property
     - SuperOffice Data Type


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


Powerofficego Product to SuperOffice Listproducttypeitems
---------------------------------------------------------
Every Powerofficego Product will be synchronized with a SuperOffice Listproducttypeitems.

Once a link between a Powerofficego Product and a SuperOffice Listproducttypeitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a SuperOffice Listproducttypeitems:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - SuperOffice Listproducttypeitems Property
     - SuperOffice Data Type


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

