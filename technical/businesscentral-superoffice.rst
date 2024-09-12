========================================
Business Central to SuperOffice Dataflow
========================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Contacts person to SuperOffice Listcountryitems
----------------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Contacts person and a SuperOffice Listcountryitems must be established.

A Business Central Contacts person will merge with a SuperOffice Listcountryitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - SuperOffice Listcountryitems Property
   * - country
     - TwoLetterISOCountry

Once a link between a Business Central Contacts person and a SuperOffice Listcountryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a SuperOffice Listcountryitems:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - SuperOffice Listcountryitems Property
     - SuperOffice Data Type


Business Central Currencies to SuperOffice Pricelist
----------------------------------------------------
Before any synchronization can take place, a link between a Business Central Currencies and a SuperOffice Pricelist must be established.

A Business Central Currencies will merge with a SuperOffice Pricelist if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - SuperOffice Pricelist Property
   * - code
     - Currency

Once a link between a Business Central Currencies and a SuperOffice Pricelist is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Currencies and a SuperOffice Pricelist:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - SuperOffice Pricelist Property
     - SuperOffice Data Type


Business Central Customers company to SuperOffice Listcountryitems
------------------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers company and a SuperOffice Listcountryitems must be established.

A Business Central Customers company will merge with a SuperOffice Listcountryitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - SuperOffice Listcountryitems Property
   * - country
     - TwoLetterISOCountry

Once a link between a Business Central Customers company and a SuperOffice Listcountryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a SuperOffice Listcountryitems:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - SuperOffice Listcountryitems Property
     - SuperOffice Data Type


Business Central Customers person to SuperOffice Listcountryitems
-----------------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Customers person and a SuperOffice Listcountryitems must be established.

A Business Central Customers person will merge with a SuperOffice Listcountryitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - SuperOffice Listcountryitems Property
   * - country
     - TwoLetterISOCountry

Once a link between a Business Central Customers person and a SuperOffice Listcountryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a SuperOffice Listcountryitems:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - SuperOffice Listcountryitems Property
     - SuperOffice Data Type


Business Central Employees to SuperOffice Listcountryitems
----------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Employees and a SuperOffice Listcountryitems must be established.

A Business Central Employees will merge with a SuperOffice Listcountryitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - SuperOffice Listcountryitems Property
   * - country
     - TwoLetterISOCountry

Once a link between a Business Central Employees and a SuperOffice Listcountryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a SuperOffice Listcountryitems:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - SuperOffice Listcountryitems Property
     - SuperOffice Data Type


Businesscentral Customers to SuperOffice Contact
------------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Customers and a SuperOffice Contact must be established.

A new SuperOffice Contact will be created from a Businesscentral Customers if it is connected to a Businesscentral Contact, Employee, Employees, Contacts-person, or Customers-person that is synchronized into SuperOffice.

Once a link between a Businesscentral Customers and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers Property
     - SuperOffice Contact Property
     - SuperOffice Data Type


Business Central Salesorders to SuperOffice Quotealternative
------------------------------------------------------------
Before any synchronization can take place, a link between a Business Central Salesorders and a SuperOffice Quotealternative must be established.

A new SuperOffice Quotealternative will be created from a Business Central Salesorders if it is connected to a Business Central Businesscentral-salesorderlines that is synchronized into SuperOffice.

Once a link between a Business Central Salesorders and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - totalAmountExcludingTax
     - TotalPrice
     - "float"


Business Central Companies to SuperOffice Contact
-------------------------------------------------
Every Business Central Companies will be synchronized with a SuperOffice Contact.

Once a link between a Business Central Companies and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Companies and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Companies Property
     - SuperOffice Contact Property
     - SuperOffice Data Type


Business Central Contacts person to SuperOffice Person
------------------------------------------------------
Every Business Central Contacts person will be synchronized with a SuperOffice Person.

Once a link between a Business Central Contacts person and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - addressLine1
     - Address.Street.Address1
     - "string"
   * - addressLine2
     - Address.Street.Address2
     - "string"
   * - city
     - Address.Street.City
     - "string"
   * - country
     - Country.CountryId
     - "integer"
   * - email
     - Emails.Value
     - "string"
   * - id
     - PersonId
     - "integer"
   * - mobilePhoneNumber
     - MobilePhones.Value
     - "string"
   * - phoneNumber
     - OfficePhones.Value
     - "string"
   * - postalCode
     - Address.Street.Zipcode
     - "string"


Business Central Customers company to SuperOffice Contact
---------------------------------------------------------
Every Business Central Customers company will be synchronized with a SuperOffice Contact.

Once a link between a Business Central Customers company and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers company and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Customers company Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - address.city
     - Address.Postal.City
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.countryLetterCode
     - Country.CountryId
     - "integer"
   * - address.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - addressLine1
     - Address.Postal.Address1
     - "string"
   * - addressLine1
     - Address.Street.Address1
     - "string"
   * - addressLine2
     - Address.Postal.Address2
     - "string"
   * - addressLine2
     - Address.Street.Address2
     - "string"
   * - city
     - Address.Postal.City
     - "string"
   * - city
     - Address.Street.City
     - "string"
   * - country
     - Country.CountryId
     - "integer"
   * - displayName
     - Name
     - "string"
   * - id
     - ContactId
     - "integer"
   * - phoneNumber
     - Phones.Value
     - "string"
   * - postalCode
     - Address.Postal.Zipcode
     - "string"
   * - postalCode
     - Address.Street.Zipcode
     - "string"
   * - website
     - Urls.Value
     - "string"


Business Central Customers person to SuperOffice Person
-------------------------------------------------------
Every Business Central Customers person will be synchronized with a SuperOffice Person.

Once a link between a Business Central Customers person and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers person and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers person Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - addressLine1
     - Address.Street.Address1
     - "string"
   * - addressLine2
     - Address.Street.Address2
     - "string"
   * - city
     - Address.Street.City
     - "string"
   * - country
     - Country.CountryId
     - "integer"
   * - email
     - Emails.Value
     - "string"
   * - id
     - PersonId
     - "integer"
   * - phoneNumber
     - OfficePhones.Value
     - "string"
   * - postalCode
     - Address.Street.Zipcode
     - "string"


Business Central Employees to SuperOffice Person
------------------------------------------------
Every Business Central Employees will be synchronized with a SuperOffice Person.

Once a link between a Business Central Employees and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Employees and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Business Central Employees Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - birthDate
     - BirthDate
     - N/A
   * - email
     - Emails.Value
     - "string"
   * - givenName
     - Firstname
     - "string"
   * - jobTitle
     - Contact.ContactId
     - "integer"
   * - mobilePhone
     - MobilePhones.Value
     - "string"
   * - personalEmail
     - Emails.Value
     - "string"
   * - phoneNumber
     - OfficePhones.Value
     - "string"
   * - surname
     - Lastname
     - "string"


Business Central Currencies to SuperOffice Listcurrencyitems
------------------------------------------------------------
Every Business Central Currencies will be synchronized with a SuperOffice Listcurrencyitems.

If a matching SuperOffice Listcurrencyitems already exists, the Business Central Currencies will be merged with the existing one.
If no matching SuperOffice Listcurrencyitems is found, a new SuperOffice Listcurrencyitems will be created.

A Business Central Currencies will merge with a SuperOffice Listcurrencyitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - SuperOffice Listcurrencyitems Property
   * - code
     - Name

Once a link between a Business Central Currencies and a SuperOffice Listcurrencyitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Currencies and a SuperOffice Listcurrencyitems:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - SuperOffice Listcurrencyitems Property
     - SuperOffice Data Type


Business Central Itemcategories to SuperOffice Listproductcategoryitems
-----------------------------------------------------------------------
Every Business Central Itemcategories will be synchronized with a SuperOffice Listproductcategoryitems.

Once a link between a Business Central Itemcategories and a SuperOffice Listproductcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Itemcategories and a SuperOffice Listproductcategoryitems:

.. list-table::
   :header-rows: 1

   * - Business Central Itemcategories Property
     - SuperOffice Listproductcategoryitems Property
     - SuperOffice Data Type
   * - displayName
     - Name
     - "string"


Business Central Items to SuperOffice Product
---------------------------------------------
Every Business Central Items will be synchronized with a SuperOffice Product.

Once a link between a Business Central Items and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - displayName
     - Name
     - "string"
   * - displayName.string
     - Name
     - "string"
   * - displayName2
     - Name
     - "string"
   * - itemCategoryId
     - ProductCategoryKey
     - "string"
   * - taxGroupCode
     - VAT
     - N/A
   * - unitCost
     - UnitCost
     - "string"
   * - unitPrice
     - UnitListPrice
     - N/A


Business Central Salesorderlines to SuperOffice Quoteline
---------------------------------------------------------
Every Business Central Salesorderlines will be synchronized with a SuperOffice Quoteline.

Once a link between a Business Central Salesorderlines and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorderlines and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorderlines Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - description
     - Description
     - "string"
   * - description
     - Name
     - "string"
   * - discountPercent
     - DiscountPercent
     - "integer"
   * - discountPercent
     - ERPDiscountPercent
     - N/A
   * - documentId
     - QuoteAlternativeId
     - "integer"
   * - itemId
     - ERPProductKey
     - "string"
   * - quantity
     - Quantity
     - N/A
   * - taxPercent
     - VAT
     - "integer"
   * - unitPrice
     - UnitListPrice
     - N/A


Business Central Salesorders to SuperOffice Listcountryitems
------------------------------------------------------------
Every Business Central Salesorders will be synchronized with a SuperOffice Listcountryitems.

If a matching SuperOffice Listcountryitems already exists, the Business Central Salesorders will be merged with the existing one.
If no matching SuperOffice Listcountryitems is found, a new SuperOffice Listcountryitems will be created.

A Business Central Salesorders will merge with a SuperOffice Listcountryitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - SuperOffice Listcountryitems Property
   * - billToCountry
     - TwoLetterISOCountry
   * - shipToCountry
     - TwoLetterISOCountry

Once a link between a Business Central Salesorders and a SuperOffice Listcountryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a SuperOffice Listcountryitems:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - SuperOffice Listcountryitems Property
     - SuperOffice Data Type


Business Central Salesquotes to SuperOffice Listcountryitems
------------------------------------------------------------
Every Business Central Salesquotes will be synchronized with a SuperOffice Listcountryitems.

If a matching SuperOffice Listcountryitems already exists, the Business Central Salesquotes will be merged with the existing one.
If no matching SuperOffice Listcountryitems is found, a new SuperOffice Listcountryitems will be created.

A Business Central Salesquotes will merge with a SuperOffice Listcountryitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - SuperOffice Listcountryitems Property
   * - billToCountry
     - Name
   * - shipToCountry
     - Name

Once a link between a Business Central Salesquotes and a SuperOffice Listcountryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesquotes and a SuperOffice Listcountryitems:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - SuperOffice Listcountryitems Property
     - SuperOffice Data Type

