===================================
SuperOffice to SuperOffice Dataflow
===================================

Generated: 2023-05-23 06:26:42

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Listcurrencyitems to SuperOffice Pricelist
------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Listcurrencyitems and a SuperOffice Pricelist must be established.

A SuperOffice Listcurrencyitems will merge with a SuperOffice Pricelist if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - SuperOffice Pricelist Property
   * - Name
     - Currency

Once a link between a SuperOffice Listcurrencyitems and a SuperOffice Pricelist is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a SuperOffice Pricelist:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - SuperOffice Pricelist Property
     - SuperOffice Data Type
   * - Name
     - Currency
     - "string"


SuperOffice Ownercontactlink to SuperOffice Contact
---------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Ownercontactlink and a SuperOffice Contact must be established.

A SuperOffice Ownercontactlink will merge with a SuperOffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - SuperOffice Contact Property
   * - contact_id
     - ContactId

Once a link between a SuperOffice Ownercontactlink and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - contact_id
     - ContactId
     - "string"
   * - name
     - Name
     - "string"
   * - ownercontactlink.contact_id
     - ContactId
     - "string"
   * - ownercontactlink.contact_id.name
     - Name
     - "string"


SuperOffice Quote to SuperOffice Sale
-------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quote and a SuperOffice Sale must be established.

A SuperOffice Quote will merge with a SuperOffice Sale if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     - SuperOffice Sale Property
   * - SaleId
     - SaleId

Once a link between a SuperOffice Quote and a SuperOffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quote and a SuperOffice Sale:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quote Property
     - SuperOffice Sale Property
     - SuperOffice Data Type


SuperOffice User to SuperOffice Person
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a SuperOffice Person must be established.

A SuperOffice User will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Person Property
   * - personEmail
     - Emails.Value

Once a link between a SuperOffice User and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - contactId
     - Contact.ContactId
     - "integer"
   * - firstName
     - Firstname
     - "string"
   * - lastName
     - Lastname
     - "string"
   * - personEmail
     - Emails.Value
     - "string"


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


HubSpot Company to SuperOffice Contact
--------------------------------------
Every HubSpot Company will be synchronized with a SuperOffice Contact.

Once a link between a HubSpot Company and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - id
     - ContactId
     - "integer"
   * - properties.address
     - Address.Postal.Address1
     - "string"
   * - properties.address
     - Address.Street.Address1
     - "string"
   * - properties.address2
     - Address.Postal.Address2
     - "string"
   * - properties.address2
     - Address.Street.Address2
     - "string"
   * - properties.city
     - Address.Postal.City
     - "string"
   * - properties.city
     - Address.Street.City
     - "string"
   * - properties.country
     - Country.CountryId
     - "integer"
   * - properties.name
     - Name
     - "string"
   * - properties.phone
     - Phones.Value
     - "string"
   * - properties.website
     - Domains
     - "list"
   * - properties.website
     - Urls.Value
     - "string"
   * - properties.zip
     - Address.Postal.Zipcode
     - "string"
   * - properties.zip
     - Address.Street.Zipcode
     - "string"


HubSpot Department to SuperOffice Contact
-----------------------------------------
Every HubSpot Department will be synchronized with a SuperOffice Contact.

Once a link between a HubSpot Department and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Department and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - HubSpot Department Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - name
     - Name
     - "string"


HubSpot Order to SuperOffice Quotealternative
---------------------------------------------
Before any synchronization can take place, a link between a HubSpot Order and a SuperOffice Quotealternative must be established.

A new SuperOffice Quotealternative will be created from a HubSpot Order if it is connected to a HubSpot Lineitem, Tripletex-orderline, Superoffice-quoteline, or Poweroffice-salesorderline that is synchronized into SuperOffice.

Once a link between a HubSpot Order and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Order and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - HubSpot Order Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - invoiceComment
     - Name
     - "string"
   * - isClosed
     - sesam_Accepted
     - "boolean"


Poweroffice Productgroup to SuperOffice Listproductcategoryitems
----------------------------------------------------------------
Every Poweroffice Productgroup will be synchronized with a SuperOffice Listproductcategoryitems.

Once a link between a Poweroffice Productgroup and a SuperOffice Listproductcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Productgroup and a SuperOffice Listproductcategoryitems:

.. list-table::
   :header-rows: 1

   * - Poweroffice Productgroup Property
     - SuperOffice Listproductcategoryitems Property
     - SuperOffice Data Type
   * - Name
     - Name
     - "string"


SuperOffice User to SuperOffice Listcategoryitems
-------------------------------------------------
Every SuperOffice User will be synchronized with a SuperOffice Listcategoryitems.

Once a link between a SuperOffice User and a SuperOffice Listcategoryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a SuperOffice Listcategoryitems:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - SuperOffice Listcategoryitems Property
     - SuperOffice Data Type
   * - contactCategory
     - Name
     - "string"


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

