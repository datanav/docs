========================
SuperOffice to  Dataflow
========================

Generated: 2024-03-26 13:42:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Customers company
-----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a  Customers company must be established.

A new  Customers company will be created from a SuperOffice Contact if it is connected to a SuperOffice Quotealternative that is synchronized into .

Once a link between a SuperOffice Contact and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Customers company:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Customers company Property
     -  Data Type
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


SuperOffice Contact to  Customers person
----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a  Customers person must be established.

A new  Customers person will be created from a SuperOffice Contact if it is connected to a SuperOffice Quotealternative that is synchronized into .

Once a link between a SuperOffice Contact and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Customers person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Customers person Property
     -  Data Type


SuperOffice Person to  Customers company
----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a  Customers company must be established.

A new  Customers company will be created from a SuperOffice Person if it is connected to a SuperOffice Quotealternative that is synchronized into .

Once a link between a SuperOffice Person and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Customers company:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Customers company Property
     -  Data Type
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


SuperOffice Person to  Customers person
---------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a  Customers person must be established.

A new  Customers person will be created from a SuperOffice Person if it is connected to a SuperOffice Quotealternative that is synchronized into .

Once a link between a SuperOffice Person and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Customers person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Customers person Property
     -  Data Type
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


SuperOffice Quotealternative to  Salesorders
--------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a  Salesorders must be established.

A new  Salesorders will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into .

Once a link between a SuperOffice Quotealternative and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     -  Salesorders Property
     -  Data Type
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


SuperOffice Contact to  Companies
---------------------------------
Every SuperOffice Contact will be synchronized with a  Companies.

Once a link between a SuperOffice Contact and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Companies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Companies Property
     -  Data Type


SuperOffice Product to  Items
-----------------------------
Every SuperOffice Product will be synchronized with a  Items.

Once a link between a SuperOffice Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Items:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Items Property
     -  Data Type
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
     - "decimal"
   * - UnitListPrice
     - unitPrice
     - "decimal"
   * - VAT
     - itemCategoryId
     - "string"
   * - VAT
     - taxGroupCode
     - "string"
   * - VAT
     - taxGroupId
     - "string"


SuperOffice Quoteline to  Salesorderlines
-----------------------------------------
Every SuperOffice Quoteline will be synchronized with a  Salesorderlines.

Once a link between a SuperOffice Quoteline and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     -  Salesorderlines Property
     -  Data Type
   * - Description
     - description
     - "string"
   * - DiscountPercent
     - discountPercent
     - "decimal"
   * - ERPDiscountPercent
     - discountPercent
     - "decimal"
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
     - "integer", "decimal"]
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
     - "decimal"

