============================
Wave to SuperOffice Dataflow
============================

Generated: 2024-09-11 11:28:27

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


WaveWave Financial Customer to SuperOffice Person
-------------------------------------------------
Before any synchronization can take place, a link between a WaveWave Financial Customer and a SuperOffice Person must be established.

A new SuperOffice Person will be created from a WaveWave Financial Customer if it is connected to a WaveWave Financial Wave-invoice that is synchronized into SuperOffice.

A WaveWave Financial Customer will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WaveWave Financial Customer Property
     - SuperOffice Person Property
   * - email
     - Emails.Value

Once a link between a WaveWave Financial Customer and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WaveWave Financial Customer and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - WaveWave Financial Customer Property
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


WaveWave Financial Customer to SuperOfficeSuperoffice Contact
-------------------------------------------------------------
Every WaveWave Financial Customer will be synchronized with a SuperOfficeSuperoffice Contact.

Once a link between a WaveWave Financial Customer and a SuperOfficeSuperoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WaveWave Financial Customer and a SuperOfficeSuperoffice Contact:

.. list-table::
   :header-rows: 1

   * - WaveWave Financial Customer Property
     - SuperOfficeSuperoffice Contact Property
     - SuperOfficeSuperoffice Data Type
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


WaveWave Financial Vendor to SuperOfficeSuperoffice Contact
-----------------------------------------------------------
Before any synchronization can take place, a link between a WaveWave Financial Vendor and a SuperOfficeSuperoffice Contact must be established.

A new SuperOfficeSuperoffice Contact will be created from a WaveWave Financial Vendor if it is connected to a WaveWave Financial Wave-vendor, Wave-customer, Wave-customer-person, or Wave-customer-contact that is synchronized into SuperOfficeSuperoffice.

Once a link between a WaveWave Financial Vendor and a SuperOfficeSuperoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WaveWave Financial Vendor and a SuperOfficeSuperoffice Contact:

.. list-table::
   :header-rows: 1

   * - WaveWave Financial Vendor Property
     - SuperOfficeSuperoffice Contact Property
     - SuperOfficeSuperoffice Data Type
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

