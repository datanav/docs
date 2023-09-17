======================================
Wave Financial to SuperOffice Dataflow
======================================

Generated: 2023-09-17 18:19:36

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to SuperOffice Person
------------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a SuperOffice Person must be established.

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


Wave Customer to SuperOffice Person
-----------------------------------
Every Wave Customer will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the Wave Customer will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

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
     - "list"
   * - website
     - Urls.Value
     - "string"


Wave Customer person to SuperOffice Contact
-------------------------------------------
Every Wave Customer person will be synchronized with a SuperOffice Contact.

Once a link between a Wave Customer person and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - SuperOffice Contact Property
     - SuperOffice Data Type


Wave Vendor to SuperOffice Contact
----------------------------------
Every Wave Vendor will be synchronized with a SuperOffice Contact.

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
   * - phone
     - Phones.Value
     - "string"
   * - website
     - Domains
     - "list"
   * - website
     - Urls.Value
     - "string"


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
     - "decimal"

