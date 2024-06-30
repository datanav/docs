=================================
SuperOffice to Tripletex Dataflow
=================================

Generated: 2024-06-30 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Tripletex Customer
-----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, User, Quote, Person, Contact, Quoteline, or Quotealternative that is synchronized into Tripletex.

A SuperOffice Contact will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Customer Property
   * - Emails.Value
     - email

Once a link between a SuperOffice Contact and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - Address.Postal.Address1
     - deliveryAddress.addressLine1
     - "string"
   * - Address.Postal.Address1
     - physicalAddress.addressLine1
     - "string"
   * - Address.Postal.Address1
     - postalAddress.addressLine1
     - "string"
   * - Address.Postal.Address2
     - deliveryAddress.addressLine2
     - "string"
   * - Address.Postal.Address2
     - physicalAddress.addressLine2
     - "string"
   * - Address.Postal.Address2
     - postalAddress.addressLine2
     - "string"
   * - Address.Postal.City
     - deliveryAddress.city
     - "string"
   * - Address.Postal.City
     - physicalAddress.city
     - "string"
   * - Address.Postal.City
     - postalAddress.city
     - "string"
   * - Address.Postal.Zipcode
     - deliveryAddress.postalCode
     - "string"
   * - Address.Postal.Zipcode
     - physicalAddress.postalCode
     - "string"
   * - Address.Postal.Zipcode
     - postalAddress.postalCode
     - "string"
   * - Address.Street.Address1
     - deliveryAddress.addressLine1
     - "string"
   * - Address.Street.Address1
     - physicalAddress.addressLine1
     - "string"
   * - Address.Street.Address1
     - postalAddress.addressLine1
     - "string"
   * - Address.Street.Address2
     - deliveryAddress.addressLine2
     - "string"
   * - Address.Street.Address2
     - physicalAddress.addressLine2
     - "string"
   * - Address.Street.Address2
     - postalAddress.addressLine2
     - "string"
   * - Address.Street.City
     - deliveryAddress.city
     - "string"
   * - Address.Street.City
     - physicalAddress.city
     - "string"
   * - Address.Street.City
     - postalAddress.city
     - "string"
   * - Address.Street.Zipcode
     - deliveryAddress.postalCode
     - "string"
   * - Address.Street.Zipcode
     - physicalAddress.postalCode
     - "string"
   * - Address.Street.Zipcode
     - postalAddress.postalCode
     - "string"
   * - Associate.AssociateId
     - accountManager.id
     - "integer"
   * - ContactId
     - id
     - "integer"
   * - Country.CountryId
     - deliveryAddress.country.id
     - "string"
   * - Country.CountryId
     - physicalAddress.country.id
     - "integer"
   * - Country.CountryId
     - postalAddress.country.id
     - "integer"
   * - Emails.Value
     - email
     - "string"
   * - Name
     - name
     - "string"
   * - OrgNr (Dependant on having wd:Q852835 in Country.TwoLetterISOCountryDependant on having wd:Q852835 in Country.TwoLetterISOCountry)
     - customerNumber
     - "string"
   * - OrgNr (Dependant on having NO in Country.TwoLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having NOR in Country.TwoLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having NO in Country.TwoLetterISOCountry)
     - organizationNumber
     - N/A
   * - Phones.Value
     - phoneNumber
     - "string"
   * - Urls.Value
     - url
     - "string"
   * - Urls.Value
     - website
     - "string"


SuperOffice Person to Tripletex Contact
---------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a SuperOffice Person if it is connected to a SuperOffice Sale, Quote, Quoteline, or Quotealternative that is synchronized into Tripletex.

A SuperOffice Person will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tripletex Contact Property
   * - Emails.Value
     - email

Once a link between a SuperOffice Person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - Contact.ContactId
     - customer.id
     - "integer"
   * - Emails.Value
     - email
     - "string"
   * - Firstname
     - firstName
     - "string"
   * - Lastname
     - lastName
     - "string"
   * - MobilePhones.Value
     - phoneNumberMobile
     - N/A
   * - OfficePhones.Value
     - phoneNumberWork
     - "string"


SuperOffice Person to Tripletex Customer person
-----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a SuperOffice Person if it is connected to a SuperOffice Sale, Quote, Quoteline, or Quotealternative that is synchronized into Tripletex.

A SuperOffice Person will merge with a Tripletex Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tripletex Customer person Property
   * - Emails.Value
     - email

Once a link between a SuperOffice Person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - Address.Street.Address1
     - deliveryAddress.addressLine1
     - "string"
   * - Address.Street.Address1
     - physicalAddress.addressLine1
     - "string"
   * - Address.Street.Address1
     - postalAddress.addressLine1
     - "string"
   * - Address.Street.Address2
     - deliveryAddress.addressLine2
     - "string"
   * - Address.Street.Address2
     - physicalAddress.addressLine2
     - "string"
   * - Address.Street.Address2
     - postalAddress.addressLine2
     - "string"
   * - Address.Street.City
     - deliveryAddress.city
     - "string"
   * - Address.Street.City
     - physicalAddress.city
     - "string"
   * - Address.Street.City
     - postalAddress.city
     - "string"
   * - Address.Street.Zipcode
     - deliveryAddress.postalCode
     - "string"
   * - Address.Street.Zipcode
     - physicalAddress.postalCode
     - "string"
   * - Address.Street.Zipcode
     - postalAddress.postalCode
     - "string"
   * - Associate.AssociateId
     - accountManager.id
     - "integer"
   * - Country.CountryId
     - deliveryAddress.country.id
     - "string"
   * - Country.CountryId
     - physicalAddress.country.id
     - "integer"
   * - Country.CountryId
     - postalAddress.country.id
     - "integer"
   * - Emails.Value
     - email
     - "string"
   * - MobilePhones.Value
     - phoneNumberMobile
     - "string"
   * - OfficePhones.Value
     - phoneNumber
     - "string"
   * - PersonId
     - id
     - "integer"


SuperOffice Person to Tripletex Employee
----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Tripletex Employee must be established.

A SuperOffice Person will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tripletex Employee Property
   * - Emails.Value
     - email

Once a link between a SuperOffice Person and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - Address.Street.Address1
     - address.addressLine1
     - "string"
   * - Address.Street.Address2
     - address.addressLine2
     - "string"
   * - Address.Street.City
     - address.city
     - "string"
   * - Address.Street.Zipcode
     - address.postalCode
     - "string"
   * - BirthDate
     - dateOfBirth
     - N/A
   * - Contact.ContactId
     - department.id (Dependant on having wd:Q703534 in  )
     - N/A
   * - Country.CountryId
     - address.country.id
     - "integer"
   * - Emails.Value
     - email
     - "string"
   * - Firstname
     - firstName
     - "string"
   * - Lastname
     - lastName
     - "string"
   * - MobilePhones.Value
     - phoneNumberMobile
     - N/A
   * - OfficePhones.Value
     - phoneNumberWork
     - "string"
   * - PersonId
     - id
     - "integer"
   * - PrivatePhones.Value
     - phoneNumberHome
     - "string"


SuperOffice User to Tripletex Contact
-------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a Tripletex Contact must be established.

A SuperOffice User will merge with a Tripletex Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Tripletex Contact Property
   * - personEmail
     - email

Once a link between a SuperOffice User and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - contactId
     - customer.id
     - "integer"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - personEmail
     - email
     - "string"


SuperOffice User to Tripletex Customer person
---------------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a Tripletex Customer person must be established.

A SuperOffice User will merge with a Tripletex Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Tripletex Customer person Property
   * - personEmail
     - email

Once a link between a SuperOffice User and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - personEmail
     - email
     - "string"


SuperOffice User to Tripletex Employee
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a Tripletex Employee must be established.

A SuperOffice User will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Tripletex Employee Property
   * - personEmail
     - email

Once a link between a SuperOffice User and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - contactId
     - department.id
     - N/A
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - personEmail
     - email
     - "string"


SuperOffice Contact to Tripletex Contact
----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, Quote, Quoteline, or Quotealternative that is synchronized into Tripletex.

Once a link between a SuperOffice Contact and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Contact Property
     - Tripletex Data Type


SuperOffice Contact to Tripletex Customer person
------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Tripletex Customer person must be established.

A new Tripletex Customer person will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, User, Quote, Person, Contact, Quoteline, or Quotealternative that is synchronized into Tripletex.

Once a link between a SuperOffice Contact and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - Address.Postal.Address1
     - deliveryAddress.addressLine1
     - "string"
   * - Address.Postal.Address1
     - physicalAddress.addressLine1
     - "string"
   * - Address.Postal.Address1
     - postalAddress.addressLine1
     - "string"
   * - Address.Postal.Address2
     - deliveryAddress.addressLine2
     - "string"
   * - Address.Postal.Address2
     - physicalAddress.addressLine2
     - "string"
   * - Address.Postal.Address2
     - postalAddress.addressLine2
     - "string"
   * - Address.Postal.City
     - deliveryAddress.city
     - "string"
   * - Address.Postal.City
     - physicalAddress.city
     - "string"
   * - Address.Postal.City
     - postalAddress.city
     - "string"
   * - Address.Postal.Zipcode
     - deliveryAddress.postalCode
     - "string"
   * - Address.Postal.Zipcode
     - physicalAddress.postalCode
     - "string"
   * - Address.Postal.Zipcode
     - postalAddress.postalCode
     - "string"
   * - Address.Street.Address1
     - deliveryAddress.addressLine1
     - "string"
   * - Address.Street.Address1
     - physicalAddress.addressLine1
     - "string"
   * - Address.Street.Address1
     - postalAddress.addressLine1
     - "string"
   * - Address.Street.Address2
     - deliveryAddress.addressLine2
     - "string"
   * - Address.Street.Address2
     - physicalAddress.addressLine2
     - "string"
   * - Address.Street.Address2
     - postalAddress.addressLine2
     - "string"
   * - Address.Street.City
     - deliveryAddress.city
     - "string"
   * - Address.Street.City
     - physicalAddress.city
     - "string"
   * - Address.Street.City
     - postalAddress.city
     - "string"
   * - Address.Street.Zipcode
     - deliveryAddress.postalCode
     - "string"
   * - Address.Street.Zipcode
     - physicalAddress.postalCode
     - "string"
   * - Address.Street.Zipcode
     - postalAddress.postalCode
     - "string"
   * - ContactId
     - id
     - "integer"
   * - Country.CountryId
     - deliveryAddress.country.id
     - "string"
   * - Country.CountryId
     - physicalAddress.country.id
     - "integer"
   * - Country.CountryId
     - postalAddress.country.id
     - "integer"


SuperOffice Person to Tripletex Customer
----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a SuperOffice Person if it is connected to a SuperOffice Sale, Quote, Quoteline, or Quotealternative that is synchronized into Tripletex.

Once a link between a SuperOffice Person and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Tripletex Customer Property
     - Tripletex Data Type


SuperOffice Quotealternative to Tripletex Order
-----------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a Tripletex Order must be established.

A new Tripletex Order will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline that is synchronized into Tripletex.

Once a link between a SuperOffice Quotealternative and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - Name
     - invoiceComment
     - "string"


SuperOffice Product to Tripletex Product
----------------------------------------
Every SuperOffice Product will be synchronized with a Tripletex Product.

Once a link between a SuperOffice Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - Code
     - number
     - "string"
   * - Description
     - description
     - "string"
   * - ERPPriceListKey
     - currency.id
     - "integer"
   * - ERPProductKey
     - number
     - "string"
   * - Name
     - name
     - "string"
   * - QuantityUnit
     - productUnit.id
     - "integer"
   * - Supplier
     - supplier.id
     - "integer"
   * - UnitCost
     - costExcludingVatCurrency
     - "integer"
   * - UnitListPrice
     - priceExcludingVatCurrency
     - "float"
   * - VAT
     - vatType.id
     - "integer"


SuperOffice Project to Tripletex Project
----------------------------------------
Every SuperOffice Project will be synchronized with a Tripletex Project.

Once a link between a SuperOffice Project and a Tripletex Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Project and a Tripletex Project:

.. list-table::
   :header-rows: 1

   * - SuperOffice Project Property
     - Tripletex Project Property
     - Tripletex Data Type
   * - Associate.AssociateId
     - projectManager.id
     - "integer"
   * - EndDate
     - endDate
     - N/A
   * - Name
     - name
     - "string"
   * - NextMilestoneDate
     - startDate
     - N/A
   * - ProjectMembers.PersonId
     - contact.id
     - "integer"


SuperOffice Quoteline to Tripletex Orderline
--------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Tripletex Orderline.

Once a link between a SuperOffice Quoteline and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - Description
     - description
     - "string"
   * - DiscountPercent
     - count
     - "float"
   * - DiscountPercent
     - description
     - "string"
   * - DiscountPercent
     - discount
     - "float"
   * - DiscountPercent
     - unitCostCurrency
     - "float"
   * - DiscountPercent
     - unitPriceExcludingVatCurrency
     - "float"
   * - DiscountPercent
     - vatType.id
     - "integer"
   * - ERPDiscountPercent
     - discount
     - "float"
   * - ERPProductKey
     - product.id
     - "integer"
   * - Name
     - count
     - "float"
   * - Name
     - description
     - "string"
   * - Name
     - discount
     - "float"
   * - Name
     - unitCostCurrency
     - "float"
   * - Name
     - unitPriceExcludingVatCurrency
     - "float"
   * - Name
     - vatType.id
     - "integer"
   * - Quantity
     - count
     - N/A
   * - Quantity
     - description
     - "string"
   * - Quantity
     - discount
     - "float"
   * - Quantity
     - unitCostCurrency
     - "float"
   * - Quantity
     - unitPriceExcludingVatCurrency
     - "float"
   * - Quantity
     - vatType.id
     - "integer"
   * - QuantityUnit
     - count
     - "float"
   * - QuantityUnit
     - description
     - "string"
   * - QuantityUnit
     - discount
     - "float"
   * - QuantityUnit
     - unitCostCurrency
     - "float"
   * - QuantityUnit
     - unitPriceExcludingVatCurrency
     - "float"
   * - QuantityUnit
     - vatType.id
     - "integer"
   * - QuoteAlternativeId
     - order.id
     - "integer"
   * - Rank (Dependant on having  in Rank)
     - count
     - "float"
   * - Rank (Dependant on having  in Rank)
     - description
     - "string"
   * - Rank (Dependant on having  in Rank)
     - discount
     - "float"
   * - Rank (Dependant on having  in Rank)
     - unitCostCurrency
     - "float"
   * - Rank (Dependant on having  in Rank)
     - unitPriceExcludingVatCurrency
     - "float"
   * - Rank (Dependant on having  in Rank)
     - vatType.id
     - "integer"
   * - UnitListPrice
     - count
     - "float"
   * - UnitListPrice
     - description
     - "string"
   * - UnitListPrice
     - discount
     - "float"
   * - UnitListPrice
     - unitCostCurrency
     - "float"
   * - UnitListPrice
     - unitPriceExcludingVatCurrency
     - "float"
   * - UnitListPrice
     - vatType.id
     - "integer"
   * - VAT
     - count
     - "float"
   * - VAT
     - description
     - "string"
   * - VAT
     - discount
     - "float"
   * - VAT
     - unitCostCurrency
     - "float"
   * - VAT
     - unitPriceExcludingVatCurrency
     - "float"
   * - VAT
     - vatType.id
     - "integer"

