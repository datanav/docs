=================================
Tripletex to SuperOffice Dataflow
=================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to SuperOffice Person
---------------------------------------
Every Tripletex Contact will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the Tripletex Contact will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A Tripletex Contact will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - SuperOffice Person Property
   * - email
     - Emails.Value

Once a link between a Tripletex Contact and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - customer.id
     - Contact.ContactId
     - "integer"
   * - email
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"
   * - lastName
     - Lastname
     - "string"
   * - phoneNumberMobile
     - MobilePhones.Value
     - "string"
   * - phoneNumberWork
     - OfficePhones.Value
     - "string"


Tripletex Customer person to SuperOffice Person
-----------------------------------------------
Every Tripletex Customer person will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the Tripletex Customer person will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A Tripletex Customer person will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - SuperOffice Person Property
   * - email
     - Emails.Value

Once a link between a Tripletex Customer person and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - deliveryAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - deliveryAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - deliveryAddress.city
     - Address.Street.City
     - "string"
   * - deliveryAddress.country.id
     - Country.CountryId
     - "integer"
   * - deliveryAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - id
     - PersonId
     - "integer"
   * - phoneNumber
     - OfficePhones.Value
     - "string"
   * - phoneNumberMobile
     - MobilePhones.Value
     - "string"
   * - physicalAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - physicalAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - physicalAddress.city
     - Address.Street.City
     - "string"
   * - physicalAddress.country.id
     - Country.CountryId
     - "integer"
   * - physicalAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - postalAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - postalAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - postalAddress.city
     - Address.Street.City
     - "string"
   * - postalAddress.country.id
     - Country.CountryId
     - "integer"
   * - postalAddress.postalCode
     - Address.Street.Zipcode
     - "string"


Tripletex Customer to SuperOffice Contact
-----------------------------------------
Every Tripletex Customer will be synchronized with a SuperOffice Contact.

If a matching SuperOffice Contact already exists, the Tripletex Customer will be merged with the existing one.
If no matching SuperOffice Contact is found, a new SuperOffice Contact will be created.

A Tripletex Customer will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - SuperOffice Contact Property
   * - email
     - Emails.Value

Once a link between a Tripletex Customer and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - customerNumber
     - OrgNr (Dependant on having wd:Q852835 in Country.TwoLetterISOCountryDependant on having wd:Q852835 in Country.TwoLetterISOCountry)
     - "string"
   * - deliveryAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - deliveryAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - deliveryAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - deliveryAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - deliveryAddress.city
     - Address.Postal.City
     - "string"
   * - deliveryAddress.city
     - Address.Street.City
     - "string"
   * - deliveryAddress.country.id
     - Country.CountryId
     - "integer"
   * - deliveryAddress.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - deliveryAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - id
     - ContactId
     - "integer"
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrgNr (Dependant on having NO in Country.TwoLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountryDependant on having NO in Country.ThreeLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountry)
     - "string"
   * - phoneNumber
     - Phones.Value
     - "string"
   * - physicalAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - physicalAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - physicalAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - physicalAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - physicalAddress.city
     - Address.Postal.City
     - "string"
   * - physicalAddress.city
     - Address.Street.City
     - "string"
   * - physicalAddress.country.id
     - Country.CountryId
     - "integer"
   * - physicalAddress.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - physicalAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - postalAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - postalAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - postalAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - postalAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - postalAddress.city
     - Address.Postal.City
     - "string"
   * - postalAddress.city
     - Address.Street.City
     - "string"
   * - postalAddress.country.id
     - Country.CountryId
     - "integer"
   * - postalAddress.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - postalAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - url
     - Urls.Value
     - "string"
   * - website
     - Urls.Value
     - "string"


Tripletex Employee to SuperOffice Person
----------------------------------------
Every Tripletex Employee will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the Tripletex Employee will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A Tripletex Employee will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - SuperOffice Person Property
   * - email
     - Emails.Value

Once a link between a Tripletex Employee and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - address.addressLine1
     - Address.Street.Address1
     - "string"
   * - address.addressLine2
     - Address.Street.Address2
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.country.id
     - Country.CountryId
     - "integer"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - dateOfBirth
     - BirthDate
     - N/A
   * - department.id (Dependant on having wd:Q703534 in  )
     - Contact.ContactId
     - "integer"
   * - email
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
   * - phoneNumberHome
     - PrivatePhones.Value
     - "string"
   * - phoneNumberMobile
     - MobilePhones.Value
     - "string"
   * - phoneNumberWork
     - OfficePhones.Value
     - "string"


Tripletex Supplier to SuperOffice Contact
-----------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a SuperOffice Contact must be established.

A new SuperOffice Contact will be created from a Tripletex Supplier if it is connected to a Tripletex Product, or Productgrouprelation that is synchronized into SuperOffice.

A Tripletex Supplier will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - SuperOffice Contact Property
   * - email
     - Emails.Value

Once a link between a Tripletex Supplier and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - deliveryAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - deliveryAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - deliveryAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - deliveryAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - deliveryAddress.changes
     - Address.Postal.City
     - "string"
   * - deliveryAddress.changes
     - Address.Street.City
     - "string"
   * - deliveryAddress.city
     - Address.Postal.City
     - "string"
   * - deliveryAddress.city
     - Address.Street.City
     - "string"
   * - deliveryAddress.city
     - Country.CountryId
     - "integer"
   * - deliveryAddress.country.id
     - Country.CountryId
     - "integer"
   * - deliveryAddress.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - deliveryAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - id
     - ContactId
     - "integer"
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrgNr (Dependant on having NO in Country.TwoLetterISOCountry)
     - "string"
   * - phoneNumber
     - Phones.Value
     - "string"
   * - physicalAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - physicalAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - physicalAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - physicalAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - physicalAddress.city
     - Address.Postal.City
     - "string"
   * - physicalAddress.city
     - Address.Street.City
     - "string"
   * - physicalAddress.country.id
     - Country.CountryId
     - "integer"
   * - physicalAddress.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - physicalAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - postalAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - postalAddress.addressLine1
     - Address.Street.Address1
     - "string"
   * - postalAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - postalAddress.addressLine2
     - Address.Street.Address2
     - "string"
   * - postalAddress.city
     - Address.Postal.City
     - "string"
   * - postalAddress.city
     - Address.Street.City
     - "string"
   * - postalAddress.country.id
     - Country.CountryId
     - "integer"
   * - postalAddress.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - postalAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - url
     - Urls.Value
     - "string"


Tripletex Contact to SuperOffice Contact
----------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a SuperOffice Contact must be established.

A new SuperOffice Contact will be created from a Tripletex Contact if it is connected to a Tripletex Order that is synchronized into SuperOffice.

Once a link between a Tripletex Contact and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - SuperOffice Contact Property
     - SuperOffice Data Type


Tripletex Customer to SuperOffice Person
----------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a SuperOffice Person must be established.

A new SuperOffice Person will be created from a Tripletex Customer if it is connected to a Tripletex Order that is synchronized into SuperOffice.

Once a link between a Tripletex Customer and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - SuperOffice Person Property
     - SuperOffice Data Type


Tripletex Order to SuperOffice Quotealternative
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Order and a SuperOffice Quotealternative must be established.

A new SuperOffice Quotealternative will be created from a Tripletex Order if it is connected to a Tripletex Orderline that is synchronized into SuperOffice.

Once a link between a Tripletex Order and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - invoiceComment
     - Name
     - "string"


Tripletex Department to SuperOffice Contact
-------------------------------------------
Every Tripletex Department will be synchronized with a SuperOffice Contact.

Once a link between a Tripletex Department and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - departmentNumber
     - OrgNr (Dependant on having wd:Q2366457 in Country.TwoLetterISOCountryDependant on having wd:Q2366457 in Country.TwoLetterISOCountry)
     - "string"
   * - name
     - Name
     - "string"


Tripletex Orderline to SuperOffice Quoteline
--------------------------------------------
Every Tripletex Orderline will be synchronized with a SuperOffice Quoteline.

Once a link between a Tripletex Orderline and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - count
     - DiscountPercent
     - "integer"
   * - count
     - Name
     - "string"
   * - count
     - Quantity
     - N/A
   * - count
     - QuantityUnit
     - "integer"
   * - count
     - Rank (Dependant on having  in Rank)
     - "integer"
   * - count
     - UnitListPrice
     - "string"
   * - count
     - VAT
     - "integer"
   * - description
     - Description
     - "string"
   * - description
     - DiscountPercent
     - "integer"
   * - description
     - Name
     - "string"
   * - description
     - Quantity
     - "integer"
   * - description
     - QuantityUnit
     - "integer"
   * - description
     - Rank (Dependant on having  in Rank)
     - "integer"
   * - description
     - UnitListPrice
     - "string"
   * - description
     - VAT
     - "integer"
   * - discount
     - DiscountPercent
     - "integer"
   * - discount
     - ERPDiscountPercent
     - N/A
   * - discount
     - Name
     - "string"
   * - discount
     - Quantity
     - "integer"
   * - discount
     - QuantityUnit
     - "integer"
   * - discount
     - Rank (Dependant on having  in Rank)
     - "integer"
   * - discount
     - UnitListPrice
     - "string"
   * - discount
     - VAT
     - "integer"
   * - order.id
     - QuoteAlternativeId
     - "integer"
   * - product.id
     - ERPProductKey
     - "string"
   * - unitCostCurrency
     - DiscountPercent
     - "integer"
   * - unitCostCurrency
     - Name
     - "string"
   * - unitCostCurrency
     - Quantity
     - "integer"
   * - unitCostCurrency
     - QuantityUnit
     - "integer"
   * - unitCostCurrency
     - Rank (Dependant on having  in Rank)
     - "integer"
   * - unitCostCurrency
     - UnitListPrice
     - "string"
   * - unitCostCurrency
     - VAT
     - "integer"
   * - unitPriceExcludingVatCurrency
     - DiscountPercent
     - "integer"
   * - unitPriceExcludingVatCurrency
     - Name
     - "string"
   * - unitPriceExcludingVatCurrency
     - Quantity
     - "integer"
   * - unitPriceExcludingVatCurrency
     - QuantityUnit
     - "integer"
   * - unitPriceExcludingVatCurrency
     - Rank (Dependant on having  in Rank)
     - "integer"
   * - unitPriceExcludingVatCurrency
     - UnitListPrice
     - N/A
   * - unitPriceExcludingVatCurrency
     - VAT
     - "integer"
   * - vatType.id
     - DiscountPercent
     - "integer"
   * - vatType.id
     - Name
     - "string"
   * - vatType.id
     - Quantity
     - "integer"
   * - vatType.id
     - QuantityUnit
     - "integer"
   * - vatType.id
     - Rank (Dependant on having  in Rank)
     - "integer"
   * - vatType.id
     - UnitListPrice
     - "string"
   * - vatType.id
     - VAT
     - "integer"


Tripletex Product to SuperOffice Product
----------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a SuperOffice Product.

Once a link between a Tripletex Product and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - costExcludingVatCurrency
     - UnitCost
     - "string"
   * - currency.id
     - ERPPriceListKey
     - "string"
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - number
     - Code
     - "string"
   * - number
     - ERPProductKey
     - "string"
   * - priceExcludingVatCurrency
     - UnitListPrice
     - N/A
   * - productUnit.id
     - QuantityUnit
     - "string"
   * - supplier.id
     - Supplier
     - "string"
   * - vatType.id
     - VAT
     - "integer"

