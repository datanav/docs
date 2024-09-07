================================
Businessnxt to Invoiced Dataflow
================================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Order to Invoiced Invoices
--------------------------------------
Every Businessnxt Order will be synchronized with a Invoiced Invoices.

Once a link between a Businessnxt Order and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Order and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - Businessnxt Order Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - totalDiscountAmountInCurrency
     - discounts
     - "string"


Businessnxt Orderline to Invoiced Lineitem
------------------------------------------
Every Businessnxt Orderline will be synchronized with a Invoiced Lineitem.

Once a link between a Businessnxt Orderline and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     - Invoiced Lineitem Property
     - Invoiced Data Type


Businessnxt Product to Invoiced Items
-------------------------------------
Every Businessnxt Product will be synchronized with a Invoiced Items.

Once a link between a Businessnxt Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - description
     - description
     - "string"

