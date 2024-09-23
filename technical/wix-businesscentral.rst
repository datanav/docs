====================================
Wix.com to Business Central Dataflow
====================================

Generated: 2024-09-23 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Business Central Contacts (human data)
----------------------------------------------------------
Every Wix.com Contacts will be synchronized with a Business Central Contacts (human data).

Once a link between a Wix.com Contacts and a Business Central Contacts (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Business Central Contacts (human data):

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Business Central Contacts (human data) Property
     - Business Central Data Type
   * - primaryInfo.email
     - email
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
   * - priceData.price
     - unitPrice
     - N/A

