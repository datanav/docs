====================
Wix.com to  Dataflow
====================

Generated: 2024-03-26 13:42:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to  Customers company
--------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a  Customers company must be established.

A new  Customers company will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into .

Once a link between a Wix.com Contacts and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Customers company Property
     -  Data Type


Wix.com Contacts to  Customers person
-------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a  Customers person must be established.

A new  Customers person will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into .

Once a link between a Wix.com Contacts and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Customers person Property
     -  Data Type
   * - info.name.first
     - displayName
     - "string"
   * - info.name.last
     - displayName
     - "string"
   * - primaryInfo.email
     - email
     - "string"
   * - primaryInfo.email
     - id (Dependant on having wd:Q1273217 in type)
     - "string"
   * - primaryInfo.phone
     - phoneNumber
     - "string"


Wix.com Contacts to  Contacts person
------------------------------------
Every Wix.com Contacts will be synchronized with a  Contacts person.

Once a link between a Wix.com Contacts and a  Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Contacts person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Contacts person Property
     -  Data Type
   * - info.name.first
     - displayName
     - "string"
   * - info.name.last
     - displayName
     - "string"
   * - primaryInfo.email
     - email
     - "string"
   * - primaryInfo.phone
     - mobilePhoneNumber
     - "string"
   * - primaryInfo.phone
     - phoneNumber
     - "string"


Wix.com Orders to  Salesorderlines
----------------------------------
Every Wix.com Orders will be synchronized with a  Salesorderlines.

Once a link between a Wix.com Orders and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Salesorderlines Property
     -  Data Type
   * - id
     - documentId
     - "string"
   * - lineItems.name
     - description
     - "string"
   * - lineItems.name
     - discountPercent
     - "decimal"
   * - lineItems.name
     - quantity
     - "integer", "decimal"]
   * - lineItems.name
     - taxPercent
     - "decimal"
   * - lineItems.name
     - unitPrice
     - "float"
   * - lineItems.price
     - amountExcludingTax
     - "string"
   * - lineItems.price
     - description
     - "string"
   * - lineItems.price
     - discountPercent
     - "decimal"
   * - lineItems.price
     - quantity
     - "integer", "decimal"]
   * - lineItems.price
     - taxPercent
     - "decimal"
   * - lineItems.price
     - unitPrice
     - "float"
   * - lineItems.productId
     - itemId
     - "string"
   * - lineItems.quantity
     - description
     - "string"
   * - lineItems.quantity
     - discountPercent
     - "decimal"
   * - lineItems.quantity
     - invoiceQuantity
     - "string"
   * - lineItems.quantity
     - quantity
     - "integer", "decimal"]
   * - lineItems.quantity
     - taxPercent
     - "decimal"
   * - lineItems.quantity
     - unitPrice
     - "float"


Wix.com Orders to  Salesorders
------------------------------
Every Wix.com Orders will be synchronized with a  Salesorders.

Once a link between a Wix.com Orders and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Salesorders Property
     -  Data Type
   * - buyerInfo.id
     - customerId
     - "string"
   * - currency
     - currencyId
     - "string"
   * - totals.total
     - totalAmountExcludingTax
     - "string"


Wix.com Products to  Items
--------------------------
Every Wix.com Products will be synchronized with a  Items.

Once a link between a Wix.com Products and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Items:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Items Property
     -  Data Type
   * - costAndProfitData.itemCost
     - unitCost
     - "decimal"
   * - costRange.maxValue
     - unitCost
     - "decimal"
   * - name
     - displayName
     - "string"
   * - name
     - displayName.string
     - "string"
   * - name
     - displayName2
     - "string"
   * - priceData.price
     - unitPrice
     - "decimal"

