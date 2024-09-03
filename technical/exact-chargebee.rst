==================
Exact to  Dataflow
==================

Generated: 2024-09-03 08:16:57

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Exact to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Exact Items to  Item
--------------------
Every Exact Items will be synchronized with a  Item.

Once a link between a Exact Items and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Items and a  Item:

.. list-table::
   :header-rows: 1

   * - Exact Items Property
     -  Item Property
     -  Data Type


Exact Salesorders to  Order
---------------------------
Every Exact Salesorders will be synchronized with a  Order.

Once a link between a Exact Salesorders and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Exact Salesorders and a  Order:

.. list-table::
   :header-rows: 1

   * - Exact Salesorders Property
     -  Order Property
     -  Data Type
   * - Currency
     - currency_code
     - "string"

