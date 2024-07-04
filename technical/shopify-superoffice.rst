===============================
Shopify to Superoffice Dataflow
===============================

Generated: 2024-07-04 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Order to Superoffice Quotealternative
---------------------------------------------
Before any synchronization can take place, a link between a Shopify Order and a Superoffice Quotealternative must be established.

A new Superoffice Quotealternative will be created from a Shopify Order if it is connected to a Shopify Order that is synchronized into Superoffice.

Once a link between a Shopify Order and a Superoffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Superoffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Superoffice Quotealternative Property
     - Superoffice Data Type
   * - current_total_price
     - TotalPrice
     - "float"
   * - total_price
     - TotalPrice
     - "float"


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
   * - default_address.address1
     - Address.Street.Address1
     - "string"
   * - default_address.address2
     - Address.Street.Address2
     - "string"
   * - default_address.city
     - Address.Street.City
     - "string"
   * - default_address.country
     - Country.CountryId
     - "integer"
   * - default_address.zip
     - Address.Street.Zipcode
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - first_name
     - Firstname
     - "string"
   * - id
     - PersonId
     - "integer"
   * - last_name
     - Lastname
     - "string"
   * - phone
     - OfficePhones.Value
     - "string"


Shopify Order to Superoffice Quoteline
--------------------------------------
Every Shopify Order will be synchronized with a Superoffice Quoteline.

Once a link between a Shopify Order and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - Superoffice Quoteline Property
     - Superoffice Data Type
   * - line_items.price
     - UnitListPrice
     - N/A
   * - line_items.quantity
     - Quantity
     - N/A
   * - line_items.title
     - Name
     - "string"
   * - line_items.total_discount
     - ERPDiscountPercent
     - "integer"


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
   * - title
     - Name
     - "string"
   * - variants.price
     - UnitListPrice
     - N/A
   * - variants.title
     - Name
     - "string"

