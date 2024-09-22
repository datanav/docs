===============================
Shopify to SuperOffice Dataflow
===============================

Generated: 2024-09-22 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Shopify to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Shopify Customer to SuperOffice Person
--------------------------------------
Every Shopify Customer will be synchronized with a SuperOffice Person.

Once a link between a Shopify Customer and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Customer and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Shopify Customer Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - default_address.phone
     - OfficePhones.Value
     - "string"
   * - email
     - Emails.Value
     - "string"
   * - first_name
     - Firstname
     - "string"
   * - last_name
     - Lastname
     - "string"
   * - phone
     - MobilePhones.Value
     - "string"


Shopify Order to SuperOffice Quoteline
--------------------------------------
Every Shopify Order will be synchronized with a SuperOffice Quoteline.

Once a link between a Shopify Order and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Order and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Shopify Order Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - id
     - QuoteAlternativeId
     - "integer"
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


Shopify Sesamproduct to SuperOffice Product
-------------------------------------------
Every Shopify Sesamproduct will be synchronized with a SuperOffice Product.

Once a link between a Shopify Sesamproduct and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Shopify Sesamproduct and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Shopify Sesamproduct Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - sesam_priceExclVAT
     - UnitListPrice
     - N/A
   * - title
     - Name
     - "string"
   * - variants.title
     - Description
     - "string"

