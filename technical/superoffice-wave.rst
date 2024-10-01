============================
SuperOffice to Wave Dataflow
============================

Generated: 2024-10-01 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to Wave Customer
-----------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Wave Customer must be established.

A new Wave Customer will be created from a SuperOffice Person if it is connected to a SuperOffice Sale, Quote, Quoteline, or Quotealternative that is synchronized into Wave.

A SuperOffice Person will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wave Customer Property
   * - Emails.Value
     - email

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
   * - Emails.Value
     - email
     - "string"
   * - Firstname
     - firstName
     - "string"
   * - Lastname
     - lastName
     - N/A
   * - MobilePhones.Value
     - mobile
     - "string"
   * - OfficePhones.Value
     - phone
     - "string"


SuperOffice User to Wave Customer
---------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a Wave Customer must be established.

A SuperOffice User will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wave Customer Property
   * - personEmail
     - email

Once a link between a SuperOffice User and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wave Customer Property
     - Wave Data Type
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - N/A
   * - personEmail
     - email
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

