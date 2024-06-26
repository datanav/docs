=======================================
SuperOffice to Businesscentral Dataflow
=======================================

Generated: 2024-06-26 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Businesscentral Customers company
--------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Businesscentral Customers company must be established.

A new Businesscentral Customers company will be created from a SuperOffice Contact if it is connected to a SuperOffice Quotealternative that is synchronized into Businesscentral.

Once a link between a SuperOffice Contact and a Businesscentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Businesscentral Customers company:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Businesscentral Customers company Property
     - Businesscentral Data Type
   * - Address.Postal.Address1
     - addressLine1
     - "string"
   * - Address.Postal.Address2
     - addressLine2
     - "string"
   * - Address.Postal.City
     - address.city
     - "string"
   * - Address.Postal.City
     - city
     - "string"
   * - Address.Postal.Zipcode
     - address.postalCode
     - "string"
   * - Address.Postal.Zipcode
     - postalCode
     - "string"
   * - Address.Street.Address1
     - addressLine1
     - "string"
   * - Address.Street.Address2
     - addressLine2
     - "string"
   * - Address.Street.City
     - address.city
     - "string"
   * - Address.Street.City
     - city
     - "string"
   * - Address.Street.Zipcode
     - address.postalCode
     - "string"
   * - Address.Street.Zipcode
     - postalCode
     - "string"
   * - ContactId
     - id
     - "string"
   * - Country.CountryId
     - address.countryLetterCode
     - "string"
   * - Country.CountryId
     - country
     - "string"
   * - Emails.Value
     - id (Dependant on having wd:Q1273217 in type)
     - "string"
   * - Name
     - displayName
     - "string"
   * - OrgNr
     - id (Dependant on having  in typeDependant on having  in type)
     - "string"
   * - Phones.Value
     - phoneNumber
     - "string"
   * - Urls.Value
     - website
     - "string"


SuperOffice Contact to Businesscentral Customers person
-------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Businesscentral Customers person must be established.

A new Businesscentral Customers person will be created from a SuperOffice Contact if it is connected to a SuperOffice Quotealternative that is synchronized into Businesscentral.

Once a link between a SuperOffice Contact and a Businesscentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Businesscentral Customers person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Businesscentral Customers person Property
     - Businesscentral Data Type


SuperOffice Person to Businesscentral Customers company
-------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Businesscentral Customers company must be established.

A new Businesscentral Customers company will be created from a SuperOffice Person if it is connected to a SuperOffice Quotealternative that is synchronized into Businesscentral.

Once a link between a SuperOffice Person and a Businesscentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Businesscentral Customers company:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Businesscentral Customers company Property
     - Businesscentral Data Type
   * - Address.Street.Address1
     - addressLine1
     - "string"
   * - Address.Street.Address2
     - addressLine2
     - "string"
   * - Address.Street.City
     - city
     - "string"
   * - Address.Street.Zipcode
     - postalCode
     - "string"
   * - Country.CountryId
     - country
     - "string"
   * - PersonId
     - id
     - "string"


SuperOffice Person to Businesscentral Customers person
------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Businesscentral Customers person must be established.

A new Businesscentral Customers person will be created from a SuperOffice Person if it is connected to a SuperOffice Quotealternative that is synchronized into Businesscentral.

Once a link between a SuperOffice Person and a Businesscentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Businesscentral Customers person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Businesscentral Customers person Property
     - Businesscentral Data Type
   * - Address.Street.Address1
     - addressLine1
     - "string"
   * - Address.Street.Address2
     - addressLine2
     - "string"
   * - Address.Street.City
     - address.city
     - "string"
   * - Address.Street.City
     - addressLine2
     - "string"
   * - Address.Street.City
     - city
     - "string"
   * - Address.Street.Zipcode
     - address.postalCode
     - "string"
   * - Address.Street.Zipcode
     - postalCode
     - "string"
   * - Country.CountryId
     - country
     - "string"
   * - Emails.Value
     - email
     - "string"
   * - Emails.Value
     - id (Dependant on having wd:Q1273217 in type)
     - "string"
   * - OfficePhones.Value
     - phoneNumber
     - "string"
   * - PersonId
     - id
     - "string"


SuperOffice Quotealternative to Businesscentral Salesorders
-----------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a Businesscentral Salesorders must be established.

A new Businesscentral Salesorders will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into Businesscentral.

Once a link between a SuperOffice Quotealternative and a Businesscentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Businesscentral Salesorders:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Businesscentral Salesorders Property
     - Businesscentral Data Type
   * - TotalPrice
     - totalAmountExcludingTax
     - "string"
   * - VAT
     - billToCountry
     - "string"
   * - VAT
     - billingPostalAddress.countryLetterCode
     - "string"
   * - VAT
     - shipToCountry
     - "string"
   * - VAT
     - shippingPostalAddress.countryLetterCode
     - "string"


SuperOffice Contact to Businesscentral Companies
------------------------------------------------
Every SuperOffice Contact will be synchronized with a Businesscentral Companies.

Once a link between a SuperOffice Contact and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


SuperOffice Product to Businesscentral Items
--------------------------------------------
Every SuperOffice Product will be synchronized with a Businesscentral Items.

Once a link between a SuperOffice Product and a Businesscentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Businesscentral Items:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Businesscentral Items Property
     - Businesscentral Data Type
   * - Name
     - displayName
     - "string"
   * - Name
     - displayName.string
     - "string"
   * - Name
     - displayName2
     - "string"
   * - ProductCategoryKey
     - itemCategoryId
     - "string"
   * - UnitCost
     - unitCost
     - N/A
   * - UnitListPrice
     - unitPrice
     - N/A
   * - VAT
     - itemCategoryId
     - "string"
   * - VAT
     - taxGroupCode
     - "string"
   * - VAT
     - taxGroupId
     - "string"


SuperOffice Quoteline to Businesscentral Salesorderlines
--------------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Businesscentral Salesorderlines.

Once a link between a SuperOffice Quoteline and a Businesscentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Businesscentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Businesscentral Salesorderlines Property
     - Businesscentral Data Type
   * - Description
     - description
     - "string"
   * - DiscountPercent
     - discountPercent
     - N/A
   * - ERPDiscountPercent
     - discountPercent
     - N/A
   * - ERPProductKey
     - itemId
     - "string"
   * - Name
     - description
     - "string"
   * - Quantity
     - invoiceQuantity
     - "string"
   * - Quantity
     - quantity
     - N/A
   * - QuoteAlternativeId
     - documentId
     - "string"
   * - UnitListPrice
     - amountExcludingTax
     - "string"
   * - UnitListPrice
     - unitPrice
     - "float"
   * - VAT
     - taxPercent
     - N/A

