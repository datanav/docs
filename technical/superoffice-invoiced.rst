================================
SuperOffice to Invoiced Dataflow
================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Product to Invoiced Items
-------------------------------------
Every SuperOffice Product will be synchronized with a Invoiced Items.

Once a link between a SuperOffice Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - Description
     - description
     - "string"
   * - ERPPriceListKey
     - currency
     - "string"
   * - Name
     - name
     - "string"
   * - UnitCost
     - unit_cost
     - "string"


SuperOffice Quoteline to Invoiced Lineitem
------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Invoiced Lineitem.

Once a link between a SuperOffice Quoteline and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Invoiced Lineitem Property
     - Invoiced Data Type
   * - Description
     - items.description
     - "string"
   * - DiscountPercent
     - items.discounts
     - "string"
   * - ERPDiscountPercent
     - items.discounts
     - "string"
   * - Name
     - items.name
     - "string"
   * - Quantity
     - items.quantity
     - "string"
   * - UnitListPrice
     - items.amount
     - "string"

