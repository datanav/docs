================================
Business Central to Wix Dataflow
================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Contacts person to Wix Contacts
------------------------------------------------
Every Business Central Contacts person will be synchronized with a Wix Contacts.

Once a link between a Business Central Contacts person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Contacts person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Business Central Contacts person Property
     - Wix Contacts Property
     - Wix Data Type
   * - displayName
     - info.name.first
     - "string"
   * - displayName
     - info.name.last
     - "string"
   * - email
     - primaryInfo.email
     - "string"
   * - mobilePhoneNumber
     - primaryInfo.phone
     - "string"
   * - phoneNumber
     - primaryInfo.phone
     - "string"


Business Central Currencies to Wix Currencies
---------------------------------------------
Every Business Central Currencies will be synchronized with a Wix Currencies.

If a matching Wix Currencies already exists, the Business Central Currencies will be merged with the existing one.
If no matching Wix Currencies is found, a new Wix Currencies will be created.

A Business Central Currencies will merge with a Wix Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - Wix Currencies Property
   * - code
     - code

Once a link between a Business Central Currencies and a Wix Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Currencies and a Wix Currencies:

.. list-table::
   :header-rows: 1

   * - Business Central Currencies Property
     - Wix Currencies Property
     - Wix Data Type


Business Central Items to Wix Products
--------------------------------------
Every Business Central Items will be synchronized with a Wix Products.

Once a link between a Business Central Items and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Items and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Business Central Items Property
     - Wix Products Property
     - Wix Data Type
   * - displayName
     - name
     - "string"
   * - displayName.string
     - name
     - "string"
   * - displayName2
     - name
     - "string"
   * - unitCost
     - costAndProfitData.itemCost
     - N/A
   * - unitCost
     - costRange.maxValue
     - "string"
   * - unitPrice
     - priceData.price
     - N/A


Business Central Salesorders to Wix Orders
------------------------------------------
Every Business Central Salesorders will be synchronized with a Wix Orders.

Once a link between a Business Central Salesorders and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Wix Orders Property
     - Wix Data Type

