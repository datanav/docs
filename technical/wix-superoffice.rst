====================
Wix.com to  Dataflow
====================

Generated: 2024-03-26 00:00:03

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to  Person
---------------------------
Every Wix.com Contacts will be synchronized with a  Person.

If a matching  Person already exists, the Wix.com Contacts will be merged with the existing one.
If no matching  Person is found, a new  Person will be created.

A Wix.com Contacts will merge with a  Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Person Property
   * - primaryInfo.email
     - Emails.Value

Once a link between a Wix.com Contacts and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Person Property
     -  Data Type
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


Wix.com Members to  Person
--------------------------
Before any synchronization can take place, a link between a Wix.com Members and a  Person must be established.

A Wix.com Members will merge with a  Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Person Property
   * - loginEmail
     - Emails.Value

Once a link between a Wix.com Members and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a  Person:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Person Property
     -  Data Type
   * - loginEmail
     - Emails.Value
     - "string"


Wix.com Orders to  Quotealternative
-----------------------------------
Before any synchronization can take place, a link between a Wix.com Orders and a  Quotealternative must be established.

A new  Quotealternative will be created from a Wix.com Orders if it is connected to a Wix.com Wix-orders that is synchronized into .

Once a link between a Wix.com Orders and a  Quotealternative is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Quotealternative:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Quotealternative Property
     -  Data Type
   * - totals.total
     - TotalPrice
     - "float"


Wix.com Orders to  Quoteline
----------------------------
Every Wix.com Orders will be synchronized with a  Quoteline.

Once a link between a Wix.com Orders and a  Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Quoteline:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Quoteline Property
     -  Data Type
   * - id
     - QuoteAlternativeId
     - "integer"
   * - lineItems.name
     - Name
     - "string"
   * - lineItems.price
     - UnitListPrice
     - "if-null", "integer", "string"], "decimal"]
   * - lineItems.productId
     - ERPProductKey
     - "string"
   * - lineItems.quantity
     - Quantity
     - "integer", "decimal"]
   * - totals.total
     - TotalPrice
     - "if-null", "integer", "string"], "decimal"]


Wix.com Products to  Product
----------------------------
Every Wix.com Products will be synchronized with a  Product.

Once a link between a Wix.com Products and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Product Property
     -  Data Type
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
     - "decimal"
   * - priceData.currency
     - ERPPriceListKey
     - "string"
   * - priceData.price
     - UnitListPrice
     - "decimal"

