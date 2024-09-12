============================
Wave to SuperOffice Dataflow
============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Currency to SuperOffice Pricelist
--------------------------------------
Before any synchronization can take place, a link between a Wave Currency and a SuperOffice Pricelist must be established.

A Wave Currency will merge with a SuperOffice Pricelist if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - SuperOffice Pricelist Property
   * - code
     - Currency

Once a link between a Wave Currency and a SuperOffice Pricelist is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a SuperOffice Pricelist:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - SuperOffice Pricelist Property
     - SuperOffice Data Type


Wave Customer person to SuperOffice Person
------------------------------------------
Every Wave Customer person will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the Wave Customer person will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A Wave Customer person will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - SuperOffice Person Property
   * - email
     - Emails.Value

Once a link between a Wave Customer person and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
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
   * - address.country.code
     - Country.CountryId
     - "integer"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
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
   * - mobile
     - MobilePhones.Value
     - "string"
   * - phone
     - OfficePhones.Value
     - "string"
   * - shippingDetails.address.addressLine1
     - Address.Street.Address1
     - "string"
   * - shippingDetails.address.addressLine2
     - Address.Street.Address2
     - "string"
   * - shippingDetails.address.city
     - Address.Street.City
     - "string"
   * - shippingDetails.address.country.code
     - Country.CountryId
     - "integer"
   * - shippingDetails.address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - shippingDetails.phone
     - OfficePhones.Value
     - "string"


Wave Customer person to SuperOffice User
----------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a SuperOffice User must be established.

A Wave Customer person will merge with a SuperOffice User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - SuperOffice User Property
   * - email
     - personEmail

Once a link between a Wave Customer person and a SuperOffice User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a SuperOffice User:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - SuperOffice User Property
     - SuperOffice Data Type


Wave Customer to SuperOffice Person
-----------------------------------
Before any synchronization can take place, a link between a Wave Customer and a SuperOffice Person must be established.

A new SuperOffice Person will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into SuperOffice.

A Wave Customer will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - SuperOffice Person Property
   * - email
     - Emails.Value

Once a link between a Wave Customer and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
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
   * - address.country.code
     - Country.CountryId
     - "integer"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"
   * - id
     - Contact.ContactId
     - "integer"
   * - id
     - PersonId
     - "integer"
   * - lastName
     - Lastname
     - "string"
   * - mobile
     - MobilePhones.Value
     - "string"
   * - phone
     - OfficePhones.Value
     - "string"
   * - shippingDetails.address.addressLine1
     - Address.Street.Address1
     - "string"
   * - shippingDetails.address.addressLine2
     - Address.Street.Address2
     - "string"
   * - shippingDetails.address.city
     - Address.Street.City
     - "string"
   * - shippingDetails.address.country.code
     - Country.CountryId
     - "integer"
   * - shippingDetails.address.postalCode
     - Address.Street.Zipcode
     - "string"


Wave Customer to SuperOffice User
---------------------------------
Before any synchronization can take place, a link between a Wave Customer and a SuperOffice User must be established.

A Wave Customer will merge with a SuperOffice User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - SuperOffice User Property
   * - email
     - personEmail

Once a link between a Wave Customer and a SuperOffice User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a SuperOffice User:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - SuperOffice User Property
     - SuperOffice Data Type


Wave Vendor to SuperOffice Person
---------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a SuperOffice Person must be established.

A Wave Vendor will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - SuperOffice Person Property
   * - email
     - Emails.Value

Once a link between a Wave Vendor and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
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
   * - address.country.code
     - Country.CountryId
     - "integer"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - firstName
     - Firstname
     - "string"
   * - id
     - Contact.ContactId
     - "integer"
   * - id
     - PersonId
     - "integer"
   * - lastName
     - Lastname
     - "string"
   * - mobile
     - MobilePhones.Value
     - "string"
   * - phone
     - OfficePhones.Value
     - "string"


Wave Vendor to SuperOffice User
-------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a SuperOffice User must be established.

A Wave Vendor will merge with a SuperOffice User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - SuperOffice User Property
   * - email
     - personEmail

Once a link between a Wave Vendor and a SuperOffice User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a SuperOffice User:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - SuperOffice User Property
     - SuperOffice Data Type


Wave Customer to SuperOffice Contact
------------------------------------
Every Wave Customer will be synchronized with a SuperOffice Contact.

Once a link between a Wave Customer and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - address.addressLine1
     - Address.Postal.Address1
     - "string"
   * - address.addressLine1
     - Address.Street.Address1
     - "string"
   * - address.addressLine2
     - Address.Postal.Address2
     - "string"
   * - address.addressLine2
     - Address.Street.Address2
     - "string"
   * - address.city
     - Address.Postal.City
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.country.code
     - Country.CountryId
     - "integer"
   * - address.countryCode
     - Country.CountryId
     - "integer"
   * - address.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - id
     - ContactId
     - "integer"
   * - name
     - Name
     - "string"
   * - phone
     - Phones.Value
     - "string"
   * - shippingDetails.address.addressLine1
     - Address.Postal.Address1
     - "string"
   * - shippingDetails.address.addressLine1
     - Address.Street.Address1
     - "string"
   * - shippingDetails.address.addressLine2
     - Address.Postal.Address2
     - "string"
   * - shippingDetails.address.addressLine2
     - Address.Street.Address2
     - "string"
   * - shippingDetails.address.city
     - Address.Postal.City
     - "string"
   * - shippingDetails.address.city
     - Address.Street.City
     - "string"
   * - shippingDetails.address.country.code
     - Country.CountryId
     - "integer"
   * - shippingDetails.address.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - shippingDetails.address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - shippingDetails.phone
     - Phones.Value
     - "string"
   * - website
     - Domains
     - N/A
   * - website
     - Urls.Value
     - "string"


Wave Invoice to SuperOffice Quotealternative
--------------------------------------------
Before any synchronization can take place, a link between a Wave Invoice and a SuperOffice Quotealternative must be established.

A new SuperOffice Quotealternative will be created from a Wave Invoice if it is connected to a Wave Invoice that is synchronized into SuperOffice.

Once a link between a Wave Invoice and a SuperOffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a SuperOffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - SuperOffice Quotealternative Property
     - SuperOffice Data Type
   * - memo
     - Description
     - "string"
   * - memo
     - Name
     - "string"
   * - title
     - Name
     - "string"
   * - total.value
     - TotalPrice
     - "float"


Wave Vendor to SuperOffice Contact
----------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a SuperOffice Contact must be established.

A new SuperOffice Contact will be created from a Wave Vendor if it is connected to a Wave Vendor, Customer, Customer-person, or Customer-contact that is synchronized into SuperOffice.

Once a link between a Wave Vendor and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - address.addressLine1
     - Address.Postal.Address1
     - "string"
   * - address.addressLine1
     - Address.Street.Address1
     - "string"
   * - address.addressLine2
     - Address.Postal.Address2
     - "string"
   * - address.addressLine2
     - Address.Street.Address2
     - "string"
   * - address.city
     - Address.Postal.City
     - "string"
   * - address.city
     - Address.Street.City
     - "string"
   * - address.country.code
     - Country.CountryId
     - "integer"
   * - address.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - address.postalCode
     - Address.Street.Zipcode
     - "string"
   * - id
     - ContactId
     - "integer"
   * - name
     - Name
     - "string"
   * - website
     - Urls.Value
     - "string"


Wave Business to SuperOffice Ownercontactlink
---------------------------------------------
Every Wave Business will be synchronized with a SuperOffice Ownercontactlink.

Once a link between a Wave Business and a SuperOffice Ownercontactlink is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Business and a SuperOffice Ownercontactlink:

.. list-table::
   :header-rows: 1

   * - Wave Business Property
     - SuperOffice Ownercontactlink Property
     - SuperOffice Data Type


Wave Country to SuperOffice Listcountryitems
--------------------------------------------
Every Wave Country will be synchronized with a SuperOffice Listcountryitems.

If a matching SuperOffice Listcountryitems already exists, the Wave Country will be merged with the existing one.
If no matching SuperOffice Listcountryitems is found, a new SuperOffice Listcountryitems will be created.

A Wave Country will merge with a SuperOffice Listcountryitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     - SuperOffice Listcountryitems Property
   * - name
     - Name
   * - code
     - TwoLetterISOCountry

Once a link between a Wave Country and a SuperOffice Listcountryitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Country and a SuperOffice Listcountryitems:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     - SuperOffice Listcountryitems Property
     - SuperOffice Data Type


Wave Currency to SuperOffice Listcurrencyitems
----------------------------------------------
Every Wave Currency will be synchronized with a SuperOffice Listcurrencyitems.

If a matching SuperOffice Listcurrencyitems already exists, the Wave Currency will be merged with the existing one.
If no matching SuperOffice Listcurrencyitems is found, a new SuperOffice Listcurrencyitems will be created.

A Wave Currency will merge with a SuperOffice Listcurrencyitems if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - SuperOffice Listcurrencyitems Property
   * - code
     - Name

Once a link between a Wave Currency and a SuperOffice Listcurrencyitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a SuperOffice Listcurrencyitems:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - SuperOffice Listcurrencyitems Property
     - SuperOffice Data Type


Wave Invoice to SuperOffice Quoteline
-------------------------------------
Every Wave Invoice will be synchronized with a SuperOffice Quoteline.

Once a link between a Wave Invoice and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - id
     - QuoteAlternativeId
     - "integer"
   * - items.description
     - Description
     - "string"
   * - items.price
     - UnitListPrice
     - N/A
   * - items.product.id
     - ERPProductKey
     - "string"
   * - items.quantity
     - Quantity
     - N/A
   * - total.value
     - TotalPrice
     - N/A


Wave Product to SuperOffice Product
-----------------------------------
Every Wave Product will be synchronized with a SuperOffice Product.

Once a link between a Wave Product and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - unitPrice
     - UnitListPrice
     - N/A


Wave User to SuperOffice User
-----------------------------
Every Wave User will be synchronized with a SuperOffice User.

Once a link between a Wave User and a SuperOffice User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave User and a SuperOffice User:

.. list-table::
   :header-rows: 1

   * - Wave User Property
     - SuperOffice User Property
     - SuperOffice Data Type

