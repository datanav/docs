========================
Businessnxt to  Dataflow
========================

Generated: 2024-09-03 08:57:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Orderline to  Quotationline
---------------------------------------
Every Businessnxt Orderline will be synchronized with a  Quotationline.

Once a link between a Businessnxt Orderline and a  Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a  Quotationline:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     -  Quotationline Property
     -  Data Type


Businessnxt Product to  Products
--------------------------------
Every Businessnxt Product will be synchronized with a  Products.

Once a link between a Businessnxt Product and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a  Products:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
     -  Products Property
     -  Data Type
   * - priceQuantity
     - ProductPrice
     - "string"
   * - quantityPerUnit
     - ProductQuantity
     - "string"

