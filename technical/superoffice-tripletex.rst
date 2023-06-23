=================================
SuperOffice to Tripletex Dataflow
=================================

Generated: 2023-06-23 11:20:27

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
   * - OrgNr (Dependant on having NOR in Country.ThreeLetterISOCountry)
     - organizationNumber
     - "replace"," ","", "string"]
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
Every SuperOffice Person will be synchronized with a Tripletex Contact.

If a matching Tripletex Contact already exists, the SuperOffice Person will be merged with the existing one.
If no matching Tripletex Contact is found, a new Tripletex Contact will be created.

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
     - "if","matches","+*","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
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
     - "if", "neq", "_.", "X"], "integer", "string"]
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


SuperOffice Product to Tripletex Product
----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Product and a Tripletex Product must be established.

A new Tripletex Product will be created from a SuperOffice Product if it is connected to a SuperOffice Quoteline that is synchronized into Tripletex.

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
Before any synchronization can take place, a link between a SuperOffice Product and a Tripletex Productunit must be established.

A SuperOffice Product will merge with a Tripletex Productunit if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Tripletex Productunit Property
   * - QuantityUnit
     - name

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
   * - Name
     - name
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


SuperOffice Sale to Tripletex Order
-----------------------------------
Every SuperOffice Sale will be synchronized with a Tripletex Order.

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
   * - Person.PersonId
     - contact.id
     - "integer"
   * - Saledate
     - deliveryDate
     - "datetime-format","%Y-%m-%d","_."]
   * - Saledate
     - orderDate
     - "datetime-format","%Y-%m-%d","_."]

