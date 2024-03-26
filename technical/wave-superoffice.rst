===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-03-26 13:42:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to  Person
-------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a  Person must be established.

A Wave Customer person will merge with a  Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Person Property
   * - email
     - Emails.Value

Once a link between a Wave Customer person and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Person:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Person Property
     -  Data Type
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


Wave Vendor to  Person
----------------------
Before any synchronization can take place, a link between a Wave Vendor and a  Person must be established.

A Wave Vendor will merge with a  Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Person Property
   * - email
     - Emails.Value

Once a link between a Wave Vendor and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Person:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Person Property
     -  Data Type
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
     - "list"
   * - website
     - Urls.Value
     - "string"


Wave Invoice to  Quotealternative
---------------------------------
Before any synchronization can take place, a link between a Wave Invoice and a  Quotealternative must be established.

A new  Quotealternative will be created from a Wave Invoice if it is connected to a Wave Invoice that is synchronized into .

Once a link between a Wave Invoice and a  Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Quotealternative:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Quotealternative Property
     -  Data Type
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

A new SuperOffice Contact will be created from a Wave Vendor if it is connected to a Wave Vendor, Customer, or Customer-person that is synchronized into SuperOffice.

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


Wave Invoice to  Quoteline
--------------------------
Every Wave Invoice will be synchronized with a  Quoteline.

Once a link between a Wave Invoice and a  Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Quoteline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Quoteline Property
     -  Data Type
   * - id
     - QuoteAlternativeId
     - "integer"
   * - items.description
     - Description
     - "string"
   * - items.price
     - UnitListPrice
     - "if-null", "integer", "string"], "decimal"]
   * - items.product.id
     - ERPProductKey
     - "string"
   * - items.quantity
     - Quantity
     - "integer", "decimal"]
   * - total.value
     - TotalPrice
     - "if-null", "integer", "string"], "decimal"]


Wave Product to  Product
------------------------
Every Wave Product will be synchronized with a  Product.

Once a link between a Wave Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Product Property
     -  Data Type
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - unitPrice
     - UnitListPrice
     - "decimal"

