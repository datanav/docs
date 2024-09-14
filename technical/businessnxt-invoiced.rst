=================================
Business Nxt to Invoiced Dataflow
=================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Order to Invoiced Invoices
---------------------------------------
Every Business Nxt Order will be synchronized with a Invoiced Invoices.

Once a link between a Business Nxt Order and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Order and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - Business Nxt Order Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - totalDiscountAmountInCurrency
     - discounts
     - "string"


Business Nxt Orderline to Invoiced Lineitem
-------------------------------------------
Every Business Nxt Orderline will be synchronized with a Invoiced Lineitem.

Once a link between a Business Nxt Orderline and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - Invoiced Lineitem Property
     - Invoiced Data Type


Business Nxt Product to Invoiced Items
--------------------------------------
Every Business Nxt Product will be synchronized with a Invoiced Items.

Once a link between a Business Nxt Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Business Nxt Product Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - description
     - description
     - "string"

