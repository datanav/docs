=============================================
Visma Business Nxt to PowerOffice GO Dataflow
=============================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Visma Business Nxt to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Visma Order to PowerOffice Salesorders
--------------------------------------
Every Visma Order will be synchronized with a PowerOffice Salesorders.

Once a link between a Visma Order and a PowerOffice Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Order and a PowerOffice Salesorders:

.. list-table::
   :header-rows: 1

   * - Visma Order Property
     - PowerOffice Salesorders Property
     - PowerOffice Data Type
   * - orderDate
     - SalesOrderDate
     - "string"


Visma Orderline to PowerOffice Salesorderlines
----------------------------------------------
Every Visma Orderline will be synchronized with a PowerOffice Salesorderlines.

Once a link between a Visma Orderline and a PowerOffice Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Orderline and a PowerOffice Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Visma Orderline Property
     - PowerOffice Salesorderlines Property
     - PowerOffice Data Type
   * - orderNo
     - sesam_SalesOrderId
     - "string"


Visma Product to PowerOffice Product
------------------------------------
Every Visma Product will be synchronized with a PowerOffice Product.

Once a link between a Visma Product and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Product and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - Visma Product Property
     - PowerOffice Product Property
     - PowerOffice Data Type
   * - description
     - description
     - "string"
   * - priceQuantity
     - salesPrice
     - N/A
   * - quantityPerUnit
     - availableStock
     - "integer"

