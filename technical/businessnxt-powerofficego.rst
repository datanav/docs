=====================================
Businessnxt to Powerofficego Dataflow
=====================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Order to Powerofficego Salesorders
----------------------------------------------
Every Businessnxt Order will be synchronized with a Powerofficego Salesorders.

Once a link between a Businessnxt Order and a Powerofficego Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Order and a Powerofficego Salesorders:

.. list-table::
   :header-rows: 1

   * - Businessnxt Order Property
     - Powerofficego Salesorders Property
     - Powerofficego Data Type
   * - orderDate
     - SalesOrderDate
     - "string"


Businessnxt Orderline to Powerofficego Salesorderlines
------------------------------------------------------
Every Businessnxt Orderline will be synchronized with a Powerofficego Salesorderlines.

Once a link between a Businessnxt Orderline and a Powerofficego Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a Powerofficego Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     - Powerofficego Salesorderlines Property
     - Powerofficego Data Type
   * - orderNo
     - sesam_SalesOrderId
     - "string"


Businessnxt Product to Powerofficego Product
--------------------------------------------
Every Businessnxt Product will be synchronized with a Powerofficego Product.

Once a link between a Businessnxt Product and a Powerofficego Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a Powerofficego Product:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
     - Powerofficego Product Property
     - Powerofficego Data Type
   * - description
     - description
     - "string"
   * - priceQuantity
     - salesPrice
     - N/A
   * - quantityPerUnit
     - availableStock
     - "integer"

