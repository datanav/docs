===============================
Shopify to Superoffice Dataflow
===============================

Generated: 2024-06-25 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to Superoffice Person
--------------------------------------
Every Shopify Customer will be synchronized with a Superoffice Person.

Once a link between a Shopify Customer and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - addresses.address1
     - Address.Street.Address1
     - "string"
   * - addresses.address2
     - Address.Street.Address2
     - "string"
   * - addresses.city
     - Address.Street.City
     - "string"
   * - addresses.country
     - Country.CountryId
     - "integer"
   * - addresses.zip
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - id
     - PersonId
     - "integer"
   * - phone
     - OfficePhones.Value
     - "string"


Shopify Product to Superoffice Product
--------------------------------------
Every Shopify Product will be synchronized with a Superoffice Product.

Once a link between a Shopify Product and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Product and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Shopify Product Property
     - Superoffice Product Property
     - Superoffice Data Type
   * - variants.price
     - UnitListPrice
     - N/A
   * - variants.title
     - Name
     - "string"

