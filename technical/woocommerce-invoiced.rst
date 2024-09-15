================================
WooCommerce to Invoiced Dataflow
================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to Invoiced Customers person
-------------------------------------------------
Every WooCommerce Customer will be synchronized with a Invoiced Customers person.

Once a link between a WooCommerce Customer and a Invoiced Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Invoiced Customers person:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Invoiced Customers person Property
     - Invoiced Data Type


WooCommerce Order to Invoiced Invoices
--------------------------------------
Every WooCommerce Order will be synchronized with a Invoiced Invoices.

Once a link between a WooCommerce Order and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
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


WooCommerce Order to Invoiced Lineitem
--------------------------------------
Every WooCommerce Order will be synchronized with a Invoiced Lineitem.

Once a link between a WooCommerce Order and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Order and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - WooCommerce Order Property
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


WooCommerce Product to Invoiced Items
-------------------------------------
Every WooCommerce Product will be synchronized with a Invoiced Items.

Once a link between a WooCommerce Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - WooCommerce Product Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - name
     - name
     - "string"
   * - price
     - unit_cost
     - "string"

