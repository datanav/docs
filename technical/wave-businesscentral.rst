===========================
Wave Financial to  Dataflow
===========================

Generated: 2023-11-30 20:48:33

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Product to  Items
----------------------
Every Wave Product will be synchronized with a  Items.

Once a link between a Wave Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Items:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Items Property
     -  Data Type


Wave Customer to  Company
-------------------------
Every Wave Customer will be synchronized with a  Company.

Once a link between a Wave Customer and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Company:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Company Property
     -  Data Type


Wave Vendor to  Company
-----------------------
Every Wave Vendor will be synchronized with a  Company.

Once a link between a Wave Vendor and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Company:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Company Property
     -  Data Type


Wave Invoice to  Salesorderlines
--------------------------------
Every Wave Invoice will be synchronized with a  Salesorderlines.

Once a link between a Wave Invoice and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Salesorderlines Property
     -  Data Type
   * - items.description
     - description
     - "string"
   * - items.price
     - amountExcludingTax
     - "string"
   * - items.product.id
     - itemId
     - "string"
   * - items.quantity
     - invoiceQuantity
     - "string"


Wave Invoice to  Salesorders
----------------------------
Every Wave Invoice will be synchronized with a  Salesorders.

Once a link between a Wave Invoice and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Salesorders Property
     -  Data Type
   * - customer.id
     - customerId
     - "string"
   * - total.value
     - totalAmountExcludingTax
     - "string"

