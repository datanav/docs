===================================
Wix.com to BusinessCentral Dataflow
===================================

Generated: 2024-09-11 08:39:13

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to BusinessCentral Customers company
-----------------------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a BusinessCentral Customers company must be established.

A new BusinessCentral Customers company will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into BusinessCentral.

Once a link between a Wix.com Contacts and a BusinessCentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a BusinessCentral Customers company:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - BusinessCentral Customers company Property
     - BusinessCentral Data Type


Wix.com Contacts to BusinessCentral Customers person
----------------------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a BusinessCentral Customers person must be established.

A new BusinessCentral Customers person will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into BusinessCentral.

Once a link between a Wix.com Contacts and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type
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


Wix.com Contacts to BusinessCentral Contacts person
---------------------------------------------------
Every Wix.com Contacts will be synchronized with a BusinessCentral Contacts person.

Once a link between a Wix.com Contacts and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
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


Wix.com Orders to BusinessCentral Salesorderlines
-------------------------------------------------
Every Wix.com Orders will be synchronized with a BusinessCentral Salesorderlines.

Once a link between a Wix.com Orders and a BusinessCentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a BusinessCentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - BusinessCentral Salesorderlines Property
     - BusinessCentral Data Type
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


Wix.com Orders to BusinessCentral Salesorders
---------------------------------------------
Every Wix.com Orders will be synchronized with a BusinessCentral Salesorders.

Once a link between a Wix.com Orders and a BusinessCentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a BusinessCentral Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - BusinessCentral Salesorders Property
     - BusinessCentral Data Type
   * - buyerInfo.id
     - customerId
     - "string"
   * - currency
     - currencyId
     - "string"
   * - totals.total
     - totalAmountExcludingTax
     - "string"


Wix.com Products to BusinessCentral Items
-----------------------------------------
Every Wix.com Products will be synchronized with a BusinessCentral Items.

Once a link between a Wix.com Products and a BusinessCentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a BusinessCentral Items:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - BusinessCentral Items Property
     - BusinessCentral Data Type
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

