=======================================
Visma Business Nxt to Invoiced Dataflow
=======================================

Generated: 2024-09-11 07:47:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Visma Business Nxt to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Visma Order to Invoiced Invoices
--------------------------------
Every Visma Order will be synchronized with a Invoiced Invoices.

Once a link between a Visma Order and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Order and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - Visma Order Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - totalDiscountAmountInCurrency
     - discounts
     - "string"


Visma Orderline to Invoiced Lineitem
------------------------------------
Every Visma Orderline will be synchronized with a Invoiced Lineitem.

Once a link between a Visma Orderline and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Orderline and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Visma Orderline Property
     - Invoiced Lineitem Property
     - Invoiced Data Type


Visma Product to Invoiced Items
-------------------------------
Every Visma Product will be synchronized with a Invoiced Items.

Once a link between a Visma Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Visma Product Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - description
     - description
     - "string"

