===============================
Wix.com to SuperOffice Dataflow
===============================

Generated: 2024-09-24 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to SuperOffice Person
--------------------------------------
Every Wix.com Contacts will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the Wix.com Contacts will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A Wix.com Contacts will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - SuperOffice Person Property
   * - primaryInfo.email
     - Emails.Value

Once a link between a Wix.com Contacts and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - info.name.first
     - Firstname
     - "string"
   * - info.name.last
     - Lastname
     - "string"
   * - primaryInfo.email
     - Emails.Value
     - "string"
   * - primaryInfo.phone
     - OfficePhones.Value
     - "string"


Wix.com Members to SuperOffice Person
-------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a SuperOffice Person must be established.

A Wix.com Members will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - SuperOffice Person Property
   * - loginEmail
     - Emails.Value

Once a link between a Wix.com Members and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - loginEmail
     - Emails.Value
     - "string"


Wix.com Orders to SuperOffice Quoteline
---------------------------------------
Every Wix.com Orders will be synchronized with a SuperOffice Quoteline.

Once a link between a Wix.com Orders and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
   * - id
     - QuoteAlternativeId
     - "integer"
   * - lineItems.name
     - Name
     - "string"
   * - lineItems.price
     - UnitListPrice
     - N/A
   * - lineItems.productId
     - ERPProductKey
     - "string"
   * - lineItems.quantity
     - Quantity
     - N/A


Wix.com Products to SuperOffice Product
---------------------------------------
Every Wix.com Products will be synchronized with a SuperOffice Product.

Once a link between a Wix.com Products and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - costAndProfitData.itemCost
     - UnitCost
     - "string"
   * - costRange.maxValue
     - UnitCost
     - "string"
   * - name
     - Name
     - "string"
   * - priceData.currency
     - ERPPriceListKey
     - "string"
   * - priceData.price
     - UnitListPrice
     - N/A

