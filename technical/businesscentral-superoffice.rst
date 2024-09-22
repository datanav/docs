========================================
Business Central to SuperOffice Dataflow
========================================

Generated: 2024-09-22 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Business Central Contacts (human data) to SuperOffice Person
------------------------------------------------------------
Every Business Central Contacts (human data) will be synchronized with a SuperOffice Person.

Once a link between a Business Central Contacts (human data) and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts (human data) and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts (human data) Property
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


Business Central Customers (organisation data) to SuperOffice Contact
---------------------------------------------------------------------
Every Business Central Customers (organisation data) will be synchronized with a SuperOffice Contact.

Once a link between a Business Central Customers (organisation data) and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (organisation data) and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (organisation data) Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
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


Business Central Customers (human data) to SuperOffice Person
-------------------------------------------------------------
Every Business Central Customers (human data) will be synchronized with a SuperOffice Person.

Once a link between a Business Central Customers (human data) and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Customers (human data) and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Business Central Customers (human data) Property
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
   * - givenName
     - Firstname
     - "string"
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
     - Name
     - "string"
   * - discountPercent
     - ERPDiscountPercent
     - "integer"
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

