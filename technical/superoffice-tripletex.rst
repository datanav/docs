=================================
SuperOffice to Tripletex Dataflow
=================================

Generated: 2023-05-12 13:01:04

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Tripletex Customer
-----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, User, Person, or Quotealternative that is synchronized into Tripletex.

A SuperOffice Contact will merge with a Tripletex Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Customer Property
   * - Emails.Value
     - email
   * - Emails.Value
     - invoiceEmail
   * - Emails.Value
     - overdueNoticeEmail

Once a link between a SuperOffice Contact and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - Address.Postal.Address1
     - postalAddress.addressLine1
     - "string"
   * - Address.Postal.Address2
     - postalAddress.addressLine2
     - "string"
   * - Address.Postal.City
     - postalAddress.city
     - "string"
   * - Address.Postal.Zipcode
     - postalAddress.postalCode
     - "string"
   * - Address.Street.Address1
     - physicalAddress.addressLine1
     - "string"
   * - Address.Street.Address2
     - physicalAddress.addressLine2
     - "string"
   * - Address.Street.City
     - physicalAddress.city
     - "string"
   * - Address.Street.Zipcode
     - physicalAddress.postalCode
     - "string"
   * - Associate.AssociateId
     - accountManager.id
     - "integer"
   * - ContactId
     - id
     - "integer"
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
   * - OrgNr (Dependant on having NOR in Country.ThreeLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountry)
     - organizationNumber
     - "string"
   * - Phones.Value
     - phoneNumber
     - "string"


SuperOffice Contact to Tripletex Supplier
-----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Tripletex Supplier must be established.

A SuperOffice Contact will merge with a Tripletex Supplier if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Supplier Property
   * - Emails.Value
     - email
   * - Emails.Value
     - invoiceEmail
   * - Emails.Value
     - overdueNoticeEmail

Once a link between a SuperOffice Contact and a Tripletex Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Tripletex Supplier:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Supplier Property
     - Tripletex Data Type
   * - Address.Postal.Address1
     - postalAddress.addressLine1
     - "string"
   * - Address.Postal.Address2
     - postalAddress.addressLine2
     - "string"
   * - Address.Postal.City
     - postalAddress.city
     - "string"
   * - Address.Postal.Zipcode
     - postalAddress.postalCode
     - "string"
   * - Address.Street.Address1
     - physicalAddress.addressLine1
     - "string"
   * - Address.Street.Address2
     - physicalAddress.addressLine2
     - "string"
   * - Address.Street.City
     - physicalAddress.city
     - "string"
   * - Address.Street.Zipcode
     - physicalAddress.postalCode
     - "string"
   * - ContactId
     - id
     - "integer"
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
   * - Phones.Value
     - phoneNumber
     - "string"


SuperOffice Person to Tripletex Contact
---------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a SuperOffice Person if it is connected to a SuperOffice Sale, or Quotealternative that is synchronized into Tripletex.

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
     - "string"
   * - OfficePhones.Value
     - phoneNumberWork
     - "string"


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
   * - BirthDate
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - Contact.ContactId
     - department.id
     - ""if", "eq"]]"
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
     - "string"
   * - OfficePhones.Value
     - phoneNumberWork
     - "string"
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


SuperOffice Listproductcategoryitems to Tripletex Productgroup
--------------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a Tripletex Productgroup.

Once a link between a SuperOffice Listproductcategoryitems and a Tripletex Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a Tripletex Productgroup:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     - Tripletex Productgroup Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


SuperOffice Product to Tripletex Product
----------------------------------------
Every SuperOffice Product will be synchronized with a Tripletex Product.

If a matching Tripletex Product already exists, the SuperOffice Product will be merged with the existing one.
If no matching Tripletex Product is found, a new Tripletex Product will be created.

A SuperOffice Product will merge with a Tripletex Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Tripletex Product Property
   * - ERPProductKey
     - number

Once a link between a SuperOffice Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Tripletex Product Property
     - Tripletex Data Type
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
   * - PriceUnit
     - productUnit.id
     - "integer"
   * - Supplier
     - supplier.id
     - "integer"
   * - UnitCost
     - costExcludingVatCurrency
     - "string"
   * - UnitListPrice
     - priceExcludingVatCurrency
     - "float"
   * - VAT
     - vatType
     - "integer"
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
   * - Associate
     - projectManager.id
     - "integer"
   * - Associate.AssociateId
     - projectManager.id
     - "integer"
   * - EndDate
     - endDate
     - "datetime-format","%Y-%m-%d","_."]
   * - Name
     - name
     - "string"
   * - NextMilestoneDate
     - startDate
     - "datetime-format","%Y-%m-%d","_."]


SuperOffice Quotealternative to Tripletex Order
-----------------------------------------------
When a Superoffice QuoteAlternative gets Accepted = "true", it  will be synchronized with a Tripletex Order.

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
   * - DiscountPercent
     - discount
     - "float"
   * - ERPProductKey
     - product.id
     - "integer"
   * - Name
     - description
     - "string"
   * - Quantity
     - count
     - "float"
   * - QuoteAlternativeId
     - order.id
     - "integer"
   * - TotalPrice
     - unitPriceExcludingVatCurrency
     - "float"
   * - UnitListPrice
     - unitPriceExcludingVatCurrency
     - "float"
   * - VAT
     - vatType.id
     - "integer"


SuperOffice Sale to Tripletex Order
-----------------------------------
When a Superoffice Sale gets the status "Sold", it  will be synchronized with a Tripletex Order.

Once a link between a SuperOffice Sale and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - Associate.AssociateId
     - ourContactEmployee.id
     - "integer"
   * - Contact.ContactId
     - customer.id
     - "integer"
   * - Currency.Id
     - currency.id
     - "integer"
   * - Heading
     - invoiceComment
     - "string"
   * - Person.PersonId
     - contact.id
     - "integer"
   * - Saledate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - Saledate
     - orderDate
     - "datetime-format","%Y-%m-%d","_."]


SuperOffice User to Tripletex Employee
--------------------------------------
Every SuperOffice User will be synchronized with a Tripletex Employee.

If a matching Tripletex Employee already exists, the SuperOffice User will be merged with the existing one.
If no matching Tripletex Employee is found, a new Tripletex Employee will be created.

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
     - ""if", "eq"]]"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - personEmail
     - email
     - "string"

