======================================
Wave Financial to Superoffice Dataflow
======================================

Generated: 2024-06-27 07:11:13

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer contact to Superoffice Person
-------------------------------------------
Before any synchronization can take place, a link between a Wave Customer contact and a Superoffice Person must be established.

A Wave Customer contact will merge with a Superoffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer contact Property
     - Superoffice Person Property
   * - email
     - Emails.Value

Once a link between a Wave Customer contact and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer contact and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Wave Customer contact Property
     - Superoffice Person Property
     - Superoffice Data Type


Wave Customer person to Superoffice Person
------------------------------------------
Every Wave Customer person will be synchronized with a Superoffice Person.

If a matching Superoffice Person already exists, the Wave Customer person will be merged with the existing one.
If no matching Superoffice Person is found, a new Superoffice Person will be created.

A Wave Customer person will merge with a Superoffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Superoffice Person Property
   * - email
     - Emails.Value

Once a link between a Wave Customer person and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Superoffice Person Property
     - Superoffice Data Type
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


Wave Customer to Superoffice Person
-----------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Superoffice Person must be established.

A new Superoffice Person will be created from a Wave Customer if it is connected to a Wave Invoice that is synchronized into Superoffice.

A Wave Customer will merge with a Superoffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Superoffice Person Property
   * - email
     - Emails.Value

Once a link between a Wave Customer and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Superoffice Person Property
     - Superoffice Data Type
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


Wave Vendor to Superoffice Person
---------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Superoffice Person must be established.

A Wave Vendor will merge with a Superoffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Superoffice Person Property
   * - email
     - Emails.Value

Once a link between a Wave Vendor and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Superoffice Person Property
     - Superoffice Data Type
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


Wave Customer to Superoffice Contact
------------------------------------
Every Wave Customer will be synchronized with a Superoffice Contact.

Once a link between a Wave Customer and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Superoffice Contact Property
     - Superoffice Data Type
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


Wave Invoice to Superoffice Quotealternative
--------------------------------------------
Before any synchronization can take place, a link between a Wave Invoice and a Superoffice Quotealternative must be established.

A new Superoffice Quotealternative will be created from a Wave Invoice if it is connected to a Wave Invoice that is synchronized into Superoffice.

Once a link between a Wave Invoice and a Superoffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Superoffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Superoffice Quotealternative Property
     - Superoffice Data Type
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


Wave Vendor to Superoffice Contact
----------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Superoffice Contact must be established.

A new Superoffice Contact will be created from a Wave Vendor if it is connected to a Wave Vendor, Customer, or Customer-person that is synchronized into Superoffice.

Once a link between a Wave Vendor and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Superoffice Contact Property
     - Superoffice Data Type
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


Wave Invoice to Superoffice Quoteline
-------------------------------------
Every Wave Invoice will be synchronized with a Superoffice Quoteline.

Once a link between a Wave Invoice and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Superoffice Quoteline Property
     - Superoffice Data Type
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


Wave Product to Superoffice Product
-----------------------------------
Every Wave Product will be synchronized with a Superoffice Product.

Once a link between a Wave Product and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Superoffice Product Property
     - Superoffice Data Type
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - unitPrice
     - UnitListPrice
     - N/A

