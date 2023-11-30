========================
SuperOffice to  Dataflow
========================

Generated: 2023-11-30 20:48:28

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Company
-------------------------------
Every SuperOffice Contact will be synchronized with a  Company.

Once a link between a SuperOffice Contact and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Company:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Company Property
     -  Data Type


SuperOffice Product to  Items
-----------------------------
Every SuperOffice Product will be synchronized with a  Items.

Once a link between a SuperOffice Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Items:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Items Property
     -  Data Type


SuperOffice Quoteline to  Salesorderlines
-----------------------------------------
Every SuperOffice Quoteline will be synchronized with a  Salesorderlines.

Once a link between a SuperOffice Quoteline and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     -  Salesorderlines Property
     -  Data Type
   * - Description
     - description
     - "string"
   * - DiscountPercent
     - discountPercent
     - "string"
   * - ERPProductKey
     - itemId
     - "string"
   * - Quantity
     - invoiceQuantity
     - "string"
   * - UnitListPrice
     - amountExcludingTax
     - "string"

