====================================
Wix.com to Business Central Dataflow
====================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Business Central Customers company
------------------------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Business Central Customers company must be established.

A new Business Central Customers company will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into Business Central.

Once a link between a Wix.com Contacts and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Business Central Customers company Property
     - Business Central Data Type


Wix.com Contacts to Business Central Customers person
-----------------------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Business Central Customers person must be established.

A new Business Central Customers person will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into Business Central.

Once a link between a Wix.com Contacts and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Business Central Customers person Property
     - Business Central Data Type
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


Wix.com Contacts to Business Central Contacts person
----------------------------------------------------
Every Wix.com Contacts will be synchronized with a Business Central Contacts person.

Once a link between a Wix.com Contacts and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Business Central Contacts person Property
     - Business Central Data Type
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


Wix.com Orders to Business Central Salesorderlines
--------------------------------------------------
Every Wix.com Orders will be synchronized with a Business Central Salesorderlines.

Once a link between a Wix.com Orders and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
   * - id
     - documentId
     - "string"
   * - lineItems.name
     - description
     - "string"
   * - lineItems.name
     - discountPercent
     - N/A
   * - lineItems.name
     - quantity
     - N/A
   * - lineItems.name
     - taxPercent
     - N/A
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
     - N/A
   * - lineItems.price
     - quantity
     - N/A
   * - lineItems.price
     - taxPercent
     - N/A
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
     - N/A
   * - lineItems.quantity
     - invoiceQuantity
     - "string"
   * - lineItems.quantity
     - quantity
     - N/A
   * - lineItems.quantity
     - taxPercent
     - N/A
   * - lineItems.quantity
     - unitPrice
     - "float"


Wix.com Orders to Business Central Salesorders
----------------------------------------------
Every Wix.com Orders will be synchronized with a Business Central Salesorders.

Once a link between a Wix.com Orders and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Business Central Salesorders Property
     - Business Central Data Type
   * - buyerInfo.id
     - customerId
     - "string"
   * - currency
     - currencyId
     - "string"
   * - totals.total
     - totalAmountExcludingTax
     - "string"


Wix.com Products to Business Central Items
------------------------------------------
Every Wix.com Products will be synchronized with a Business Central Items.

Once a link between a Wix.com Products and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Business Central Items Property
     - Business Central Data Type
   * - costAndProfitData.itemCost
     - unitCost
     - N/A
   * - costRange.maxValue
     - unitCost
     - N/A
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
     - N/A

