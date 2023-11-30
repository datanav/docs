====================
Wix.com to  Dataflow
====================

Generated: 2023-11-30 20:49:03

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Wix.com Inventory to  Items
---------------------------
Every Wix.com Inventory will be synchronized with a  Items.

Once a link between a Wix.com Inventory and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Inventory and a  Items:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     -  Items Property
     -  Data Type


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
   * - lineItems.price
     - amountExcludingTax
     - "string"
   * - lineItems.productId
     - itemId
     - "string"
   * - lineItems.quantity
     - invoiceQuantity
     - "string"
   * - lineItems.quantity
     - quantity
     - "string"


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
   * - totals.total
     - totalAmountExcludingTax
     - "string"

