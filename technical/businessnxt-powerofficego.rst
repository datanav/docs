=======================================
Business Nxt to PowerOffice GO Dataflow
=======================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Currency to PowerOffice GO Currency
------------------------------------------------
Every Business Nxt Currency will be synchronized with a PowerOffice GO Currency.

Once a link between a Business Nxt Currency and a PowerOffice GO Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Currency and a PowerOffice GO Currency:

.. list-table::
   :header-rows: 1

   * - Business Nxt Currency Property
     - PowerOffice GO Currency Property
     - PowerOffice GO Data Type


Business Nxt Order to PowerOffice GO Salesorders
------------------------------------------------
Every Business Nxt Order will be synchronized with a PowerOffice GO Salesorders.

Once a link between a Business Nxt Order and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Order and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - Business Nxt Order Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type
   * - orderDate
     - SalesOrderDate
     - "string"


Business Nxt Orderline to PowerOffice GO Salesorderlines
--------------------------------------------------------
Every Business Nxt Orderline will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a Business Nxt Orderline and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type
   * - orderNo
     - sesam_SalesOrderId
     - "string"


Business Nxt Product to PowerOffice GO Product
----------------------------------------------
Every Business Nxt Product will be synchronized with a PowerOffice GO Product.

Once a link between a Business Nxt Product and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Product and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - Business Nxt Product Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type
   * - description
     - description
     - "string"
   * - priceQuantity
     - salesPrice
     - N/A
   * - quantityPerUnit
     - availableStock
     - "integer"


Business Nxt Productcategory to PowerOffice GO Productgroup
-----------------------------------------------------------
Every Business Nxt Productcategory will be synchronized with a PowerOffice GO Productgroup.

Once a link between a Business Nxt Productcategory and a PowerOffice GO Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Productcategory and a PowerOffice GO Productgroup:

.. list-table::
   :header-rows: 1

   * - Business Nxt Productcategory Property
     - PowerOffice GO Productgroup Property
     - PowerOffice GO Data Type

