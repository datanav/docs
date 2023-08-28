=================================
Tripletex to SuperOffice Dataflow
=================================

Generated: 2023-08-28 15:10:48

Introduction.
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
   * - invoiceEmail
     - Emails.Value
   * - overdueNoticeEmail
     - Emails.Value

Once a link between a Tripletex Customer and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
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
     - OrgNr (Dependant on having NOR in Country.ThreeLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountryDependant on having NO in Country.ThreeLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountry)
     - "string"
   * - phoneNumber
     - Phones.Value
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
   * - physicalAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - postalAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - postalAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - postalAddress.city
     - Address.Postal.City
     - "string"
   * - postalAddress.country.id
     - Country.CountryId
     - "integer"
   * - postalAddress.postalCode
     - Address.Postal.Zipcode
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
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - dateOfBirth
     - BirthDate
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - department.id
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
Every Tripletex Supplier will be synchronized with a SuperOffice Contact.

If a matching SuperOffice Contact already exists, the Tripletex Supplier will be merged with the existing one.
If no matching SuperOffice Contact is found, a new SuperOffice Contact will be created.

A Tripletex Supplier will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - SuperOffice Contact Property
   * - email
     - Emails.Value
   * - invoiceEmail
     - Emails.Value
   * - overdueNoticeEmail
     - Emails.Value

Once a link between a Tripletex Supplier and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - email
     - Emails.Value
     - "string"
   * - id
     - ContactId
     - "integer"
   * - name
     - Name
     - "string"
   * - phoneNumber
     - Phones.Value
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
   * - physicalAddress.postalCode
     - Address.Street.Zipcode
     - "string"
   * - postalAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - postalAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - postalAddress.city
     - Address.Postal.City
     - "string"
   * - postalAddress.country.id
     - Country.CountryId
     - "integer"
   * - postalAddress.postalCode
     - Address.Postal.Zipcode
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
     - "integer"
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
     - "string"
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

If a matching SuperOffice Product already exists, the Tripletex Product will be merged with the existing one.
If no matching SuperOffice Product is found, a new SuperOffice Product will be created.

A Tripletex Product will merge with a SuperOffice Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - SuperOffice Product Property
   * - number
     - ERPProductKey

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
   * - priceExcludingVatCurrency
     - UnitListPrice
     - "decimal"
   * - productUnit.id
     - QuantityUnit
     - "string"
   * - supplier.id
     - Supplier
     - "string"
   * - vatType.id
     - VAT
     - "integer"


Tripletex Productgroup to SuperOffice Listproductcategoryitems
--------------------------------------------------------------
Every Tripletex Productgroup will be synchronized with a SuperOffice Listproductcategoryitems.

Once a link between a Tripletex Productgroup and a SuperOffice Listproductcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a SuperOffice Listproductcategoryitems:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - SuperOffice Listproductcategoryitems Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"

