========================================
SuperOffice to Business Central Dataflow
========================================

Generated: 2024-09-11 11:42:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to BusinessCentral Customers company
--------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a BusinessCentral Customers company must be established.

A new BusinessCentral Customers company will be created from a SuperOffice Contact if it is connected to a SuperOffice Quotealternative that is synchronized into BusinessCentral.

Once a link between a SuperOffice Contact and a BusinessCentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a BusinessCentral Customers company:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - BusinessCentral Customers company Property
     - BusinessCentral Data Type
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


SuperOffice Contact to BusinessCentral Customers person
-------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a BusinessCentral Customers person must be established.

A new BusinessCentral Customers person will be created from a SuperOffice Contact if it is connected to a SuperOffice Quotealternative that is synchronized into BusinessCentral.

Once a link between a SuperOffice Contact and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type


SuperOffice Person to BusinessCentral Customers company
-------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a BusinessCentral Customers company must be established.

A new BusinessCentral Customers company will be created from a SuperOffice Person if it is connected to a SuperOffice Quotealternative that is synchronized into BusinessCentral.

Once a link between a SuperOffice Person and a BusinessCentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a BusinessCentral Customers company:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - BusinessCentral Customers company Property
     - BusinessCentral Data Type
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


SuperOffice Person to BusinessCentral Customers person
------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a BusinessCentral Customers person must be established.

A new BusinessCentral Customers person will be created from a SuperOffice Person if it is connected to a SuperOffice Quotealternative that is synchronized into BusinessCentral.

Once a link between a SuperOffice Person and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type
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


SuperOffice Quotealternative to Business Central Salesorders
------------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a Business Central Salesorders must be established.

A new Business Central Salesorders will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into Business Central.

Once a link between a SuperOffice Quotealternative and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Business Central Salesorders Property
     - Business Central Data Type
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


SuperOffice Contact to BusinessCentral Companies
------------------------------------------------
Every SuperOffice Contact will be synchronized with a BusinessCentral Companies.

Once a link between a SuperOffice Contact and a BusinessCentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a BusinessCentral Companies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - BusinessCentral Companies Property
     - BusinessCentral Data Type


SuperOffice Product to Business Central Items
---------------------------------------------
Every SuperOffice Product will be synchronized with a Business Central Items.

Once a link between a SuperOffice Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Business Central Items Property
     - Business Central Data Type
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


SuperOffice Quoteline to Business Central Salesorderlines
---------------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Business Central Salesorderlines.

Once a link between a SuperOffice Quoteline and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
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

