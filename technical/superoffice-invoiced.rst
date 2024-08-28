========================
SuperOffice to  Dataflow
========================

Generated: 2024-08-28 08:16:18

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Quoteline to  Lineitem
----------------------------------
Every SuperOffice Quoteline will be synchronized with a  Lineitem.

Once a link between a SuperOffice Quoteline and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     -  Lineitem Property
     -  Data Type
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

