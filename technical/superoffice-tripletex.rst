=================================
SuperOffice to Tripletex Dataflow
=================================

Generated: 2023-10-05 06:16:43

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Tripletex Customer
-----------------------------------------
Every SuperOffice Contact will be synchronized with a Tripletex Customer.

If a matching Tripletex Customer already exists, the SuperOffice Contact will be merged with the existing one.
If no matching Tripletex Customer is found, a new Tripletex Customer will be created.

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
   * - OrgNr (Dependant on having NO in Country.TwoLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having NOR in Country.TwoLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountryDependant on having NOR in Country.ThreeLetterISOCountryDependant on having NO in Country.TwoLetterISOCountryDependant on having NO in Country.TwoLetterISOCountry)
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
     - deliveryAddress.changes
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
     - deliveryAddress.changes
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
     - deliveryAddress.city
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
   * - Phones.Value
     - phoneNumber
     - "string"


SuperOffice Person to Tripletex Contact
---------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a SuperOffice Person if it is connected to a SuperOffice Sale, Quote, Project, Quoteline, or Quotealternative that is synchronized into Tripletex.

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
     - "if","matches","+* *","_."],"join"," ","slice", 1,"split", " ","_."]]],"_."]
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
     - "datetime-format","%Y-%m-%d","_."]
   * - Contact.ContactId
     - department.id
     - "if", "neq", "_.", "X"], "integer", "string"]
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
     - "string"
   * - OfficePhones.Value
     - phoneNumberWork
     - "string"
   * - PersonId
     - id
     - "integer"
   * - PrivatePhones.Value
     - phoneNumberHome
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


SuperOffice Contact to Tripletex Contact
----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a SuperOffice Contact if it is connected to a SuperOffice Quotealternative that is synchronized into Tripletex.

Once a link between a SuperOffice Contact and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Tripletex Contact Property
     - Tripletex Data Type


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


SuperOffice Person to Tripletex Customer
----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a SuperOffice Person if it is connected to a SuperOffice Quotealternative that is synchronized into Tripletex.

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


SuperOffice Listbusinessitems to Tripletex Customercategory
-----------------------------------------------------------
Every SuperOffice Listbusinessitems will be synchronized with a Tripletex Customercategory.

Once a link between a SuperOffice Listbusinessitems and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listbusinessitems and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listbusinessitems Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


SuperOffice Listcategoryitems to Tripletex Customercategory
-----------------------------------------------------------
Every SuperOffice Listcategoryitems will be synchronized with a Tripletex Customercategory.

Once a link between a SuperOffice Listcategoryitems and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcategoryitems and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcategoryitems Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


SuperOffice Listproductcategoryitems to Tripletex Customercategory
------------------------------------------------------------------
Every SuperOffice Listproductcategoryitems will be synchronized with a Tripletex Customercategory.

Once a link between a SuperOffice Listproductcategoryitems and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


SuperOffice Listproductfamilyitems to Tripletex Customercategory
----------------------------------------------------------------
Every SuperOffice Listproductfamilyitems will be synchronized with a Tripletex Customercategory.

Once a link between a SuperOffice Listproductfamilyitems and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductfamilyitems and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductfamilyitems Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


SuperOffice Listproducttypeitems to Tripletex Customercategory
--------------------------------------------------------------
Every SuperOffice Listproducttypeitems will be synchronized with a Tripletex Customercategory.

Once a link between a SuperOffice Listproducttypeitems and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproducttypeitems and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproducttypeitems Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


SuperOffice Listprojectstatusitems to Tripletex Customercategory
----------------------------------------------------------------
Every SuperOffice Listprojectstatusitems will be synchronized with a Tripletex Customercategory.

Once a link between a SuperOffice Listprojectstatusitems and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listprojectstatusitems and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listprojectstatusitems Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


SuperOffice Listprojecttypeitems to Tripletex Customercategory
--------------------------------------------------------------
Every SuperOffice Listprojecttypeitems will be synchronized with a Tripletex Customercategory.

Once a link between a SuperOffice Listprojecttypeitems and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listprojecttypeitems and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listprojecttypeitems Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


SuperOffice Listsaletypeitems to Tripletex Customercategory
-----------------------------------------------------------
Every SuperOffice Listsaletypeitems will be synchronized with a Tripletex Customercategory.

Once a link between a SuperOffice Listsaletypeitems and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listsaletypeitems and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listsaletypeitems Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


SuperOffice Listticketcategoryitems to Tripletex Customercategory
-----------------------------------------------------------------
Every SuperOffice Listticketcategoryitems will be synchronized with a Tripletex Customercategory.

Once a link between a SuperOffice Listticketcategoryitems and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listticketcategoryitems and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listticketcategoryitems Property
     - Tripletex Customercategory Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"

