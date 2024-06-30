===============================
Wix.com to Superoffice Dataflow
===============================

Generated: 2024-06-30 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Superoffice Person
--------------------------------------
Every Wix.com Contacts will be synchronized with a Superoffice Person.

If a matching Superoffice Person already exists, the Wix.com Contacts will be merged with the existing one.
If no matching Superoffice Person is found, a new Superoffice Person will be created.

A Wix.com Contacts will merge with a Superoffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Superoffice Person Property
   * - primaryInfo.email
     - Emails.Value

Once a link between a Wix.com Contacts and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - info.emails
     - Emails.Value
     - "string"
   * - info.name.first
     - Firstname
     - "string"
   * - info.name.last
     - Lastname
     - "string"
   * - info.phones
     - MobilePhones.Value
     - "string"
   * - primaryInfo.email
     - Emails.Value
     - "string"
   * - primaryInfo.phone
     - MobilePhones.Value
     - "string"
   * - primaryInfo.phone
     - OfficePhones.Value
     - "string"


Wix.com Members to Superoffice Person
-------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Superoffice Person must be established.

A Wix.com Members will merge with a Superoffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Superoffice Person Property
   * - loginEmail
     - Emails.Value

Once a link between a Wix.com Members and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - loginEmail
     - Emails.Value
     - "string"


Wix.com Orders to Superoffice Quotealternative
----------------------------------------------
Before any synchronization can take place, a link between a Wix.com Orders and a Superoffice Quotealternative must be established.

A new Superoffice Quotealternative will be created from a Wix.com Orders if it is connected to a Wix.com Wix-orders that is synchronized into Superoffice.

Once a link between a Wix.com Orders and a Superoffice Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Superoffice Quotealternative:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Superoffice Quotealternative Property
     - Superoffice Data Type
   * - totals.total
     - TotalPrice
     - "float"


Wix.com Orders to Superoffice Quoteline
---------------------------------------
Every Wix.com Orders will be synchronized with a Superoffice Quoteline.

Once a link between a Wix.com Orders and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Superoffice Quoteline Property
     - Superoffice Data Type
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
   * - totals.total
     - TotalPrice
     - N/A


Wix.com Products to Superoffice Product
---------------------------------------
Every Wix.com Products will be synchronized with a Superoffice Product.

Once a link between a Wix.com Products and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Superoffice Product Property
     - Superoffice Data Type
   * - costAndProfitData.itemCost
     - UnitCost
     - "string"
   * - costRange.maxValue
     - UnitCost
     - "string"
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - price.currency
     - ERPPriceListKey
     - "string"
   * - price.price
     - UnitListPrice
     - N/A
   * - priceData.currency
     - ERPPriceListKey
     - "string"
   * - priceData.price
     - UnitListPrice
     - N/A

