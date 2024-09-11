======================================
Business Nxt to PowerOfficeGO Dataflow
======================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessNxt Order to PowerOfficeGO Salesorders
----------------------------------------------
Every BusinessNxt Order will be synchronized with a PowerOfficeGO Salesorders.

Once a link between a BusinessNxt Order and a PowerOfficeGO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Order and a PowerOfficeGO Salesorders:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Order Property
     - PowerOfficeGO Salesorders Property
     - PowerOfficeGO Data Type
   * - orderDate
     - SalesOrderDate
     - "string"


BusinessNxt Orderline to PowerOfficeGO Salesorderlines
------------------------------------------------------
Every BusinessNxt Orderline will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a BusinessNxt Orderline and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type
   * - orderNo
     - sesam_SalesOrderId
     - "string"


BusinessNxt Product to PowerOfficeGO Product
--------------------------------------------
Every BusinessNxt Product will be synchronized with a PowerOfficeGO Product.

Once a link between a BusinessNxt Product and a PowerOfficeGO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Product and a PowerOfficeGO Product:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Product Property
     - PowerOfficeGO Product Property
     - PowerOfficeGO Data Type
   * - description
     - description
     - "string"
   * - priceQuantity
     - salesPrice
     - N/A
   * - quantityPerUnit
     - availableStock
     - "integer"

