=======================================
Businesscentral to Superoffice Dataflow
=======================================

Generated: 2024-07-06 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Businesscentral Salesorders to Superoffice Quotealternative
-----------------------------------------------------------
Before any synchronization can take place, a link between a Businesscentral Salesorders and a Superoffice Quotealternative must be established.

A new Superoffice Quotealternative will be created from a Businesscentral Salesorders if it is connected to a Businesscentral Salesorderlines that is synchronized into Superoffice.

Once a link between a Businesscentral Salesorders and a Superoffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a Superoffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     - Superoffice Quotealternative Property
     - Superoffice Data Type
   * - totalAmountExcludingTax
     - TotalPrice
     - "float"


Businesscentral Companies to Superoffice Contact
------------------------------------------------
Every Businesscentral Companies will be synchronized with a Superoffice Contact.

Once a link between a Businesscentral Companies and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Companies and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Companies Property
     - Superoffice Contact Property
     - Superoffice Data Type


Businesscentral Contacts person to Superoffice Person
-----------------------------------------------------
Every Businesscentral Contacts person will be synchronized with a Superoffice Person.

Once a link between a Businesscentral Contacts person and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     - Superoffice Person Property
     - Superoffice Data Type
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


Businesscentral Customers company to Superoffice Contact
--------------------------------------------------------
Every Businesscentral Customers company will be synchronized with a Superoffice Contact.

Once a link between a Businesscentral Customers company and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     - Superoffice Contact Property
     - Superoffice Data Type
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


Businesscentral Customers person to Superoffice Person
------------------------------------------------------
Every Businesscentral Customers person will be synchronized with a Superoffice Person.

Once a link between a Businesscentral Customers person and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     - Superoffice Person Property
     - Superoffice Data Type
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


Businesscentral Employees to Superoffice Person
-----------------------------------------------
Every Businesscentral Employees will be synchronized with a Superoffice Person.

Once a link between a Businesscentral Employees and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     - Superoffice Person Property
     - Superoffice Data Type
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


Businesscentral Items to Superoffice Product
--------------------------------------------
Every Businesscentral Items will be synchronized with a Superoffice Product.

Once a link between a Businesscentral Items and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     - Superoffice Product Property
     - Superoffice Data Type
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


Businesscentral Salesorderlines to Superoffice Quoteline
--------------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a Superoffice Quoteline.

Once a link between a Businesscentral Salesorderlines and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     - Superoffice Quoteline Property
     - Superoffice Data Type
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

