=================================
Tripletex to SuperOffice Dataflow
=================================

Generated: 2023-05-23 00:14:23

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


Tripletex Currency to SuperOffice Pricelist
-------------------------------------------
Before any synchronization can take place, a link between a Tripletex Currency and a SuperOffice Pricelist must be established.

A Tripletex Currency will merge with a SuperOffice Pricelist if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - SuperOffice Pricelist Property
   * - code
     - Currency

Once a link between a Tripletex Currency and a SuperOffice Pricelist is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a SuperOffice Pricelist:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - SuperOffice Pricelist Property
     - SuperOffice Data Type
   * - code
     - Currency
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
   * - deliveryAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - deliveryAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - deliveryAddress.changes
     - Address.Postal.City
     - "string"
   * - deliveryAddress.city
     - Country.CountryId
     - "integer"
   * - deliveryAddress.postalCode
     - Address.Postal.Zipcode
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
     - OrgNr (Dependant on having NOR in Country.ThreeLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountry)
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
   * - deliveryAddress.addressLine1
     - Address.Postal.Address1
     - "string"
   * - deliveryAddress.addressLine2
     - Address.Postal.Address2
     - "string"
   * - deliveryAddress.changes
     - Address.Postal.City
     - "string"
   * - deliveryAddress.city
     - Country.CountryId
     - "integer"
   * - deliveryAddress.postalCode
     - Address.Postal.Zipcode
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
     - Quantity
     - "integer"
   * - description
     - Name
     - "string"
   * - discount
     - DiscountPercent
     - "integer"
   * - order.id
     - QuoteAlternativeId
     - "integer"
   * - product.id
     - ERPProductKey
     - "string"
   * - unitPriceExcludingVatCurrency
     - TotalPrice
     - "integer"
   * - unitPriceExcludingVatCurrency
     - UnitListPrice
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


Tripletex Project to SuperOffice Project
----------------------------------------
Every Tripletex Project will be synchronized with a SuperOffice Project.

Once a link between a Tripletex Project and a SuperOffice Project is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a SuperOffice Project:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     - SuperOffice Project Property
     - SuperOffice Data Type
   * - endDate
     - EndDate
     - "datetime-format","%Y-%m-%dT%H:%M:%S","_."]
   * - name
     - Name
     - "string"
   * - projectManager.id
     - Associate
     - "integer"
   * - projectManager.id
     - Associate.AssociateId
     - "integer"
   * - startDate
     - NextMilestoneDate
     - "string"

