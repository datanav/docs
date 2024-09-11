================================
BusinessNxt to Invoiced Dataflow
================================

Generated: 2024-09-11 08:37:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessNxt Order to Invoiced Invoices
--------------------------------------
Every BusinessNxt Order will be synchronized with a Invoiced Invoices.

Once a link between a BusinessNxt Order and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Order and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Order Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - totalDiscountAmountInCurrency
     - discounts
     - "string"


BusinessNxt Orderline to Invoiced Lineitem
------------------------------------------
Every BusinessNxt Orderline will be synchronized with a Invoiced Lineitem.

Once a link between a BusinessNxt Orderline and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - Invoiced Lineitem Property
     - Invoiced Data Type


BusinessNxt Product to Invoiced Items
-------------------------------------
Every BusinessNxt Product will be synchronized with a Invoiced Items.

Once a link between a BusinessNxt Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Product Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - description
     - description
     - "string"

