===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-07-04 09:57:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Invoice to  Orders
-----------------------
Every Wave Invoice will be synchronized with a  Orders.

Once a link between a Wave Invoice and a  Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Orders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Orders Property
     -  Data Type


Wave Product to  Products
-------------------------
Every Wave Product will be synchronized with a  Products.

Once a link between a Wave Product and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Products:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Products Property
     -  Data Type
   * - name
     - name
     - "string"
   * - unitPrice
     - sale_price
     - "string"

