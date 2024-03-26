======================
Tripletex to  Dataflow
======================

Generated: 2024-03-26 00:00:03

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Tripletex Customer person to  Person
------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer person and a  Person must be established.

A Tripletex Customer person will merge with a  Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     -  Person Property
   * - email
     - Emails.Value

Once a link between a Tripletex Customer person and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a  Person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     -  Person Property
     -  Data Type
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


Tripletex Employee to  Person
-----------------------------
Every Tripletex Employee will be synchronized with a  Person.

If a matching  Person already exists, the Tripletex Employee will be merged with the existing one.
If no matching  Person is found, a new  Person will be created.

A Tripletex Employee will merge with a  Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Person Property
   * - email
     - Emails.Value

Once a link between a Tripletex Employee and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Person:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Person Property
     -  Data Type
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
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
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


Tripletex Order to  Quotealternative
------------------------------------
Before any synchronization can take place, a link between a Tripletex Order and a  Quotealternative must be established.

A new  Quotealternative will be created from a Tripletex Order if it is connected to a Tripletex Orderline that is synchronized into .

Once a link between a Tripletex Order and a  Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a  Quotealternative:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     -  Quotealternative Property
     -  Data Type
   * - invoiceComment
     - Name
     - "string"


Tripletex Department to  Contact
--------------------------------
Every Tripletex Department will be synchronized with a  Contact.

Once a link between a Tripletex Department and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Contact Property
     -  Data Type
   * - departmentNumber
     - OrgNr (Dependant on having wd:Q2366457 in Country.TwoLetterISOCountry)
     - "string"
   * - name
     - Name
     - "string"


Tripletex Orderline to  Quoteline
---------------------------------
Every Tripletex Orderline will be synchronized with a  Quoteline.

Once a link between a Tripletex Orderline and a  Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a  Quoteline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     -  Quoteline Property
     -  Data Type
   * - count
     - DiscountPercent
     - "integer"
   * - count
     - Name
     - "string"
   * - count
     - Quantity
     - "integer", "decimal"]
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
     - "decimal"
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
     - "if-null", "integer", "string"], "decimal"]
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


Tripletex Product to  Product
-----------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Product.

Once a link between a Tripletex Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Product Property
     -  Data Type
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

