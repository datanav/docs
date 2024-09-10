===============================
Customerp to Chargebee Dataflow
===============================

Generated: 2024-09-10 14:20:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Customerp to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Customerp Order to Chargebee Order
----------------------------------
Every Customerp Order will be synchronized with a Chargebee Order.

Once a link between a Customerp Order and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Customerp Order and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - Customerp Order Property
     - Chargebee Order Property
     - Chargebee Data Type


Customerp Product to Chargebee Item
-----------------------------------
Every Customerp Product will be synchronized with a Chargebee Item.

Once a link between a Customerp Product and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Customerp Product and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Customerp Product Property
     - Chargebee Item Property
     - Chargebee Data Type

