============================
SuperOffice to Wave Dataflow
============================

Generated: 2023-10-05 08:40:35

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Wave Customer person
-------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Wave Customer person must be established.

A new Wave Customer person will be created from a SuperOffice Contact if it is connected to a SuperOffice Person, Contact, Quoteline, or Quotealternative that is synchronized into Wave.

Once a link between a SuperOffice Contact and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Wave Customer person Property
     - Wave Data Type
   * - Address.Postal.Address1
     - address.addressLine1
     - "string"
   * - Address.Postal.Address1
     - shippingDetails.address.addressLine1
     - "string"
   * - Address.Postal.Address2
     - address.addressLine2
     - "string"
   * - Address.Postal.Address2
     - shippingDetails.address.addressLine2
     - "string"
   * - Address.Postal.City
     - address.city
     - "string"
   * - Address.Postal.City
     - shippingDetails.address.city
     - "string"
   * - Address.Postal.Zipcode
     - address.postalCode
     - "string"
   * - Address.Postal.Zipcode
     - shippingDetails.address.postalCode
     - "string"
   * - Address.Street.Address1
     - address.addressLine1
     - "string"
   * - Address.Street.Address1
     - shippingDetails.address.addressLine1
     - "string"
   * - Address.Street.Address2
     - address.addressLine2
     - "string"
   * - Address.Street.Address2
     - shippingDetails.address.addressLine2
     - "string"
   * - Address.Street.City
     - address.city
     - "string"
   * - Address.Street.City
     - shippingDetails.address.city
     - "string"
   * - Address.Street.Zipcode
     - address.postalCode
     - "string"
   * - Address.Street.Zipcode
     - shippingDetails.address.postalCode
     - "string"
   * - ContactId
     - id
     - "string"
   * - Country.CountryId
     - address.country.code
     - "string"
   * - Country.CountryId
     - shippingDetails.address.country.code
     - "string"


SuperOffice Contact to Wave Customer
------------------------------------
Every SuperOffice Contact will be synchronized with a Wave Customer.

Once a link between a SuperOffice Contact and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Wave Customer Property
     - Wave Data Type
   * - Address.Postal.Address1
     - address.addressLine1
     - "string"
   * - Address.Postal.Address1
     - shippingDetails.address.addressLine1
     - "string"
   * - Address.Postal.Address2
     - address.addressLine2
     - "string"
   * - Address.Postal.Address2
     - shippingDetails.address.addressLine2
     - "string"
   * - Address.Postal.City
     - address.city
     - "string"
   * - Address.Postal.City
     - shippingDetails.address.city
     - "string"
   * - Address.Postal.Zipcode
     - address.postalCode
     - "string"
   * - Address.Postal.Zipcode
     - shippingDetails.address.postalCode
     - "string"
   * - Address.Street.Address1
     - address.addressLine1
     - "string"
   * - Address.Street.Address1
     - shippingDetails.address.addressLine1
     - "string"
   * - Address.Street.Address2
     - address.addressLine2
     - "string"
   * - Address.Street.Address2
     - shippingDetails.address.addressLine2
     - "string"
   * - Address.Street.City
     - address.city
     - "string"
   * - Address.Street.City
     - shippingDetails.address.city
     - "string"
   * - Address.Street.Zipcode
     - address.postalCode
     - "string"
   * - Address.Street.Zipcode
     - shippingDetails.address.postalCode
     - "string"
   * - Country.CountryId
     - address.country.code
     - "string"
   * - Country.CountryId
     - shippingDetails.address.country.code
     - "string"
   * - Domains
     - website
     - "string"
   * - Name
     - name
     - "if","or","is-empty","_."],"eq","","_."]],"-","_."]
   * - Phones.Value
     - phone
     - "string"
   * - Phones.Value
     - shippingDetails.phone
     - "string"
   * - Urls.Value
     - website
     - "string"


SuperOffice Person to Wave Customer person
------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Wave Customer person must be established.

A new Wave Customer person will be created from a SuperOffice Person if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into Wave.

Once a link between a SuperOffice Person and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wave Customer person Property
     - Wave Data Type
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
   * - Country.CountryId
     - address.country.code
     - "string"
   * - Emails.Value
     - email
     - "string"
   * - Firstname
     - firstName
     - "string"
   * - Lastname
     - lastName
     - "if","or","is-empty","_."],"eq","","_."]],"-","_."]
   * - MobilePhones.Value
     - mobile
     - "string"
   * - OfficePhones.Value
     - phone
     - "string"


SuperOffice Person to Wave Customer
-----------------------------------
Every SuperOffice Person will be synchronized with a Wave Customer.

Once a link between a SuperOffice Person and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wave Customer Property
     - Wave Data Type
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
   * - Contact.ContactId
     - id
     - "string"
   * - Country.CountryId
     - address.country.code
     - "string"
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
     - mobile
     - "string"


SuperOffice Quotealternative to Wave Invoice
--------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a Wave Invoice must be established.

A new Wave Invoice will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Sale, Quote, Quoteline, or Quotealternative that is synchronized into Wave.

Once a link between a SuperOffice Quotealternative and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Wave Invoice Property
     - Wave Data Type
   * - Description
     - memo
     - "string"
   * - Name
     - title
     - "string"


SuperOffice Product to Wave Product
-----------------------------------
Every SuperOffice Product will be synchronized with a Wave Product.

Once a link between a SuperOffice Product and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Wave Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Wave Product Property
     - Wave Data Type
   * - Description
     - description
     - "string"
   * - Name
     - name
     - "string"
   * - UnitListPrice
     - unitPrice
     - "string"


SuperOffice Quoteline to Wave Invoice
-------------------------------------
Every SuperOffice Quoteline will be synchronized with a Wave Invoice.

Once a link between a SuperOffice Quoteline and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Wave Invoice Property
     - Wave Data Type

