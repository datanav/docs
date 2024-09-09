================================
Woocommerce to Invoiced Dataflow
================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Customer to Invoiced Customers person
-------------------------------------------------
Every Woocommerce Customer will be synchronized with a Invoiced Customers person.

Once a link between a Woocommerce Customer and a Invoiced Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Customer and a Invoiced Customers person:

.. list-table::
   :header-rows: 1

   * - Woocommerce Customer Property
     - Invoiced Customers person Property
     - Invoiced Data Type


Woocommerce Order to Invoiced Invoices
--------------------------------------
Every Woocommerce Order will be synchronized with a Invoiced Invoices.

Once a link between a Woocommerce Order and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - currency
     - currency
     - "string"
   * - customer_id
     - customer
     - "string"
   * - discount_total
     - discounts
     - "string"


Woocommerce Order to Invoiced Lineitem
--------------------------------------
Every Woocommerce Order will be synchronized with a Invoiced Lineitem.

Once a link between a Woocommerce Order and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     - Invoiced Lineitem Property
     - Invoiced Data Type
   * - line_items.name
     - items.name
     - "string"
   * - line_items.price
     - items.amount
     - "string"
   * - line_items.quantity
     - items.quantity
     - "string"


Woocommerce Product to Invoiced Items
-------------------------------------
Every Woocommerce Product will be synchronized with a Invoiced Items.

Once a link between a Woocommerce Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - name
     - name
     - "string"
   * - price
     - unit_cost
     - "string"

