============================
Wix.com to Invoiced Dataflow
============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Orders to Invoiced Invoices
-----------------------------------
Every Wix.com Orders will be synchronized with a Invoiced Invoices.

Once a link between a Wix.com Orders and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - buyerInfo.id
     - customer
     - "string"
   * - currency
     - currency
     - "string"


Wix.com Orders to Invoiced Lineitem
-----------------------------------
Every Wix.com Orders will be synchronized with a Invoiced Lineitem.

Once a link between a Wix.com Orders and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - Invoiced Lineitem Property
     - Invoiced Data Type
   * - lineItems.name
     - items.name
     - "string"
   * - lineItems.price
     - items.amount
     - "string"
   * - lineItems.quantity
     - items.quantity
     - "string"


Wix.com Products to Invoiced Items
----------------------------------
Every Wix.com Products will be synchronized with a Invoiced Items.

Once a link between a Wix.com Products and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - costAndProfitData.itemCost
     - unit_cost
     - "string"
   * - costRange.maxValue
     - unit_cost
     - "string"
   * - name
     - name
     - "string"
   * - priceData.currency
     - currency
     - "string"

