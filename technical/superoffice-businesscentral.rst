========================================
SuperOffice to Business Central Dataflow
========================================

Generated: 2024-10-01 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Business Central Companies
-------------------------------------------------
Every SuperOffice Contact will be synchronized with a Business Central Companies.

Once a link between a SuperOffice Contact and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Business Central Companies Property
     - Business Central Data Type


SuperOffice Product to Business Central Items
---------------------------------------------
Every SuperOffice Product will be synchronized with a Business Central Items.

Once a link between a SuperOffice Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Business Central Items Property
     - Business Central Data Type
   * - Name
     - displayName
     - "string"
   * - UnitCost
     - unitCost
     - N/A
   * - UnitListPrice
     - unitPrice
     - N/A


SuperOffice Quoteline to Business Central Salesorderlines
---------------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Business Central Salesorderlines.

Once a link between a SuperOffice Quoteline and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
   * - DiscountPercent
     - discountPercent
     - N/A
   * - ERPDiscountPercent
     - discountPercent
     - N/A
   * - ERPProductKey
     - itemId
     - "string"
   * - Name
     - description
     - "string"
   * - Quantity
     - quantity
     - N/A
   * - QuoteAlternativeId
     - documentId
     - "string"
   * - UnitListPrice
     - unitPrice
     - "float"
   * - VAT
     - taxPercent
     - N/A

