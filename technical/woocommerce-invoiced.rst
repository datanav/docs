================================
Woocommerce to Invoiced Dataflow
================================

Generated: 2024-09-03 09:00:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Woocommerce to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Woocommerce Customer to  Customers person
-----------------------------------------
Every Woocommerce Customer will be synchronized with a  Customers person.

Once a link between a Woocommerce Customer and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Customer and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Woocommerce Customer Property
     -  Customers person Property
     -  Data Type


Woocommerce Order to  Invoices
------------------------------
Every Woocommerce Order will be synchronized with a  Invoices.

Once a link between a Woocommerce Order and a  Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a  Invoices:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     -  Invoices Property
     -  Data Type
   * - currency
     - currency
     - "string"
   * - customer_id
     - customer
     - "string"
   * - discount_total
     - discounts
     - "string"


Woocommerce Order to  Lineitem
------------------------------
Every Woocommerce Order will be synchronized with a  Lineitem.

Once a link between a Woocommerce Order and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Order and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - Woocommerce Order Property
     -  Lineitem Property
     -  Data Type
   * - line_items.name
     - items.name
     - "string"
   * - line_items.price
     - items.amount
     - "string"
   * - line_items.quantity
     - items.quantity
     - "string"


Woocommerce Product to  Items
-----------------------------
Every Woocommerce Product will be synchronized with a  Items.

Once a link between a Woocommerce Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Woocommerce Product and a  Items:

.. list-table::
   :header-rows: 1

   * - Woocommerce Product Property
     -  Items Property
     -  Data Type
   * - name
     - name
     - "string"
   * - price
     - unit_cost
     - "string"

