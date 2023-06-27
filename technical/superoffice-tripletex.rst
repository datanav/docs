=================================
SuperOffice to Tripletex Dataflow
=================================

Generated: 2023-06-27 05:12:36

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Tripletex Customer
-----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, User, Quote, Person, Quoteline, or Quotealternative that is synchronized into Tripletex.

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
   * - OrgNr (Dependant on having NOR in Country.ThreeLetterISOCountry)
     - organizationNumber
     - "replace"," ","", "string"]
   * - Phones.Value
     - phoneNumber
     - "string"


SuperOffice Contact to Tripletex Department
-------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Tripletex Department must be established.

A new Tripletex Department will be created from a SuperOffice Contact if it is connected to a SuperOffice User, or Person that is synchronized into Tripletex.

Once a link between a SuperOffice Contact and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Department Property
     - Tripletex Data Type


SuperOffice Person to Tripletex Contact
---------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a SuperOffice Person if it is connected to a SuperOffice Sale, Quote, Project, Quoteline, or Quotealternative that is synchronized into Tripletex.

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
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
   * - OfficePhones.Value
     - phoneNumberWork
     - "string"


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


SuperOffice Ownercontactlink to Tripletex Department
----------------------------------------------------
Every SuperOffice Ownercontactlink will be synchronized with a Tripletex Department.

Once a link between a SuperOffice Ownercontactlink and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - name
     - name
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


SuperOffice Product to Tripletex Productunit
--------------------------------------------
Every SuperOffice Product will be synchronized with a Tripletex Productunit.

Once a link between a SuperOffice Product and a Tripletex Productunit is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Tripletex Productunit:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Tripletex Productunit Property
     - Tripletex Data Type
   * - QuantityUnit
     - commonCode
     - "string"
   * - QuantityUnit
     - name
     - "string"


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
     - "datetime-format","%Y-%m-%d","_."]
   * - Name
     - name
     - "string"
   * - NextMilestoneDate
     - startDate
     - "datetime-format","%Y-%m-%d","_."]
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
   * - UnitListPrice
     - unitPriceExcludingVatCurrency
     - "float"
   * - VAT
     - vatType.id
     - "integer"


SuperOffice User to Tripletex Employee
--------------------------------------
Every SuperOffice User will be synchronized with a Tripletex Employee.

Once a link between a SuperOffice User and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Tripletex Employee Property
     - Tripletex Data Type
   * - contactId
     - department.id
     - "if", "neq", "_.", "X"], "integer", "string"]
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - personEmail
     - email
     - "string"

